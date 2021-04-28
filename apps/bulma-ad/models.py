from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 03.12.2020 11:33:22 UTC+3
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
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms4',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms7',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms8',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms9',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms10',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms11',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms12',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms13',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms14',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms15',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms16',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms17',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms18',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms19',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms21',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms22',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms23',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms24',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms25',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms26',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms27',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdatatables0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'telements0',
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
    'tdatatables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="<span class=\"icon\"><i class=\"fa fa-book\"></i></span>")
    db.tindex0.insert(f0="<span class=\"icon\"><i class=\"fa fa-book\"></i></span>")
    db.tindex0.insert(f0="<span class=\"icon\"><i class=\"fa fa-book\"></i></span>")
    db.tindex0.insert(f0="<span class=\"icon\"><i class=\"fa fa-book\"></i></span>")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="<span class=\"icon\"><i class=\"fa fa-user\"></i></span>")
    db.tindex1.insert(f0="<span class=\"icon\"><i class=\"fa fa-user\"></i></span>")
    db.tindex1.insert(f0="<span class=\"icon\"><i class=\"fa fa-user\"></i></span>")
    db.tindex1.insert(f0="<span class=\"icon\"><i class=\"fa fa-user\"></i></span>")
    db.commit()

