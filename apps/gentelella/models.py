from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 25.11.2020 16:43:07 msk, src: https://github.com/ColorlibHQ/gentelella
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
    'dfform0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    Field('f6','boolean',  ),
    Field('f7','boolean',  ),
    Field('f8','string', length=1024, ),
    Field('f9','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXadvanced0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXadvanced1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXadvanced2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXadvanced3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXvalidation0',
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
    Field('f10','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXwizards0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXwizards1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXupload0',
    )
db.commit()

db.define_table(
    'dfcalendar0',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar1',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpageX4030',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpageX4040',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpageX5000',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflogin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflogin1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tformXadvanced7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXelements0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXelements1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinvoice0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinvoice1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXdynamic5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    )
db.commit()

db.define_table(
    'totherXcharts0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tprojects0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tprofile0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

if not db(db.tformXadvanced0).count():
    db.tformXadvanced0.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced0.insert(f0="25", f1="26", f2="27", f3="28", f4="29", f5="30", f6="1")
    db.tformXadvanced0.insert(f0="2", f1="3", f2="4", f3="5", f4="6", f5="7", f6="8")
    db.tformXadvanced0.insert(f0="9", f1="10", f2="11", f3="12", f4="13", f5="14", f6="15")
    db.tformXadvanced0.insert(f0="16", f1="17", f2="18", f3="19", f4="20", f5="21", f6="22")
    db.tformXadvanced0.insert(f0="23", f1="24", f2="25", f3="26", f4="27", f5="28", f6="29")
    db.tformXadvanced0.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.commit()

if not db(db.tformXadvanced1).count():
    db.tformXadvanced1.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced1.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.tformXadvanced1.insert(f0="6", f1="7", f2="8", f3="9", f4="10", f5="11", f6="12")
    db.tformXadvanced1.insert(f0="13", f1="14", f2="15", f3="16", f4="17", f5="18", f6="19")
    db.tformXadvanced1.insert(f0="20", f1="21", f2="22", f3="23", f4="24", f5="25", f6="26")
    db.tformXadvanced1.insert(f0="27", f1="28", f2="29", f3="30", f4="1", f5="2", f6="3")
    db.tformXadvanced1.insert(f0="4", f1="5", f2="6", f3="7", f4="8", f5="9", f6="10")
    db.commit()

if not db(db.tformXadvanced2).count():
    db.tformXadvanced2.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced2.insert(f0="25", f1="26", f2="27", f3="28", f4="29", f5="30", f6="1")
    db.tformXadvanced2.insert(f0="2", f1="3", f2="4", f3="5", f4="6", f5="7", f6="8")
    db.tformXadvanced2.insert(f0="9", f1="10", f2="11", f3="12", f4="13", f5="14", f6="15")
    db.tformXadvanced2.insert(f0="16", f1="17", f2="18", f3="19", f4="20", f5="21", f6="22")
    db.tformXadvanced2.insert(f0="23", f1="24", f2="25", f3="26", f4="27", f5="28", f6="29")
    db.tformXadvanced2.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.commit()

if not db(db.tformXadvanced3).count():
    db.tformXadvanced3.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced3.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.tformXadvanced3.insert(f0="6", f1="7", f2="8", f3="9", f4="10", f5="11", f6="12")
    db.tformXadvanced3.insert(f0="13", f1="14", f2="15", f3="16", f4="17", f5="18", f6="19")
    db.tformXadvanced3.insert(f0="20", f1="21", f2="22", f3="23", f4="24", f5="25", f6="26")
    db.tformXadvanced3.insert(f0="27", f1="28", f2="29", f3="30", f4="1", f5="2", f6="3")
    db.tformXadvanced3.insert(f0="4", f1="5", f2="6", f3="7", f4="8", f5="9", f6="10")
    db.commit()

if not db(db.tformXadvanced4).count():
    db.tformXadvanced4.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced4.insert(f0="25", f1="26", f2="27", f3="28", f4="29", f5="30", f6="1")
    db.tformXadvanced4.insert(f0="2", f1="3", f2="4", f3="5", f4="6", f5="7", f6="8")
    db.tformXadvanced4.insert(f0="9", f1="10", f2="11", f3="12", f4="13", f5="14", f6="15")
    db.tformXadvanced4.insert(f0="16", f1="17", f2="18", f3="19", f4="20", f5="21", f6="22")
    db.tformXadvanced4.insert(f0="23", f1="24", f2="25", f3="26", f4="27", f5="28", f6="29")
    db.tformXadvanced4.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.commit()

if not db(db.tformXadvanced5).count():
    db.tformXadvanced5.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced5.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.tformXadvanced5.insert(f0="6", f1="7", f2="8", f3="9", f4="10", f5="11", f6="12")
    db.tformXadvanced5.insert(f0="13", f1="14", f2="15", f3="16", f4="17", f5="18", f6="19")
    db.tformXadvanced5.insert(f0="20", f1="21", f2="22", f3="23", f4="24", f5="25", f6="26")
    db.tformXadvanced5.insert(f0="27", f1="28", f2="29", f3="30", f4="1", f5="2", f6="3")
    db.tformXadvanced5.insert(f0="4", f1="5", f2="6", f3="7", f4="8", f5="9", f6="10")
    db.commit()

if not db(db.tformXadvanced6).count():
    db.tformXadvanced6.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced6.insert(f0="25", f1="26", f2="27", f3="28", f4="29", f5="30", f6="1")
    db.tformXadvanced6.insert(f0="2", f1="3", f2="4", f3="5", f4="6", f5="7", f6="8")
    db.tformXadvanced6.insert(f0="9", f1="10", f2="11", f3="12", f4="13", f5="14", f6="15")
    db.tformXadvanced6.insert(f0="16", f1="17", f2="18", f3="19", f4="20", f5="21", f6="22")
    db.tformXadvanced6.insert(f0="23", f1="24", f2="25", f3="26", f4="27", f5="28", f6="29")
    db.tformXadvanced6.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.commit()

if not db(db.tformXadvanced7).count():
    db.tformXadvanced7.insert(f0="Su", f1="Mo", f2="Tu", f3="We", f4="Th", f5="Fr", f6="Sa")
    db.tformXadvanced7.insert(f0="30", f1="31", f2="1", f3="2", f4="3", f5="4", f6="5")
    db.tformXadvanced7.insert(f0="6", f1="7", f2="8", f3="9", f4="10", f5="11", f6="12")
    db.tformXadvanced7.insert(f0="13", f1="14", f2="15", f3="16", f4="17", f5="18", f6="19")
    db.tformXadvanced7.insert(f0="20", f1="21", f2="22", f3="23", f4="24", f5="25", f6="26")
    db.tformXadvanced7.insert(f0="27", f1="28", f2="29", f3="30", f4="1", f5="2", f6="3")
    db.tformXadvanced7.insert(f0="4", f1="5", f2="6", f3="7", f4="8", f5="9", f6="10")
    db.commit()

if not db(db.tgeneralXelements0).count():
    db.tgeneralXelements0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXelements0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXelements0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tgeneralXelements1).count():
    db.tgeneralXelements1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXelements1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXelements1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="1", f1="Call of Duty", f2="455-981-221", f3="El snort testosterone trophy driving gloves handsome gerry Richardson helvetica tousled street art master testosterone trophy driving gloves handsome gerry Richardson", f4="$64.50")
    db.tinvoice0.insert(f0="1", f1="Need for Speed IV", f2="247-925-726", f3="Wes Anderson umami biodiesel", f4="$50.00")
    db.tinvoice0.insert(f0="1", f1="Monsters DVD", f2="735-845-642", f3="Terry Richardson helvetica tousled street art master, El snort testosterone trophy driving gloves handsome letterpress erry Richardson helvetica tousled", f4="$10.70")
    db.tinvoice0.insert(f0="1", f1="Grown Ups Blue Ray", f2="422-568-642", f3="Tousled lomo letterpress erry Richardson helvetica tousled street art master helvetica tousled street art master, El snort testosterone", f4="$25.99")
    db.commit()

