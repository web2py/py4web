import os

DB_URI = 'sqlite://storage.db'
DB_POOL_SIZE = 1
SESSION_TYPE = 'cookies'
SESSION_SECRET_KEY = '<my secret key>'
MEMCACHE_CLIENTS = ['127.0.0.1:11211']
REDIS_SERVER = 'localhost:6379'
APP_FOLDER = os.path.dirname(__file__)
DB_FOLDER = os.path.join(APP_FOLDER, 'databases')
T_FOLDER = os.path.join(APP_FOLDER, 'translations')
