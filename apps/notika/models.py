from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 01.12.2020 12:08:01 UTC+3
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
    'dfindex0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex7',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX21',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX22',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX23',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX24',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX25',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX26',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX27',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX30',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX31',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX32',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX33',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX34',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX35',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX36',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX37',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX40',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX41',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX42',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX43',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX44',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX45',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX46',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindexX47',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfanalytics0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfanalytics1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets6',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox3',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox4',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox5',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox6',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox7',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox8',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox9',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfinbox10',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfviewXemail0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfviewXemail1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcomposeXemail0',
    )
db.commit()

db.define_table(
    'dfanimations0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfanimations1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgoogleXmap0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgoogleXmap1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdataXmap0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdataXmap1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcodeXeditor0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcodeXeditor1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfimageXcropper0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfimageXcropper1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwizard0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwizard1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfflotXcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfflotXcharts1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbarXcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbarXcharts1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflineXcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflineXcharts1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfareaXcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfareaXcharts1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnormalXtable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnormalXtable1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdataXtable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdataXtable1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements7',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements8',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements9',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements10',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements11',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements12',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements13',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements14',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements15',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements16',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements17',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements18',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements19',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements20',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements21',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements22',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXelements23',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXelements24',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXelements25',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements26',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements27',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXcomponents0',
    )
db.commit()

db.define_table(
    'dfformXexamples0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples4',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXexamples5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples7',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXexamples8',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples9',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXexamples10',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfnotification0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnotification1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfalert0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfalert1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodals0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodals1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbuttons1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftabs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftabs1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfaccordion0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfaccordion1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdialog0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdialog1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpopovers0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpopovers1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftooltips0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftooltips1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdropdown0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdropdown1',
    Field('f0','string', length=1024, ),
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
    'dfinvoice0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinvoice1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftypography1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcolor0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcolor1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister2',
    Field('f0','boolean',  ),
    )
db.commit()

db.define_table(
    'dfloginXregister3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXregister6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindexX20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindexX30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindexX40',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tanalytics0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tanalytics1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tanalytics2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinbox0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tnormalXtable5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
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

if not db(db.tindex0).count():
    db.tindex0.insert(f0="4555", f1="Samsung Galaxy Mega", f2="$921")
    db.tindex0.insert(f0="4556", f1="Huawei Ascend P6", f2="$240")
    db.tindex0.insert(f0="8778", f1="HTC One M8", f2="$400")
    db.tindex0.insert(f0="5667", f1="Samsung Galaxy Alpha", f2="$870")
    db.tindex0.insert(f0="7886", f1="LG G3", f2="$790")
    db.commit()

if not db(db.tindexX20).count():
    db.tindexX20.insert(f0="4555", f1="Samsung Galaxy Mega", f2="$921")
    db.tindexX20.insert(f0="4556", f1="Huawei Ascend P6", f2="$240")
    db.tindexX20.insert(f0="8778", f1="HTC One M8", f2="$400")
    db.tindexX20.insert(f0="5667", f1="Samsung Galaxy Alpha", f2="$870")
    db.tindexX20.insert(f0="7886", f1="LG G3", f2="$790")
    db.commit()

if not db(db.tindexX30).count():
    db.tindexX30.insert(f0="4555", f1="Samsung Galaxy Mega", f2="$921")
    db.tindexX30.insert(f0="4556", f1="Huawei Ascend P6", f2="$240")
    db.tindexX30.insert(f0="8778", f1="HTC One M8", f2="$400")
    db.tindexX30.insert(f0="5667", f1="Samsung Galaxy Alpha", f2="$870")
    db.tindexX30.insert(f0="7886", f1="LG G3", f2="$790")
    db.commit()

if not db(db.tindexX40).count():
    db.tindexX40.insert(f0="4555", f1="Samsung Galaxy Mega", f2="$921")
    db.tindexX40.insert(f0="4556", f1="Huawei Ascend P6", f2="$240")
    db.tindexX40.insert(f0="8778", f1="HTC One M8", f2="$400")
    db.tindexX40.insert(f0="5667", f1="Samsung Galaxy Alpha", f2="$870")
    db.tindexX40.insert(f0="7886", f1="LG G3", f2="$790")
    db.commit()

if not db(db.tanalytics0).count():
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/google.png\"/>", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/bing.png\"/>", f1="<i class=\"notika-icon notika-down-arrow\"></i>")
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/baidu.png\"/>", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/yahoo.png\"/>", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/duckduckgo.png\"/>", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics0.insert(f0="<img alt=\"\" class=\"search-engine-img\" src=\"static/tte/img/search-engines/yandex.png\"/>", f1="<i class=\"notika-icon notika-down-arrow\"></i>")
    db.commit()