if not db(db.tinvoice1).count():
    db.tinvoice1.insert(f0="Tax (9.3%)", f1="$10.34")
    db.tinvoice1.insert(f0="Shipping:", f1="$5.80")
    db.tinvoice1.insert(f0="Total:", f1="$265.24")
    db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables2).count():
    db.ttables2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables2.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables3).count():
    db.ttables3.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables3.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables3.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables4).count():
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000040", f2="May 23, 2014 11:47:56 PM", f3="<i class=\"success fa fa-long-arrow-up\"></i>", f4="John Blank L", f5="Paid", f6="$7.45", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000039", f2="May 23, 2014 11:30:12 PM", f3="<i class=\"success fa fa-long-arrow-up\"></i>", f4="John Blank L", f5="Paid", f6="$741.20", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000038", f2="May 24, 2014 10:55:33 PM", f3="<i class=\"success fa fa-long-arrow-up\"></i>", f4="Mike Smith", f5="Paid", f6="$432.26", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000037", f2="May 24, 2014 10:52:44 PM", f3="121000204", f4="Mike Smith", f5="Paid", f6="$333.21", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000040", f2="May 24, 2014 11:47:56 PM", f3="121000210", f4="John Blank L", f5="Paid", f6="$7.45", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000039", f2="May 26, 2014 11:30:12 PM", f3="<i class=\"error fa fa-long-arrow-down\"></i>", f4="John Blank L", f5="Paid", f6="$741.20", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000038", f2="May 26, 2014 10:55:33 PM", f3="121000203", f4="Mike Smith", f5="Paid", f6="$432.26", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000037", f2="May 26, 2014 10:52:44 PM", f3="121000204", f4="Mike Smith", f5="Paid", f6="$333.21", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000040", f2="May 27, 2014 11:47:56 PM", f3="121000210", f4="John Blank L", f5="Paid", f6="$7.45", f7="<a href=\"#\">View</a>")
    db.ttables4.insert(f0="<input class=\"flat\" name=\"table_records\" type=\"checkbox\"/>", f1="121000039", f2="May 28, 2014 11:30:12 PM", f3="121000208", f4="John Blank L", f5="Paid", f6="$741.20", f7="<a href=\"#\">View</a>")
    db.commit()

