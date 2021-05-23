import sys

if len(sys.argv) > 1 and sys.argv[1] == "--usegevent":
    sys.argv.pop(1)
    from gevent import monkey

    monkey.patch_all()


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

__author__ = "Massimo Di Pierro <massimo.dipierro@gmail.com>"
__license__ = "BSDv3"
__version__ = "1.20210522.2"
