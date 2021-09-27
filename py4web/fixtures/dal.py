import copy
from pydal import DAL as _DAL
from threadsafevariable import ThreadSafeVariable
from omfitt import BaseFixture, RouteContext

from ..core.core_events import core_event_bus, CoreEvents


# this global object will be used to store their state to restore it for every http request
ICECUBE = {}


@core_event_bus.on(CoreEvents.APPS_LOADED)
def update_icecube(*a, **kw):
    ICECUBE.update(ThreadSafeVariable.freeze())


class DAL(_DAL, BaseFixture):

    reconnect_on_request = True

    def take_on(self, app_cxt, ctx):
        if self.reconnect_on_request:
            self._adapter.reconnect()
        ThreadSafeVariable.restore(ICECUBE)

    def on_finalize(self, app_ctx, ctx: RouteContext):
        if ctx.successful:
            self.commit()
        else:
            self.rollback()


# make sure some variables in pydal are thread safe
def thread_safe_pydal_patch():
    Field = _DAL.Field
    tsafe_attrs = [
        "readable",
        "writable",
        "default",
        "update",
        "requires",
        "widget",
        "represent",
    ]
    [setattr(Field, a, ThreadSafeVariable()) for a in tsafe_attrs]

    # hack 'copy.copy' behavior, since it makes a shallow copy,
    # but ThreadSafe-attributes (see above) are class-level, so:
    # no copy -> no attr in ICECUBE for the fresh one -> gevent-error on try to access to any of ThreadSafe-attributes
    def field_copy(self):
        # to prevent infinite recursion
        # temporarily set __copy__ to None
        me = self.__class__.__copy__
        self.__class__.__copy__ = None
        clone = copy.copy(self)
        self.__class__.__copy__ = me
        [setattr(clone, a, getattr(self, a)) for a in tsafe_attrs]
        return clone

    # to avoid possible future problems
    if hasattr(Field, "__copy__"):
        raise RuntimeError("code fix required!")
    setattr(Field, "__copy__", field_copy)


thread_safe_pydal_patch()