if not db(db.ttablesXdynamic0).count():
    db.ttablesXdynamic0.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.ttablesXdynamic0.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.ttablesXdynamic0.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.ttablesXdynamic0.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.ttablesXdynamic0.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.ttablesXdynamic0.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.ttablesXdynamic0.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.ttablesXdynamic0.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.ttablesXdynamic0.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.ttablesXdynamic0.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.ttablesXdynamic0.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.ttablesXdynamic0.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.ttablesXdynamic0.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.ttablesXdynamic0.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.ttablesXdynamic0.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.ttablesXdynamic0.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.ttablesXdynamic0.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.ttablesXdynamic0.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.ttablesXdynamic0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.ttablesXdynamic0.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.ttablesXdynamic0.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.ttablesXdynamic0.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.ttablesXdynamic0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.ttablesXdynamic0.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.ttablesXdynamic0.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.ttablesXdynamic0.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.ttablesXdynamic0.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.ttablesXdynamic0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.ttablesXdynamic0.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.ttablesXdynamic0.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.ttablesXdynamic0.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.ttablesXdynamic0.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.ttablesXdynamic0.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.ttablesXdynamic0.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.ttablesXdynamic0.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.ttablesXdynamic0.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.ttablesXdynamic0.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.ttablesXdynamic0.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.ttablesXdynamic0.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.ttablesXdynamic0.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.ttablesXdynamic0.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.ttablesXdynamic0.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.ttablesXdynamic0.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.ttablesXdynamic0.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.ttablesXdynamic0.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.ttablesXdynamic0.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.ttablesXdynamic0.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.ttablesXdynamic0.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.ttablesXdynamic0.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.ttablesXdynamic0.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.ttablesXdynamic0.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.ttablesXdynamic0.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.ttablesXdynamic0.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.ttablesXdynamic0.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.ttablesXdynamic0.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.ttablesXdynamic0.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.ttablesXdynamic0.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.commit()

if not db(db.ttablesXdynamic1).count():
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Tiger Nixon", f3="System Architect", f4="Edinburgh", f5="61", f6="2011/04/25", f7="$320,800")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Garrett Winters", f3="Accountant", f4="Tokyo", f5="63", f6="2011/07/25", f7="$170,750")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Ashton Cox", f3="Junior Technical Author", f4="San Francisco", f5="66", f6="2009/01/12", f7="$86,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Cedric Kelly", f3="Senior Javascript Developer", f4="Edinburgh", f5="22", f6="2012/03/29", f7="$433,060")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Airi Satou", f3="Accountant", f4="Tokyo", f5="33", f6="2008/11/28", f7="$162,700")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Brielle Williamson", f3="Integration Specialist", f4="New York", f5="61", f6="2012/12/02", f7="$372,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Herrod Chandler", f3="Sales Assistant", f4="San Francisco", f5="59", f6="2012/08/06", f7="$137,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Rhona Davidson", f3="Integration Specialist", f4="Tokyo", f5="55", f6="2010/10/14", f7="$327,900")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Colleen Hurst", f3="Javascript Developer", f4="San Francisco", f5="39", f6="2009/09/15", f7="$205,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Sonya Frost", f3="Software Engineer", f4="Edinburgh", f5="23", f6="2008/12/13", f7="$103,600")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jena Gaines", f3="Office Manager", f4="London", f5="30", f6="2008/12/19", f7="$90,560")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Quinn Flynn", f3="Support Lead", f4="Edinburgh", f5="22", f6="2013/03/03", f7="$342,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Charde Marshall", f3="Regional Director", f4="San Francisco", f5="36", f6="2008/10/16", f7="$470,600")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Haley Kennedy", f3="Senior Marketing Designer", f4="London", f5="43", f6="2012/12/18", f7="$313,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Tatyana Fitzpatrick", f3="Regional Director", f4="London", f5="19", f6="2010/03/17", f7="$385,750")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Michael Silva", f3="Marketing Designer", f4="London", f5="66", f6="2012/11/27", f7="$198,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Paul Byrd", f3="Chief Financial Officer (CFO)", f4="New York", f5="64", f6="2010/06/09", f7="$725,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Gloria Little", f3="Systems Administrator", f4="New York", f5="59", f6="2009/04/10", f7="$237,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Bradley Greer", f3="Software Engineer", f4="London", f5="41", f6="2012/10/13", f7="$132,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Dai Rios", f3="Personnel Lead", f4="Edinburgh", f5="35", f6="2012/09/26", f7="$217,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jenette Caldwell", f3="Development Lead", f4="New York", f5="30", f6="2011/09/03", f7="$345,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Yuri Berry", f3="Chief Marketing Officer (CMO)", f4="New York", f5="40", f6="2009/06/25", f7="$675,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Caesar Vance", f3="Pre-Sales Support", f4="New York", f5="21", f6="2011/12/12", f7="$106,450")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Doris Wilder", f3="Sales Assistant", f4="Sidney", f5="23", f6="2010/09/20", f7="$85,600")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Angelica Ramos", f3="Chief Executive Officer (CEO)", f4="London", f5="47", f6="2009/10/09", f7="$1,200,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Gavin Joyce", f3="Developer", f4="Edinburgh", f5="42", f6="2010/12/22", f7="$92,575")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jennifer Chang", f3="Regional Director", f4="Singapore", f5="28", f6="2010/11/14", f7="$357,650")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Brenden Wagner", f3="Software Engineer", f4="San Francisco", f5="28", f6="2011/06/07", f7="$206,850")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Fiona Green", f3="Chief Operating Officer (COO)", f4="San Francisco", f5="48", f6="2010/03/11", f7="$850,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Shou Itou", f3="Regional Marketing", f4="Tokyo", f5="20", f6="2011/08/14", f7="$163,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Michelle House", f3="Integration Specialist", f4="Sidney", f5="37", f6="2011/06/02", f7="$95,400")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Suki Burks", f3="Developer", f4="London", f5="53", f6="2009/10/22", f7="$114,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Prescott Bartlett", f3="Technical Author", f4="London", f5="27", f6="2011/05/07", f7="$145,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Gavin Cortez", f3="Team Leader", f4="San Francisco", f5="22", f6="2008/10/26", f7="$235,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Martena Mccray", f3="Post-Sales support", f4="Edinburgh", f5="46", f6="2011/03/09", f7="$324,050")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Unity Butler", f3="Marketing Designer", f4="San Francisco", f5="47", f6="2009/12/09", f7="$85,675")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Howard Hatfield", f3="Office Manager", f4="San Francisco", f5="51", f6="2008/12/16", f7="$164,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Hope Fuentes", f3="Secretary", f4="San Francisco", f5="41", f6="2010/02/12", f7="$109,850")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Vivian Harrell", f3="Financial Controller", f4="San Francisco", f5="62", f6="2009/02/14", f7="$452,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Timothy Mooney", f3="Office Manager", f4="London", f5="37", f6="2008/12/11", f7="$136,200")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jackson Bradshaw", f3="Director", f4="New York", f5="65", f6="2008/09/26", f7="$645,750")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Olivia Liang", f3="Support Engineer", f4="Singapore", f5="64", f6="2011/02/03", f7="$234,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Bruno Nash", f3="Software Engineer", f4="London", f5="38", f6="2011/05/03", f7="$163,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Sakura Yamamoto", f3="Support Engineer", f4="Tokyo", f5="37", f6="2009/08/19", f7="$139,575")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Thor Walton", f3="Developer", f4="New York", f5="61", f6="2013/08/11", f7="$98,540")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Finn Camacho", f3="Support Engineer", f4="San Francisco", f5="47", f6="2009/07/07", f7="$87,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Serge Baldwin", f3="Data Coordinator", f4="Singapore", f5="64", f6="2012/04/09", f7="$138,575")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Zenaida Frank", f3="Software Engineer", f4="New York", f5="63", f6="2010/01/04", f7="$125,250")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Zorita Serrano", f3="Software Engineer", f4="San Francisco", f5="56", f6="2012/06/01", f7="$115,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jennifer Acosta", f3="Junior Javascript Developer", f4="Edinburgh", f5="43", f6="2013/02/01", f7="$75,650")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Cara Stevens", f3="Sales Assistant", f4="New York", f5="46", f6="2011/12/06", f7="$145,600")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Hermione Butler", f3="Regional Director", f4="London", f5="47", f6="2011/03/21", f7="$356,250")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Lael Greer", f3="Systems Administrator", f4="London", f5="21", f6="2009/02/27", f7="$103,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Jonas Alexander", f3="Developer", f4="San Francisco", f5="30", f6="2010/07/14", f7="$86,500")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Shad Decker", f3="Regional Director", f4="Edinburgh", f5="51", f6="2008/11/13", f7="$183,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Michael Bruce", f3="Javascript Developer", f4="Singapore", f5="29", f6="2011/06/27", f7="$183,000")
    db.ttablesXdynamic1.insert(f0="==0", f1="<input id=\"check-all\" type=\"checkbox\"/>", f2="Donna Snider", f3="Customer Support", f4="New York", f5="27", f6="2011/01/25", f7="$112,000")
    db.commit()

