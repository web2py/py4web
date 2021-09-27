from py4web import Action, Session, DAL, Field, App
from pathlib import Path
from omfitt import FixtureShop

from ..todo import app as todo_app


# define database and tables
db = DAL(
    "sqlite://storage.db", folder=str(Path(__file__).parent / "databases")
)
db.define_table("todo", Field("info"))
db.commit()


@FixtureShop.make_from
class shop:
    session = Session()


action = Action(shop)
app = App(action, str(Path(__file__).parent))

@action('index')
@action.uses('index.html')
def index():
    # ctx.app_ctx
    # ctx.request.method
    # ctx.response.headers[...] = ...
    session = shop.session
    if 'counter' not in session:
        session['counter'] = 1
    session['counter'] += 1
    return dict(
        app_name=app.ctx.app_name,
        author = 'Val',
        content=f"Hi there! counter: {session['counter']}"
    )


todo_app._action.fitter.shop.fixtures.db = db

ctx = app.mount('tst')
todo_app.mount('todo', ctx, base_url='todo')


#todo_app.shop.fixtures.db = db
#todo_app.mount(__name__, app_ctx=dict(base_url = 'todo'))