if not db(db.tanalytics1).count():
    db.tanalytics1.insert(f0="themeforest.net", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics1.insert(f0="codecanyon.net", f1="<i class=\"notika-icon notika-down-arrow\"></i>")
    db.tanalytics1.insert(f0="google.com", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics1.insert(f0="yahoo.com", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.tanalytics1.insert(f0="youtube.com", f1="<i class=\"notika-icon notika-down-arrow\"></i>")
    db.tanalytics1.insert(f0="bing.com", f1="<i class=\"notika-icon notika-up-arrow\"></i>")
    db.commit()

if not db(db.tanalytics2).count():
    db.tanalytics2.insert(f0="External Backlinks", f1="<h4>54,302</h4>")
    db.tanalytics2.insert(f0="Page Speed Score", f1="<h4>87</h4>")
    db.tanalytics2.insert(f0="Citation Flow", f1="<h4>987</h4>")
    db.tanalytics2.insert(f0="Mozrank", f1="<h4>9.43</h4>")
    db.tanalytics2.insert(f0="Domain Authority", f1="<h4>455</h4>")
    db.tanalytics2.insert(f0="Alexa Rank", f1="<h4>342,234</h4>")
    db.commit()

if not db(db.tinbox0).count():
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Marshall Horne </a>", f2="<a href=\"#\"> Praesent nec nisl sed neque ornare maximus at ac enim. </a>", f3="==0", f4="Wed, Jan 13")
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Grant Franco </a> <span class=\"label label-warning\"> Finance </span>", f2="<a href=\"#\"> Etiam maximus tellus a turpis tempor mollis. </a>", f3="==0", f4="Mon, Oct 19")
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Ferdinand Meadows </a>", f2="<a href=\"#\"> Aenean hendrerit ligula eget augue gravida semper. </a>", f3="<i class=\"notika-icon notika-paperclip\"></i>", f4="Sat, Aug 29")
    db.tinbox0.insert(f0="<label><input checked=\"\" class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Ivor Rios </a> <span class=\"label label-info\"> Social </span>", f2="<a href=\"#\"> Sed quis augue in nunc venenatis finibus. </a>", f3="<i class=\"notika-icon notika-paperclip\"></i>", f4="Sat, Dec 12")
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Maxwell Murphy </a>", f2="<a href=\"#\"> Quisque eu tortor quis justo viverra cursus. </a>", f3="==0", f4="Sun, May 17")
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Henry Patterson </a>", f2="<a href=\"#\"> Aliquam nec justo interdum, ornare mi non, elementum lacus. </a>", f3="<i class=\"notika-icon notika-paperclip\"></i>", f4="Thu, Aug 06")
    db.tinbox0.insert(f0="<label><input class=\"i-checks\" type=\"checkbox\"/></label>", f1="<a href=\"#\"> Maxwell Murphy </a>", f2="<a href=\"#\"> Quisque eu tortor quis justo viverra cursus. </a>", f3="==0", f4="Sun, May 17")
    db.commit()

if not db(db.tnormalXtable0).count():
    db.tnormalXtable0.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable0.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable0.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable0.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable0.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.tnormalXtable0.insert(f0="6", f1="Benjamin", f2="Parnell", f3="@wayne234", f4="Pokie")
    db.tnormalXtable0.insert(f0="7", f1="Katherine", f2="Buckland", f3="@anitabelle", f4="Wokie")
    db.tnormalXtable0.insert(f0="8", f1="Nicholas", f2="Walmart", f3="@mwalmart", f4="Spike")
    db.commit()

