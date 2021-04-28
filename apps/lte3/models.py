import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 26.04.2021 15:09:02 UTC+3

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
    db.app_images.insert(f0='dist/img/AdminLTELogo.png', )
    db.app_images.insert(f0='dist/img/user1-128x128.jpg', )
    db.app_images.insert(f0='dist/img/user8-128x128.jpg', )
    db.app_images.insert(f0='dist/img/user3-128x128.jpg', )
    db.app_images.insert(f0='dist/img/user2-160x160.jpg', )
    db.app_images.insert(f0='dist/img/user7-128x128.jpg', )
    db.app_images.insert(f0='dist/img/user5-128x128.jpg', )
    db.app_images.insert(f0='dist/img/user6-128x128.jpg', )
    db.app_images.insert(f0='dist/img/default-150x150.png', )
    db.app_images.insert(f0='dist/img/user4-128x128.jpg', )
    db.app_images.insert(f0='dist/img/photo2.png', )
    db.app_images.insert(f0='dist/img/photo1.png', )
    db.app_images.insert(f0='dist/img/photo3.jpg', )
    db.app_images.insert(f0='dist/img/credit/visa.png', )
    db.app_images.insert(f0='dist/img/credit/mastercard.png', )
    db.app_images.insert(f0='dist/img/credit/american-express.png', )
    db.app_images.insert(f0='dist/img/credit/paypal2.png', )
    db.app_images.insert(f0='dist/img/photo4.jpg', )
    db.app_images.insert(f0='dist/img/prod-1.jpg', )
    db.app_images.insert(f0='dist/img/prod-2.jpg', )
    db.app_images.insert(f0='dist/img/prod-3.jpg', )
    db.app_images.insert(f0='dist/img/prod-4.jpg', )
    db.app_images.insert(f0='dist/img/prod-5.jpg', )
    db.app_images.insert(f0='dist/img/avatar.png', )
    db.app_images.insert(f0='dist/img/avatar2.png', )
    db.app_images.insert(f0='dist/img/avatar3.png', )
    db.app_images.insert(f0='dist/img/avatar4.png', )
    db.app_images.insert(f0='dist/img/avatar5.png', )

db.commit()

db.define_table( 'css_js_files',
    Field('orig_file_path', requires=IS_NOT_EMPTY(),  ),
    Field('found_in_file', default='' ),
    Field('app_name', default='' ),
    )

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
    'dfindex30',
    Field('f0','string', length=1024, ),
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
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets7',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets8',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets9',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfwidgets10',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftopXnav0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftopXnavXsidebar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfboxed0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffixedXsidebar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffixedXsidebarXcustom0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffixedXtopnav0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffixedXfooter0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcollapsedXsidebar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfchartjs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfflot0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinline0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuplot0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgeneral0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dficons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsliders0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodals0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar4',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar5',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnavbar6',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftimeline0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfribbons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfadvanced0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfeditors0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfvalidation0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfvalidation1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfsimple0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsimple1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdata0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfjsgrid0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgallery0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfkanban0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmailbox0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcompose0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfreadXmail0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinvoice0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofileA0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofileA1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprofileA2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfeXcommerce0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprojects0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprojectXadd0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprojectXedit0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprojectXdetail0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontacts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffaq0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcontactXus0',
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
    'dfregisterA0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfrecoverXpassword0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginXv20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfregisterXv20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforgotXpasswordXv20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfrecoverXpasswordXv20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflockscreen0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflegacyXuserXmenu0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflanguageXmenu0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfX5000',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfX5001',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpace0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblank0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfstarter0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfenhanced0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfenhanced1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfiframe0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsimpleXresults0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsimpleXresults1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfenhancedXresults0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfenhancedXresults1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex30',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbuttons0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbuttons1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbuttons2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbuttons3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbuttons4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdata0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdata1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tmailbox0',
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

