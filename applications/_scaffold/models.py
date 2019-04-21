import os
from web3py import DAL, Field
from . import settings

### Establish a database connection
db = DAL(settings.DB_URI, 
         folder=os.path.join(os.path.dirname(__file__), 'databases'),
         pool_size=settings.DB_POOL_SIZE)

### Define you table below
#
# db.define_table('thing', Field('name'))
#