if not db(db.ttablesXdynamic2).count():
    db.ttablesXdynamic2.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.ttablesXdynamic2.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.ttablesXdynamic2.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.ttablesXdynamic2.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.ttablesXdynamic2.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.ttablesXdynamic2.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.ttablesXdynamic2.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.ttablesXdynamic2.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.ttablesXdynamic2.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.ttablesXdynamic2.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.ttablesXdynamic2.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.ttablesXdynamic2.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.ttablesXdynamic2.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.ttablesXdynamic2.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.ttablesXdynamic2.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.ttablesXdynamic2.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.ttablesXdynamic2.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.ttablesXdynamic2.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.ttablesXdynamic2.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.ttablesXdynamic2.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.ttablesXdynamic2.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.ttablesXdynamic2.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.ttablesXdynamic2.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.ttablesXdynamic2.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.ttablesXdynamic2.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.ttablesXdynamic2.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.ttablesXdynamic2.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.ttablesXdynamic2.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.ttablesXdynamic2.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.ttablesXdynamic2.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.ttablesXdynamic2.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.ttablesXdynamic2.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.ttablesXdynamic2.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.ttablesXdynamic2.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.ttablesXdynamic2.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.ttablesXdynamic2.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.ttablesXdynamic2.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.ttablesXdynamic2.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.ttablesXdynamic2.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.ttablesXdynamic2.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.ttablesXdynamic2.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.ttablesXdynamic2.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.ttablesXdynamic2.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.ttablesXdynamic2.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.ttablesXdynamic2.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.ttablesXdynamic2.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.ttablesXdynamic2.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.ttablesXdynamic2.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.ttablesXdynamic2.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.ttablesXdynamic2.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.ttablesXdynamic2.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.ttablesXdynamic2.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.ttablesXdynamic2.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.ttablesXdynamic2.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.ttablesXdynamic2.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.ttablesXdynamic2.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.ttablesXdynamic2.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.commit()