db.define_table(
    'tinvoice1',
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
    'tprojectXedit0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinvoiceXprint0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinvoiceXprint1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

if not db(db.tindex30).count():
    db.tindex30.insert(f0="<img alt=\"Product 1\" class=\"img-circle img-size-32 mr-2\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="$13 USD", f2="<small class=\"text-success mr-1\"><i class=\"fas fa-arrow-up\"></i> 12% </small>", f3="<a class=\"text-muted\" href=\"#\"><i class=\"fas fa-search\"></i></a>")
    db.tindex30.insert(f0="<img alt=\"Product 1\" class=\"img-circle img-size-32 mr-2\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="$29 USD", f2="<small class=\"text-warning mr-1\"><i class=\"fas fa-arrow-down\"></i> 0.5% </small>", f3="<a class=\"text-muted\" href=\"#\"><i class=\"fas fa-search\"></i></a>")
    db.tindex30.insert(f0="<img alt=\"Product 1\" class=\"img-circle img-size-32 mr-2\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="$1,230 USD", f2="<small class=\"text-danger mr-1\"><i class=\"fas fa-arrow-down\"></i> 3% </small>", f3="<a class=\"text-muted\" href=\"#\"><i class=\"fas fa-search\"></i></a>")
    db.tindex30.insert(f0="<img alt=\"Product 1\" class=\"img-circle img-size-32 mr-2\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"badge bg-danger\">NEW</span>", f1="$199 USD", f2="<small class=\"text-success mr-1\"><i class=\"fas fa-arrow-up\"></i> 63% </small>", f3="<a class=\"text-muted\" href=\"#\"><i class=\"fas fa-search\"></i></a>")
    db.commit()

if not db(db.tindex20).count():
    db.tindex20.insert(f0="<a href=\"#\">OR9842</a>", f1="Call of Duty IV", f2="<span class=\"badge badge-success\">Shipped</span>", f3="<div class=\"sparkbar\" data-color=\"#00a65a\" data-height=\"20\">90,80,90,-70,61,-83,63</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR1848</a>", f1="Samsung Smart TV", f2="<span class=\"badge badge-warning\">Pending</span>", f3="<div class=\"sparkbar\" data-color=\"#f39c12\" data-height=\"20\">90,80,-90,70,61,-83,68</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR7429</a>", f1="iPhone 6 Plus", f2="<span class=\"badge badge-danger\">Delivered</span>", f3="<div class=\"sparkbar\" data-color=\"#f56954\" data-height=\"20\">90,-80,90,70,-61,83,63</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR7429</a>", f1="Samsung Smart TV", f2="<span class=\"badge badge-info\">Processing</span>", f3="<div class=\"sparkbar\" data-color=\"#00c0ef\" data-height=\"20\">90,80,-90,70,-61,83,63</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR1848</a>", f1="Samsung Smart TV", f2="<span class=\"badge badge-warning\">Pending</span>", f3="<div class=\"sparkbar\" data-color=\"#f39c12\" data-height=\"20\">90,80,-90,70,61,-83,68</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR7429</a>", f1="iPhone 6 Plus", f2="<span class=\"badge badge-danger\">Delivered</span>", f3="<div class=\"sparkbar\" data-color=\"#f56954\" data-height=\"20\">90,-80,90,70,-61,83,63</div>")
    db.tindex20.insert(f0="<a href=\"#\">OR9842</a>", f1="Call of Duty IV", f2="<span class=\"badge badge-success\">Shipped</span>", f3="<div class=\"sparkbar\" data-color=\"#00a65a\" data-height=\"20\">90,80,90,-70,61,-83,63</div>")
    db.commit()

if not db(db.tbuttons0).count():
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-default\" type=\"button\">Default</button>", f1="<button class=\"btn btn-block btn-default btn-lg\" type=\"button\">Default</button>", f2="<button class=\"btn btn-block btn-default btn-sm\" type=\"button\">Default</button>", f3="<button class=\"btn btn-block btn-default btn-xs\" type=\"button\">Default</button>", f4="<button class=\"btn btn-block btn-default btn-flat\" type=\"button\">Default</button>", f5="<button class=\"btn btn-block btn-default disabled\" type=\"button\">Default</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-primary\" type=\"button\">Primary</button>", f1="<button class=\"btn btn-block btn-primary btn-lg\" type=\"button\">Primary</button>", f2="<button class=\"btn btn-block btn-primary btn-sm\" type=\"button\">Primary</button>", f3="<button class=\"btn btn-block btn-primary btn-xs\" type=\"button\">Primary</button>", f4="<button class=\"btn btn-block btn-primary btn-flat\" type=\"button\">Primary</button>", f5="<button class=\"btn btn-block btn-primary disabled\" type=\"button\">Primary</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-secondary\" type=\"button\">Secondary</button>", f1="<button class=\"btn btn-block btn-secondary btn-lg\" type=\"button\">Secondary</button>", f2="<button class=\"btn btn-block btn-secondary btn-sm\" type=\"button\">Secondary</button>", f3="<button class=\"btn btn-block btn-secondary btn-xs\" type=\"button\">Secondary</button>", f4="<button class=\"btn btn-block btn-secondary btn-flat\" type=\"button\">Secondary</button>", f5="<button class=\"btn btn-block btn-secondary disabled\" type=\"button\">Secondary</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-success\" type=\"button\">Success</button>", f1="<button class=\"btn btn-block btn-success btn-lg\" type=\"button\">Success</button>", f2="<button class=\"btn btn-block btn-success btn-sm\" type=\"button\">Success</button>", f3="<button class=\"btn btn-block btn-success btn-xs\" type=\"button\">Success</button>", f4="<button class=\"btn btn-block btn-success btn-flat\" type=\"button\">Success</button>", f5="<button class=\"btn btn-block btn-success disabled\" type=\"button\">Success</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-info\" type=\"button\">Info</button>", f1="<button class=\"btn btn-block btn-info btn-lg\" type=\"button\">Info</button>", f2="<button class=\"btn btn-block btn-info btn-sm\" type=\"button\">Info</button>", f3="<button class=\"btn btn-block btn-info btn-xs\" type=\"button\">Info</button>", f4="<button class=\"btn btn-block btn-info btn-flat\" type=\"button\">Info</button>", f5="<button class=\"btn btn-block btn-info disabled\" type=\"button\">Info</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-danger\" type=\"button\">Danger</button>", f1="<button class=\"btn btn-block btn-danger btn-lg\" type=\"button\">Danger</button>", f2="<button class=\"btn btn-block btn-danger btn-sm\" type=\"button\">Danger</button>", f3="<button class=\"btn btn-block btn-danger btn-xs\" type=\"button\">Danger</button>", f4="<button class=\"btn btn-block btn-danger btn-flat\" type=\"button\">Danger</button>", f5="<button class=\"btn btn-block btn-danger disabled\" type=\"button\">Danger</button>")
    db.tbuttons0.insert(f0="<button class=\"btn btn-block btn-warning\" type=\"button\">Warning</button>", f1="<button class=\"btn btn-block btn-warning btn-lg\" type=\"button\">Warning</button>", f2="<button class=\"btn btn-block btn-warning btn-sm\" type=\"button\">Warning</button>", f3="<button class=\"btn btn-block btn-warning btn-xs\" type=\"button\">Warning</button>", f4="<button class=\"btn btn-block btn-warning btn-flat\" type=\"button\">Warning</button>", f5="<button class=\"btn btn-block btn-warning disabled\" type=\"button\">Warning</button>")
    db.commit()