if not db(db.tnormalXtable1).count():
    db.tnormalXtable1.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable1.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable1.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable1.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable1.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.tnormalXtable1.insert(f0="6", f1="Benjamin", f2="Parnell", f3="@wayne234", f4="Pokie")
    db.tnormalXtable1.insert(f0="7", f1="Katherine", f2="Buckland", f3="@anitabelle", f4="Wokie")
    db.tnormalXtable1.insert(f0="8", f1="Nicholas", f2="Walmart", f3="@mwalmart", f4="Spike")
    db.commit()

if not db(db.tnormalXtable2).count():
    db.tnormalXtable2.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable2.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable2.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable2.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable2.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.tnormalXtable2.insert(f0="6", f1="Benjamin", f2="Parnell", f3="@wayne234", f4="Pokie")
    db.tnormalXtable2.insert(f0="7", f1="Katherine", f2="Buckland", f3="@anitabelle", f4="Wokie")
    db.tnormalXtable2.insert(f0="8", f1="Nicholas", f2="Walmart", f3="@mwalmart", f4="Spike")
    db.commit()

if not db(db.tnormalXtable3).count():
    db.tnormalXtable3.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable3.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable3.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable3.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable3.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.tnormalXtable3.insert(f0="6", f1="Benjamin", f2="Parnell", f3="@wayne234", f4="Pokie")
    db.tnormalXtable3.insert(f0="7", f1="Katherine", f2="Buckland", f3="@anitabelle", f4="Wokie")
    db.tnormalXtable3.insert(f0="8", f1="Nicholas", f2="Walmart", f3="@mwalmart", f4="Spike")
    db.commit()

if not db(db.tnormalXtable4).count():
    db.tnormalXtable4.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable4.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable4.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable4.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable4.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.tnormalXtable4.insert(f0="6", f1="Benjamin", f2="Parnell", f3="@wayne234", f4="Pokie")
    db.tnormalXtable4.insert(f0="7", f1="Katherine", f2="Buckland", f3="@anitabelle", f4="Wokie")
    db.tnormalXtable4.insert(f0="8", f1="Nicholas", f2="Walmart", f3="@mwalmart", f4="Spike")
    db.commit()

if not db(db.tnormalXtable5).count():
    db.tnormalXtable5.insert(f0="1", f1="Alexandra", f2="Christopher", f3="@makinton", f4="Ducky")
    db.tnormalXtable5.insert(f0="3", f1="Sebastian", f2="Johnston", f3="@sebastian", f4="Jaycee")
    db.tnormalXtable5.insert(f0="4", f1="Mitchell", f2="Christin", f3="@mitchell4u", f4="AdskiDeAnus")
    db.tnormalXtable5.insert(f0="2", f1="Madeleine", f2="Hollaway", f3="@hollway", f4="Cheese")
    db.tnormalXtable5.insert(f0="5", f1="Elizabeth", f2="Belkitt", f3="@belkitt", f4="Goat")
    db.commit()

if not db(db.tdataXtable0).count():
    db.tdataXtable0.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtable0.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtable0.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtable0.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtable0.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtable0.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtable0.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtable0.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtable0.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtable0.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtable0.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtable0.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtable0.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtable0.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtable0.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtable0.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtable0.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtable0.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtable0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtable0.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtable0.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtable0.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtable0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtable0.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtable0.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtable0.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtable0.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtable0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtable0.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtable0.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtable0.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtable0.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtable0.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtable0.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtable0.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtable0.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtable0.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtable0.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtable0.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtable0.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtable0.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtable0.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtable0.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtable0.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtable0.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtable0.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtable0.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtable0.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtable0.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtable0.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtable0.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtable0.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtable0.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtable0.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtable0.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtable0.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtable0.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtable0.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="1", f1="Crusal Damperal", f2="$500", f3="05", f4="$3000")
    db.tinvoice0.insert(f0="2", f1="Indriacal Superral", f2="$650", f3="06", f4="$7000")
    db.tinvoice0.insert(f0="3", f1="Vidaska Adrioal", f2="$400", f3="03", f4="$2000")
    db.tinvoice0.insert(f0="4", f1="Croustal Desrikal", f2="$600", f3="04", f4="$7000")
    db.commit()
