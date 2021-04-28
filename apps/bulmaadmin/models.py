from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 03.12.2020 12:09:10 UTC+3
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
    'dfforms0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms6',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelements0',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    Field('f10','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="<abbr title=\"Position\">Pos</abbr>", f1="Team", f2="<abbr title=\"Played\">Pld</abbr>", f3="<abbr title=\"Won\">W</abbr>", f4="<abbr title=\"Drawn\">D</abbr>", f5="<abbr title=\"Lost\">L</abbr>", f6="<abbr title=\"Goals for\">GF</abbr>", f7="<abbr title=\"Goals against\">GA</abbr>", f8="<abbr title=\"Goal difference\">GD</abbr>", f9="<abbr title=\"Points\">Pts</abbr>", f10="Qualification or relegation")
    db.ttables0.insert(f0="1", f1="<a href=\"https://en.wikipedia.org/wiki/Leicester_City_F.C.\" title=\"Leicester City F.C.\">Leicester City</a> <strong>(C)</strong>", f2="38", f3="23", f4="12", f5="3", f6="68", f7="36", f8="+32", f9="81", f10="<a href=\"https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.ttables0.insert(f0="2", f1="<a href=\"https://en.wikipedia.org/wiki/Arsenal_F.C.\" title=\"Arsenal F.C.\">Arsenal</a>", f2="38", f3="20", f4="11", f5="7", f6="65", f7="36", f8="+29", f9="71", f10="<a href=\"https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.ttables0.insert(f0="3", f1="<a href=\"https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C.\" title=\"Tottenham Hotspur F.C.\">Tottenham Hotspur</a>", f2="38", f3="19", f4="13", f5="6", f6="69", f7="35", f8="+34", f9="70", f10="<a href=\"https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.ttables0.insert(f0="4", f1="<a href=\"https://en.wikipedia.org/wiki/Manchester_City_F.C.\" title=\"Manchester City F.C.\">Manchester City</a>", f2="38", f3="19", f4="9", f5="10", f6="71", f7="41", f8="+30", f9="66", f10="<a href=\"https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Play-off_round\" title=\"201617 UEFA Champions League\">Champions League play-off round</a>")
    db.ttables0.insert(f0="5", f1="<a href=\"https://en.wikipedia.org/wiki/Manchester_United_F.C.\" title=\"Manchester United F.C.\">Manchester United</a>", f2="38", f3="19", f4="9", f5="10", f6="49", f7="35", f8="+14", f9="66", f10="<a href=\"https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Group_stage\" title=\"201617 UEFA Europa League\">Europa League group stage</a>")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="Admin", f1="Irfan Maulana", f2="Jakarta, Indonesia", f3="August 12, 1995", f4="<a class=\"button is-primary\"><span class=\"icon is-small\"> <i class=\"fa fa-edit\"></i> </span><span>Edit</span></a> <a class=\"button is-danger\"><span class=\"icon is-small\"> <i class=\"fa fa-trash-o\"></i> </span><span>Delete</span></a>")
    db.ttables1.insert(f0="Admin", f1="Irfan Maulana 2", f2="Jakarta, Indonesia", f3="December 25, 1996", f4="<a class=\"button is-primary\"><span class=\"icon is-small\"> <i class=\"fa fa-edit\"></i> </span><span>Edit</span></a> <a class=\"button is-danger\"><span class=\"icon is-small\"> <i class=\"fa fa-trash-o\"></i> </span><span>Delete</span></a>")
    db.ttables1.insert(f0="Admin", f1="Irfan Maulana 3", f2="Jakarta, Indonesia", f3="January 20, 1998", f4="<a class=\"button is-primary\"><span class=\"icon is-small\"> <i class=\"fa fa-edit\"></i> </span><span>Edit</span></a> <a class=\"button is-danger\"><span class=\"icon is-small\"> <i class=\"fa fa-trash-o\"></i> </span><span>Delete</span></a>")
    db.ttables1.insert(f0="Admin", f1="Irfan Maulana 4", f2="Jakarta, Indonesia", f3="November 9, 1999", f4="<a class=\"button is-primary\"><span class=\"icon is-small\"> <i class=\"fa fa-edit\"></i> </span><span>Edit</span></a> <a class=\"button is-danger\"><span class=\"icon is-small\"> <i class=\"fa fa-trash-o\"></i> </span><span>Delete</span></a>")
    db.ttables1.insert(f0="Admin", f1="Irfan Maulana 5", f2="Jakarta, Indonesia", f3="January 11, 2001", f4="<a class=\"button is-primary\"><span class=\"icon is-small\"> <i class=\"fa fa-edit\"></i> </span><span>Edit</span></a> <a class=\"button is-danger\"><span class=\"icon is-small\"> <i class=\"fa fa-trash-o\"></i> </span><span>Delete</span></a>")
    db.commit()
