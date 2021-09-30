import re
import sys
import os
import click
import importlib
import traceback

from .globs import app as om_app
from .loggers import error_logger, get_error_snapshot
from .utils import module2filename

from .core_events import core_event_bus, CoreEvents


def _clear_modules(module_name):
    # all files/submodules
    names = [
        name
        for name in sys.modules
        if (name + ".").startswith(module_name + ".")
    ]
    for name in names:
        del sys.modules[name]


class Reloader:

    ROUTES = None
    MODULES = {}
    ERRORS = {}

    @classmethod
    def install_reloader_hook(cls):
        core_event_bus.on(CoreEvents.RELOAD_APPS, cls.reimport_apps)

    @classmethod
    def expand_apps_to_reload(cls, *app_names):
        ret = set()
        for app_name in app_names:
            ret.add(app_name)
            module_name = f"apps.{app_name}"
            app = getattr(sys.modules[module_name], 'app', None)
            get_all_clients = getattr(app, 'get_all_clients', None)
            if not get_all_clients:
                continue
            clients = get_all_clients()
            for m_name in (capp._module_name for capp in clients):
                if not re.match(r'apps\.\w+', m_name):
                    continue
                ret.add(m_name.split('.')[1])
        return ret

    @classmethod
    def clear_routes(cls, app_name=''):
        if app_name and app_name[0] != '/':
            app_name = '/' + app_name
        routes = app_name + '/*'
        om_app.router.remove(routes)
        if app_name:
            om_app.router.remove(app_name)

    @classmethod
    def reimport_apps(cls, *apps):
        if not apps:
            return
        apps = cls.expand_apps_to_reload(*apps)
        for app in apps:
            _clear_modules(f"apps.{app}")
            cls.clear_routes(app)
        for app in apps:
            cls.import_app(app, clear_before_import=False)

    @classmethod
    def import_apps(cls):
        """Import or reimport modules and exposed static files"""
        cls.clear_routes()
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        # if first time reload dummy top module
        if not cls.MODULES:
            path = os.path.join(folder, "__init__.py")
            loader = importlib.machinery.SourceFileLoader("apps", path)
            loader.load_module()
        # Then load all the apps as submodules
        for app_name in os.listdir(folder):
            cls.import_app(app_name, clear_before_import=False)

    @classmethod
    def import_app(cls, app_name, clear_before_import=True):
        if clear_before_import:
            cls.clear_routes(app_name)
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        path = os.path.join(folder, app_name)
        init = os.path.join(path, "__init__.py")

        if os.path.isdir(path) and not path.endswith("__") and os.path.exists(init):
            module_name = f"apps.{app_name}"
            is_loaded = module_name in sys.modules
            try:
                module = cls.MODULES.get(app_name)
                if not module:
                    if is_loaded:
                        click.secho(f"[X] already loaded {app_name}       ", fg="green")
                    else:
                        click.echo(f"[ ] loading {app_name} ...")
                else:
                    if is_loaded:
                        click.secho(f"[X] already reloaded {app_name}       ", fg="green")
                    else:
                        click.echo(f"[ ] reloading {app_name} ...")
                        # forget the module
                        del cls.MODULES[app_name]

                if is_loaded:
                    cls.MODULES[app_name] = module
                    cls.ERRORS[app_name] = None
                else:
                    module = importlib.machinery.SourceFileLoader(
                        module_name, init
                    ).load_module()
                    click.secho(f"\x1b[A[X] loaded {app_name}       ", fg="green")
                    cls.MODULES[app_name] = module
                    cls.ERRORS[app_name] = None
            except Exception as err:
                cls.ERRORS[app_name] = traceback.format_exc()
                error_logger.log(
                    app_name, get_error_snapshot()
                )
                click.secho(
                    f"\x1b[A[FAILED] loading {app_name} ({err})",
                    fg="red",
                )
                # clear all files/submodules if the loading fails
                _clear_modules(module_name)
                return None

    @classmethod
    def register_routes(cls):
        routes = []
        for route in om_app.routes.values():
            for method, method_obj in route.methods.items():
                func = method_obj.handler
                rule = route.rule
                routes.append(
                    {
                        "rule": rule,
                        "method": method,
                        "filename": module2filename(func.__module__),
                        "action": func.__name__,
                    }
                )
        cls.ROUTES = sorted(routes, key=lambda item: item["rule"])