if not db(db.tbuttons1).count():
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-primary\" type=\"button\">Primary</button>", f1="<button class=\"btn btn-block btn-outline-primary btn-lg\" type=\"button\">Primary</button>", f2="<button class=\"btn btn-block btn-outline-primary btn-sm\" type=\"button\">Primary</button>", f3="<button class=\"btn btn-block btn-outline-primary btn-xs\" type=\"button\">Primary</button>", f4="<button class=\"btn btn-block btn-outline-primary btn-flat\" type=\"button\">Primary</button>", f5="<button class=\"btn btn-block btn-outline-primary disabled\" type=\"button\">Primary</button>")
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-secondary\" type=\"button\">Secondary</button>", f1="<button class=\"btn btn-block btn-outline-secondary btn-lg\" type=\"button\">Secondary</button>", f2="<button class=\"btn btn-block btn-outline-secondary btn-sm\" type=\"button\">Secondary</button>", f3="<button class=\"btn btn-block btn-outline-secondary btn-xs\" type=\"button\">Secondary</button>", f4="<button class=\"btn btn-block btn-outline-secondary btn-flat\" type=\"button\">Secondary</button>", f5="<button class=\"btn btn-block btn-outline-secondary disabled\" type=\"button\">Secondary</button>")
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-success\" type=\"button\">Success</button>", f1="<button class=\"btn btn-block btn-outline-success btn-lg\" type=\"button\">Success</button>", f2="<button class=\"btn btn-block btn-outline-success btn-sm\" type=\"button\">Success</button>", f3="<button class=\"btn btn-block btn-outline-success btn-xs\" type=\"button\">Success</button>", f4="<button class=\"btn btn-block btn-outline-success btn-flat\" type=\"button\">Success</button>", f5="<button class=\"btn btn-block btn-outline-success disabled\" type=\"button\">Success</button>")
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-info\" type=\"button\">Info</button>", f1="<button class=\"btn btn-block btn-outline-info btn-lg\" type=\"button\">Info</button>", f2="<button class=\"btn btn-block btn-outline-info btn-sm\" type=\"button\">Info</button>", f3="<button class=\"btn btn-block btn-outline-info btn-xs\" type=\"button\">Info</button>", f4="<button class=\"btn btn-block btn-outline-info btn-flat\" type=\"button\">Info</button>", f5="<button class=\"btn btn-block btn-outline-info disabled\" type=\"button\">Info</button>")
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-danger\" type=\"button\">Danger</button>", f1="<button class=\"btn btn-block btn-outline-danger btn-lg\" type=\"button\">Danger</button>", f2="<button class=\"btn btn-block btn-outline-danger btn-sm\" type=\"button\">Danger</button>", f3="<button class=\"btn btn-block btn-outline-danger btn-xs\" type=\"button\">Danger</button>", f4="<button class=\"btn btn-block btn-outline-danger btn-flat\" type=\"button\">Danger</button>", f5="<button class=\"btn btn-block btn-outline-danger disabled\" type=\"button\">Danger</button>")
    db.tbuttons1.insert(f0="<button class=\"btn btn-block btn-outline-warning\" type=\"button\">Warning</button>", f1="<button class=\"btn btn-block btn-outline-warning btn-lg\" type=\"button\">Warning</button>", f2="<button class=\"btn btn-block btn-outline-warning btn-sm\" type=\"button\">Warning</button>", f3="<button class=\"btn btn-block btn-outline-warning btn-xs\" type=\"button\">Warning</button>", f4="<button class=\"btn btn-block btn-outline-warning btn-flat\" type=\"button\">Warning</button>", f5="<button class=\"btn btn-block btn-outline-warning disabled\" type=\"button\">Warning</button>")
    db.commit()

