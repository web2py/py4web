
import sys
import os
import click
import importlib
import traceback

from .globs import app, request, response, static_file
from .loggers import error_logger, get_error_snapshot
from .utils import module2filename


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
    DIRTY_APPS = {}

    @classmethod
    def check_dirty(cls):
        """Should be installed by client."""
        app_name = request.app_name
        DIRTY_APPS = cls.DIRTY_APPS
        if app_name in DIRTY_APPS:
            cls.import_app(app_name)
            del DIRTY_APPS[app_name]
        ## APP_WATCH tasks, if used by any app
        # try_app_watch_tasks()

    @classmethod
    def clear_routes(cls, app_name=''):
        if app_name and app_name[0] != '/':
            app_name = '/' + app_name
        routes = app_name + '/*'
        app.router.remove(routes)
        if app_name:
            app.router.remove(app_name)

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

            try:
                module = cls.MODULES.get(app_name)
                if not module:
                    click.echo(f"[ ] loading {app_name} ...")
                else:
                    click.echo(f"[ ] reloading {app_name} ...")
                    # forget the module
                    del cls.MODULES[app_name]
                    _clear_modules(module_name)
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

        cls.expose_static(path)

    @classmethod
    def expose_static(cls, app_path):
        path = app_path
        static_folder = os.path.join(path, "static")
        if not os.path.exists(static_folder):
            return

        app_name = path.split(os.path.sep)[-1]
        prefix = "" if app_name == "_default" else ("/%s" % app_name)

        @app.route(prefix + r"/static/<re((_\d+(\.\d+){2}/)?)><fp.path()>")
        def server_static(fp, static_folder=static_folder):
            filename = fp
            response.headers.setdefault("Pragma", "cache")
            response.headers.setdefault("Cache-Control", "private")
            return static_file(filename, root=static_folder)

    @classmethod
    def register_routes(cls):
        routes = []
        for route in app.routes.values():
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
