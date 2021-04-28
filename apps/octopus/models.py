from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 01.12.2020 12:03:27 UTC+3
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
    'dfpagesXsearchXresults0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsearchXresults1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXuserXprofile0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXuserXprofile1',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXuserXprofile2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsignin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfmailboxXfolder0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsignup0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfpagesXrecoverXpassword0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXlockXscreen0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsessionXtimeout0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXcalendar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXtimeline0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXmediaXgallery0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXinvoice0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXblank0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesX4040',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXlogXviewer0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXtypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXicons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXtabs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXpanels0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXwidgets0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXportlets0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXalerts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXnotifications0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXmodals0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXmodals1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXlightbox0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXlightbox1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXprogressbars0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXsliders0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXcarousels0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXaccordions0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXnestable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXtreeXview0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXgridXsystem0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXanimations0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXelementsXextra0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic1',
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
    Field('f19','string', length=1024, ),
    Field('f20','string', length=1024, ),
    Field('f21','string', length=1024, ),
    Field('f22','string', length=1024, ),
    Field('f23','string', length=1024, ),
    Field('f24','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic3',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    Field('f6','boolean',  ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','boolean',  ),
    Field('f9','string', length=1024, ),
    Field('f10','string', length=1024, ),
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXbasic5',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    Field('f6','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXbasic6',
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
    'dfformsXbasic7',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced2',
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
    'dfformsXadvanced3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced4',
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
    'dfformsXadvanced5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced9',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXadvanced10',
    )
db.commit()

db.define_table(
    'dfformsXadvanced11',
    )
db.commit()

db.define_table(
    'dfformsXadvanced12',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXvalidation0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXvalidation1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXvalidation2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXvalidation3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXvalidation4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXwizard0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXwizard1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXwizard2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXwizard3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXwizard4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXwizard5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformsXcodeXeditor0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXcodeXeditor1',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXbasic0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXadvanced0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXresponsive0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXeditable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXajax0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXpricing0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmapsXgoogleXmaps0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmapsXgoogleXmapsXbuilder0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmapsXgoogleXmapsXbuilder1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmapsXvector0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflayoutsXdefault0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflayoutsXboxed0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflayoutsXmenuXcollapsed0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflayoutsXscroll0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmailboxXemail0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmailboxXcompose0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmailboxXcompose1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXinvoice0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXinvoice1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXlogXviewer0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXlogXviewer1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXlogXviewer2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbasic9',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXadvanced0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXadvanced1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXadvanced2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXresponsive0',
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
    'ttablesXresponsive1',
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
    'ttablesXresponsive2',
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
    'ttablesXeditable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXajax0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXinvoiceXprint0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tpagesXinvoiceXprint1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="1", f1="JSOFT - Responsive HTML5 Template", f2="<span class=\"label label-success\">Success</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 100%;\">100%</div></div>")
    db.tindex0.insert(f0="2", f1="JSOFT - Responsive Drupal 7 Theme", f2="<span class=\"label label-success\">Success</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 100%;\">100%</div></div>")
    db.tindex0.insert(f0="3", f1="Tucson - Responsive HTML5 Template", f2="<span class=\"label label-warning\">Warning</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 60%;\">60%</div></div>")
    db.tindex0.insert(f0="4", f1="Tucson - Responsive Business WordPress Theme", f2="<span class=\"label label-success\">Success</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 90%;\">90%</div></div>")
    db.tindex0.insert(f0="5", f1="JSOFT - Responsive Admin HTML5 Template", f2="<span class=\"label label-warning\">Warning</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 45%;\">45%</div></div>")
    db.tindex0.insert(f0="6", f1="JSOFT - Responsive HTML5 Template", f2="<span class=\"label label-danger\">Danger</span>", f3="<div class=\"progress progress-sm progress-half-rounded m-none mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 40%;\">40%</div></div>")
    db.tindex0.insert(f0="7", f1="JSOFT - Responsive Drupal 7 Theme", f2="<span class=\"label label-success\">Success</span>", f3="<div class=\"progress progress-sm progress-half-rounded mt-xs light\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar progress-bar-primary\" role=\"progressbar\" style=\"width: 95%;\">95%</div></div>")
    db.commit()

if not db(db.tpagesXinvoice0).count():
    db.tpagesXinvoice0.insert(f0="123456", f1="Porto HTML5 Template", f2="Multipourpouse Website Template", f3="$14.00", f4="2", f5="$28.00")
    db.tpagesXinvoice0.insert(f0="654321", f1="Tucson HTML5 Template", f2="Awesome Website Template", f3="$17.00", f4="1", f5="$17.00")
    db.commit()

if not db(db.tpagesXinvoice1).count():
    db.tpagesXinvoice1.insert(f0="Shipping", f1="$0.00")
    db.tpagesXinvoice1.insert(f0="Grand Total", f1="$73.00")
    db.commit()

if not db(db.tpagesXlogXviewer0).count():
    db.tpagesXlogXviewer0.insert(f0="<i class=\"fa fa-bug fa-fw text-muted text-md va-middle\"></i>", f1="13/04/2014 18:25:59", f2="my.host - oh snap! another exception")
    db.tpagesXlogXviewer0.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="13/04/2014 21:50:17", f2="GET / HTTP/1.1 200 1225")
    db.tpagesXlogXviewer0.insert(f0="<i class=\"fa fa-warning fa-fw text-warning text-md va-middle\"></i>", f1="13/04/2014 17:44:21", f2="DocumentRoot [/var/www/porto-admin/] does not exist")
    db.tpagesXlogXviewer0.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:18", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer0.insert(f0="<i class=\"fa fa-ban fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 22:13:39", f2="not a tree object")
    db.commit()

