from py4web import Action, Session, DAL, Field, App
from pathlib import Path
from omfitt import FixtureShop
from py4web.app_methods import URL as URLMeth

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
app = App(__name__, action)
app.URL = URLMeth(app)


@action('index')
@action.uses('index.html')
def index():
    session = shop.session
    if 'counter' not in session:
        session['counter'] = 1
    session['counter'] += 1
    return dict(
        app_name=app.ctx.app_name,
        author = 'Val',
        content=f"Hi there! counter: {session['counter']}"
    )


# replace db-fixture with our one
todo_app.shop.fixtures.db = db

# mount our app
this_app_ctx = app.mount('tst')

# mount todo-app as part of this app
todo_app.mount('todo', this_app_ctx, base_url='todo')