if not db(db.ttablesXdynamic3).count():
    db.ttablesXdynamic3.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.ttablesXdynamic3.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.ttablesXdynamic3.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.ttablesXdynamic3.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.ttablesXdynamic3.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.ttablesXdynamic3.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.ttablesXdynamic3.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.ttablesXdynamic3.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.ttablesXdynamic3.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.ttablesXdynamic3.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.ttablesXdynamic3.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.ttablesXdynamic3.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.ttablesXdynamic3.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.ttablesXdynamic3.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.ttablesXdynamic3.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.ttablesXdynamic3.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.ttablesXdynamic3.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.ttablesXdynamic3.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.ttablesXdynamic3.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.ttablesXdynamic3.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.ttablesXdynamic3.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.ttablesXdynamic3.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.ttablesXdynamic3.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.ttablesXdynamic3.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.ttablesXdynamic3.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.ttablesXdynamic3.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.ttablesXdynamic3.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.ttablesXdynamic3.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.ttablesXdynamic3.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.ttablesXdynamic3.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.ttablesXdynamic3.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.ttablesXdynamic3.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.ttablesXdynamic3.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.ttablesXdynamic3.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.ttablesXdynamic3.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.ttablesXdynamic3.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.ttablesXdynamic3.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.ttablesXdynamic3.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.ttablesXdynamic3.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.ttablesXdynamic3.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.ttablesXdynamic3.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.ttablesXdynamic3.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.ttablesXdynamic3.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.ttablesXdynamic3.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.ttablesXdynamic3.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.ttablesXdynamic3.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.ttablesXdynamic3.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.ttablesXdynamic3.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.ttablesXdynamic3.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.ttablesXdynamic3.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.ttablesXdynamic3.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.ttablesXdynamic3.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.ttablesXdynamic3.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.ttablesXdynamic3.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.ttablesXdynamic3.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.ttablesXdynamic3.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.ttablesXdynamic3.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.commit()

if not db(db.ttablesXdynamic4).count():
    db.ttablesXdynamic4.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.ttablesXdynamic4.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.ttablesXdynamic4.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.ttablesXdynamic4.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.ttablesXdynamic4.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.ttablesXdynamic4.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.ttablesXdynamic4.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.ttablesXdynamic4.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.ttablesXdynamic4.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.ttablesXdynamic4.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.ttablesXdynamic4.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.ttablesXdynamic4.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.ttablesXdynamic4.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.ttablesXdynamic4.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.ttablesXdynamic4.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.ttablesXdynamic4.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.ttablesXdynamic4.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.ttablesXdynamic4.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.ttablesXdynamic4.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.ttablesXdynamic4.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.ttablesXdynamic4.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.ttablesXdynamic4.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.ttablesXdynamic4.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.ttablesXdynamic4.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.ttablesXdynamic4.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.ttablesXdynamic4.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.ttablesXdynamic4.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.ttablesXdynamic4.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.ttablesXdynamic4.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.ttablesXdynamic4.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.ttablesXdynamic4.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.ttablesXdynamic4.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.ttablesXdynamic4.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.ttablesXdynamic4.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.ttablesXdynamic4.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.ttablesXdynamic4.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.ttablesXdynamic4.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.ttablesXdynamic4.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.ttablesXdynamic4.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.ttablesXdynamic4.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.ttablesXdynamic4.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.ttablesXdynamic4.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.ttablesXdynamic4.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.ttablesXdynamic4.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.ttablesXdynamic4.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.ttablesXdynamic4.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.ttablesXdynamic4.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.ttablesXdynamic4.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.ttablesXdynamic4.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.ttablesXdynamic4.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.ttablesXdynamic4.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.ttablesXdynamic4.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.ttablesXdynamic4.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.ttablesXdynamic4.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.ttablesXdynamic4.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.ttablesXdynamic4.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.ttablesXdynamic4.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.commit()

