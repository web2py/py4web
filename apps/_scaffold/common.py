"""
This file defines cache, session, and translator T object for the app
These are fixtures that every app needs so probably you will not be editing this file
"""
import os
import sys
import logging
from py4web import Session, Cache, Translator, DAL, Field
from py4web.utils.mailer import Mailer
from py4web.utils.auth import Auth
from py4web.utils.tags import Tags
from py4web.utils.factories import ActionFactory, ButtonFactory
from . import settings

# implement custom loggers form settings.LOGGERS
logger = logging.getLogger("py4web:" + settings.APP_NAME)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
for item in settings.LOGGERS:
    level, filename = item.split(":", 1)
    if filename in ("stdout", "stderr"):
        handler = logging.StreamHandler(getattr(sys, filename))
    else:
        handler = logging.FileHandler(filename)
    handler.setLevel(getattr(logging, level.upper(), "ERROR"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# connect to db
db = DAL(settings.DB_URI, folder=settings.DB_FOLDER, pool_size=settings.DB_POOL_SIZE)

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
T = Translator(settings.T_FOLDER)

# pick the session type that suits you best
if settings.SESSION_TYPE == "cookies":
    session = Session(secret=settings.SESSION_SECRET_KEY)
elif settings.SESSION_TYPE == "redis":
    import redis

    host, port = settings.REDIS_SERVER.split(":")
    # for more options: https://github.com/andymccurdy/redis-py/blob/master/redis/client.py
    conn = redis.Redis(host=host, port=int(port))
    conn.set = lambda k, v, e, cs=conn.set, ct=conn.ttl: (cs(k, v), e and ct(e))
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == "memcache":
    import memcache, time

    conn = memcache.Client(settings.MEMCACHE_CLIENTS, debug=0)
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == "database":
    from py4web.utils.dbstore import DBStore

    session = Session(secret=settings.SESSION_SECRET_KEY, storage=DBStore(db))

auth = Auth(session, db)
auth.registration_requires_confirmation = settings.VERIFY_EMAIL

if settings.SMTP_SERVER:
    auth.mailer = Mailer(
        server=settings.SMTP_SERVER,
        sender=settings.SMTP_SENDER,
        login=settings.SMTP_LOGIN,
        tls=settings.SMTP_TLS,
    )

if auth.db:
    groups = Tags(db.auth_user, "groups")

if settings.USE_PAM:
    from py4web.utils.auth_plugins.pam_plugin import PamPlugin

    auth.register_plugin(PamPlugin())

if settings.USE_LDAP:
    from py4web.utils.auth_plugins.ldap_plugin import LDAPPlugin

    auth.register_plugin(LDAPPlugin(**settings.LDAP_SETTINGS))

if settings.OAUTH2GOOGLE_CLIENT_ID:
    from py4web.utils.auth_plugins.oauth2google import OAuth2Google  # TESTED

    auth.register_plugin(
        OAuth2Google(
            client_id=settings.OAUTH2GOOGLE_CLIENT_ID,
            client_secret=settings.OAUTH2GOOGLE_CLIENT_SECRET,
            callback_url="auth/plugin/oauth2google/callback",
        )
    )
if settings.OAUTH2FACEBOOK_CLIENT_ID:
    from py4web.utils.auth_plugins.oauth2facebook import OAuth2Facebook  # UNTESTED

    auth.register_plugin(
        OAuth2Facebook(
            client_id=settings.OAUTH2FACEBOOK_CLIENT_ID,
            client_secret=settings.OAUTH2FACEBOOK_CLIENT_SECRET,
            callback_url="auth/plugin/oauth2google/callback",
        )
    )

if settings.USE_CELERY:
    from celery import Celery
    # to use from . common import scheduled and then use it accoding to celery docs
    # examples in tasks.py
    scheduler = Celery('apps.%s.tasks' % settings.APP_NAME, broker=settings.CELERY_BROKER)


# we enable auth, which requres sessions, T, db and we make T available to
# the template, although we recommend client-side translations instead
auth.enable(uses=(session, T, db), env=dict(T=T))

unauthenticated = ActionFactory(db, session, T, auth)
authenticated = ActionFactory(db, session, T, auth.user)
