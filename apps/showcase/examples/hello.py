from py4web import action

from .common import T


@action("hello")
@action.uses(T)
def hello():
    return str(T("Hello World"))
