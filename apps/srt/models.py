from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.12.2020 09:47:13 UTC+3, src: https://github.com/puikinsh/srtdash-admin-dashboard

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
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex21',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex30',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex3Xhorizontalmenu0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbarchart0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflinechart0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpiechart0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfaccordion0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfalert0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbadge0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbutton0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbuttonXgroup0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcards0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdropdown0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflistXgroup0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmediaXobject0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodal0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagination0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpopovers0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprogressbar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftab0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform0',
    Field('f0','string', length=1024, ),
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
    )
db.commit()

db.define_table(
    'dfform2',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    Field('f5','boolean',  ),
    Field('f6','boolean',  ),
    Field('f7','boolean',  ),
    )
db.commit()

db.define_table(
    'dfform3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfform5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfform6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
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
    'dfform8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','boolean',  ),
    )
db.commit()

db.define_table(
    'dfform9',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform10',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgrid0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffontawesome0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfthemify0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftableXbasic0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftableXlayout0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdatatable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmaps0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinvoice0',
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
    'dflogin20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dflogin30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfregister0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregister20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregister30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfregister40',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfscreenlock0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfscreenlock20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfresetXpass0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpricing0',
    Field('f0','string', length=1024, ),
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
    'tindex1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex21',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXbasic9',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXlayout0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXlayout1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXlayout2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXlayout3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttableXlayout4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
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
    'tinvoice0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Dashcoin", f2="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f3="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f4="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f5="$ 56746,857", f6="<canvas id=\"mvaluechart\"></canvas>")
    db.tindex0.insert(f0="<div class=\"mv-icon\"><img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></div>", f1="LiteCoin", f2="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f3="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f4="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f5="$ 56746,857", f6="<canvas id=\"mvaluechart2\"></canvas>")
    db.tindex0.insert(f0="<div class=\"mv-icon\"><img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></div>", f1="Euthorium", f2="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f3="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f4="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f5="$ 56746,857", f6="<canvas id=\"mvaluechart3\"></canvas>")
    db.tindex0.insert(f0="<div class=\"mv-icon\"><img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></div>", f1="Bitcoindash", f2="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f3="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f4="<img alt=\"icon\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f5="$ 56746,857", f6="<canvas id=\"mvaluechart4\"></canvas>")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="78211", f1="4.00 AM", f2="Pending", f3="$758.90", f4="$05245.090")
    db.tindex1.insert(f0="782782", f1="4.00 AM", f2="Pending", f3="$77878.90", f4="$7778.090")
    db.tindex1.insert(f0="89675978", f1="4.00 AM", f2="Pending", f3="$0768.90", f4="$0945.090")
    db.commit()

if not db(db.tindex2).count():
    db.tindex2.insert(f0="8964978", f1="4.00 AM", f2="Pending", f3="$445.90", f4="$094545.090")
    db.tindex2.insert(f0="89675978", f1="4.00 AM", f2="Pending", f3="$78.90", f4="$074852945.090")
    db.tindex2.insert(f0="78527878", f1="4.00 AM", f2="Pending", f3="$0768.90", f4="$65465.090")
    db.commit()

if not db(db.tindex20).count():
    db.tindex20.insert(f0="Ladis Sunglass", f1="#894750374", f2="<span class=\"pending_dot\">Pending</span>", f3="01976 74 92 00", f4="9241", f5="View Order")
    db.tindex20.insert(f0="Ladis Sunglass", f1="#894750374", f2="<span class=\"shipment_dot\">Shipment</span>", f3="01976 74 92 00", f4="9241", f5="View Order")
    db.tindex20.insert(f0="Ladis Sunglass", f1="#894750374", f2="<span class=\"pending_dot\">Pending</span>", f3="01976 74 92 00", f4="9241", f5="View Order")
    db.tindex20.insert(f0="Ladis Sunglass", f1="#894750374", f2="<span class=\"confirmed _dot\">Confirmed </span>", f3="01976 74 92 00", f4="9241", f5="View Order")
    db.tindex20.insert(f0="Ladis Sunglass", f1="#894750374", f2="<span class=\"pending_dot\">Pending</span>", f3="01976 74 92 00", f4="9241", f5="View Order")
    db.commit()

if not db(db.tindex21).count():
    db.tindex21.insert(f0="Ladis Sunglass", f1="$56", f2="$160", f3="$20")
    db.tindex21.insert(f0="Ladis Sunglass", f1="$26", f2="$500", f3="$20")
    db.tindex21.insert(f0="Ladis Sunglass", f1="$26", f2="$500", f3="$20")
    db.tindex21.insert(f0="Ladis Sunglass", f1="$56", f2="$250", f3="$10")
    db.tindex21.insert(f0="Ladis Sunglass", f1="$56", f2="$125", f3="$50")
    db.commit()