if not db(db.ttablesXdynamic5).count():
    db.ttablesXdynamic5.insert(f0="Tiger", f1="Nixon", f2="System Architect", f3="Edinburgh", f4="61", f5="2011/04/25", f6="$320,800", f7="5421", f8="t.nixon@datatables.net")
    db.ttablesXdynamic5.insert(f0="Garrett", f1="Winters", f2="Accountant", f3="Tokyo", f4="63", f5="2011/07/25", f6="$170,750", f7="8422", f8="g.winters@datatables.net")
    db.ttablesXdynamic5.insert(f0="Ashton", f1="Cox", f2="Junior Technical Author", f3="San Francisco", f4="66", f5="2009/01/12", f6="$86,000", f7="1562", f8="a.cox@datatables.net")
    db.ttablesXdynamic5.insert(f0="Cedric", f1="Kelly", f2="Senior Javascript Developer", f3="Edinburgh", f4="22", f5="2012/03/29", f6="$433,060", f7="6224", f8="c.kelly@datatables.net")
    db.ttablesXdynamic5.insert(f0="Airi", f1="Satou", f2="Accountant", f3="Tokyo", f4="33", f5="2008/11/28", f6="$162,700", f7="5407", f8="a.satou@datatables.net")
    db.ttablesXdynamic5.insert(f0="Brielle", f1="Williamson", f2="Integration Specialist", f3="New York", f4="61", f5="2012/12/02", f6="$372,000", f7="4804", f8="b.williamson@datatables.net")
    db.ttablesXdynamic5.insert(f0="Herrod", f1="Chandler", f2="Sales Assistant", f3="San Francisco", f4="59", f5="2012/08/06", f6="$137,500", f7="9608", f8="h.chandler@datatables.net")
    db.ttablesXdynamic5.insert(f0="Rhona", f1="Davidson", f2="Integration Specialist", f3="Tokyo", f4="55", f5="2010/10/14", f6="$327,900", f7="6200", f8="r.davidson@datatables.net")
    db.ttablesXdynamic5.insert(f0="Colleen", f1="Hurst", f2="Javascript Developer", f3="San Francisco", f4="39", f5="2009/09/15", f6="$205,500", f7="2360", f8="c.hurst@datatables.net")
    db.ttablesXdynamic5.insert(f0="Sonya", f1="Frost", f2="Software Engineer", f3="Edinburgh", f4="23", f5="2008/12/13", f6="$103,600", f7="1667", f8="s.frost@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jena", f1="Gaines", f2="Office Manager", f3="London", f4="30", f5="2008/12/19", f6="$90,560", f7="3814", f8="j.gaines@datatables.net")
    db.ttablesXdynamic5.insert(f0="Quinn", f1="Flynn", f2="Support Lead", f3="Edinburgh", f4="22", f5="2013/03/03", f6="$342,000", f7="9497", f8="q.flynn@datatables.net")
    db.ttablesXdynamic5.insert(f0="Charde", f1="Marshall", f2="Regional Director", f3="San Francisco", f4="36", f5="2008/10/16", f6="$470,600", f7="6741", f8="c.marshall@datatables.net")
    db.ttablesXdynamic5.insert(f0="Haley", f1="Kennedy", f2="Senior Marketing Designer", f3="London", f4="43", f5="2012/12/18", f6="$313,500", f7="3597", f8="h.kennedy@datatables.net")
    db.ttablesXdynamic5.insert(f0="Tatyana", f1="Fitzpatrick", f2="Regional Director", f3="London", f4="19", f5="2010/03/17", f6="$385,750", f7="1965", f8="t.fitzpatrick@datatables.net")
    db.ttablesXdynamic5.insert(f0="Michael", f1="Silva", f2="Marketing Designer", f3="London", f4="66", f5="2012/11/27", f6="$198,500", f7="1581", f8="m.silva@datatables.net")
    db.ttablesXdynamic5.insert(f0="Paul", f1="Byrd", f2="Chief Financial Officer (CFO)", f3="New York", f4="64", f5="2010/06/09", f6="$725,000", f7="3059", f8="p.byrd@datatables.net")
    db.ttablesXdynamic5.insert(f0="Gloria", f1="Little", f2="Systems Administrator", f3="New York", f4="59", f5="2009/04/10", f6="$237,500", f7="1721", f8="g.little@datatables.net")
    db.ttablesXdynamic5.insert(f0="Bradley", f1="Greer", f2="Software Engineer", f3="London", f4="41", f5="2012/10/13", f6="$132,000", f7="2558", f8="b.greer@datatables.net")
    db.ttablesXdynamic5.insert(f0="Dai", f1="Rios", f2="Personnel Lead", f3="Edinburgh", f4="35", f5="2012/09/26", f6="$217,500", f7="2290", f8="d.rios@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jenette", f1="Caldwell", f2="Development Lead", f3="New York", f4="30", f5="2011/09/03", f6="$345,000", f7="1937", f8="j.caldwell@datatables.net")
    db.ttablesXdynamic5.insert(f0="Yuri", f1="Berry", f2="Chief Marketing Officer (CMO)", f3="New York", f4="40", f5="2009/06/25", f6="$675,000", f7="6154", f8="y.berry@datatables.net")
    db.ttablesXdynamic5.insert(f0="Caesar", f1="Vance", f2="Pre-Sales Support", f3="New York", f4="21", f5="2011/12/12", f6="$106,450", f7="8330", f8="c.vance@datatables.net")
    db.ttablesXdynamic5.insert(f0="Doris", f1="Wilder", f2="Sales Assistant", f3="Sidney", f4="23", f5="2010/09/20", f6="$85,600", f7="3023", f8="d.wilder@datatables.net")
    db.ttablesXdynamic5.insert(f0="Angelica", f1="Ramos", f2="Chief Executive Officer (CEO)", f3="London", f4="47", f5="2009/10/09", f6="$1,200,000", f7="5797", f8="a.ramos@datatables.net")
    db.ttablesXdynamic5.insert(f0="Gavin", f1="Joyce", f2="Developer", f3="Edinburgh", f4="42", f5="2010/12/22", f6="$92,575", f7="8822", f8="g.joyce@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jennifer", f1="Chang", f2="Regional Director", f3="Singapore", f4="28", f5="2010/11/14", f6="$357,650", f7="9239", f8="j.chang@datatables.net")
    db.ttablesXdynamic5.insert(f0="Brenden", f1="Wagner", f2="Software Engineer", f3="San Francisco", f4="28", f5="2011/06/07", f6="$206,850", f7="1314", f8="b.wagner@datatables.net")
    db.ttablesXdynamic5.insert(f0="Fiona", f1="Green", f2="Chief Operating Officer (COO)", f3="San Francisco", f4="48", f5="2010/03/11", f6="$850,000", f7="2947", f8="f.green@datatables.net")
    db.ttablesXdynamic5.insert(f0="Shou", f1="Itou", f2="Regional Marketing", f3="Tokyo", f4="20", f5="2011/08/14", f6="$163,000", f7="8899", f8="s.itou@datatables.net")
    db.ttablesXdynamic5.insert(f0="Michelle", f1="House", f2="Integration Specialist", f3="Sidney", f4="37", f5="2011/06/02", f6="$95,400", f7="2769", f8="m.house@datatables.net")
    db.ttablesXdynamic5.insert(f0="Suki", f1="Burks", f2="Developer", f3="London", f4="53", f5="2009/10/22", f6="$114,500", f7="6832", f8="s.burks@datatables.net")
    db.ttablesXdynamic5.insert(f0="Prescott", f1="Bartlett", f2="Technical Author", f3="London", f4="27", f5="2011/05/07", f6="$145,000", f7="3606", f8="p.bartlett@datatables.net")
    db.ttablesXdynamic5.insert(f0="Gavin", f1="Cortez", f2="Team Leader", f3="San Francisco", f4="22", f5="2008/10/26", f6="$235,500", f7="2860", f8="g.cortez@datatables.net")
    db.ttablesXdynamic5.insert(f0="Martena", f1="Mccray", f2="Post-Sales support", f3="Edinburgh", f4="46", f5="2011/03/09", f6="$324,050", f7="8240", f8="m.mccray@datatables.net")
    db.ttablesXdynamic5.insert(f0="Unity", f1="Butler", f2="Marketing Designer", f3="San Francisco", f4="47", f5="2009/12/09", f6="$85,675", f7="5384", f8="u.butler@datatables.net")
    db.ttablesXdynamic5.insert(f0="Howard", f1="Hatfield", f2="Office Manager", f3="San Francisco", f4="51", f5="2008/12/16", f6="$164,500", f7="7031", f8="h.hatfield@datatables.net")
    db.ttablesXdynamic5.insert(f0="Hope", f1="Fuentes", f2="Secretary", f3="San Francisco", f4="41", f5="2010/02/12", f6="$109,850", f7="6318", f8="h.fuentes@datatables.net")
    db.ttablesXdynamic5.insert(f0="Vivian", f1="Harrell", f2="Financial Controller", f3="San Francisco", f4="62", f5="2009/02/14", f6="$452,500", f7="9422", f8="v.harrell@datatables.net")
    db.ttablesXdynamic5.insert(f0="Timothy", f1="Mooney", f2="Office Manager", f3="London", f4="37", f5="2008/12/11", f6="$136,200", f7="7580", f8="t.mooney@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jackson", f1="Bradshaw", f2="Director", f3="New York", f4="65", f5="2008/09/26", f6="$645,750", f7="1042", f8="j.bradshaw@datatables.net")
    db.ttablesXdynamic5.insert(f0="Olivia", f1="Liang", f2="Support Engineer", f3="Singapore", f4="64", f5="2011/02/03", f6="$234,500", f7="2120", f8="o.liang@datatables.net")
    db.ttablesXdynamic5.insert(f0="Bruno", f1="Nash", f2="Software Engineer", f3="London", f4="38", f5="2011/05/03", f6="$163,500", f7="6222", f8="b.nash@datatables.net")
    db.ttablesXdynamic5.insert(f0="Sakura", f1="Yamamoto", f2="Support Engineer", f3="Tokyo", f4="37", f5="2009/08/19", f6="$139,575", f7="9383", f8="s.yamamoto@datatables.net")
    db.ttablesXdynamic5.insert(f0="Thor", f1="Walton", f2="Developer", f3="New York", f4="61", f5="2013/08/11", f6="$98,540", f7="8327", f8="t.walton@datatables.net")
    db.ttablesXdynamic5.insert(f0="Finn", f1="Camacho", f2="Support Engineer", f3="San Francisco", f4="47", f5="2009/07/07", f6="$87,500", f7="2927", f8="f.camacho@datatables.net")
    db.ttablesXdynamic5.insert(f0="Serge", f1="Baldwin", f2="Data Coordinator", f3="Singapore", f4="64", f5="2012/04/09", f6="$138,575", f7="8352", f8="s.baldwin@datatables.net")
    db.ttablesXdynamic5.insert(f0="Zenaida", f1="Frank", f2="Software Engineer", f3="New York", f4="63", f5="2010/01/04", f6="$125,250", f7="7439", f8="z.frank@datatables.net")
    db.ttablesXdynamic5.insert(f0="Zorita", f1="Serrano", f2="Software Engineer", f3="San Francisco", f4="56", f5="2012/06/01", f6="$115,000", f7="4389", f8="z.serrano@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jennifer", f1="Acosta", f2="Junior Javascript Developer", f3="Edinburgh", f4="43", f5="2013/02/01", f6="$75,650", f7="3431", f8="j.acosta@datatables.net")
    db.ttablesXdynamic5.insert(f0="Cara", f1="Stevens", f2="Sales Assistant", f3="New York", f4="46", f5="2011/12/06", f6="$145,600", f7="3990", f8="c.stevens@datatables.net")
    db.ttablesXdynamic5.insert(f0="Hermione", f1="Butler", f2="Regional Director", f3="London", f4="47", f5="2011/03/21", f6="$356,250", f7="1016", f8="h.butler@datatables.net")
    db.ttablesXdynamic5.insert(f0="Lael", f1="Greer", f2="Systems Administrator", f3="London", f4="21", f5="2009/02/27", f6="$103,500", f7="6733", f8="l.greer@datatables.net")
    db.ttablesXdynamic5.insert(f0="Jonas", f1="Alexander", f2="Developer", f3="San Francisco", f4="30", f5="2010/07/14", f6="$86,500", f7="8196", f8="j.alexander@datatables.net")
    db.ttablesXdynamic5.insert(f0="Shad", f1="Decker", f2="Regional Director", f3="Edinburgh", f4="51", f5="2008/11/13", f6="$183,000", f7="6373", f8="s.decker@datatables.net")
    db.ttablesXdynamic5.insert(f0="Michael", f1="Bruce", f2="Javascript Developer", f3="Singapore", f4="29", f5="2011/06/27", f6="$183,000", f7="5384", f8="m.bruce@datatables.net")
    db.ttablesXdynamic5.insert(f0="Donna", f1="Snider", f2="Customer Support", f3="New York", f4="27", f5="2011/01/25", f6="$112,000", f7="4226", f8="d.snider@datatables.net")
    db.commit()

