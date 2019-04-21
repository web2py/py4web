from web3py import action, request, abort, redirect, Session, Cache
from . import settings
from . import models

# define global objects that may or may not be used by th actions
session = Session(secret=settings.SESSION_SECRET_KEY)
cache = Cache(size=1000)
db = models.db

# define your actions below, here is an example of /<app_name>/index

@action('index', method='GET')             # the function below is exposed as index.html
@action.uses('generic.html', session, db)  # it uses the generic.html template, a session, and the db
def index():
    message = 'Hello World'
    return dict(message='Welcome to %s' % request.app_name)
