"""
The _dashboard app provides a web-based interface for managing py4web applications.

This app follows the standard py4web structure with:
- settings.py: configuration and environment variables
- common.py: shared fixtures (session, translator, authentication)
- models.py: database models and utilities
- controllers.py: action handlers for routes

Additional modules include:
- utils.py: helper functions
- diff2kryten.py: utility for diffing files
"""

# check compatibility
import py4web

assert py4web.check_compatible("1.20190709.1")

# by importing controllers you expose the actions defined in it
from . import controllers

# optional parameters
__version__ = "20260105"
__author__ = "Massimo Di Pierro <massimo.dipierro@gmail.com>"
__license__ = "BSD-3-Clause"
