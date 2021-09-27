from pathlib import Path
from py4web import Action, DAL, Field, Session, Cache, abort, App
from omfitt import FixtureShop, BaseFixture, RouteContext, Ctx, FixtureHolder
from py4web.core.utils import dumps
from py4web.app_methods import URL as URLMeth

APP_NAME = __name__.split('.')[-1]



cache = Cache(size=1000)

# define database and tables
db = DAL(
    "sqlite://storage.db", folder=str(Path(__file__).parent / "databases")
)
db.define_table("todo", Field("info"))
db.commit()


class DefaultJson(BaseFixture):
    def on_output(self, app_ctx, ctx: RouteContext):
        if isinstance(ctx.output, dict):
            ctx.output = dumps(ctx.output)
            ctx.response.headers['Content-Type'] = 'application/json'


class UserIn(BaseFixture):
    def take_on(self, app_ctx, ctx: RouteContext):
        session: Session = ctx.ask('session')
        if not session:
            raise RuntimeError('The session is required')
        if session.get('user', None) is None:
            abort(401)


@FixtureShop.make_from
class shop:
    db = FixtureHolder(db)
    session = Session()
    user_in = UserIn()


requires_user = [shop.session, shop.user_in]

action = Action(shop, default_fixtures=([DefaultJson()], []))
app = App(action, str(Path(__file__).parent))
URL = app.URL = URLMeth(app)

# example index page using session, template and vue.js
@action("index")  # the function below is exposed as a GET action
@action.uses("index.html")  # we use the template index.html to render it
def index():
    session = shop.session
    session["counter"] = session.get("counter", 0) + 1
    session["user"] = {"id": 1}  # store a user in session
    return dict(session=session)


# example of GET/POST/DELETE RESTful APIs

@action("api:api")  # a GET API function  api:api == route_name:rule
@action.uses(*requires_user)
def todo():
    db = shop.db
    return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())


@action("$api", method="POST")  # $api reference named route 'api'
@action.uses(*requires_user)
def todo_post():
    db = shop.db
    return dict(id=db.todo.insert(info=app.request.json.get("info")))


@action("api/<id:int>", method="DELETE")
@action.uses(*requires_user)
def todo_id(id):
    db = shop.db
    db(db.todo.id == id).delete()
    return dict()


# example of caching
@action("uuid")
@cache.memoize(expiration=5)  # here we cache the result for 5 seconds
def uuid():
    import uuid

    return str(uuid.uuid4())


app.mount(APP_NAME)
