"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""
import os
# db settings
APP_FOLDER = os.path.dirname(__file__)
# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = os.path.join(APP_FOLDER, 'databases')
DB_URI = 'sqlite://storage.db'
DB_POOL_SIZE = 1

# session settings
SESSION_TYPE = 'cookies'
SESSION_SECRET_KEY = '<my secret key>'
MEMCACHE_CLIENTS = ['127.0.0.1:11211']
REDIS_SERVER = 'localhost:6379'

# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = None
OAUTH2GOOGLE_CLIENT_SECRET = None

# single sign on Google (will be used if provided)
OAUTH2FACEBOOK_CLIENT_ID = None
OAUTH2FACEBOOK_CLIENT_SECRET = None

# enable PAM
USE_PAM = False

# enable LDAP
USE_LDAP = False
LDAP_SETTING = {
    'mode': 'ad',
    'server': 'my.domain.controller',                                                                  
    'base_dn': 'ou=Users,dc=domain,dc=com'} 

# i18n settings
T_FOLDER = os.path.join(APP_FOLDER, 'translations')

# try import private settings
try: from . settings_private import *
except: pass
