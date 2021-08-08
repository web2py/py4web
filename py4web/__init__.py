import sys

__author__ = "Massimo Di Pierro <massimo.dipierro@gmail.com>"
__license__ = "BSDv3"
__version__ = "1.20210807.1"


def _maybe_gevent():
    for arg in sys.argv[1:]:
        if 'gevent' in arg.lower():
            from gevent import monkey
            monkey.patch_all()
            break
_maybe_gevent()


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
    Current,
    Flash,
    user_in,  # additional fixtures
    URL,  # custom helper
    check_compatible,
)  # checks for version compatibility

