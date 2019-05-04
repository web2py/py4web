import os
from web3py import DAL, Field
from . import settings

### Establish a database connection
APP_FOLDER = os.path.dirname(__file__)
DB_FOLDER = os.path.join(APP_FOLDER, 'databases')

db = DAL(settings.DB_URI, folder=DB_FOLDER, pool_size=settings.DB_POOL_SIZE)

### Define you table below
#
# db.define_table('thing', Field('name'))
#