if not db(db.totherXcharts0).count():
    db.totherXcharts0.insert(f0="<span class=\"sparkline_line\" style=\"height: 160px;\"><canvas height=\"60\" style=\"display: inline-block; vertical-align: top; width: 94px; height: 30px;\" width=\"200\"></canvas></span>", f1="Line Graph")
    db.totherXcharts0.insert(f0="<span class=\"sparkline_area\" style=\"height: 160px;\"><canvas height=\"60\" style=\"display: inline-block; vertical-align: top; width: 94px; height: 30px;\" width=\"200\"></canvas></span>", f1="Line Area Graph")
    db.totherXcharts0.insert(f0="<span class=\"sparkline_bar\" style=\"height: 160px;\"><canvas height=\"60\" style=\"display: inline-block; vertical-align: top; width: 94px; height: 30px;\" width=\"200\"></canvas></span>", f1="Bar Graph")
    db.totherXcharts0.insert(f0="<span class=\"sparkline_pie\" style=\"height: 160px;\"><canvas height=\"60\" style=\"display: inline-block; vertical-align: top; width: 94px; height: 30px;\" width=\"200\"></canvas></span>", f1="Pie Chart")
    db.totherXcharts0.insert(f0="<span class=\"sparkline_discreet\" style=\"height: 160px;\"><canvas height=\"60\" style=\"display: inline-block; vertical-align: top; width: 94px; height: 30px;\" width=\"200\"></canvas></span>", f1="Discrete chart")
    db.commit()

