import sys
from .core import (
    request,
    response,
    abort,

    check_compatible,
    import_apps,
    reload_apps,
    wsgi,
    BaseAction,

    URL,
    redirect,
    Cache,

    HTTP,
    P4WException,
)

from .fixtures import (
    Template,
    Session,
)

__all__ = (
    'request',
    'response',
    'abort',

    'check_compatible',
    'import_apps',
    'reload_apps',
    'wsgi',
    'Action',

    'URL',
    'redirect',
    'Cache',

    'Template',
    'Session',

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
