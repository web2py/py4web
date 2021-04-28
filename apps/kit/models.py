import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 28.04.2021 12:04:48 UTC+3, src: https://github.com/adminkit/adminkit


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
    db.app_images.insert(f0='img/icons/icon-48x48.png', )
    db.app_images.insert(f0='img/avatars/avatar-5.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-2.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-4.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-3.jpg', )
    db.app_images.insert(f0='img/avatars/avatar.jpg', )
    db.app_images.insert(f0='img/photos/unsplash-1.jpg', )
    db.app_images.insert(f0='img/photos/unsplash-2.jpg', )
    db.app_images.insert(f0='img/photos/unsplash-3.jpg', )

db.commit()

db.define_table( 'app_css_js',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    )

db.define_table( 'app_js_script',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    Field('in_html', ),
    )

db.commit()

db.define_table(
    'dfindex0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXprofile0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsettings0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsettings1',
    Field('f0','string', length=1024, ),
    Field('f1','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsettings2',
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
    'dfpagesXsettings3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
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
    'dfpagesXsignXin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfpagesXsignXup0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXalerts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXcards0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXgeneral0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXgrid0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXmodals0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuiXtypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dficonsXfeather0',
    Field('f0','string', length=1024, ),
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
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformsXlayouts3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','boolean',  ),
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
    'dfformsXbasicXinputs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftablesXbootstrap0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfchartsXchartjs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmapsXgoogle0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
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
    'tpagesXinvoice0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttablesXbootstrap6',
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
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="Firefox", f1="3801")
    db.tindex0.insert(f0="IE", f1="1689")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="Project Apollo", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-success\">Done</span>", f4="Vanessa Tucker")
    db.tindex1.insert(f0="Project Fireball", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-danger\">Cancelled</span>", f4="William Harris")
    db.tindex1.insert(f0="Project Hades", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-success\">Done</span>", f4="Sharon Lessman")
    db.tindex1.insert(f0="Project Nitro", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-warning\">In progress</span>", f4="Vanessa Tucker")
    db.tindex1.insert(f0="Project Phoenix", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-success\">Done</span>", f4="William Harris")
    db.tindex1.insert(f0="Project X", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-success\">Done</span>", f4="Sharon Lessman")
    db.tindex1.insert(f0="Project Romeo", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-success\">Done</span>", f4="Christina Mason")
    db.tindex1.insert(f0="Project Wombat", f1="01/01/2020", f2="31/06/2020", f3="<span class=\"badge bg-warning\">In progress</span>", f4="William Harris")
    db.commit()

if not db(db.tpagesXinvoice0).count():
    db.tpagesXinvoice0.insert(f0="AdminKit Demo Theme Customization", f1="2", f2="$150.00")
    db.tpagesXinvoice0.insert(f0="Monthly Subscription", f1="3", f2="$25.00")
    db.tpagesXinvoice0.insert(f0="Additional Service", f1="1", f2="$100.00")
    db.tpagesXinvoice0.insert(f0="==0", f1="Subtotal", f2="$275.00")
    db.tpagesXinvoice0.insert(f0="==0", f1="Shipping", f2="$8.00")
    db.tpagesXinvoice0.insert(f0="==0", f1="Discount", f2="5%")
    db.tpagesXinvoice0.insert(f0="==0", f1="Total", f2="$268.85")
    db.commit()

