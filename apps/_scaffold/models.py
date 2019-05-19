import os
from web3py import DAL, Field
from . import settings

print('in models')

db = DAL(settings.DB_URI, folder=settings.DB_FOLDER, pool_size=settings.DB_POOL_SIZE)

### Define you table below
#
# db.define_table('thing', Field('name'))
#
