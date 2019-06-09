"""
This file defines the database connection(s) and models
"""
import os
from web3py import DAL, Field
from . import settings
# the DAL object (does not have to be called db but it is a useful convention)
db = DAL(settings.DB_URI, folder=settings.DB_FOLDER, pool_size=settings.DB_POOL_SIZE)

### Define you table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#