if not db(db.tbuttons2).count():
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-primary\" type=\"button\">Primary</button>", f1="<button class=\"btn btn-block bg-gradient-primary btn-lg\" type=\"button\">Primary</button>", f2="<button class=\"btn btn-block bg-gradient-primary btn-sm\" type=\"button\">Primary</button>", f3="<button class=\"btn btn-block bg-gradient-primary btn-xs\" type=\"button\">Primary</button>", f4="<button class=\"btn btn-block bg-gradient-primary btn-flat\" type=\"button\">Primary</button>", f5="<button class=\"btn btn-block bg-gradient-primary disabled\" type=\"button\">Primary</button>")
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-secondary\" type=\"button\">Secondary</button>", f1="<button class=\"btn btn-block bg-gradient-secondary btn-lg\" type=\"button\">Secondary</button>", f2="<button class=\"btn btn-block bg-gradient-secondary btn-sm\" type=\"button\">Secondary</button>", f3="<button class=\"btn btn-block bg-gradient-secondary btn-xs\" type=\"button\">Secondary</button>", f4="<button class=\"btn btn-block bg-gradient-secondary btn-flat\" type=\"button\">Secondary</button>", f5="<button class=\"btn btn-block bg-gradient-secondary disabled\" type=\"button\">Secondary</button>")
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-success\" type=\"button\">Success</button>", f1="<button class=\"btn btn-block bg-gradient-success btn-lg\" type=\"button\">Success</button>", f2="<button class=\"btn btn-block bg-gradient-success btn-sm\" type=\"button\">Success</button>", f3="<button class=\"btn btn-block bg-gradient-success btn-xs\" type=\"button\">Success</button>", f4="<button class=\"btn btn-block bg-gradient-success btn-flat\" type=\"button\">Success</button>", f5="<button class=\"btn btn-block bg-gradient-success disabled\" type=\"button\">Success</button>")
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-info\" type=\"button\">Info</button>", f1="<button class=\"btn btn-block bg-gradient-info btn-lg\" type=\"button\">Info</button>", f2="<button class=\"btn btn-block bg-gradient-info btn-sm\" type=\"button\">Info</button>", f3="<button class=\"btn btn-block bg-gradient-info btn-xs\" type=\"button\">Info</button>", f4="<button class=\"btn btn-block bg-gradient-info btn-flat\" type=\"button\">Info</button>", f5="<button class=\"btn btn-block bg-gradient-info disabled\" type=\"button\">Info</button>")
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-danger\" type=\"button\">Danger</button>", f1="<button class=\"btn btn-block bg-gradient-danger btn-lg\" type=\"button\">Danger</button>", f2="<button class=\"btn btn-block bg-gradient-danger btn-sm\" type=\"button\">Danger</button>", f3="<button class=\"btn btn-block bg-gradient-danger btn-xs\" type=\"button\">Danger</button>", f4="<button class=\"btn btn-block bg-gradient-danger btn-flat\" type=\"button\">Danger</button>", f5="<button class=\"btn btn-block bg-gradient-danger disabled\" type=\"button\">Danger</button>")
    db.tbuttons2.insert(f0="<button class=\"btn btn-block bg-gradient-warning\" type=\"button\">Warning</button>", f1="<button class=\"btn btn-block bg-gradient-warning btn-lg\" type=\"button\">Warning</button>", f2="<button class=\"btn btn-block bg-gradient-warning btn-sm\" type=\"button\">Warning</button>", f3="<button class=\"btn btn-block bg-gradient-warning btn-xs\" type=\"button\">Warning</button>", f4="<button class=\"btn btn-block bg-gradient-warning btn-flat\" type=\"button\">Warning</button>", f5="<button class=\"btn btn-block bg-gradient-warning disabled\" type=\"button\">Warning</button>")
    db.commit()

