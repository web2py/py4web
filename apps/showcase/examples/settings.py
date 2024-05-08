"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""
import os

MODE = os.environ.get("PY4WEB_DASHBOARD_MODE", "none")
# db settings
APP_FOLDER = os.path.dirname(os.path.dirname(__file__))
APP_NAME = os.path.split(APP_FOLDER)[-1]
# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = os.path.join(APP_FOLDER, "databases")
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 1
DB_MIGRATE = MODE == "full"
DB_FAKE_MIGRATE = False  # maybe?

# location where to store uploaded files:
UPLOAD_FOLDER = os.path.join(APP_FOLDER, "uploads")

# send email on regstration
VERIFY_EMAIL = False

# account requires to be approved ?
REQUIRES_APPROVAL = False

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
]  # syntax "severity:filename" filename can be stderr or stdout


# i18n settings
T_FOLDER = os.path.join(APP_FOLDER, "translations")

## hcaptcha config
HCAPTCHA_SITE_KEY = ""
HCAPTCHA_SECRET_KEY = ""
HCAPTCHA_VERIFY_URL = "https://hcaptcha.com/siteverify"
