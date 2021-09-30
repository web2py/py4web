
import os
from types import SimpleNamespace
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
    Reloader.reimport_apps(*app_names)
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


class StaticRegistry:

    # mounted[base_url] = SimpleNamespace: {
    #   folder: static_path, client_apps: {foo, bar}
    # }
    mounted = {}

    def register(self, base_url, folder, app):
        folder_apps = self.mounted.get(base_url)
        if folder_apps:
            if os.path.samefile(folder_apps.folder, folder):
                raise KeyError(f'URL already in use: {base_url} => path:{folder_apps.folder}')
            folder_apps.client_apps.add(app)
        self.mounted[base_url] = SimpleNamespace(
            folder=folder, client_apps={app}
        )

    def get_registered(self, base_url, folder):
        folder_apps = self.mounted.get(base_url)
        if not folder_apps:
            return None
        if os.path.samefile(folder_apps.folder, folder):
            return folder_apps

    def __contains__(self, base_url_folder_tuple):
        if isinstance(base_url_folder_tuple, str):
            raise TypeError(
                f'A pair like [url, folder] is required, got string: {base_url_folder_tuple}'
            )
        base_url, folder = base_url_folder_tuple
        folder_apps = self.mounted.get(base_url)
        if not folder_apps:
            return False
        return os.path.samefile(folder_apps.folder, folder)


_static_registry = StaticRegistry()

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


class ConfigSetter:
    def __init__(self, keys_class, defaults_factory=None, novalue=None):
        self.novalue = novalue
        self.defaults_factory = defaults_factory
        self.keys = {
            k for k in keys_class.__dict__
            if not k.startswith('_')
        }

    def extend(self, dst, src, optional_keys = None, get_default = None):
        self.apply(dst, src, optional_keys, get_default, extend_mode=False)

    def apply(self, dst, src, optional_keys = None, get_default = None, extend_mode=False):
        optional_keys = optional_keys or set()
        if get_default is None:
            if self.defaults_factory:
                get_default = self.defaults_factory(src).get
            else:
                get_default = {}.get

        no_value = self.novalue
        if isinstance(src, dict):
            get = src.get
        else:
            get = lambda k, default: getattr(src, k, default)
        for k in self.keys:
            if (
                extend_mode and
                getattr(src, k, no_value) is not no_value
            ):
                continue
            v = get(k, no_value)
            if v is no_value:
                try:
                    v = get_default(k)
                except KeyError:
                    if k not in optional_keys:
                        raise KeyError(f'Missing key: {k}')
                    continue
            setattr(dst, k, v)

    def dict_from(self, src, get_default=None):
        defaults = get_default or {}.get
        ret = {}
        no_value = self.novalue
        for k in self.keys:
            v = getattr(src, k, no_value)
            if v is no_value:
                v = defaults(k, no_value)
            if v is no_value:
                raise KeyError(f'Missing key: {k}')
            ret[k] = v


class AppConfigKeys:
    folder = None

    # optional
    base_url = None
    static_base_url = None
    static_version = None

    static_folder = None
    template_folder = None


class AppConfig(AppConfigKeys):
    __getitem__ = lambda s, k: getattr(s, k)
    __setitem__ = lambda s, k, v: setattr(s, k, v)
    get = lambda s, k, d=None: getattr(s, k, d)


class AppConfigDefaultsFactory:
    base_url = None
    static_version = '0.0.1'

    def __init__(self, src):
        if isinstance(src, dict):
            src = SimpleNamespace(**src)
        self.src = src

    def static_base_url(self):
        ret = getattr(self.src, 'base_url', None)
        return ret

    def folder(self):
        # to allow to use for static/template folders
        folder = getattr(self.src, 'folder', None)
        if folder is None:
            folder = '.'
        return folder

    def static_folder(self):
        return os.path.join(self.folder(), 'static')

    def template_folder(self):
        return os.path.join(self.folder(), 'templates')

    def get(self, k):
        no_value = []
        attr = getattr(self, k, no_value)
        if attr is no_value:
            raise KeyError(f'{k}')
        return attr() if callable(attr) else attr


_config_setter = ConfigSetter(AppConfigKeys, AppConfigDefaultsFactory)


class BaseCtx(_BaseCtx, AppConfigKeys):
    config_setter = _config_setter

    def __init__(self, app: 'App', name, master_ctx: 'BaseCtx', props):
        super().__init__(app, name, master_ctx, props)
        self.config_setter.apply(self, props)

        # set ctx-specific props
        self.app_name = self.root.name
        self.route_map = props.get('route_map', {})


