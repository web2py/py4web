
import ombott
import logging
from omfitt import (
    BaseFixture,
    BaseProcessor,
    FixtureService,
    Fitter,
    BaseAction as _BaseAction,
    BaseApp,
    BaseCtx as _BaseCtx,
)

from . import globs
from .globs import request
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
        ticket_uuid = error_logger.log(app_ctx.app_name, snapshot) or "unknown"
        return ombott.HTTPResponse(
            body=error_page(
                500,
                button_text=ticket_uuid,
                href="/_dashboard/ticket/" + ticket_uuid,
            ),
            status=500,
        )


_processor = BaseProcessor()
_fixture_service = FixtureService()
_exception_hadlers = {
    '*': _default_exception_handler
}


class BaseAction(_BaseAction):
    def __init__(self, *shops, default_fixtures=None):
        fitter = Fitter(
            _processor, _fixture_service, shops,
            _exception_hadlers, default_fixtures
        )
        super().__init__(fitter)


class BaseCtx(_BaseCtx):
    def __init__(self, app, name, master_ctx: 'BaseCtx' = None, props=None):
        super().__init__(app, name, master_ctx, props)
        if self.props is None:
            self.props = {}
        self.app_name = self.root.name
        self.base_url = self.props.get('base_url', '')
        self.static_url = self.props.get('static_url', name)
        self.static_version = self.props.get('static_version', '0.0.1')
        # {':login' : '/main/login'}


class App(BaseApp):
    def __init__(self, action: BaseAction, app_folder):
        super().__init__(action)
        self.folder = app_folder
        self.URL = None

    @property
    def ctx(self):
        return self._local.ctx

    def _make_ctx(self, name, master_ctx, props):
        return BaseCtx(self, name, master_ctx, props)

    def _mount_route(self, ctx: BaseCtx, fun, route_args):
        path, method, name, prop, kw = route_args
        is_index = False
        if prop:
            path = ctx.route_map.get(prop, path)
        if not path:
            return
        if path[0] != '/':
            is_index = path == 'index'
            path = '/' + '/'.join(p for p in (ctx.root.name, ctx.base_url, path) if p)
        full_name = None
        if not name and prop:
            name = prop
        if name:
            full_name = f'{".".join(c.name for c in ctx.mount_stack)}.{name}'
        route = globs.app.add_route(path, method, fun, full_name)
        ctx.routes.append(route)
        if is_index:
            route = globs.app.add_route(path[:-6] or '/', method, fun, full_name)
            ctx.routes.append(route)
        if name:
            if name in ctx.named_routes:
                raise KeyError('The route name already in use: {name}')
            ctx.named_routes[name] = route

    @property
    def request(self):
        return request

    def setup(self, app_ctx: BaseCtx, route_ctx):
        super().setup(app_ctx, route_ctx)
        route_ctx.request = request
        route_ctx.response = globs.response
        route_ctx.provide('URL', self.URL)