if not db(db.ttableXbasic0).count():
    db.ttableXbasic0.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic0.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic0.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic0.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic1).count():
    db.ttableXbasic1.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic1.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic1.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic1.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic2).count():
    db.ttableXbasic2.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic2.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic2.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic2.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic3).count():
    db.ttableXbasic3.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic3.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic3.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic3.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic4).count():
    db.ttableXbasic4.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic4.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic4.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic4.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic5).count():
    db.ttableXbasic5.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic5.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic5.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic5.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic6).count():
    db.ttableXbasic6.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic6.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic6.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic6.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic7).count():
    db.ttableXbasic7.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic7.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic7.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic7.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic8).count():
    db.ttableXbasic8.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic8.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXbasic9).count():
    db.ttableXbasic9.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXbasic9.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXlayout0).count():
    db.ttableXlayout0.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout0.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout0.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout0.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXlayout1).count():
    db.ttableXlayout1.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout1.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout1.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout1.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXlayout2).count():
    db.ttableXlayout2.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout2.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout2.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout2.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXlayout3).count():
    db.ttableXlayout3.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout3.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout3.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="$120", f4="<i class=\"ti-trash\"></i>")
    db.ttableXlayout3.insert(f0="1", f1="jone", f2="09 / 07 / 2018", f3="$150", f4="<i class=\"ti-trash\"></i>")
    db.commit()

if not db(db.ttableXlayout4).count():
    db.ttableXlayout4.insert(f0="1", f1="Mark", f2="09 / 07 / 2018", f3="<div class=\"progress\" style=\"height: 8px;\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar\" role=\"progressbar\" style=\"width: 50%;\"></div></div>", f4="<span class=\"status-p bg-primary\"> pending </span>", f5="<ul class=\"d-flex justify-content-center\"><li class=\"mr-3\"><a class=\"text-secondary\" href=\"#\"><i class=\"fa fa-edit\"></i></a></li><li><a class=\"text-danger\" href=\"#\"><i class=\"ti-trash\"></i></a></li></ul>")
    db.ttableXlayout4.insert(f0="2", f1="Mark", f2="09 / 07 / 2018", f3="<div class=\"progress\" style=\"height: 8px;\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 80%;\"></div></div>", f4="<span class=\"status-p bg-warning\"> pending </span>", f5="<ul class=\"d-flex justify-content-center\"><li class=\"mr-3\"><a class=\"text-secondary\" href=\"#\"><i class=\"fa fa-edit\"></i></a></li><li><a class=\"text-danger\" href=\"#\"><i class=\"ti-trash\"></i></a></li></ul>")
    db.ttableXlayout4.insert(f0="3", f1="Mark", f2="09 / 07 / 2018", f3="<div class=\"progress\" style=\"height: 8px;\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar bg-success\" role=\"progressbar\" style=\"width: 100%;\"></div></div>", f4="<span class=\"status-p bg-success\"> complate </span>", f5="<ul class=\"d-flex justify-content-center\"><li class=\"mr-3\"><a class=\"text-secondary\" href=\"#\"><i class=\"fa fa-edit\"></i></a></li><li><a class=\"text-danger\" href=\"#\"><i class=\"ti-trash\"></i></a></li></ul>")
    db.ttableXlayout4.insert(f0="4", f1="Mark", f2="09 / 07 / 2018", f3="<div class=\"progress\" style=\"height: 8px;\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 85%;\"></div></div>", f4="<span class=\"status-p bg-warning\"> panding </span>", f5="<ul class=\"d-flex justify-content-center\"><li class=\"mr-3\"><a class=\"text-secondary\" href=\"#\"><i class=\"fa fa-edit\"></i></a></li><li><a class=\"text-danger\" href=\"#\"><i class=\"ti-trash\"></i></a></li></ul>")
    db.commit()

if not db(db.tdatatable0).count():
    db.tdatatable0.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdatatable0.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdatatable0.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdatatable0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable0.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.tdatatable0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable0.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.commit()

if not db(db.tdatatable1).count():
    db.tdatatable1.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdatatable1.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdatatable1.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdatatable1.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable1.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable1.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable1.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.tdatatable1.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable1.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable1.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable1.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.commit()

if not db(db.tdatatable2).count():
    db.tdatatable2.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdatatable2.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdatatable2.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdatatable2.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable2.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable2.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable2.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.tdatatable2.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable2.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable2.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="29", f4="2011/12/12", f5="$106,450")
    db.tdatatable2.insert(f0="Bruno Nash", f1="Software Engineer", f2="Edinburgh", f3="21", f4="2012/03/29", f5="$433,060")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="1", f1="Crazy Toys", f2="1", f3="$20", f4="$40")
    db.tinvoice0.insert(f0="2", f1="Beautiful flowers", f2="2", f3="$50", f4="$100")
    db.tinvoice0.insert(f0="total balance :", f1="$140")
    db.commit()