if not db(db.tpagesXlogXviewer1).count():
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:30", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:29", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:28", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:27", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:26", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-times-circle fa-fw text-danger text-md va-middle\"></i>", f1="13/04/2014 21:55:25", f2="File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="<i class=\"fa fa-ban fa-fw text-danger text-md va-middle\"></i>", f1="12/04/2014 22:13:39", f2="not a tree object")
    db.commit()

if not db(db.tpagesXlogXviewer2).count():
    db.tpagesXlogXviewer2.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="12/04/2014 21:50:54", f2="GET / HTTP/1.1 200 1225")
    db.tpagesXlogXviewer2.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="12/04/2014 21:50:53", f2="GET /assets/vendor/bootstrap/css/bootstrap.css HTTP/1.1 200 110495")
    db.tpagesXlogXviewer2.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="12/04/2014 21:50:52", f2="GET /assets/stylesheets/theme.css HTTP/1.1 200 1273")
    db.tpagesXlogXviewer2.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="12/04/2014 21:50:51", f2="GET /assets/stylesheets/skin.css HTTP/1.1 200 230")
    db.tpagesXlogXviewer2.insert(f0="<i class=\"fa fa-info fa-fw text-info text-md va-middle\"></i>", f1="12/04/2014 21:50:50", f2="GET /assets/vendor/jquery/jquery.js HTTP/1.1 200 244962")
    db.commit()

