
from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate 

#with python cli
#import pydal
#from py4web import *
#from apps.vuestic.models import db

my_app_name = "vuestic"

if not db(db.auth_user).count():
    body = {
        "username": "nil",
        "email": "nil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        #"password": str(pydal.validators.CRYPT()("xyz12345")[0]),
        "first_name": "MainUser",
        "last_name": "MainUserLast",
    }
    db.auth_user.insert(**body)
    db.commit()

db.define_table(
    'test_table',
    Field( 'f0', 'string', label='l0'),
    Field( 'f1', 'string', label='l1'),
    Field( 'f2', 'string', label='l2'),
    )

if not db(db.test_table).count():
    populate(db.test_table, n=10)
    db.commit()