if not db(db.tbuttons3).count():
    db.tbuttons3.insert(f0="<div class=\"btn-group\"><button class=\"btn btn-default\" type=\"button\">Left</button><button class=\"btn btn-default\" type=\"button\">Middle</button><button class=\"btn btn-default\" type=\"button\">Right</button></div>", f1="<div class=\"btn-group\"><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group\"><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group\"><button class=\"btn btn-default\" type=\"button\">1</button><button class=\"btn btn-default\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-default dropdown-toggle dropdown-icon\" data-toggle=\"dropdown\" type=\"button\"></button><div class=\"dropdown-menu\"><a class=\"dropdown-item\" href=\"#\">Dropdown link</a><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></div></div></div>")
    db.tbuttons3.insert(f0="<div class=\"btn-group\"><button class=\"btn btn-info\" type=\"button\">Left</button><button class=\"btn btn-info\" type=\"button\">Middle</button><button class=\"btn btn-info\" type=\"button\">Right</button></div>", f1="<div class=\"btn-group\"><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group\"><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group\"><button class=\"btn btn-info\" type=\"button\">1</button><button class=\"btn btn-info\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-info dropdown-toggle dropdown-icon\" data-toggle=\"dropdown\" type=\"button\"></button><div class=\"dropdown-menu\"><a class=\"dropdown-item\" href=\"#\">Dropdown link</a><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></div></div></div>")
    db.tbuttons3.insert(f0="<div class=\"btn-group\"><button class=\"btn btn-danger\" type=\"button\">Left</button><button class=\"btn btn-danger\" type=\"button\">Middle</button><button class=\"btn btn-danger\" type=\"button\">Right</button></div>", f1="<div class=\"btn-group\"><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group\"><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group\"><button class=\"btn btn-danger\" type=\"button\">1</button><button class=\"btn btn-danger\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-danger dropdown-toggle dropdown-icon\" data-toggle=\"dropdown\" type=\"button\"></button><div class=\"dropdown-menu\"><a class=\"dropdown-item\" href=\"#\">Dropdown link</a><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></div></div></div>")
    db.tbuttons3.insert(f0="<div class=\"btn-group\"><button class=\"btn btn-warning\" type=\"button\">Left</button><button class=\"btn btn-warning\" type=\"button\">Middle</button><button class=\"btn btn-warning\" type=\"button\">Right</button></div>", f1="<div class=\"btn-group\"><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group\"><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group\"><button class=\"btn btn-warning\" type=\"button\">1</button><button class=\"btn btn-warning\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-warning dropdown-toggle dropdown-icon\" data-toggle=\"dropdown\" type=\"button\"></button><div class=\"dropdown-menu\"><a class=\"dropdown-item\" href=\"#\">Dropdown link</a><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></div></div></div>")
    db.tbuttons3.insert(f0="<div class=\"btn-group\"><button class=\"btn btn-success\" type=\"button\">Left</button><button class=\"btn btn-success\" type=\"button\">Middle</button><button class=\"btn btn-success\" type=\"button\">Right</button></div>", f1="<div class=\"btn-group\"><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group\"><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group\"><button class=\"btn btn-success\" type=\"button\">1</button><button class=\"btn btn-success\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-success dropdown-toggle dropdown-icon\" data-toggle=\"dropdown\" type=\"button\"></button><div class=\"dropdown-menu\"><a class=\"dropdown-item\" href=\"#\">Dropdown link</a><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></div></div></div>")
    db.commit()

if not db(db.tbuttons4).count():
    db.tbuttons4.insert(f0="<div class=\"btn-group-vertical\"><button class=\"btn btn-default\" type=\"button\">Top</button><button class=\"btn btn-default\" type=\"button\">Middle</button><button class=\"btn btn-default\" type=\"button\">Bottom</button></div>", f1="<div class=\"btn-group-vertical\"><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-default\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group-vertical\"><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-default btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group-vertical\"><button class=\"btn btn-default\" type=\"button\">1</button><button class=\"btn btn-default\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\" type=\"button\"></button><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li></ul></div></div>")
    db.tbuttons4.insert(f0="<div class=\"btn-group-vertical\"><button class=\"btn btn-info\" type=\"button\">Top</button><button class=\"btn btn-info\" type=\"button\">Middle</button><button class=\"btn btn-info\" type=\"button\">Bottom</button></div>", f1="<div class=\"btn-group-vertical\"><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-info\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group-vertical\"><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-info btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group-vertical\"><button class=\"btn btn-info\" type=\"button\">1</button><button class=\"btn btn-info\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-info dropdown-toggle\" data-toggle=\"dropdown\" type=\"button\"></button><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li></ul></div></div>")
    db.tbuttons4.insert(f0="<div class=\"btn-group-vertical\"><button class=\"btn btn-danger\" type=\"button\">Top</button><button class=\"btn btn-danger\" type=\"button\">Middle</button><button class=\"btn btn-danger\" type=\"button\">Bottom</button></div>", f1="<div class=\"btn-group-vertical\"><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-danger\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group-vertical\"><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-danger btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group-vertical\"><button class=\"btn btn-danger\" type=\"button\">1</button><button class=\"btn btn-danger\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-danger dropdown-toggle\" data-toggle=\"dropdown\" type=\"button\"></button><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li></ul></div></div>")
    db.tbuttons4.insert(f0="<div class=\"btn-group-vertical\"><button class=\"btn btn-warning\" type=\"button\">Top</button><button class=\"btn btn-warning\" type=\"button\">Middle</button><button class=\"btn btn-warning\" type=\"button\">Bottom</button></div>", f1="<div class=\"btn-group-vertical\"><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-warning\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group-vertical\"><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-warning btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group-vertical\"><button class=\"btn btn-warning\" type=\"button\">1</button><button class=\"btn btn-warning\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-warning dropdown-toggle\" data-toggle=\"dropdown\" type=\"button\"></button><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li></ul></div></div>")
    db.tbuttons4.insert(f0="<div class=\"btn-group-vertical\"><button class=\"btn btn-success\" type=\"button\">Top</button><button class=\"btn btn-success\" type=\"button\">Middle</button><button class=\"btn btn-success\" type=\"button\">Bottom</button></div>", f1="<div class=\"btn-group-vertical\"><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-success\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f2="<div class=\"btn-group-vertical\"><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-left\"></i></button><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-center\"></i></button><button class=\"btn btn-success btn-flat\" type=\"button\"><i class=\"fas fa-align-right\"></i></button></div>", f3="<div class=\"btn-group-vertical\"><button class=\"btn btn-success\" type=\"button\">1</button><button class=\"btn btn-success\" type=\"button\">2</button><div class=\"btn-group\"><button class=\"btn btn-success dropdown-toggle\" data-toggle=\"dropdown\" type=\"button\"></button><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li><li><a class=\"dropdown-item\" href=\"#\">Dropdown link</a></li></ul></div></div>")
    db.commit()

