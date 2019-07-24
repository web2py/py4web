import os
from py4web import DAL, Field
db = DAL('sqlite://test', folder=os.path.join(os.path.dirname(__file__), 'databases'))
db.define_table('thing', Field('name'))
