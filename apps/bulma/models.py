import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 05.05.2021 11:21:30 UTC+3, src: https://github.com/BulmaTemplates/bulma-templates

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
    db.app_images.insert(f0='images/admin.png', )
    db.app_images.insert(f0='images/band.png', )
    db.app_images.insert(f0='images/blog.png', )
    db.app_images.insert(f0='images/cards.png', )
    db.app_images.insert(f0='images/cheatsheet.png', )
    db.app_images.insert(f0='images/cover.png', )
    db.app_images.insert(f0='images/documentation.jpg', )
    db.app_images.insert(f0='images/forum.png', )
    db.app_images.insert(f0='images/hello-parallax.png', )
    db.app_images.insert(f0='images/ghost-blog.png', )
    db.app_images.insert(f0='images/hero.png', )
    db.app_images.insert(f0='images/inbox.png', )
    db.app_images.insert(f0='images/instaalbum.png', )
    db.app_images.insert(f0='images/kanban.png', )
    db.app_images.insert(f0='images/kanban2.png', )
    db.app_images.insert(f0='images/landing.png', )
    db.app_images.insert(f0='images/login.png', )
    db.app_images.insert(f0='images/modalcards.png', )
    db.app_images.insert(f0='images/neumorphic-login.png', )
    db.app_images.insert(f0='images/personal.png', )
    db.app_images.insert(f0='images/showcase.png', )
    db.app_images.insert(f0='images/register.png', )
    db.app_images.insert(f0='images/tabs.png', )
    db.app_images.insert(f0='images/contact.png', )
    db.app_images.insert(f0='images/blog2.png', )
    db.app_images.insert(f0='images/absurd2.png', )
    db.app_images.insert(f0='images/fav_icon.png', )
    db.app_images.insert(f0='images/favicon.png', )
    db.app_images.insert(f0='images/bulma.png', )
    db.app_images.insert(f0='images/first-post.png', )
    db.app_images.insert(f0='images/undraw_Camera_re_cnp4.svg', )

db.commit()

db.define_table( 'app_css_js',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    )

db.define_table( 'app_js_script',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    Field('in_html', ),
    )

db.define_table( 'app_html_text',
    Field('f0', requires=IS_NOT_EMPTY(), ),
    Field('key',requires=IS_NOT_EMPTY(), ),
    Field('in_html', ),
    )

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
    'dfdocumentation0',
    Field('f0','string', length=1024, ),
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
    'dfloginA0',
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
    'dfregisterA0',
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
