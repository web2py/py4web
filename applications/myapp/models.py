import os
from web3py import DAL, Field
db = DAL('sqlite://test', folder=os.path.join(os.path.dirname(__file__), 'databases'))
db.define_table('thing', Field('name'))
