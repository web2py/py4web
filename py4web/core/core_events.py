from enum import Enum


class CoreEvents(str, Enum):
    BEFORE_APPS_LOAD = 'before_apps_load'
    APPS_LOADED = 'apps_loaded'
    RELOAD_APPS = 'reload_apps'


class CoreEventBus:
    __slots__ = ('events_subs',)

    def __init__(self):
        self.events_subs = {k: set() for k in CoreEvents}

    def on(self, event, cb=None):
        if not cb:
            return lambda cb: self.on(event, cb)
        self.events_subs[CoreEvents(event)].add(cb)
        return cb

    def emit(self, event, *args, **kw):
        [cb(*args, **kw) for cb in self.events_subs[CoreEvents(event)].copy()]

    def off(self, event, cb):
        if event == '*':
            evnts = CoreEvents
        else:
            evnts = [CoreEvents(event)]
        es = self.events_subs
        [es[e].difference_update({cb}) for e in evnts]


core_event_bus = CoreEventBus()