if not db(db.tdata0).count():
    db.tdata0.insert(f0="Trident", f1="Internet Explorer 4.0", f2="Win 95+", f3="4", f4="X")
    db.tdata0.insert(f0="Trident", f1="Internet Explorer 5.0", f2="Win 95+", f3="5", f4="C")
    db.tdata0.insert(f0="Trident", f1="Internet Explorer 5.5", f2="Win 95+", f3="5.5", f4="A")
    db.tdata0.insert(f0="Trident", f1="Internet Explorer 6", f2="Win 98+", f3="6", f4="A")
    db.tdata0.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="7", f4="A")
    db.tdata0.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="6", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="1.7", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="1.9", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="1.7", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="1.7", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="1", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="1.1", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="1.2", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="1.3", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="1.4", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="1.5", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="1.6", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="1.7", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata0.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="1.8", f4="A")
    db.tdata0.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="125.5", f4="A")
    db.tdata0.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="312.8", f4="A")
    db.tdata0.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="419.3", f4="A")
    db.tdata0.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="522.1", f4="A")
    db.tdata0.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="420", f4="A")
    db.tdata0.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="420.1", f4="A")
    db.tdata0.insert(f0="Webkit", f1="S60", f2="S60", f3="413", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="-", f4="A")
    db.tdata0.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="8.5", f4="<sup>1</sup>")
    db.tdata0.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="3.1", f4="C")
    db.tdata0.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="3.3", f4="A")
    db.tdata0.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="3.5", f4="A")
    db.tdata0.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="-", f4="X")
    db.tdata0.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="1", f4="C")
    db.tdata0.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="1", f4="C")
    db.tdata0.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="-", f4="C")
    db.tdata0.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="-", f4="A")
    db.tdata0.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="-", f4="X")
    db.tdata0.insert(f0="Misc", f1="Links", f2="Text only", f3="-", f4="X")
    db.tdata0.insert(f0="Misc", f1="Lynx", f2="Text only", f3="-", f4="X")
    db.tdata0.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="-", f4="C")
    db.tdata0.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="-", f4="C")
    db.tdata0.insert(f0="Other browsers", f1="All others", f2="-", f3="-", f4="U")
    db.tdata0.insert(f0="Rendering engine", f1="Browser", f2="Platform(s)", f3="Engine version", f4="CSS grade")
    db.commit()

