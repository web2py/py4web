"""
This file defines the settings for the _dashboard app.
"""

import os

# dashboard mode
MODE = os.environ.get("PY4WEB_DASHBOARD_MODE", "none")

# folder where apps are stored
FOLDER = os.environ["PY4WEB_APPS_FOLDER"]

# app names that can be managed
APP_NAMES = os.environ.get("PY4WEB_APP_NAMES")

# app folder
APP_FOLDER = os.path.dirname(__file__)

# translations folder
T_FOLDER = os.path.join(APP_FOLDER, "translations")

# py4web ignore file name
PY4WEB_IGNORE = ".py4web_ignore"