if not db(db.telements0).count():
    db.telements0.insert(f0="<abbr title=\"Position\">Pos</abbr>", f1="Team", f2="<abbr title=\"Played\">Pld</abbr>", f3="<abbr title=\"Won\">W</abbr>", f4="<abbr title=\"Drawn\">D</abbr>", f5="<abbr title=\"Lost\">L</abbr>", f6="<abbr title=\"Goals for\">GF</abbr>", f7="<abbr title=\"Goals against\">GA</abbr>", f8="<abbr title=\"Goal difference\">GD</abbr>", f9="<abbr title=\"Points\">Pts</abbr>", f10="Qualification or relegation")
    db.telements0.insert(f0="1", f1="<a href=\"https://en.wikipedia.org/wiki/Leicester_City_F.C.\" title=\"Leicester City F.C.\">Leicester City</a> <strong>(C)</strong>", f2="38", f3="23", f4="12", f5="3", f6="68", f7="36", f8="+32", f9="81", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.telements0.insert(f0="2", f1="<a href=\"https://en.wikipedia.org/wiki/Arsenal_F.C.\" title=\"Arsenal F.C.\">Arsenal</a>", f2="38", f3="20", f4="11", f5="7", f6="65", f7="36", f8="+29", f9="71", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.telements0.insert(f0="3", f1="<a href=\"https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C.\" title=\"Tottenham Hotspur F.C.\">Tottenham Hotspur</a>", f2="38", f3="19", f4="13", f5="6", f6="69", f7="35", f8="+34", f9="70", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Champions_League#Group_stage\" title=\"201617 UEFA Champions League\">Champions League group stage</a>")
    db.telements0.insert(f0="4", f1="<a href=\"https://en.wikipedia.org/wiki/Manchester_City_F.C.\" title=\"Manchester City F.C.\">Manchester City</a>", f2="38", f3="19", f4="9", f5="10", f6="71", f7="41", f8="+30", f9="66", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Champions_League#Play-off_round\" title=\"201617 UEFA Champions League\">Champions League play-off round</a>")
    db.telements0.insert(f0="5", f1="<a href=\"https://en.wikipedia.org/wiki/Manchester_United_F.C.\" title=\"Manchester United F.C.\">Manchester United</a>", f2="38", f3="19", f4="9", f5="10", f6="49", f7="35", f8="+14", f9="66", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Europa_League#Group_stage\" title=\"201617 UEFA Europa League\">Europa League group stage</a>")
    db.telements0.insert(f0="6", f1="<a href=\"https://en.wikipedia.org/wiki/Southampton_F.C.\" title=\"Southampton F.C.\">Southampton</a>", f2="38", f3="18", f4="9", f5="11", f6="59", f7="41", f8="+18", f9="63", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Europa_League#Group_stage\" title=\"201617 UEFA Europa League\">Europa League group stage</a>")
    db.telements0.insert(f0="7", f1="<a href=\"https://en.wikipedia.org/wiki/West_Ham_United_F.C.\" title=\"West Ham United F.C.\">West Ham United</a>", f2="38", f3="16", f4="14", f5="8", f6="65", f7="51", f8="+14", f9="62", f10="<a href=\"https://en.wikipedia.org/wiki/201617_UEFA_Europa_League#Third_qualifying_round\" title=\"201617 UEFA Europa League\">Europa League third qualifying round</a>")
    db.telements0.insert(f0="8", f1="<a href=\"https://en.wikipedia.org/wiki/Liverpool_F.C.\" title=\"Liverpool F.C.\">Liverpool</a>", f2="38", f3="16", f4="12", f5="10", f6="63", f7="50", f8="+13", f9="60", f10="==0")
    db.telements0.insert(f0="9", f1="<a href=\"https://en.wikipedia.org/wiki/Stoke_City_F.C.\" title=\"Stoke City F.C.\">Stoke City</a>", f2="38", f3="14", f4="9", f5="15", f6="41", f7="55", f8="14", f9="51", f10="==0")
    db.telements0.insert(f0="10", f1="<a href=\"https://en.wikipedia.org/wiki/Chelsea_F.C.\" title=\"Chelsea F.C.\">Chelsea</a>", f2="38", f3="12", f4="14", f5="12", f6="59", f7="53", f8="+6", f9="50", f10="==0")
    db.telements0.insert(f0="11", f1="<a href=\"https://en.wikipedia.org/wiki/Everton_F.C.\" title=\"Everton F.C.\">Everton</a>", f2="38", f3="11", f4="14", f5="13", f6="59", f7="55", f8="+4", f9="47", f10="==0")
    db.telements0.insert(f0="12", f1="<a href=\"https://en.wikipedia.org/wiki/Swansea_City_A.F.C.\" title=\"Swansea City A.F.C.\">Swansea City</a>", f2="38", f3="12", f4="11", f5="15", f6="42", f7="52", f8="10", f9="47", f10="==0")
    db.telements0.insert(f0="13", f1="<a href=\"https://en.wikipedia.org/wiki/Watford_F.C.\" title=\"Watford F.C.\">Watford</a>", f2="38", f3="12", f4="9", f5="17", f6="40", f7="50", f8="10", f9="45", f10="==0")
    db.telements0.insert(f0="14", f1="<a href=\"https://en.wikipedia.org/wiki/West_Bromwich_Albion_F.C.\" title=\"West Bromwich Albion F.C.\">West Bromwich Albion</a>", f2="38", f3="10", f4="13", f5="15", f6="34", f7="48", f8="14", f9="43", f10="==0")
    db.telements0.insert(f0="15", f1="<a href=\"https://en.wikipedia.org/wiki/Crystal_Palace_F.C.\" title=\"Crystal Palace F.C.\">Crystal Palace</a>", f2="38", f3="11", f4="9", f5="18", f6="39", f7="51", f8="12", f9="42", f10="==0")
    db.telements0.insert(f0="16", f1="<a href=\"https://en.wikipedia.org/wiki/A.F.C._Bournemouth\" title=\"A.F.C. Bournemouth\">AFC Bournemouth</a>", f2="38", f3="11", f4="9", f5="18", f6="45", f7="67", f8="22", f9="42", f10="==0")
    db.telements0.insert(f0="17", f1="<a href=\"https://en.wikipedia.org/wiki/Sunderland_A.F.C.\" title=\"Sunderland A.F.C.\">Sunderland</a>", f2="38", f3="9", f4="12", f5="17", f6="48", f7="62", f8="14", f9="39", f10="==0")
    db.telements0.insert(f0="18", f1="<a href=\"https://en.wikipedia.org/wiki/Newcastle_United_F.C.\" title=\"Newcastle United F.C.\">Newcastle United</a> <strong>(R)</strong>", f2="38", f3="9", f4="10", f5="19", f6="44", f7="65", f8="21", f9="37", f10="<a href=\"https://en.wikipedia.org/wiki/201617_Football_League_Championship\" title=\"201617 Football League Championship\">Football League Championship</a>")
    db.telements0.insert(f0="19", f1="<a href=\"https://en.wikipedia.org/wiki/Norwich_City_F.C.\" title=\"Norwich City F.C.\">Norwich City</a> <strong>(R)</strong>", f2="38", f3="9", f4="7", f5="22", f6="39", f7="67", f8="28", f9="34", f10="<a href=\"https://en.wikipedia.org/wiki/201617_Football_League_Championship\" title=\"201617 Football League Championship\">Football League Championship</a>")
    db.telements0.insert(f0="20", f1="<a href=\"https://en.wikipedia.org/wiki/Aston_Villa_F.C.\" title=\"Aston Villa F.C.\">Aston Villa</a> <strong>(R)</strong>", f2="38", f3="3", f4="8", f5="27", f6="27", f7="76", f8="49", f9="17", f10="<a href=\"https://en.wikipedia.org/wiki/201617_Football_League_Championship\" title=\"201617 Football League Championship\">Football League Championship</a>")
    db.commit()

if not db(db.tdatatables0).count():
    db.tdatatables0.insert(f0="1", f1="Abu Bakar As-Shiddiq", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="2", f1="Umar bin Khattab", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="3", f1="Utsman bin Affan", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="4", f1="Ali bin Abi Thalib", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="5", f1="Hamzah bin Abdul-Muththalib", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="6", f1="Mushab bin Umair", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="7", f1="Zaid bin Haritsah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="8", f1="Jafar bin Abu Thalib", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="9", f1="Husain bin Ali", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="10", f1="Saad bin Muadz", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="11", f1="Ammar bin Yasir", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="12", f1="Abad bin Bisyr", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="13", f1="Salim Maula Abi Hudzaifah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="14", f1="Al-Bara bin Malik", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="15", f1="Abu Dujanah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="16", f1="Amr bin al-Jamuh", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="17", f1="Abu Ayyub al-Anshari", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="18", f1="Abu Thalhah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="19", f1="Abdullah bin Jahsy", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="20", f1="Khubaib bin Adi", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="21", f1="Ikrimah bin Abu Jahal", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="22", f1="Khadijah Binti Khuwailid", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="23", f1="Imam Al-Ghazali", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="24", f1="Sofyan Ats-Tsauri", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="25", f1="Khalid bin Walid", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="26", f1="Utbah bin Ghazwan", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="27", f1="Mushab bin Umair", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="28", f1="Muadz bin Jabal", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="29", f1="Zaid bin Haritsah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="30", f1="Fatimah binti Muhammad", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="31", f1="Bilal bin Rabah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="32", f1="Abdullah bin Zubeir", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="33", f1="Zainab Binti Jahsy Bin Riab", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="34", f1="Abu Ubaidah bin Jarrah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="35", f1="Ibnu Qayyim Al-Jauziyyah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="36", f1="Ibnu Katsir", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="37", f1="Ibnu Taimiyyah", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="38", f1="Ahmed Deedat", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="39", f1="Yusuf Qardhawi", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="40", f1="Imam Muslim", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="41", f1="Hasan Al Banna", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="42", f1="Tuanku Tambusai", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="43", f1="Tuanku Imam Bonjol", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="44", f1="Sunan Gresik", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="45", f1="Sunan Ampel", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="46", f1="Sunan Bonang", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="47", f1="Sunan Drajat", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="48", f1="Sunan Kudus", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="49", f1="Sunan Giri", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="50", f1="Sunan Kalijaga", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="51", f1="Sunan Muria", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="52", f1="Sunan Gunung Jati", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.tdatatables0.insert(f0="53", f1="Jumadil Qubro", f2="<div class=\"field is-grouped action\"><p class=\"control\"><a class=\"button is-rounded is-text\" href=\"#\"><span class=\"icon\"><i class=\"fa fa-edit\"></i></span></a></p><p class=\"control\"><a class=\"button is-rounded is-text action-delete\" data-id=\"1\"><span class=\"icon\"><i class=\"fa fa-trash\"></i></span></a></p></div>")
    db.commit()
