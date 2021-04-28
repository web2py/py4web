from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 02.01.2021 13:24:58 UTC+3, src: https://github.com/dropways/deskapp

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
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofile0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofile1',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofile2',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofile3',
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
    'dffaq0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflogin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfindex20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic1',
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
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic2',
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
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','boolean',  ),
    Field('f8','boolean',  ),
    Field('f9','boolean',  ),
    Field('f10','boolean',  ),
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','boolean',  ),
    Field('f8','boolean',  ),
    Field('f9','boolean',  ),
    Field('f10','boolean',  ),
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic5',
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
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','string', length=1024, ),
    Field('f17','string', length=1024, ),
    Field('f18','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic6',
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
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','string', length=1024, ),
    Field('f17','string', length=1024, ),
    Field('f18','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXbasic8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents3',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    Field('f6','boolean',  ),
    Field('f7','boolean',  ),
    Field('f8','boolean',  ),
    Field('f9','boolean',  ),
    Field('f10','boolean',  ),
    Field('f11','boolean',  ),
    Field('f12','boolean',  ),
    Field('f13','boolean',  ),
    Field('f14','boolean',  ),
    Field('f15','boolean',  ),
    Field('f16','boolean',  ),
    Field('f17','boolean',  ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvancedXcomponents5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXwizard0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXwizard1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXwizard2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfhtml5Xeditor0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXpickers0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXpickers1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXpickers2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfimageXcropper0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfimageXdropzone0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfimageXdropzone1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdatatable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXbuttons0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXcards0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXcardsXhover0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXmodals0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXmodals1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfuiXtabs0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXtooltipXpopover0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXsweetXalert0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXnotification0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXtimeline0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXprogressbar0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXtypography0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXlistXgroup0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXrangeXslider0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXcarousel0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffontXawesome0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffoundation0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfionicons0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfthemify0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcustomXicon0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfhighchart0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfknobXchart0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfjvectormap0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfapexcharts0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfvideoXplayer0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfresetXpassword0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblank0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontactXdirectory0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblog0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblogXdetail0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfproduct0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfproductXdetail0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgallery0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpricingXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsitemap0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfchat0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinvoice0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfintroduction0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgettingXstarted0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcolorXsettings0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfthirdXpartyXplugins0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregister0',
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
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','boolean',  ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable7',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable9',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdatatable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdatatable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdatatable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdatatable3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tthirdXpartyXplugins0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="<img alt=\"\" height=\"70\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"70\"/>", f1="<h5 class=\"font-16\">Shirt</h5>", f2="Black", f3="M", f4="$1000", f5="1", f6="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tindex0.insert(f0="<img alt=\"\" height=\"70\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"70\"/>", f1="<h5 class=\"font-16\">Boots</h5>", f2="brown", f3="9UK", f4="$900", f5="1", f6="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tindex0.insert(f0="<img alt=\"\" height=\"70\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"70\"/>", f1="<h5 class=\"font-16\">Hat</h5>", f2="Orange", f3="M", f4="$100", f5="4", f6="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tindex0.insert(f0="<img alt=\"\" height=\"70\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"70\"/>", f1="<h5 class=\"font-16\">Long Dress</h5>", f2="Gray", f3="L", f4="$1000", f5="1", f6="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tindex0.insert(f0="<img alt=\"\" height=\"70\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"70\"/>", f1="<h5 class=\"font-16\">Blazer</h5>", f2="Blue", f3="M", f4="$1000", f5="1", f6="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.commit()

if not db(db.tindex30).count():
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Jennifer O. Oster</div></div></div>", f1="Female", f2="45 kg", f3="Dr. Callie Reed", f4="19 Oct 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Typhoid</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Doris L. Larson</div></div></div>", f1="Male", f2="76 kg", f3="Dr. Ren Delan", f4="22 Jul 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Dengue</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">JosephPowell</div></div></div>", f1="Male", f2="90 kg", f3="Dr. Allen Hannagan", f4="15 Nov 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Infection</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Jake Springer</div></div></div>", f1="Female", f2="45 kg", f3="Dr. Garrett Kincy", f4="08 Oct 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Covid 19</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Paul Buckland</div></div></div>", f1="Male", f2="76 kg", f3="Dr. Maxwell Soltes", f4="12 Dec 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Asthma</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Neil Arnold</div></div></div>", f1="Male", f2="60 kg", f3="Dr. Sebastian Tandon", f4="30 Oct 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Diabetes</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Christian Dyer</div></div></div>", f1="Male", f2="80 kg", f3="Dr. Sebastian Tandon", f4="15 Jun 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Diabetes</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.tindex30.insert(f0="<div class=\"name-avatar d-flex align-items-center\"><div class=\"avatar mr-2 flex-shrink-0\"><img alt=\"\" class=\"border-radius-100 shadow\" height=\"40\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"40\"/></div><div class=\"txt\"><div class=\"weight-600\">Doris L. Larson</div></div></div>", f1="Male", f2="76 kg", f3="Dr. Ren Delan", f4="22 Jul 2020", f5="<span class=\"badge badge-pill\" data-bgcolor=\"#e7ebf5\" data-color=\"#265ed7\">Dengue</span>", f6="<div class=\"table-actions\"><a data-color=\"#265ed7\" href=\"#\"><i class=\"icon-copy dw dw-edit2\"></i></a><a data-color=\"#e95959\" href=\"#\"><i class=\"icon-copy dw dw-delete-3\"></i></a></div>")
    db.commit()

if not db(db.tbasicXtable0).count():
    db.tbasicXtable0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<span class=\"badge badge-primary\">Primary</span>")
    db.tbasicXtable0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.commit()

if not db(db.tbasicXtable1).count():
    db.tbasicXtable1.insert(f0="1")
    db.commit()

if not db(db.tbasicXtable2).count():
    db.tbasicXtable2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<span class=\"badge badge-primary\">Primary</span>")
    db.tbasicXtable2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable2.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.commit()