if not db(db.tdata1).count():
    db.tdata1.insert(f0="Trident", f1="Internet Explorer 4.0", f2="Win 95+", f3="4", f4="X")
    db.tdata1.insert(f0="Trident", f1="Internet Explorer 5.0", f2="Win 95+", f3="5", f4="C")
    db.tdata1.insert(f0="Trident", f1="Internet Explorer 5.5", f2="Win 95+", f3="5.5", f4="A")
    db.tdata1.insert(f0="Trident", f1="Internet Explorer 6", f2="Win 98+", f3="6", f4="A")
    db.tdata1.insert(f0="Trident", f1="Internet Explorer 7", f2="Win XP SP2+", f3="7", f4="A")
    db.tdata1.insert(f0="Trident", f1="AOL browser (AOL desktop)", f2="Win XP", f3="6", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Firefox 1.0", f2="Win 98+ / OSX.2+", f3="1.7", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Firefox 1.5", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Firefox 2.0", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Firefox 3.0", f2="Win 2k+ / OSX.3+", f3="1.9", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Camino 1.0", f2="OSX.2+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Camino 1.5", f2="OSX.3+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Netscape 7.2", f2="Win 95+ / Mac OS 8.6-9.2", f3="1.7", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Netscape Browser 8", f2="Win 98SE+", f3="1.7", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Netscape Navigator 9", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.0", f2="Win 95+ / OSX.1+", f3="1", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.1", f2="Win 95+ / OSX.1+", f3="1.1", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.2", f2="Win 95+ / OSX.1+", f3="1.2", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.3", f2="Win 95+ / OSX.1+", f3="1.3", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.4", f2="Win 95+ / OSX.1+", f3="1.4", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.5", f2="Win 95+ / OSX.1+", f3="1.5", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.6", f2="Win 95+ / OSX.1+", f3="1.6", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.7", f2="Win 98+ / OSX.1+", f3="1.7", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Mozilla 1.8", f2="Win 98+ / OSX.1+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Seamonkey 1.1", f2="Win 98+ / OSX.2+", f3="1.8", f4="A")
    db.tdata1.insert(f0="Gecko", f1="Epiphany 2.20", f2="Gnome", f3="1.8", f4="A")
    db.tdata1.insert(f0="Webkit", f1="Safari 1.2", f2="OSX.3", f3="125.5", f4="A")
    db.tdata1.insert(f0="Webkit", f1="Safari 1.3", f2="OSX.3", f3="312.8", f4="A")
    db.tdata1.insert(f0="Webkit", f1="Safari 2.0", f2="OSX.4+", f3="419.3", f4="A")
    db.tdata1.insert(f0="Webkit", f1="Safari 3.0", f2="OSX.4+", f3="522.1", f4="A")
    db.tdata1.insert(f0="Webkit", f1="OmniWeb 5.5", f2="OSX.4+", f3="420", f4="A")
    db.tdata1.insert(f0="Webkit", f1="iPod Touch / iPhone", f2="iPod", f3="420.1", f4="A")
    db.tdata1.insert(f0="Webkit", f1="S60", f2="S60", f3="413", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 7.0", f2="Win 95+ / OSX.1+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 7.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 8.0", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 8.5", f2="Win 95+ / OSX.2+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 9.0", f2="Win 95+ / OSX.3+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 9.2", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera 9.5", f2="Win 88+ / OSX.3+", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Opera for Wii", f2="Wii", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Nokia N800", f2="N800", f3="-", f4="A")
    db.tdata1.insert(f0="Presto", f1="Nintendo DS browser", f2="Nintendo DS", f3="8.5", f4="<sup>1</sup>")
    db.tdata1.insert(f0="KHTML", f1="Konqureror 3.1", f2="KDE 3.1", f3="3.1", f4="C")
    db.tdata1.insert(f0="KHTML", f1="Konqureror 3.3", f2="KDE 3.3", f3="3.3", f4="A")
    db.tdata1.insert(f0="KHTML", f1="Konqureror 3.5", f2="KDE 3.5", f3="3.5", f4="A")
    db.tdata1.insert(f0="Tasman", f1="Internet Explorer 4.5", f2="Mac OS 8-9", f3="-", f4="X")
    db.tdata1.insert(f0="Tasman", f1="Internet Explorer 5.1", f2="Mac OS 7.6-9", f3="1", f4="C")
    db.tdata1.insert(f0="Tasman", f1="Internet Explorer 5.2", f2="Mac OS 8-X", f3="1", f4="C")
    db.tdata1.insert(f0="Misc", f1="NetFront 3.1", f2="Embedded devices", f3="-", f4="C")
    db.tdata1.insert(f0="Misc", f1="NetFront 3.4", f2="Embedded devices", f3="-", f4="A")
    db.tdata1.insert(f0="Misc", f1="Dillo 0.8", f2="Embedded devices", f3="-", f4="X")
    db.tdata1.insert(f0="Misc", f1="Links", f2="Text only", f3="-", f4="X")
    db.tdata1.insert(f0="Misc", f1="Lynx", f2="Text only", f3="-", f4="X")
    db.tdata1.insert(f0="Misc", f1="IE Mobile", f2="Windows Mobile 6", f3="-", f4="C")
    db.tdata1.insert(f0="Misc", f1="PSP browser", f2="PSP", f3="-", f4="C")
    db.tdata1.insert(f0="Other browsers", f1="All others", f2="-", f3="-", f4="U")
    db.tdata1.insert(f0="Rendering engine", f1="Browser", f2="Platform(s)", f3="Engine version", f4="CSS grade")
    db.commit()

if not db(db.tmailbox0).count():
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check2\" type=\"checkbox\" value=\"\"/><label for=\"check2\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="28 mins ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check3\" type=\"checkbox\" value=\"\"/><label for=\"check3\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="11 hours ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check4\" type=\"checkbox\" value=\"\"/><label for=\"check4\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="==0", f5="15 hours ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check5\" type=\"checkbox\" value=\"\"/><label for=\"check5\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="Yesterday")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check6\" type=\"checkbox\" value=\"\"/><label for=\"check6\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="2 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check7\" type=\"checkbox\" value=\"\"/><label for=\"check7\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="2 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check8\" type=\"checkbox\" value=\"\"/><label for=\"check8\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="==0", f5="2 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check9\" type=\"checkbox\" value=\"\"/><label for=\"check9\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="==0", f5="2 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check10\" type=\"checkbox\" value=\"\"/><label for=\"check10\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="==0", f5="2 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check11\" type=\"checkbox\" value=\"\"/><label for=\"check11\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="4 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check12\" type=\"checkbox\" value=\"\"/><label for=\"check12\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="==0", f5="12 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check13\" type=\"checkbox\" value=\"\"/><label for=\"check13\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star-o text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="12 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check14\" type=\"checkbox\" value=\"\"/><label for=\"check14\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="14 days ago")
    db.tmailbox0.insert(f0="<div class=\"icheck-primary\"><input id=\"check15\" type=\"checkbox\" value=\"\"/><label for=\"check15\"></label></div>", f1="<a href=\"#\"><i class=\"fas fa-star text-warning\"></i></a>", f2="<a href=\"#\">Alexander Pierce</a>", f3="<b>AdminLTE 3.0 Issue</b>", f4="<i class=\"fas fa-paperclip\"></i>", f5="15 days ago")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="1", f1="Call of Duty", f2="455-981-221", f3="El snort testosterone trophy driving gloves handsome", f4="$64.50")
    db.tinvoice0.insert(f0="1", f1="Need for Speed IV", f2="247-925-726", f3="Wes Anderson umami biodiesel", f4="$50.00")
    db.tinvoice0.insert(f0="1", f1="Monsters DVD", f2="735-845-642", f3="Terry Richardson helvetica tousled street art master", f4="$10.70")
    db.tinvoice0.insert(f0="1", f1="Grown Ups Blue Ray", f2="422-568-642", f3="Tousled lomo letterpress", f4="$25.99")
    db.commit()

