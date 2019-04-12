from web3py import DAL, Field
db = DAL('sqlite://test')
db.define_table('thing', Field('name'))