if not db(db.tbasicXtable3).count():
    db.tbasicXtable3.insert(f0="1")
    db.commit()

if not db(db.tbasicXtable4).count():
    db.tbasicXtable4.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<span class=\"badge badge-primary\">Primary</span>")
    db.tbasicXtable4.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable4.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable4.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable4.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.commit()

if not db(db.tbasicXtable5).count():
    db.tbasicXtable5.insert(f0="1")
    db.commit()

if not db(db.tbasicXtable6).count():
    db.tbasicXtable6.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<span class=\"badge badge-primary\">Primary</span>")
    db.tbasicXtable6.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable6.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable6.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable6.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.commit()

if not db(db.tbasicXtable7).count():
    db.tbasicXtable7.insert(f0="1")
    db.commit()

if not db(db.tbasicXtable8).count():
    db.tbasicXtable8.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<span class=\"badge badge-primary\">Primary</span>")
    db.tbasicXtable8.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable8.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<span class=\"badge badge-secondary\">Secondary</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.tbasicXtable8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<span class=\"badge badge-success\">Success</span>")
    db.commit()

if not db(db.tbasicXtable9).count():
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.tbasicXtable9.insert(f0="==0")
    db.commit()

if not db(db.tdatatable0).count():
    db.tdatatable0.insert(f0="Gloria F. Mead", f1="25", f2="Sagittarius", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="20", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="25", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="20", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="18", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.tdatatable0.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="<div class=\"dropdown\"><a class=\"btn btn-link font-24 p-0 line-height-1 no-arrow dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\" role=\"button\"><i class=\"dw dw-more\"></i></a><div class=\"dropdown-menu dropdown-menu-right dropdown-menu-icon-list\"><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-eye\"></i> View</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-edit2\"></i> Edit</a><a class=\"dropdown-item\" href=\"#\"><i class=\"dw dw-delete-3\"></i> Delete</a></div></div>")
    db.commit()