if not db(db.tinvoice1).count():
    db.tinvoice1.insert(f0="Tax (9.3%)", f1="$10.34")
    db.tinvoice1.insert(f0="Shipping:", f1="$5.80")
    db.tinvoice1.insert(f0="Total:", f1="$265.24")
    db.commit()

if not db(db.tprojects0).count():
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"57\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 57%\"></div></div> <small> 57% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"47\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 47%\"></div></div> <small> 47% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"77\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 77%\"></div></div> <small> 77% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"60\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 60%\"></div></div> <small> 60% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"12\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 12%\"></div></div> <small> 12% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"35\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 35%\"></div></div> <small> 35% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"87\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 87%\"></div></div> <small> 87% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"77\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 77%\"></div></div> <small> 77% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.tprojects0.insert(f0="#", f1="<a> AdminLTE v3 </a> <br/> <small> Created 01.01.2019 </small>", f2="<ul class=\"list-inline\"><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li><li class=\"list-inline-item\"><img alt=\"Avatar\" class=\"table-avatar\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/></li></ul>", f3="<div class=\"progress progress-sm\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"77\" class=\"progress-bar bg-green\" role=\"progressbar\" style=\"width: 77%\"></div></div> <small> 77% Complete </small>", f4="<span class=\"badge badge-success\">Success</span>", f5="<a class=\"btn btn-primary btn-sm\" href=\"#\"><i class=\"fas fa-folder\"></i> View </a> <a class=\"btn btn-info btn-sm\" href=\"#\"><i class=\"fas fa-pencil-alt\"></i> Edit </a> <a class=\"btn btn-danger btn-sm\" href=\"#\"><i class=\"fas fa-trash\"></i> Delete </a>")
    db.commit()

if not db(db.tprojectXedit0).count():
    db.tprojectXedit0.insert(f0="Functional-requirements.docx", f1="49.8005 kb", f2="<div class=\"btn-group btn-group-sm\"><a class=\"btn btn-info\" href=\"#\"><i class=\"fas fa-eye\"></i></a><a class=\"btn btn-danger\" href=\"#\"><i class=\"fas fa-trash\"></i></a></div>")
    db.tprojectXedit0.insert(f0="UAT.pdf", f1="28.4883 kb", f2="<div class=\"btn-group btn-group-sm\"><a class=\"btn btn-info\" href=\"#\"><i class=\"fas fa-eye\"></i></a><a class=\"btn btn-danger\" href=\"#\"><i class=\"fas fa-trash\"></i></a></div>")
    db.tprojectXedit0.insert(f0="Email-from-flatbal.mln", f1="57.9003 kb", f2="<div class=\"btn-group btn-group-sm\"><a class=\"btn btn-info\" href=\"#\"><i class=\"fas fa-eye\"></i></a><a class=\"btn btn-danger\" href=\"#\"><i class=\"fas fa-trash\"></i></a></div>")
    db.tprojectXedit0.insert(f0="Logo.png", f1="50.5190 kb", f2="<div class=\"btn-group btn-group-sm\"><a class=\"btn btn-info\" href=\"#\"><i class=\"fas fa-eye\"></i></a><a class=\"btn btn-danger\" href=\"#\"><i class=\"fas fa-trash\"></i></a></div>")
    db.tprojectXedit0.insert(f0="Contract-10_12_2014.docx", f1="44.9715 kb", f2="<div class=\"btn-group btn-group-sm\"><a class=\"btn btn-info\" href=\"#\"><i class=\"fas fa-eye\"></i></a><a class=\"btn btn-danger\" href=\"#\"><i class=\"fas fa-trash\"></i></a></div>")
    db.commit()

if not db(db.tinvoiceXprint0).count():
    db.tinvoiceXprint0.insert(f0="1", f1="Call of Duty", f2="455-981-221", f3="El snort testosterone trophy driving gloves handsome", f4="$64.50")
    db.tinvoiceXprint0.insert(f0="1", f1="Need for Speed IV", f2="247-925-726", f3="Wes Anderson umami biodiesel", f4="$50.00")
    db.tinvoiceXprint0.insert(f0="1", f1="Monsters DVD", f2="735-845-642", f3="Terry Richardson helvetica tousled street art master", f4="$10.70")
    db.tinvoiceXprint0.insert(f0="1", f1="Grown Ups Blue Ray", f2="422-568-642", f3="Tousled lomo letterpress", f4="$25.99")
    db.commit()

if not db(db.tinvoiceXprint1).count():
    db.tinvoiceXprint1.insert(f0="Tax (9.3%)", f1="$10.34")
    db.tinvoiceXprint1.insert(f0="Shipping:", f1="$5.80")
    db.tinvoiceXprint1.insert(f0="Total:", f1="$265.24")
    db.commit()
