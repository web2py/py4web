import sys
import re
from .core import (
    request,
    response,
    abort,

    check_compatible,
    import_apps,
    reload_apps,
    wsgi,
    BaseAction,
    App,

    redirect,
    Cache,

    HTTP,
    P4WException,
)

from .fixtures import (
    Template,
    Session,
    DAL,
)
from .app_methods import (
    URL
)

from pydal import Field

__all__ = (
    'request',
    'response',
    'abort',

    'check_compatible',
    'import_apps',
    'reload_apps',
    'wsgi',
    'Action',
    'App',

    'URL',
    'redirect',
    'Cache',

    'Template',
    'Session',
    'DAL',
    'Field',

    'HTTP',
    'P4WException',
)

__author__ = "Massimo Di Pierro <massimo.dipierro@gmail.com>"
__license__ = "BSDv3"
__version__ = "1.20210920.1"


def _maybe_gevent():
    for arg in sys.argv[1:]:
        if 'gevent' in arg.lower():
            from gevent import monkey
            monkey.patch_all()
            break
_maybe_gevent()  # noqa


class Action(BaseAction):
    def _parse_uses_args(self, fixtures):
        return [
            Template(f) if isinstance(f, str) else f
            for f in fixtures
        ]

    def _parse_action_args(self, args, kw):
        # ('index', 'GET') - path ='index'
        # (':index', 'GET') - get path from route_map[`index`], name = index, if not passed: is not mounted
        # ('home: pages/home', 'index', 'GET') - name = home, path = pages/home
        # (':home: pages/home', 'index', 'GET') - get path from route_map[`home`], if not passed: path ='pages/home', name = home,
        # (':home:name:pages/home', 'index', 'GET') - get path from route_map[`home`], if not passed: path ='pages/home', name = home,

        path_, name, prop, kw = args[0], None, None, kw
        method = kw.get('method')

        path = path_
        prop = re.match(r':(\w+):?', path)
        if prop:
            path = path[prop.end():]
            prop = prop.group(1)
        name = re.match(r'(\w+):', path)
        if name:
            path = path[name.end():]
            name = name.group(1)
        path = path.strip()
        if name and not (path or prop):
            raise RuntimeError(f'Invalid route: {path_}')

        args = args[1:]
        if args:
            if method:
                raise TypeError(f'Got 2 values for method: {args}, {method}')
            method = args[0]
            args = args[1:]
        if args:
            raise TypeError(f'Unexpected args: {args}')
        method = method or 'GET'
        return path, method, name, prop, kw


'''
from .core import (
    action,  # main py4web decorator
    request,
    response,
    redirect,
    abort,
    HTTP,  # bottle
    DAL,
    Field,  # pydal
    render,  # yatl
    Translator,  # from pluralize
    Session,
    Cache,
    Flash,
    user_in,  # additional fixtures
    URL,  # custom helper
    check_compatible,
)  # checks for version compatibility
'''