if not db(db.tdatatable1).count():
    db.tdatatable1.insert(f0="Gloria F. Mead", f1="25", f2="Sagittarius", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="20", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="25", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="20", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="18", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable1.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.commit()

if not db(db.tdatatable2).count():
    db.tdatatable2.insert(f0="==0", f1="Tiger Nixon", f2="System Architect", f3="Tokyo", f4="2008/11/28", f5="$162,700")
    db.tdatatable2.insert(f0="==0", f1="Angelica Ramos", f2="Chief Executive Officer (CEO)", f3="London", f4="2009/10/09", f5="$1,200,000")
    db.tdatatable2.insert(f0="==0", f1="Ashton Cox", f2="Junior Technical Author", f3="San Francisco", f4="2009/01/12", f5="$86,000")
    db.tdatatable2.insert(f0="==0", f1="Bradley Greer", f2="Software Engineer", f3="London", f4="2012/10/13", f5="$132,000")
    db.tdatatable2.insert(f0="==0", f1="Brenden Wagner", f2="Software Engineer", f3="San Francisco", f4="2011/06/07", f5="$206,850")
    db.tdatatable2.insert(f0="==0", f1="Caesar Vance", f2="Pre-Sales Support", f3="New York", f4="2011/12/12", f5="$106,450")
    db.tdatatable2.insert(f0="==0", f1="Cedric Kelly", f2="Senior Javascript Developer", f3="Edinburgh", f4="2012/03/29", f5="$433,060")
    db.tdatatable2.insert(f0="==0", f1="Dai Rios", f2="Personnel Lead", f3="Edinburgh", f4="2012/09/26", f5="$217,500")
    db.tdatatable2.insert(f0="==0", f1="Doris Wilder", f2="Sales Assistant", f3="Sidney", f4="2010/09/20", f5="$85,600")
    db.tdatatable2.insert(f0="==0", f1="Fiona Green", f2="Chief Operating Officer (COO)", f3="San Francisco", f4="2010/03/11", f5="$850,000")
    db.tdatatable2.insert(f0="==0", f1="Gavin Cortez", f2="Team Leader", f3="San Francisco", f4="2008/10/26", f5="$235,500")
    db.tdatatable2.insert(f0="==0", f1="Herrod Chandler", f2="Sales Assistant", f3="San Francisco", f4="2012/08/06", f5="$137,500")
    db.tdatatable2.insert(f0="==0", f1="Hope Fuentes", f2="Secretary", f3="San Francisco", f4="2010/02/12", f5="$109,850")
    db.tdatatable2.insert(f0="==0", f1="Jena Gaines", f2="Office Manager", f3="London", f4="2008/12/19", f5="$90,560")
    db.commit()

if not db(db.tdatatable3).count():
    db.tdatatable3.insert(f0="Gloria F. Mead", f1="25", f2="Sagittarius", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="20", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="25", f2="Gemini", f3="2829 Trainer Avenue Peoria, IL 61602", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="20", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="18", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Sagittarius", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.tdatatable3.insert(f0="Andrea J. Cagle", f1="30", f2="Gemini", f3="1280 Prospect Valley Road Long Beach, CA 90802", f4="29-03-2018", f5="$162,700")
    db.commit()

if not db(db.tthirdXpartyXplugins0).count():
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">air-datepicker</span>", f1="<a class=\"text-blue\" href=\"http://t1m0n.name/air-datepicker/docs/\" target=\"_blank\">http://t1m0n.name/air-datepicker/docs/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">apexcharts</span>", f1="<a class=\"text-blue\" href=\"https://apexcharts.com/\" target=\"_blank\">https://apexcharts.com/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">bootstrap</span>", f1="<a class=\"text-blue\" href=\"https://getbootstrap.com/\" target=\"_blank\">https://getbootstrap.com/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">bootstrap select</span>", f1="<a class=\"text-blue\" href=\"https://developer.snapappointments.com/bootstrap-select/\" target=\"_blank\">https://developer.snapappointments.com/bootstrap-select/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">bootstrap-tagsinput</span>", f1="<a class=\"text-blue\" href=\"https://bootstrap-tagsinput.github.io/bootstrap-tagsinput/examples/\" target=\"_blank\">https://bootstrap-tagsinput.github.io/bootstrap-tagsinput/examples/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">Bootstrap TouchSpin</span>", f1="<a class=\"text-blue\" href=\"https://www.virtuosoft.eu/code/bootstrap-touchspin/\" target=\"_blank\">https://www.virtuosoft.eu/code/bootstrap-touchspin/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">bootstrap-wysihtml5</span>", f1="<a class=\"text-blue\" href=\"https://jhollingworth.github.io/bootstrap-wysihtml5/\" target=\"_blank\">https://jhollingworth.github.io/bootstrap-wysihtml5/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">cropperjs</span>", f1="<a class=\"text-blue\" href=\"https://fengyuanchen.github.io/cropperjs/\" target=\"_blank\">https://fengyuanchen.github.io/cropperjs/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">datatables</span>", f1="<a class=\"text-blue\" href=\"https://datatables.net/\" target=\"_blank\">https://datatables.net/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">dropzonejs</span>", f1="<a class=\"text-blue\" href=\"https://www.dropzonejs.com/\" target=\"_blank\">https://www.dropzonejs.com/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">fancybox</span>", f1="<a class=\"text-blue\" href=\"http://fancyapps.com/fancybox/\" target=\"_blank\">http://fancyapps.com/fancybox/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">fullcalendar</span>", f1="<a class=\"text-blue\" href=\"https://fullcalendar.io/\" target=\"_blank\">https://fullcalendar.io/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">Highcharts JS</span>", f1="<a class=\"text-blue\" href=\"https://www.highcharts.com/\" target=\"_blank\">https://www.highcharts.com/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">highlightjs</span>", f1="<a class=\"text-blue\" href=\"https://highlightjs.org/\" target=\"_blank\">https://highlightjs.org/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">Ion.RangeSlider</span>", f1="<a class=\"text-blue\" href=\"http://ionden.com/a/plugins/ion.rangeSlider/index.html\" target=\"_blank\">http://ionden.com/a/plugins/ion.rangeSlider/index.html</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jquery-asColor</span>", f1="<a class=\"text-blue\" href=\"https://github.com/thecreation/jquery-asColor\" target=\"_blank\">https://github.com/thecreation/jquery-asColor</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jquery-asColorPicker</span>", f1="<a class=\"text-blue\" href=\"https://github.com/thecreation/jquery-asColorPicker\" target=\"_blank\">https://github.com/thecreation/jquery-asColorPicker</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jquery-asGradient</span>", f1="<a class=\"text-blue\" href=\"https://github.com/thecreation/jquery-asGradient\" target=\"_blank\">https://github.com/thecreation/jquery-asGradient</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jQuery Knob</span>", f1="<a class=\"text-blue\" href=\"http://anthonyterrien.com/knob/\" target=\"_blank\">http://anthonyterrien.com/knob/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jquery-steps</span>", f1="<a class=\"text-blue\" href=\"http://www.jquery-steps.com\" target=\"_blank\">http://www.jquery-steps.com</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">jVectorMap</span>", f1="<a class=\"text-blue\" href=\"https://jvectormap.com/\" target=\"_blank\">https://jvectormap.com/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">malihu jquery custom scrollbar</span>", f1="<a class=\"text-blue\" href=\"http://manos.malihu.gr/jquery-custom-content-scroller/\" target=\"_blank\">http://manos.malihu.gr/jquery-custom-content-scroller/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">plyr</span>", f1="<a class=\"text-blue\" href=\"https://plyr.io/\" target=\"_blank\">https://plyr.io/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">select2</span>", f1="<a class=\"text-blue\" href=\"https://select2.github.io\" target=\"_blank\">https://select2.github.io</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">slick</span>", f1="<a class=\"text-blue\" href=\"https://kenwheeler.github.io/slick/\" target=\"_blank\">https://kenwheeler.github.io/slick/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">sweetalert2</span>", f1="<a class=\"text-blue\" href=\"https://sweetalert2.github.io/\" target=\"_blank\">https://sweetalert2.github.io/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">switchery</span>", f1="<a class=\"text-blue\" href=\"https://abpetkov.github.io/switchery/\" target=\"_blank\">https://abpetkov.github.io/switchery/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">timedropper</span>", f1="<a class=\"text-blue\" href=\"https://felicegattuso.com/projects/timedropper/\" target=\"_blank\">https://felicegattuso.com/projects/timedropper/</a>")
    db.tthirdXpartyXplugins0.insert(f0="<span class=\"badge badge-pill table-badge\">wysihtml5</span>", f1="<a class=\"text-blue\" href=\"https://github.com/xing/wysihtml5\" target=\"_blank\">https://github.com/xing/wysihtml5</a>")
    db.commit()
