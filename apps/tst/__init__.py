from py4web import Action, Session
from omfitt import Ctx, FixtureShop


@FixtureShop.make_from
class shop:
    session = Session()


action = Action(shop)


@action('index')
@action.uses('index.html')
def index(ctx=Ctx()):
    # ctx.app_ctx
    # ctx.request.method
    # ctx.response.headers[...] = ...
    session = shop.session
    if 'counter' not in session:
        session['counter'] = 1
    session['counter'] += 1
    return dict(
        app_name=ctx.app_ctx['app_name'],
        author=ctx.app_ctx['author'],
        content=f"Hi there! counter: {session['counter']}"
    )


action.mount(__name__, app_ctx=dict(author='Val'))
