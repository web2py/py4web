from py4web import action
from py4web.utils.factories import ActionFactory, Inject

from .common import T, auth, db

expose = ActionFactory(auth, T, Inject(message="Hello World"))


@expose.get("test_expose1", template="examples/generic.html")
def test_expose1():
    return dict()


@expose.get("test_expose2")
def test_expose2():
    return dict()


@expose("test_expose3")
def test_expose3():
    return dict()
