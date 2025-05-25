"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""

import os

from py4web.core import required_folder

# mode (default or development)
MODE = os.environ.get("PY4WEB_MODE")

# db settings
APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]

# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = required_folder(APP_FOLDER, "databases")
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 1
DB_MIGRATE = True
DB_FAKE_MIGRATE = False

# location where static files are stored:
STATIC_FOLDER = required_folder(APP_FOLDER, "static")

# location where to store uploaded files:
UPLOAD_FOLDER = required_folder(APP_FOLDER, "uploads")

# send verification email on registration
VERIFY_EMAIL = MODE != "development"

# complexity of the password 0: no constraints, 50: safe!
PASSWORD_ENTROPY = 0 if MODE == "development" else 50

# account requires to be approved ?
REQUIRES_APPROVAL = False

# auto login after registration
# requires False VERIFY_EMAIL & REQUIRES_APPROVAL
LOGIN_AFTER_REGISTRATION = False

# ALLOWED_ACTIONS in API / default Forms:
# ["all"]
# ["login", "logout", "request_reset_password", "reset_password", \
#  "change_password", "change_email", "profile", "config", "register",
#  "verify_email", "unsubscribe"]
# Note: if you add "login", add also "logout"
ALLOWED_ACTIONS = ["all"]

# email settings
SMTP_SSL = False
SMTP_SERVER = None
SMTP_SENDER = "you@example.com"
SMTP_LOGIN = "username:password"
SMTP_TLS = False

# session settings
SESSION_TYPE = "cookies"
SESSION_SECRET_KEY = None  # or replace with your own secret
MEMCACHE_CLIENTS = ["127.0.0.1:11211"]
REDIS_SERVER = "localhost:6379"

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename:format" filename can be stderr or stdout

# Disable default login when using OAuth
DEFAULT_LOGIN_ENABLED = True

# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = None
OAUTH2GOOGLE_CLIENT_SECRET = None

# Single sign on Google, with stored credentials for scopes (will be used if provided).
# set it to something like os.path.join(APP_FOLDER, "private/credentials.json"
OAUTH2GOOGLE_SCOPED_CREDENTIALS_FILE = None

# single sign on Okta (will be used if provided. Please also add your tenant
# name to py4web/utils/auth_plugins/oauth2okta.py. You can replace the XXX
# instances with your tenant name.)
OAUTH2OKTA_CLIENT_ID = None
OAUTH2OKTA_CLIENT_SECRET = None

# single sign on Google (will be used if provided)
OAUTH2FACEBOOK_CLIENT_ID = None
OAUTH2FACEBOOK_CLIENT_SECRET = None

# single sign on GitHub (will be used if provided)
OAUTH2GITHUB_CLIENT_ID = None
OAUTH2GITHUB_CLIENT_SECRET = None

# enable PAM
USE_PAM = False

# enable LDAP
USE_LDAP = False
LDAP_SETTINGS = {
    "mode": "ad",  # Microsoft Active Directory
    "server": "mydc.domain.com",  # FQDN or IP of one Domain Controller
    "base_dn": "cn=Users,dc=domain,dc=com",  # base dn, i.e. where the users are located
}

# i18n settings
T_FOLDER = required_folder(APP_FOLDER, "translations")

# Scheduler settings
USE_SCHEDULER = False
SCHEDULER_MAX_CONCURRENT_RUNS = 1

# Celery settings (alternative to the build-in scheduler)
USE_CELERY = False
CELERY_BROKER = "redis://localhost:6379/0"

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