if not db(db.ttablesXbasic0).count():
    db.ttablesXbasic0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttablesXbasic1).count():
    db.ttablesXbasic1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttablesXbasic2).count():
    db.ttablesXbasic2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic2.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttablesXbasic3).count():
    db.ttablesXbasic3.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic3.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic3.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttablesXbasic4).count():
    db.ttablesXbasic4.insert(f0="1", f1="active", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="2", f1="primary", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="3", f1="success", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="4", f1="warning", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="5", f1="danger", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="6", f1="info", f2="Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="7", f1="dark", f2="Lorem ipsum dolor sit amet")
    db.commit()

if not db(db.ttablesXbasic5).count():
    db.ttablesXbasic5.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic5.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic5.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.ttablesXbasic5.insert(f0="4", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic5.insert(f0="5", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttablesXbasic5.insert(f0="6", f1="Larry", f2="the Bird", f3="@twitter")
    db.ttablesXbasic5.insert(f0="7", f1="Mark", f2="Otto", f3="@mdo")
    db.ttablesXbasic5.insert(f0="8", f1="Jacob", f2="Thornton", f3="@fat")
    db.commit()

if not db(db.ttablesXbasic6).count():
    db.ttablesXbasic6.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic6.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic6.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.commit()

if not db(db.ttablesXbasic7).count():
    db.ttablesXbasic7.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic7.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic7.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.commit()

if not db(db.ttablesXbasic8).count():
    db.ttablesXbasic8.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic8.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic8.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.commit()

if not db(db.ttablesXbasic9).count():
    db.ttablesXbasic9.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic9.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXbasic9.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter", f4="<a href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"delete-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.commit()

if not db(db.ttablesXadvanced0).count():
    db.ttablesXadvanced0.insert(f0="Trident", f1="InternetExplorer 4.0", f2="Win 95+", f3="4", f4="X")
    db.ttablesXadvanced0.insert(f0="Trident", f1="InternetExplorer 5.0", f2="Win 95+", f3="5", f4="C")
    db.ttablesXadvanced0.insert(f0="Trident", f1="InternetExplorer 5.5", f2="Win 95+", f3="5.5", f4="A")
    db.ttablesXadvanced0.insert(f0="Trident", f1="InternetExplorer 6", f2="Win 98+", f3="6", f4="A")
    db.ttablesXadvanced0.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="7", f4="A")
    db.ttablesXadvanced0.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="6", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="1.7", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="1.9", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="1.7", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="1.7", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="1", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="1.1", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="1.2", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="1.3", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="1.4", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="1.5", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="1.6", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="1.7", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="1.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="125.5", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="312.8", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="419.3", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="522.1", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="420", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="420.1", f4="A")
    db.ttablesXadvanced0.insert(f0="Webkit", f1="S60", f2="S60", f3="413", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="8.5", f4="<sup>1</sup>")
    db.ttablesXadvanced0.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="3.1", f4="C")
    db.ttablesXadvanced0.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="3.3", f4="A")
    db.ttablesXadvanced0.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="3.5", f4="A")
    db.ttablesXadvanced0.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="-", f4="X")
    db.ttablesXadvanced0.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="1", f4="C")
    db.ttablesXadvanced0.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="1", f4="C")
    db.ttablesXadvanced0.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="-", f4="C")
    db.ttablesXadvanced0.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="-", f4="A")
    db.ttablesXadvanced0.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="-", f4="X")
    db.ttablesXadvanced0.insert(f0="Misc", f1="Links", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced0.insert(f0="Misc", f1="Lynx", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced0.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="-", f4="C")
    db.ttablesXadvanced0.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="-", f4="C")
    db.ttablesXadvanced0.insert(f0="Other browsers", f1="All others", f2="-", f3="-", f4="U")
    db.commit()

if not db(db.ttablesXadvanced1).count():
    db.ttablesXadvanced1.insert(f0="Trident", f1="InternetExplorer 4.0", f2="Win 95+", f3="4", f4="X")
    db.ttablesXadvanced1.insert(f0="Trident", f1="InternetExplorer 5.0", f2="Win 95+", f3="5", f4="C")
    db.ttablesXadvanced1.insert(f0="Trident", f1="InternetExplorer 5.5", f2="Win 95+", f3="5.5", f4="A")
    db.ttablesXadvanced1.insert(f0="Trident", f1="InternetExplorer 6", f2="Win 98+", f3="6", f4="A")
    db.ttablesXadvanced1.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="7", f4="A")
    db.ttablesXadvanced1.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="6", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="1.7", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="1.9", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="1.7", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="1.7", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="1", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="1.1", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="1.2", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="1.3", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="1.4", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="1.5", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="1.6", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="1.7", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="1.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="125.5", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="312.8", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="419.3", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="522.1", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="420", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="420.1", f4="A")
    db.ttablesXadvanced1.insert(f0="Webkit", f1="S60", f2="S60", f3="413", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="8.5", f4="<sup>1</sup>")
    db.ttablesXadvanced1.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="3.1", f4="C")
    db.ttablesXadvanced1.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="3.3", f4="A")
    db.ttablesXadvanced1.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="3.5", f4="A")
    db.ttablesXadvanced1.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="-", f4="X")
    db.ttablesXadvanced1.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="1", f4="C")
    db.ttablesXadvanced1.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="1", f4="C")
    db.ttablesXadvanced1.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="-", f4="C")
    db.ttablesXadvanced1.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="-", f4="A")
    db.ttablesXadvanced1.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="-", f4="X")
    db.ttablesXadvanced1.insert(f0="Misc", f1="Links", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced1.insert(f0="Misc", f1="Lynx", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced1.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="-", f4="C")
    db.ttablesXadvanced1.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="-", f4="C")
    db.ttablesXadvanced1.insert(f0="Other browsers", f1="All others", f2="-", f3="-", f4="U")
    db.commit()

