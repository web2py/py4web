import os
from web3py import action, request, abort, redirect, Session, Cache, DAL, Field, Translator
from . import settings
from . import models

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
db = models.db
T = Translator(os.path.join(os.path.dirname(__file__), 'translations'))

# pick the session type that suits you best
if settings.SESSION_TYPE == 'cookies':
    session = Session(secret=settings.SESSION_SECRET_KEY)
elif settings.SESSION_TYPE == 'redis':
    import redis
    host, port = settings.REDIS_SERVER.split(':')
    conn = redis.Redis(host=host, port=int(port))
    conn.set = lambda key, value, expiration, cs=conn.set, ct=conn.ttl: (cs(key, value), expiration != None and ct(expiration))
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == 'memcache':
    import memcache
    conn = memcache.Client(settings.MEMCACHE_CLIENTS, debug=0)
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == 'database':
    from web3py.utils.dbstore import DBStore
    session =  Session(secret=settings.SESSION_SECRET_KEY, storage=DBStore(db))

# define your actions below, here is an example of /<app_name>/index

@action('index', method='GET')                # the function below is exposed as index.html
@action.uses('generic.html', session, db, T)  # it uses the generic.html template, a session, and the db
def index():
    msg = T('Hello World from {name}')
    return dict(message=msg.format(name=request.app_name))

# expose translations in case a single page app needs them in JSON
action('translations')(action.uses(T)(lambda: T.local.language))

