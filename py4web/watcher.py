import inspect
import pathlib
import os
import logging
import click
import asyncio
import traceback
import threading
from watchgod import awatch
from .core.core_events import core_event_bus, CoreEvents
from .core.globs import request_hooks


DIRTY_APPS = set()  # apps that need to be reloaded (lazy watching)


APP_WATCH = {"files": dict(), "handlers": dict(), "tasks": dict()}

""" Decorator that binds a func as an watchdog handler of non-'.py' files.
Paths to files must be relative to app, w/o app name(folder).

@app_watch_handler(['static/sass/all.sass', 'static/sass/main.sass'])
def sass_compile(changed_files):
    print(changed_files); # paths of files that changed, for info
    sass.compile()
"""


def app_watch_handler(watched_app_subpaths):
    stack = inspect.stack
    invoker = pathlib.Path(stack()[1].filename)
    apps_path = pathlib.Path(os.environ["PY4WEB_APPS_FOLDER"])
    app = invoker.relative_to(os.environ["PY4WEB_APPS_FOLDER"]).parts[0]

    def decorator(func):
        handler = "{}.{}".format(func.__module__, func.__name__)
        APP_WATCH["handlers"][handler] = func
        for subpath in watched_app_subpaths:
            app_path = apps_path.joinpath(app, subpath).as_posix()
            if app_path not in APP_WATCH["files"]:
                APP_WATCH["files"][app_path] = []
            APP_WATCH["files"][app_path].append(handler)
        return func

    return decorator


def try_app_watch_tasks():
    if APP_WATCH["tasks"]:
        tried_tasks = []
        for handler in APP_WATCH["tasks"]:
            changed_files_dict = APP_WATCH["tasks"][handler]
            try:
                APP_WATCH["handlers"][handler](changed_files_dict.keys())
                tried_tasks.append(handler)
            except Exception:
                logging.error(traceback.format_exc())
        ## remove executed tasks from register
        for handler in tried_tasks:
            del APP_WATCH["tasks"][handler]


def watch(apps_folder, server_config, mode="sync"):
    def watch_folder_event_loop(apps_folder):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(watch_folder(apps_folder))

    async def watch_folder(apps_folder):
        click.echo(
            "watching (%s-mode) python file changes in: %s" % (mode, apps_folder)
        )
        async for changes in awatch(os.path.join(apps_folder)):
            apps = []
            for subpath in [pathlib.Path(pair[1]) for pair in changes]:
                name = subpath.relative_to(apps_folder).parts[0]
                if subpath.suffix == ".py":
                    apps.append(name)
                ## manage `app_watch_handler` decorators
                elif subpath.as_posix() in APP_WATCH["files"]:
                    handlers = APP_WATCH["files"][subpath.as_posix()]
                    for handler in handlers:
                        if handler not in APP_WATCH["tasks"]:
                            APP_WATCH["tasks"][handler] = {}
                        APP_WATCH["tasks"][handler][subpath.as_posix()] = True

            if mode == "lazy":
                DIRTY_APPS.update(apps)
            else:
                core_event_bus.emit(CoreEvents.RELOAD_APPS, *apps)
                try_app_watch_tasks()

    if server_config["number_workers"] > 1:
        click.echo("--watch option has no effect in multi-process environment \n")
        return
    elif server_config["server"].startswith(("wsgiref", "waitress", "rocket")):
        # these servers block the main thread so we open a new thread for the file watcher
        threading.Thread(
            target=watch_folder_event_loop, args=(apps_folder,), daemon=True
        ).start()
    elif server_config["server"] == "tornado":
        # tornado delegate to asyncio so we add a future into the event loop
        asyncio.ensure_future(watch_folder(apps_folder))
    elif server_config["server"].startswith("gevent"):
        watch_folder_event_loop(apps_folder)
    else:
        # should never happen
        return

    if mode == "lazy":
        request_hooks.before.add(lazy_trigger)


def lazy_trigger(*a, **kw):
    core_event_bus.emit(CoreEvents.RELOAD_APPS, *DIRTY_APPS)
    DIRTY_APPS.clear()
    try_app_watch_tasks()