if not db(db.ttablesXadvanced2).count():
    db.ttablesXadvanced2.insert(f0="Trident", f1="Internet Explorer 4.0", f2="Win 95+", f3="4", f4="X")
    db.ttablesXadvanced2.insert(f0="Trident", f1="Internet Explorer 5.0", f2="Win 95+", f3="5", f4="C")
    db.ttablesXadvanced2.insert(f0="Trident", f1="Internet Explorer 5.5", f2="Win 95+", f3="5.5", f4="A")
    db.ttablesXadvanced2.insert(f0="Trident", f1="Internet Explorer 6", f2="Win 98+", f3="6", f4="A")
    db.ttablesXadvanced2.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="7", f4="A")
    db.ttablesXadvanced2.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="6", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="1.7", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="1.9", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="1.7", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="1.7", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="1", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="1.1", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="1.2", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="1.3", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="1.4", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="1.5", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="1.6", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="1.7", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="1.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="125.5", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="312.8", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="419.3", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="522.1", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="420", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="420.1", f4="A")
    db.ttablesXadvanced2.insert(f0="Webkit", f1="S60", f2="S60", f3="413", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="8.5", f4="<sup>1</sup>")
    db.ttablesXadvanced2.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="3.1", f4="C")
    db.ttablesXadvanced2.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="3.3", f4="A")
    db.ttablesXadvanced2.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="3.5", f4="A")
    db.ttablesXadvanced2.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="-", f4="X")
    db.ttablesXadvanced2.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="1", f4="C")
    db.ttablesXadvanced2.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="1", f4="C")
    db.ttablesXadvanced2.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="-", f4="C")
    db.ttablesXadvanced2.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="-", f4="A")
    db.ttablesXadvanced2.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="-", f4="X")
    db.ttablesXadvanced2.insert(f0="Misc", f1="Links", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced2.insert(f0="Misc", f1="Lynx", f2="Text only", f3="-", f4="X")
    db.ttablesXadvanced2.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="-", f4="C")
    db.ttablesXadvanced2.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="-", f4="C")
    db.ttablesXadvanced2.insert(f0="Other browsers", f1="All others", f2="-", f3="-", f4="U")
    db.commit()

