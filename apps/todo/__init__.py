from pathlib import Path
from py4web import Action, DAL, Field, Session, Cache, abort, App
from omfitt import FixtureShop, BaseFixture, RouteContext, FixtureHolder
from py4web.core.utils import dumps
from py4web.app_methods import URL as URLMeth


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



# accessing the fixture as a shop attribute avoids
# the need to declare the fixture in uses()
# unless order matters or it is guard-fixture
@FixtureShop.make_from
class shop:
    db = FixtureHolder(db)
    session = Session()
    user_in = UserIn()


requires_user = [shop.session, shop.user_in]

action = Action(shop, default_fixtures=([DefaultJson()], []))
app = App(__name__, action)
app.URL = URLMeth(app)


# example index page using session, template and vue.js
@action("index")  # the function below is exposed as a GET action
@action.uses("index.html")  # we use the template index.html to render it
def index():
    session = shop.session
    session["counter"] = session.get("counter", 0) + 1
    session["user"] = {"id": 1}  # store a user in session
    return dict(session=session)


# example of GET/POST/DELETE RESTful APIs

# named route: <route_name>:<rule>, e.g. home:path/to/home
@action("api:api")  # a GET API function
@action.uses(*requires_user)
def todo():
    db = shop.db
    return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())


# reference named route 'api' by $<route_name>
@action("$api", method="POST")
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


# mount app
app.mount()
