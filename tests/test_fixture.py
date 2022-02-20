from types import SimpleNamespace
import pytest
import threading
from py4web.core import Fixture

result = {"seq": []}


def run_thread(func, *a):
    t = threading.Thread(target=func, args=a)
    return t


class Foo(Fixture):
    def on_request(self):
        self._safe_local = SimpleNamespace()

    @property
    def bar(self):
        return self._safe_local.a

    @bar.setter
    def bar(self, a):
        self._safe_local.a = a


foo = Foo()


def before_request():
    Fixture.__init_request_ctx__()


@pytest.fixture
def init_foo():
    def init(key, a, evnt_done=None, evnt_play=None):
        result["seq"].append(key)
        before_request()
        foo.on_request()
        foo.bar = a
        evnt_done and evnt_done.set()
        evnt_play and evnt_play.wait()
        result[key] = foo.bar
        return foo

    return init


def test_fixtute_local_storage(init_foo):
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
    assert foo.bar == "a1"
    assert result["t2"] == "a2"
    assert result["t3"] == "a3"
    assert ",".join(result["seq"]) == "t1,t2,t3"


def test_fixtute_error():
    before_request()
    # attempt to access _safe_local prop without on_request-call
    with pytest.raises(RuntimeError) as err:
        foo.bar
    assert "py4web hint" in err.value.args[0]
    assert "Foo object" in err.value.args[0]
