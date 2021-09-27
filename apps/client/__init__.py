import os
from py4web import Action, App
from omfitt import BaseFixture
from ..reusable import app as reusable_app


class Counter(BaseFixture):
    def __init__(self) -> None:
        self.cnt = 1

    def take_on(self, app_ctx, ctx):
        # expose counter value so that the following
        # fixtures can access it via ctx.ask('client_cnt')
        ctx.provide('client', {app_ctx.name: self.cnt})


app = App(Action(), os.path.dirname(__file__))
ctx = app.mount('client')

reusable_app.shop.fixtures.client_counter = Counter()
reusable_app.mount('first', ctx, base_url='first')

reusable_app.shop.fixtures.client_counter = Counter()
reusable_app.mount('second', ctx, base_url='second')

# now you can try
#  http://127.0.0.1:8000/client/first/api/index
#  http://127.0.0.1:8000/client/second/api/index
#
# refresh the pages several times to see that each route
# has its own client_counter and common total