if not db(db.tprojects0).count():
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"57\" role=\"progressbar\"></div></div> <small>57% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"47\" role=\"progressbar\"></div></div> <small>47% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"77\" role=\"progressbar\"></div></div> <small>77% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"60\" role=\"progressbar\"></div></div> <small>60% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"12\" role=\"progressbar\"></div></div> <small>12% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"35\" role=\"progressbar\"></div></div> <small>35% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"87\" role=\"progressbar\"></div></div> <small>87% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"77\" role=\"progressbar\"></div></div> <small>77% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a>Pesamakini Backend UI</a> <br/> <small>Created 01.01.2015</small>", f2="<ul class=\"list-inline\"><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li><li><img alt=\"Avatar\" class=\"avatar\" src=\"static/tte/images/user.png\"/></li></ul>", f3="<div class=\"progress progress_sm\"><div class=\"progress-bar bg-green\" data-transitiongoal=\"77\" role=\"progressbar\"></div></div> <small>77% Complete</small>", f4="<button class=\"btn btn-success btn-xs\" type=\"button\">Success</button>", f5="<a class=\"btn btn-primary btn-xs\" href=\"#\"><i class=\"fa fa-folder\"></i> View </a> <a class=\"btn btn-info btn-xs\" href=\"#\"><i class=\"fa fa-pencil\"></i> Edit </a> <a class=\"btn btn-danger btn-xs\" href=\"#\"><i class=\"fa fa-trash-o\"></i> Delete </a>")
    db.commit()

if not db(db.tprofile0).count():
    db.tprofile0.insert(f0="1", f1="New Company Takeover Review", f2="Deveint Inc", f3="18", f4="<div class=\"progress\"><div class=\"progress-bar progress-bar-success\" data-transitiongoal=\"35\"></div></div>")
    db.tprofile0.insert(f0="2", f1="New Partner Contracts Consultanci", f2="Deveint Inc", f3="13", f4="<div class=\"progress\"><div class=\"progress-bar progress-bar-danger\" data-transitiongoal=\"15\"></div></div>")
    db.tprofile0.insert(f0="3", f1="Partners and Inverstors report", f2="Deveint Inc", f3="30", f4="<div class=\"progress\"><div class=\"progress-bar progress-bar-success\" data-transitiongoal=\"45\"></div></div>")
    db.tprofile0.insert(f0="4", f1="New Company Takeover Review", f2="Deveint Inc", f3="28", f4="<div class=\"progress\"><div class=\"progress-bar progress-bar-success\" data-transitiongoal=\"75\"></div></div>")
    db.commit()
