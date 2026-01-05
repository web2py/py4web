"""
This file defines the database models and related utilities for the _dashboard app.
"""

import sys

from py4web.core import DAL


def make_safe(db):
    """
    Makes a database safe for dashboard access by wrapping field defaults/updates
    in error handlers to prevent accessing forbidden app methods.
    """
    def make_safe_field(func):
        def wrapper():
            try:
                return func()
            except Exception as exp:
                print(exp)
                print("Warning: _dashboard trying to access a forbidden method of app")
                return None
        return wrapper

    for table in db:
        for field in table:
            if callable(field.default):
                field.default = make_safe_field(field.default)
            if callable(field.update):
                field.update = make_safe_field(field.update)
