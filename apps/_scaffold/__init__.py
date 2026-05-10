# check compatibility
import py4web

# Use a real check (not assert) so the guard survives ``python -O``.
if not py4web.check_compatible("1.20190709.1"):
    raise RuntimeError("py4web 1.20190709.1+ required")

# by importing controllers you expose the actions defined in it
from . import controllers

# by importing db you expose it to the _dashboard/dbadmin
from .models import db

# import the scheduler
from .tasks import scheduler

# optional parameters
__version__ = "0.0.0"
__author__ = "you <you@example.com>"
__license__ = "anything you want"
