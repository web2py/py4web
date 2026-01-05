"""
This file defines common fixtures and utilities for the _dashboard app.
"""

import functools
import traceback

from py4web import Translator, action
from py4web.core import Fixture, Session, abort
from py4web.utils.factories import ActionFactory

from . import settings

# #######################################################
# Session
# #######################################################
session = Session()

# #######################################################
# Translator
# #######################################################
T = Translator(settings.T_FOLDER)


# #######################################################
# Authentication/Authorization Fixture
# #######################################################
class Logged(Fixture):
    """Fixture to ensure user is logged in"""
    
    def __init__(self, session):
        self.__prerequisites__ = [session]
        self.session = session

    def on_request(self, context):
        user = self.session.get("user")
        if not user or not user.get("id"):
            abort(403)


# #######################################################
# Decorators and Fixtures
# #######################################################
logged = Logged(session)
authenticated = ActionFactory(logged)
session_secured = action.uses(logged)


# #######################################################
# Error catching decorator
# #######################################################
def catch_errors(func):
    """Wraps APIs that return a status=success/error and includes a traceback in response"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            result = {"status": "error", "traceback": traceback.format_exc()}
        return result

    return wrapper