if not db(db.ttablesXresponsive0).count():
    db.ttablesXresponsive0.insert(f0="AAC", f1="AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="$1.38", f3="-0.01", f4="-0.36%", f5="$1.39", f6="$1.39", f7="$1.38", f8="9,395")
    db.ttablesXresponsive0.insert(f0="AAD", f1="ARDENT LEISURE GROUP", f2="$1.15", f3="+0.02", f4="1.32%", f5="$1.14", f6="$1.15", f7="$1.13", f8="56,431")
    db.ttablesXresponsive0.insert(f0="AAX", f1="AUSENCO LIMITED", f2="$4.00", f3="-0.04", f4="-0.99%", f5="$4.01", f6="$4.05", f7="$4.00", f8="90,641")
    db.ttablesXresponsive0.insert(f0="ABC", f1="ADELAIDE BRIGHTON LIMITED", f2="$3.00", f3="+0.06", f4="2.04%", f5="$2.98", f6="$3.00", f7="$2.96", f8="862,518")
    db.ttablesXresponsive0.insert(f0="ABP", f1="ABACUS PROPERTY GROUP", f2="$1.91", f3="0.00", f4="0.00%", f5="$1.92", f6="$1.93", f7="$1.90", f8="595,701")
    db.ttablesXresponsive0.insert(f0="ABY", f1="ADITYA BIRLA MINERALS LIMITED", f2="$0.77", f3="+0.02", f4="2.00%", f5="$0.76", f6="$0.77", f7="$0.76", f8="54,567")
    db.ttablesXresponsive0.insert(f0="ACR", f1="ACRUX LIMITED", f2="$3.71", f3="+0.01", f4="0.14%", f5="$3.70", f6="$3.72", f7="$3.68", f8="191,373")
    db.ttablesXresponsive0.insert(f0="ADU", f1="ADAMUS RESOURCES LIMITED", f2="$0.72", f3="0.00", f4="0.00%", f5="$0.73", f6="$0.74", f7="$0.72", f8="8,602,291")
    db.ttablesXresponsive0.insert(f0="AGG", f1="ANGLOGOLD ASHANTI LIMITED", f2="$7.81", f3="-0.22", f4="-2.74%", f5="$7.82", f6="$7.82", f7="$7.81", f8="148")
    db.ttablesXresponsive0.insert(f0="AGK", f1="AGL ENERGY LIMITED", f2="$13.82", f3="+0.02", f4="0.14%", f5="$13.83", f6="$13.83", f7="$13.67", f8="846,403")
    db.ttablesXresponsive0.insert(f0="AGO", f1="ATLAS IRON LIMITED", f2="$3.17", f3="-0.02", f4="-0.47%", f5="$3.11", f6="$3.22", f7="$3.10", f8="5,416,303")
    db.commit()

if not db(db.ttablesXresponsive1).count():
    db.ttablesXresponsive1.insert(f0="AAC", f1="AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="$1.38", f3="-0.01", f4="-0.36%", f5="$1.39", f6="$1.39", f7="$1.38", f8="9,395")
    db.ttablesXresponsive1.insert(f0="AAD", f1="ARDENT LEISURE GROUP", f2="$1.15", f3="+0.02", f4="1.32%", f5="$1.14", f6="$1.15", f7="$1.13", f8="56,431")
    db.ttablesXresponsive1.insert(f0="AAX", f1="AUSENCO LIMITED", f2="$4.00", f3="-0.04", f4="-0.99%", f5="$4.01", f6="$4.05", f7="$4.00", f8="90,641")
    db.ttablesXresponsive1.insert(f0="ABC", f1="ADELAIDE BRIGHTON LIMITED", f2="$3.00", f3="+0.06", f4="2.04%", f5="$2.98", f6="$3.00", f7="$2.96", f8="862,518")
    db.ttablesXresponsive1.insert(f0="ABP", f1="ABACUS PROPERTY GROUP", f2="$1.91", f3="0.00", f4="0.00%", f5="$1.92", f6="$1.93", f7="$1.90", f8="595,701")
    db.ttablesXresponsive1.insert(f0="ABY", f1="ADITYA BIRLA MINERALS LIMITED", f2="$0.77", f3="+0.02", f4="2.00%", f5="$0.76", f6="$0.77", f7="$0.76", f8="54,567")
    db.ttablesXresponsive1.insert(f0="ACR", f1="ACRUX LIMITED", f2="$3.71", f3="+0.01", f4="0.14%", f5="$3.70", f6="$3.72", f7="$3.68", f8="191,373")
    db.ttablesXresponsive1.insert(f0="ADU", f1="ADAMUS RESOURCES LIMITED", f2="$0.72", f3="0.00", f4="0.00%", f5="$0.73", f6="$0.74", f7="$0.72", f8="8,602,291")
    db.ttablesXresponsive1.insert(f0="AGG", f1="ANGLOGOLD ASHANTI LIMITED", f2="$7.81", f3="-0.22", f4="-2.74%", f5="$7.82", f6="$7.82", f7="$7.81", f8="148")
    db.ttablesXresponsive1.insert(f0="AGK", f1="AGL ENERGY LIMITED", f2="$13.82", f3="+0.02", f4="0.14%", f5="$13.83", f6="$13.83", f7="$13.67", f8="846,403")
    db.ttablesXresponsive1.insert(f0="AGO", f1="ATLAS IRON LIMITED", f2="$3.17", f3="-0.02", f4="-0.47%", f5="$3.11", f6="$3.22", f7="$3.10", f8="5,416,303")
    db.commit()

if not db(db.ttablesXresponsive2).count():
    db.ttablesXresponsive2.insert(f0="AAC", f1="AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="$1.38", f3="-0.01", f4="-0.36%", f5="$1.39", f6="$1.39", f7="$1.38", f8="9,395")
    db.ttablesXresponsive2.insert(f0="AAD", f1="ARDENT LEISURE GROUP", f2="$1.15", f3="+0.02", f4="1.32%", f5="$1.14", f6="$1.15", f7="$1.13", f8="56,431")
    db.ttablesXresponsive2.insert(f0="AAX", f1="AUSENCO LIMITED", f2="$4.00", f3="-0.04", f4="-0.99%", f5="$4.01", f6="$4.05", f7="$4.00", f8="90,641")
    db.ttablesXresponsive2.insert(f0="ABC", f1="ADELAIDE BRIGHTON LIMITED", f2="$3.00", f3="+0.06", f4="2.04%", f5="$2.98", f6="$3.00", f7="$2.96", f8="862,518")
    db.ttablesXresponsive2.insert(f0="ABP", f1="ABACUS PROPERTY GROUP", f2="$1.91", f3="0.00", f4="0.00%", f5="$1.92", f6="$1.93", f7="$1.90", f8="595,701")
    db.ttablesXresponsive2.insert(f0="ABY", f1="ADITYA BIRLA MINERALS LIMITED", f2="$0.77", f3="+0.02", f4="2.00%", f5="$0.76", f6="$0.77", f7="$0.76", f8="54,567")
    db.ttablesXresponsive2.insert(f0="ACR", f1="ACRUX LIMITED", f2="$3.71", f3="+0.01", f4="0.14%", f5="$3.70", f6="$3.72", f7="$3.68", f8="191,373")
    db.ttablesXresponsive2.insert(f0="ADU", f1="ADAMUS RESOURCES LIMITED", f2="$0.72", f3="0.00", f4="0.00%", f5="$0.73", f6="$0.74", f7="$0.72", f8="8,602,291")
    db.ttablesXresponsive2.insert(f0="AGG", f1="ANGLOGOLD ASHANTI LIMITED", f2="$7.81", f3="-0.22", f4="-2.74%", f5="$7.82", f6="$7.82", f7="$7.81", f8="148")
    db.ttablesXresponsive2.insert(f0="AGK", f1="AGL ENERGY LIMITED", f2="$13.82", f3="+0.02", f4="0.14%", f5="$13.83", f6="$13.83", f7="$13.67", f8="846,403")
    db.ttablesXresponsive2.insert(f0="AGO", f1="ATLAS IRON LIMITED", f2="$3.17", f3="-0.02", f4="-0.47%", f5="$3.11", f6="$3.22", f7="$3.10", f8="5,416,303")
    db.commit()

if not db(db.ttablesXeditable0).count():
    db.ttablesXeditable0.insert(f0="Trident", f1="InternetExplorer 4.0", f2="Win 95+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Trident", f1="InternetExplorer 5.0", f2="Win 95+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Trident", f1="InternetExplorer 5.5", f2="Win 95+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Trident", f1="InternetExplorer 6", f2="Win 98+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Webkit", f1="S60", f2="S60", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="Links", f2="Text only", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="Lynx", f2="Text only", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.ttablesXeditable0.insert(f0="Other browsers", f1="All others", f2="-", f3="<a class=\"hidden on-editing save-row\" href=\"#\"><i class=\"fa fa-save\"></i></a> <a class=\"hidden on-editing cancel-row\" href=\"#\"><i class=\"fa fa-times\"></i></a> <a class=\"on-default edit-row\" href=\"#\"><i class=\"fa fa-pencil\"></i></a> <a class=\"on-default remove-row\" href=\"#\"><i class=\"fa fa-trash-o\"></i></a>")
    db.commit()

if not db(db.ttablesXajax0).count():
    db.ttablesXajax0.insert(f0="Rendering engine", f1="Browser", f2="Platform(s)", f3="Engine version", f4="CSS grade")
    db.commit()

if not db(db.tpagesXinvoiceXprint0).count():
    db.tpagesXinvoiceXprint0.insert(f0="123456", f1="Porto HTML5 Template", f2="Multipourpouse Website Template", f3="$14.00", f4="2", f5="$28.00")
    db.tpagesXinvoiceXprint0.insert(f0="654321", f1="Tucson HTML5 Template", f2="Awesome Website Template", f3="$17.00", f4="1", f5="$17.00")
    db.commit()

if not db(db.tpagesXinvoiceXprint1).count():
    db.tpagesXinvoiceXprint1.insert(f0="Shipping", f1="$0.00")
    db.tpagesXinvoiceXprint1.insert(f0="Grand Total", f1="$73.00")
    db.commit()