if not db(db.ttablesXbootstrap0).count():
    db.ttablesXbootstrap0.insert(f0="Vanessa Tucker", f1="864-348-0485", f2="June 21, 1961", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap0.insert(f0="William Harris", f1="914-939-2458", f2="May 15, 1948", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap0.insert(f0="Sharon Lessman", f1="704-993-5435", f2="September 14, 1965", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap0.insert(f0="Christina Mason", f1="765-382-8195", f2="April 2, 1971", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap0.insert(f0="Robin Schneiders", f1="202-672-1407", f2="October 12, 1966", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.commit()

if not db(db.ttablesXbootstrap1).count():
    db.ttablesXbootstrap1.insert(f0="Vanessa Tucker", f1="864-348-0485", f2="June 21, 1961", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap1.insert(f0="William Harris", f1="914-939-2458", f2="May 15, 1948", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap1.insert(f0="Sharon Lessman", f1="704-993-5435", f2="September 14, 1965", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap1.insert(f0="Christina Mason", f1="765-382-8195", f2="April 2, 1971", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap1.insert(f0="Robin Schneiders", f1="202-672-1407", f2="October 12, 1966", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.commit()

if not db(db.ttablesXbootstrap2).count():
    db.ttablesXbootstrap2.insert(f0="Windows", f1="8.232", f2="40%")
    db.ttablesXbootstrap2.insert(f0="Mac OS", f1="3.322", f2="20%")
    db.ttablesXbootstrap2.insert(f0="Linux", f1="4.232", f2="34%")
    db.ttablesXbootstrap2.insert(f0="FreeBSD", f1="1.121", f2="12%")
    db.ttablesXbootstrap2.insert(f0="Chrome OS", f1="1.331", f2="15%")
    db.ttablesXbootstrap2.insert(f0="Android", f1="2.301", f2="20%")
    db.ttablesXbootstrap2.insert(f0="iOS", f1="1.162", f2="14%")
    db.ttablesXbootstrap2.insert(f0="Windows Phone", f1="562", f2="7%")
    db.ttablesXbootstrap2.insert(f0="Other", f1="1.181", f2="14%")
    db.commit()

if not db(db.ttablesXbootstrap3).count():
    db.ttablesXbootstrap3.insert(f0="<img alt=\"Avatar\" class=\"rounded-circle mr-2\" height=\"48\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"48\"/>", f1="864-348-0485", f2="June 21, 1961")
    db.ttablesXbootstrap3.insert(f0="<img alt=\"Avatar\" class=\"rounded-circle mr-2\" height=\"48\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"48\"/>", f1="914-939-2458", f2="May 15, 1948")
    db.ttablesXbootstrap3.insert(f0="<img alt=\"Avatar\" class=\"rounded-circle mr-2\" height=\"48\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"48\"/>", f1="704-993-5435", f2="September 14, 1965")
    db.ttablesXbootstrap3.insert(f0="<img alt=\"Avatar\" class=\"rounded-circle mr-2\" height=\"48\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"48\"/>", f1="765-382-8195", f2="April 2, 1971")
    db.commit()

if not db(db.ttablesXbootstrap4).count():
    db.ttablesXbootstrap4.insert(f0="Vanessa Tucker", f1="864-348-0485", f2="June 21, 1961", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap4.insert(f0="William Harris", f1="914-939-2458", f2="May 15, 1948", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap4.insert(f0="Sharon Lessman", f1="704-993-5435", f2="September 14, 1965", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap4.insert(f0="Christina Mason", f1="765-382-8195", f2="April 2, 1971", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap4.insert(f0="Robin Schneiders", f1="202-672-1407", f2="October 12, 1966", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.commit()

if not db(db.ttablesXbootstrap5).count():
    db.ttablesXbootstrap5.insert(f0="Vanessa Tucker", f1="864-348-0485", f2="June 21, 1961", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap5.insert(f0="William Harris", f1="914-939-2458", f2="May 15, 1948", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap5.insert(f0="Sharon Lessman", f1="704-993-5435", f2="September 14, 1965", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap5.insert(f0="Christina Mason", f1="765-382-8195", f2="April 2, 1971", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.ttablesXbootstrap5.insert(f0="Robin Schneiders", f1="202-672-1407", f2="October 12, 1966", f3="<a href=\"#\"><i class=\"align-middle\" data-feather=\"edit-2\"></i></a> <a href=\"#\"><i class=\"align-middle\" data-feather=\"trash\"></i></a>")
    db.commit()

if not db(db.ttablesXbootstrap6).count():
    db.ttablesXbootstrap6.insert(f0="1", f1="Cell", f2="Cell", f3="Cell", f4="Cell", f5="Cell", f6="Cell", f7="Cell", f8="Cell", f9="Cell")
    db.ttablesXbootstrap6.insert(f0="2", f1="Cell", f2="Cell", f3="Cell", f4="Cell", f5="Cell", f6="Cell", f7="Cell", f8="Cell", f9="Cell")
    db.ttablesXbootstrap6.insert(f0="3", f1="Cell", f2="Cell", f3="Cell", f4="Cell", f5="Cell", f6="Cell", f7="Cell", f8="Cell", f9="Cell")
    db.commit()
