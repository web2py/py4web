from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 08.12.2020 08:51:34 UTC+3, src: https://github.com/BulmaTemplates/bulma-templates

#

#import pydal

#from py4web import *
#from apps.myapp.models import db

#if not len( db().select(db.auth_user.id) ):
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
db.commit()

if not db(db.test_table).count():
    populate(db.test_table, n=10)
    db.commit()


db.define_table(
    'dfadmin0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadmin1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfband0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforum0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfhelloXparallax0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfhelloXparallax1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinstaAlbum0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinstaAlbum1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinstaAlbum2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinstaAlbum3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfkanban0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfkanbanXsearchX0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflanding0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflogin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfneumorphicXlogin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpersonal0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpersonal1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpersonal2',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfshowcase0',
    )
db.commit()

db.define_table(
    'dfshowcase1',
    )
db.commit()

db.define_table(
    'dfshowcase2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregister0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontact0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontact1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontact2',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblogXtailsaw0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblogXtailsaw1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsearch0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tadmin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpersonal0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttabs0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

if not db(db.tadmin0).count():
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.tadmin0.insert(f0="<i class=\"fa fa-bell-o\"></i>", f1="Lorum ipsum dolem aire", f2="<a class=\"button is-small is-primary\" href=\"#\">Action</a>")
    db.commit()

if not db(db.tpersonal0).count():
    db.tpersonal0.insert(f0="Address:", f1="Gurus Lab")
    db.tpersonal0.insert(f0="Phone:", f1="0123-456789")
    db.tpersonal0.insert(f0="Email:", f1="minion@despicable.me")
    db.commit()

if not db(db.ttabs0).count():
    db.ttabs0.insert(f0="Three", f1="Four")
    db.ttabs0.insert(f0="Five", f1="Six")
    db.ttabs0.insert(f0="Seven", f1="Eight")
    db.ttabs0.insert(f0="Nine", f1="Ten")
    db.ttabs0.insert(f0="Eleven", f1="Twelve")
    db.commit()