class App(BaseApp):
    request = globs.request
    response = globs.response
    add_route = staticmethod(globs.app.add_route)
    static_file = staticmethod(globs.static_file)

    static_registry = _static_registry
    config_setter = _config_setter

    def __init__(self, module_name, action: BaseAction, **props):
        super().__init__(action)
        self._module_name = module_name
        if module_name.startswith('apps'):
            mname = module_name[len('apps.'):]
            self._folder = os.path.normpath(os.path.join(
                os.environ["PY4WEB_APPS_FOLDER"],
                mname.replace('.', '/')
            ))
        self.name = module_name.split('.')[-1]
        self.app_cfg = AppConfig()
        props['name'] = self.name
        self.config_setter.apply(self.app_cfg, props)

        # clients apps set to track deps
        # if this app needs to be reloaded then all clients should also be reloaded
        self._clients = set()

        # declare AppMethods
        self.URL = None

    def __getattr__(self, k):
        if k == '_folder':
            raise AttributeError(
                'For app-modules is out of apps-dir, `folder`-prop must be abs-path'
            )
        return super().__getattr__(k)

    @property
    def ctx(self):
        return self._local.ctx

    def get_all_clients(self, clients = None):
        ret = {}
        if clients is None:
            clients = self._clients
        for app in clients:
            ret[app] = True
            ret.update(self.get_all_clients(app._clients))
        return ret

    def _make_ctx(self, name, master_ctx, props):
        if master_ctx:
            self._clients.add(master_ctx.app)
        ctx_props = AppConfig()
        self.config_setter.apply(ctx_props, props)
        self.config_setter.extend(ctx_props, self.app_cfg)
        self._resolve_base_urls(name, master_ctx, ctx_props)
        self._resolve_folders(ctx_props)
        self.expose_static(ctx_props.static_base_url, ctx_props.static_folder)
        return BaseCtx(self, name, master_ctx, ctx_props)

    def _resolve_base_urls(self, name, master_ctx, ctx_props: AppConfig):
        if ctx_props.base_url is None:
            name = name or self.name
            if master_ctx:
                ctx_props.base_url = f'{master_ctx.base_url}/{name}'
            else:
                ctx_props.base_url = f'/{name}'
        if ctx_props.static_base_url is None:
            ctx_props.static_base_url = ctx_props.base_url

    def _resolve_folders(self, ctx_props: AppConfig):

        def pjoin(*args):
            return os.path.normpath(os.path.join(*args))
        if not os.path.isabs(ctx_props.folder):
            ctx_props.folder = pjoin(self._folder, ctx_props.folder)
        folder = ctx_props.folder
        for f in (f_ for f_ in self.config_setter.keys if f_.endswith('_folder')):
            ctx_props[f] = pjoin(folder, ctx_props[f])

    def _get_abs_url(self, base_url, path):
        if not path:
            return base_url
        if path[0] != '/':
            path = f'{base_url}/{path}'
        return path

    def _mount_route(self, ctx: BaseCtx, fun, route_args):
        path, method, name, prop, kw = route_args
        # name and not prop -> define named route
        # name and prop -> define named route, redefine it with prop if passed
        # prop -> define named route

        is_index = False
        '''
        if name:
            name = name[1:]
            route = ctx.named_routes[name]
            route.add_method(method, fun)
            return
        '''
        if prop and (name is None) and path:
            # ':prop:path/to/here'
            name = prop

        if name and path:
            if prop:
                # redefine by config if passed
                path = ctx.route_map.get(prop, path)
        elif prop:
            # if we're here path is None - this is reference
            # try to get from config
            path = ctx.route_map.get(prop)
            # if not path
            # try to find in named routes - it should be defined before reference
            if not path:
                if prop in ctx.named_routes:
                    ctx.named_routes[prop].add_method(method, fun)
                    return
                else:
                    # we are currently unable to determine
                    # if this route is required or optional.
                    raise RuntimeError(f'Can`t find path/rule for route: {prop}')
        is_index = path == 'index'
        path = self._get_abs_url(ctx.base_url, path)
        full_name = None
        if name:
            full_name = f'{".".join(c.name for c in ctx.mount_stack)}.{name}'

        route = self.add_route(path, method, fun, full_name)
        ctx.routes.append(route)
        if is_index:
            route = self.add_route(path[:-len('/index')] or '/', method, fun, full_name)
            ctx.routes.append(route)
        if name:
            if name in ctx.named_routes:
                raise KeyError('The route name already in use: {name}')
            ctx.named_routes[name] = route

    def _mounted(self):
        pass

    @property
    def shop(self):
        return self._action.fitter.shop

    @property
    def shops(self):
        return self._action.fitter.shops

    def setup(self, app_ctx: BaseCtx, route_ctx):
        super().setup(app_ctx, route_ctx)
        route_ctx.request = self.request
        route_ctx.response = self.response
        route_ctx.provide('URL', self.URL)

    def make_static_handler(self, folder):
        response = self.response
        static_file = self.static_file

        def server_static(fp):
            response.headers.setdefault("Pragma", "cache")
            response.headers.setdefault("Cache-Control", "private")
            return static_file(fp, root=folder)
        return server_static

    def expose_static(self, base_url, folder):
        if not os.path.exists(folder):
            return
        registered = self.static_registry.get_registered(base_url, folder)
        if registered:
            registered.client_apps.add(self)
            return

        self.static_registry.register(base_url, folder, self)
        url = base_url + r"/static/<re((_\d+(\.\d+){2}/)?)><fp.path()>"
        h = self.make_static_handler(folder)
        self.add_route(url, 'GET', handler = h)
