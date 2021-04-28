import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 28.04.2021 11:31:58 UTC+3, src: https://github.com/tailwindadmin/admin

#import pydal
#from py4web import *
#from apps.myapp.models import db

if not db(db.auth_user).count():
    u1 = {
        "username": "anil",
        "email": "anil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Anil_first",
        "last_name": "Anil_Last",
    }

    u2 = {
        "username": "bnil",
        "email": "bnil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Bnil_first",
        "last_name": "Bnil_Last",
    }

    u3 = {
        "username": "cnil",
        "email": "cnil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Cnil_first",
        "last_name": "Cnil_Last",
    }

    for e in [u1, u2, u3]: db.auth_user.insert(**db.auth_user._filter_fields(e) )
    db.commit()

    #groups = Tags(db.auth_user)

    groups.add(1, 'manager')
    groups.add(2, ['dancer', 'teacher'])
    groups.add(3, 'dancer')
    db.commit()



db.define_table(
    'test_table',
    Field( 'f0', 'string', label='l0'),
    Field( 'f1', 'string', label='l1'),
    Field( 'f2', 'string', label='l2'),
    )
db.commit()

if not db(db.test_table).count():
    populate(db.test_table, n=50)
    db.commit()

db.define_table( 'uploaded_files',
    Field('orig_file_name', requires=IS_NOT_EMPTY(),  ),
    Field("remark",'text',),
    Field('uniq_file_name', requires=IS_NOT_EMPTY(),  ),
    Field('time', 'datetime', editable=False, default = datetime.datetime.now(), requires = IS_DATETIME( )),
    )

db.commit()
#
db.define_table( 'app_images',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    )
    
if not db(db.app_images).count():
    db.app_images.insert(f0='dist/images/login-new.jpeg', )

db.commit()

db.define_table( 'css_js_files',
    Field('orig_file_path', requires=IS_NOT_EMPTY(),  ),
    Field('found_in_file', default='' ),
    Field('app_name', default='' ),
    )

db.commit()

db.define_table(
    'dfforms0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodals0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginA0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregisterA0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="1", f1="<button class=\"bg-blue-500 hover:bg-blue-800 text-white font-light py-1 px-2 rounded-full\"> Twitter </button>", f2="4500", f3="4600", f4="<span class=\"text-green-500\"><i class=\"fas fa-arrow-up\"></i>5%</span>")
    db.tindex0.insert(f0="2", f1="<button class=\"bg-primary hover:bg-primary-dark text-white font-light py-1 px-2 rounded-full\"> Facebook </button>", f2="10000", f3="3000", f4="<span class=\"text-red-500\"><i class=\"fas fa-arrow-down\"></i>65%</span>")
    db.tindex0.insert(f0="3", f1="<button class=\"bg-success hover:bg-success-dark text-white font-light py-1 px-2 rounded-full\"> Amazon </button>", f2="10000", f3="3000", f4="<span class=\"text-red-500\"><i class=\"fas fa-arrow-down\"></i>65%</span>")
    db.tindex0.insert(f0="4", f1="<button class=\"bg-blue-500 hover:bg-blue-800 text-white font-light py-1 px-2 rounded-full\"> Microsoft </button>", f2="10000", f3="3000", f4="<span class=\"text-green-500\"><i class=\"fas fa-arrow-up\"></i>65%</span>")
    db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="Intro to CSS", f1="Adam", f2="858")
    db.ttables0.insert(f0="A Long and Winding Tour of the History of UI Frameworks and Tools and the Impact on Design", f1="Adam", f2="112")
    db.ttables0.insert(f0="Into to JavaScript", f1="Chris", f2="1,280")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="Intro to CSS", f1="Adam", f2="858")
    db.ttables1.insert(f0="A Long and Winding Tour of the History of UI Frameworks and Tools and the Impact on Design", f1="Adam", f2="112")
    db.ttables1.insert(f0="Into to JavaScript", f1="Chris", f2="1,280")
    db.commit()

if not db(db.ttables2).count():
    db.ttables2.insert(f0="Micheal Clarke", f1="Sydney", f2="MS", f3="900 $", f4="<i class=\"fas fa-check text-green-500 mx-2\"></i>", f5="<a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-eye\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-edit\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-red-500\"><i class=\"fas fa-trash\"></i></a>")
    db.ttables2.insert(f0="Rickey Ponting", f1="Sydney", f2="MS", f3="300 $", f4="<i class=\"fas fa-times text-red-500 mx-2\"></i>", f5="<a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-eye\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-edit\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-red-500\"><i class=\"fas fa-trash\"></i></a>")
    db.ttables2.insert(f0="Micheal Clarke", f1="Sydney", f2="MS", f3="900 $", f4="<i class=\"fas fa-check text-green-500 mx-2\"></i>", f5="<a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-eye\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-edit\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-red-500\"><i class=\"fas fa-trash\"></i></a>")
    db.ttables2.insert(f0="Micheal Clarke", f1="Sydney", f2="MS", f3="900 $", f4="<i class=\"fas fa-check text-green-500 mx-2\"></i>", f5="<a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-eye\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-edit\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-red-500\"><i class=\"fas fa-trash\"></i></a>")
    db.ttables2.insert(f0="Micheal Clarke", f1="Sydney", f2="MS", f3="900 $", f4="<i class=\"fas fa-check text-green-500 mx-2\"></i>", f5="<a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-eye\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-white\"><i class=\"fas fa-edit\"></i></a> <a class=\"bg-teal-300 cursor-pointer rounded p-1 mx-1 text-red-500\"><i class=\"fas fa-trash\"></i></a>")
    db.commit()
