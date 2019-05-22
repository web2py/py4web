"""
This file defines cache, session, and translator T object for the app
These are fixtures that every app needs so probably you will not be editing this file
"""
import os
from web3py import Session, Cache, Translator
from web3py.utils.auth import Auth
from . import settings
from .models import db

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
T = Translator(settings.T_FOLDER)

# pick the session type that suits you best
if settings.SESSION_TYPE == 'cookies':
    session = Session(secret=settings.SESSION_SECRET_KEY)
elif settings.SESSION_TYPE == 'redis':
    import redis
    host, port = settings.REDIS_SERVER.split(':')
    # for more options: https://github.com/andymccurdy/redis-py/blob/master/redis/client.py
    conn = redis.Redis(host=host, port=int(port))
    conn.set = lambda k, v, e, cs=conn.set, ct=conn.ttl: (cs(k, v), e and ct(e))
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == 'memcache':
    import memcache, time
    conn = memcache.Client(settings.MEMCACHE_CLIENTS, debug=0)
    session = Session(secret=settings.SESSION_SECRET_KEY, storage=conn)
elif settings.SESSION_TYPE == 'database':
    from web3py.utils.dbstore import DBStore
    session =  Session(secret=settings.SESSION_SECRET_KEY, storage=DBStore(db))

auth = Auth(db, session)
auth.base_url = '/_scaffold/auth/' ### FIX THIS SHOULD BE SOMEWHAT AUTOMATIC
auth.enable(route='auth/<path:path>')
