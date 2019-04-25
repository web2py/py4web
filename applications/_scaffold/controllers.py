from web3py import action, request, abort, redirect, Session, Cache, DAL, Field
from . import settings
from . import models

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
db = models.db
session = Session(secret=settings.SESSION_SECRET_KEY)

## for redis sessions ##
# import redis
# conn = redis.Redis(host='localhost', port=6379)
# conn.set = lambda key, value, expire, c=conn: (c.set(key,value), c.ttl(expiration))
# session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)

## for memcache sessions ##
# import memcache
# conn = memcache.Client(['127.0.0.1:11211'], debug=0)
# session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)

## for sessions in db ##
# from web3py.utils.dbstore import DBStore
# session =  Session(secret=settings.SESSION_SECRET_KEY, storage=DBStore(db))

# define your actions below, here is an example of /<app_name>/index

@action('index', method='GET')             # the function below is exposed as index.html
@action.uses('generic.html', session, db)  # it uses the generic.html template, a session, and the db
def index():
    message = 'Hello World'
    return dict(message='Welcome to %s' % request.app_name)
