import sys

__author__ = "Massimo Di Pierro <massimo.dipierro@gmail.com>"
__license__ = "BSD-3-Clause"
__version__ = "1.20250215.1"


def _maybe_gevent():
    for arg in sys.argv[1:]:
        if "gevent" in arg.lower():
            from gevent import monkey

            monkey.patch_all()
            break


_maybe_gevent()


from .core import HTTP  # checks for version compatibility; bottle
from .core import URL  # custom helper
from .core import Field  # pydal
from .core import Translator  # from pluralize
from .core import action  # main py4web decorator
from .core import render  # yatl
from .core import (DAL, Cache, Condition, Flash, Session, abort,
                   check_compatible, redirect, request, response, safely)
