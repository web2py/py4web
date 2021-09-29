from py4web import Action, App
from omfitt import FixtureShop, BaseFixture, FixtureHolder


class Titleizer(BaseFixture):
    def on_output(self, app_ctx, ctx):
        ctx.output = ctx.output.title()


class Counter(BaseFixture):
    def __init__(self):
        self.cnt = 1
        self.clients = {}

    def take_on(self, app_ctx, ctx):
        self.clients.update(ctx.ask('client'))


@FixtureShop.make_from
class shop:
    # fixture to be set by client applications  - see below
    client_counter = FixtureHolder()

    # fitter-fixture - the same for all clients,
    # so you can easily implement something like CAS!
    own_counter = Counter()
    titleizer = Titleizer()


action = Action(shop)
app = App(__name__, action)


@action("api/index")
@action.uses(shop.titleizer)
def api_index():
    c_cnt = shop.client_counter.cnt
    o_cnt = shop.own_counter.cnt
    clients = str(shop.own_counter.clients)
    shop.client_counter.cnt += 1
    shop.own_counter.cnt += 1
    app.response.headers['Content-Type'] = 'text/plain'
    return (
        'hello world! client_counter= {} / total= {} \n clients counters: {}'
        .format(c_cnt, o_cnt, clients)
    )
