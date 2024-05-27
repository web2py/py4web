import threading
import pytest

from py4web.core import Fixture


def run_thread(func, *a):
    t = threading.Thread(target=func, args=a)
    return t


class Foo(Fixture):
    def on_request(self, context):
        Fixture.local_initialize(self)

    @property
    def bar(self):
        return self.local.a

    @bar.setter
    def bar(self, a):
        self.local.a = a


results = {}
foo = Foo()


@pytest.fixture
def init_foo():
    def init(key, a, evnt_done=None, evnt_play=None):
        Fixture.local_initialize(foo)
        foo.bar = a
        evnt_done and evnt_done.set()
        evnt_play and evnt_play.wait()
        results[key] = foo.bar
        Fixture.local_delete(foo)
        return foo

    return init


def test_fixture_local_storage(init_foo):
    assert init_foo("t1", "a1") is foo
    evnt_done = threading.Event()
    evnt_play = threading.Event()
    t2 = run_thread(init_foo, "t2", "a2", evnt_done, evnt_play)
    t3 = run_thread(init_foo, "t3", "a3", None, None)
    t2.start()
    evnt_done.wait()
    t3.start()
    t3.join()
    evnt_play.set()
    t2.join()
    assert results["t1"] == "a1"
    assert results["t2"] == "a2"
    assert results["t3"] == "a3"


def test_fixture_error():
    # attempt to access _safe_local prop without on_request-call
    with pytest.raises(RuntimeError) as err:
        foo.bar
    assert "not initialized" in err.value.args[0]
    assert "Foo object" in err.value.args[0]
