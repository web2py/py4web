
import ombott
import logging
from omfitt import (
    BaseFixture,
    BaseProcessor,
    FixtureService,
    BaseGateway,
    Fitter,
)

from . import globs
from .core_events import core_event_bus, CoreEvents
from .error_pages import error_page
from .install import install_args
from .reloader import Reloader
from .loggers import get_error_snapshot, error_logger
from .exceptions import HTTP


__all__ = (
    'check_compatible',
    'import_apps',
    'reload_apps',
    'wsgi',
    'BaseAction',
)


# hold all framework hooks in one place
# NOTE: `after_request` hooks are not currently used

globs.request_hooks.before.add(BaseFixture.__init_request_ctx__)


def check_compatible(version):
    """To be called by apps to check if module version is compatible with py4web requirements"""
    from .. import __version__
    return tuple(map(int, __version__.split("."))) >= tuple(
        map(int, version.split("."))
    )


def import_apps():
    core_event_bus.emit(CoreEvents.BEFORE_APPS_LOAD)
    Reloader.import_apps()
    core_event_bus.emit(CoreEvents.APPS_LOADED)


@core_event_bus.on(CoreEvents.RELOAD_APPS)
def reload_apps(*app_names):
    [Reloader.import_app(app) for app in app_names]
    core_event_bus.emit(CoreEvents.APPS_LOADED)


def wsgi(**kwargs):
    """Initializes everything, loads apps, returns the wsgi app"""
    install_args(kwargs)
    import_apps()
    # ICECUBE.update(threadsafevariable.ThreadSafeVariable.freeze())
    return globs.app


class _Gateway(BaseGateway):
    def setup(self, app_ctx, route_ctx):
        globs.request.app_name = app_ctx['app_name']
        route_ctx.request = globs.request
        route_ctx.response = globs.response


def _default_exception_handler(app_ctx, route_ctx, ex):
    response = route_ctx.response
    try:
        raise ex
    except HTTP as http:
        response.status = http.status
        ret = getattr(http, "body", "")
        http_headers = getattr(http, 'headers', None)
        if http_headers:
            response.headers.update(http_headers)
        return ret
    except ombott.HTTPResponse as resp:
        return resp
    except Exception:
        snapshot = get_error_snapshot()
        logging.error(snapshot["traceback"])
        ticket_uuid = error_logger.log(app_ctx['app_name'], snapshot) or "unknown"
        return ombott.HTTPResponse(
            body=error_page(
                500,
                button_text=ticket_uuid,
                href="/_dashboard/ticket/" + ticket_uuid,
            ),
            status=500,
        )


_processor = BaseProcessor()
_gateway = _Gateway()
_fixture_service = FixtureService()
_exception_hadlers = {
    '*': _default_exception_handler
}


class BaseAction(Fitter):
    def __init__(self, *shops):
        super().__init__(
            _processor, _fixture_service, shops,
            self.mounter, _gateway, None, _exception_hadlers
        )

    def mounter(self, pth, *args, **kw):
        if not pth.startswith('/'):
            pth = f"/{self.ctx['app_name']}/{pth}"
        return globs.app.route(pth, *args, **kw)

    def mount(self, app_name=None, app_ctx: dict = None):
        # remove apps-folder prefix
        app_name = app_name.split('.')[-1]
        if not (app_name or app_ctx):
            raise TypeError('At least on argument is required')
        app_ctx = app_ctx.copy() if app_ctx else {}
        if 'app_name' not in app_ctx:
            if not app_name:
                raise TypeError('`app_name` is required')
            app_ctx['app_name'] = app_name
        elif app_name and app_name != app_ctx['app_name']:
            raise TypeError(
                f'Got two different `app_name`: {app_name}, {app_ctx["app_name"]}'
            )
        self.ctx = app_ctx
        super().mount()
