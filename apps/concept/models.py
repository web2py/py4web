import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 28.04.2021 08:47:33 UTC+3, src: https://github.com/puikinsh/concept


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
    db.app_images.insert(f0='assets/images/avatar-2.jpg', )
    db.app_images.insert(f0='assets/images/avatar-3.jpg', )
    db.app_images.insert(f0='assets/images/avatar-4.jpg', )
    db.app_images.insert(f0='assets/images/avatar-5.jpg', )
    db.app_images.insert(f0='assets/images/github.png', )
    db.app_images.insert(f0='assets/images/dribbble.png', )
    db.app_images.insert(f0='assets/images/dropbox.png', )
    db.app_images.insert(f0='assets/images/bitbucket.png', )
    db.app_images.insert(f0='assets/images/mail_chimp.png', )
    db.app_images.insert(f0='assets/images/slack.png', )
    db.app_images.insert(f0='assets/images/avatar-1.jpg', )
    db.app_images.insert(f0='assets/images/product-pic.jpg', )
    db.app_images.insert(f0='assets/images/product-pic-2.jpg', )
    db.app_images.insert(f0='assets/images/product-pic-3.jpg', )
    db.app_images.insert(f0='assets/images/product-pic-4.jpg', )
    db.app_images.insert(f0='assets/images/eco-product-img-1.png', )
    db.app_images.insert(f0='assets/images/eco-product-img-2.png', )
    db.app_images.insert(f0='assets/images/eco-product-img-3.png', )
    db.app_images.insert(f0='assets/images/eco-product-img-4.png', )
    db.app_images.insert(f0='assets/images/eco-slider-img-1.png', )
    db.app_images.insert(f0='assets/images/eco-slider-img-2.png', )
    db.app_images.insert(f0='assets/images/eco-slider-img-3.png', )
    db.app_images.insert(f0='assets/images/card-img-1.jpg', )
    db.app_images.insert(f0='assets/images/card-img.jpg', )
    db.app_images.insert(f0='assets/images/card-img-2.jpg', )
    db.app_images.insert(f0='assets/images/card-img-3.jpg', )
    db.app_images.insert(f0='assets/images/logo.png', )
    db.app_images.insert(f0='assets/images/error-img.png', )
    db.app_images.insert(f0='assets/vendor/timeline/img/cd-icon-picture.svg', )
    db.app_images.insert(f0='assets/vendor/timeline/img/cd-icon-movie.svg', )
    db.app_images.insert(f0='assets/vendor/timeline/img/cd-icon-location.svg', )
    db.app_images.insert(f0='assets/images/loader.svg', )

db.commit()

db.define_table( 'css_js_files',
    Field('orig_file_path', requires=IS_NOT_EMPTY(),  ),
    Field('found_in_file', default='' ),
    Field('app_name', default='' ),
    )

db.commit()

db.define_table(
    'dfecommerceXproductXcheckout0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','boolean',  ),
    Field('f10','boolean',  ),
    Field('f11','string', length=1024, ),
    Field('f12','string', length=1024, ),
    Field('f13','string', length=1024, ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','string', length=1024, ),
    Field('f17','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfecommerceXproductXcheckout1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdashboardXfinance0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinfluencerXfinder0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinfluencerXprofile0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
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
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements4',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXelements5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements7',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfformXelements8',
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
    'dfformXvalidation0',
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
    'dfformXvalidation1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXvalidation2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','boolean',  ),
    )
db.commit()

db.define_table(
    'dfformXvalidation3',
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
    Field('f10','boolean',  ),
    Field('f11','boolean',  ),
    Field('f12','boolean',  ),
    Field('f13','boolean',  ),
    Field('f14','boolean',  ),
    Field('f15','boolean',  ),
    Field('f16','string', length=1024, ),
    Field('f17','string', length=1024, ),
    Field('f18','string', length=1024, ),
    Field('f19','string', length=1024, ),
    Field('f20','string', length=1024, ),
    Field('f21','text', length=1024, ),
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
    'dfsignXup0',
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
    'dfmessageXchat0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmessageXchat1',
    Field('f0','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmessageXchat2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmessageXchat3',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmessageXchat4',
    )
db.commit()

db.define_table(
    'dfmorrisjs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmorrisjs1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfjqueryXmultiXselect0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfjqueryXmultiXselect1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsignXup0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXsignXup1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuserXprofile0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfuserXprofile1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXapp0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfpagesXapp1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
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
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdashboardXsales0',
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
    'tdashboardXinfluencer0',
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
    'tgeneralXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXtable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXtable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXtable3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXtable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tgeneralXtable5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtables1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtables2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtables3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdataXtables4',
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
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tinvoice1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="1", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #1", f3="id000001", f4="20", f5="$80.00", f6="27-08-2018 01:22:12", f7="Patricia J. King", f8="<span class=\"badge-dot badge-brand mr-1\"></span>")
    db.tindex0.insert(f0="2", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #2", f3="id000002", f4="12", f5="$180.00", f6="25-08-2018 21:12:56", f7="Rachel J. Wicker", f8="<span class=\"badge-dot badge-success mr-1\"></span>")
    db.tindex0.insert(f0="3", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #3", f3="id000003", f4="23", f5="$820.00", f6="24-08-2018 14:12:77", f7="Michael K. Ledford", f8="<span class=\"badge-dot badge-success mr-1\"></span>")
    db.tindex0.insert(f0="4", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #4", f3="id000004", f4="34", f5="$340.00", f6="23-08-2018 09:12:35", f7="Michael K. Ledford", f8="<span class=\"badge-dot badge-success mr-1\"></span>")
    db.tindex0.insert(f0="<a class=\"btn btn-outline-light float-right\" href=\"#\"> View Details </a>")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="Campaign#1", f1="98,789", f2="$4563")
    db.tindex1.insert(f0="Campaign#2", f1="2,789", f2="$325")
    db.tindex1.insert(f0="Campaign#3", f1="1,459", f2="$225")
    db.tindex1.insert(f0="Campaign#4", f1="5,035", f2="$856")
    db.tindex1.insert(f0="Campaign#5", f1="10,000", f2="$1000")
    db.tindex1.insert(f0="Campaign#5", f1="10,000", f2="$1000")
    db.tindex1.insert(f0="<a class=\"btn btn-outline-light float-right\" href=\"#\"> Details </a>")
    db.commit()

if not db(db.tdashboardXsales0).count():
    db.tdashboardXsales0.insert(f0="1", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #1", f3="id000001", f4="20", f5="$80.00", f6="27-08-2018 01:22:12", f7="Patricia J. King")
    db.tdashboardXsales0.insert(f0="2", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #2", f3="id000002", f4="12", f5="$180.00", f6="25-08-2018 21:12:56", f7="Rachel J. Wicker")
    db.tdashboardXsales0.insert(f0="3", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #3", f3="id000003", f4="23", f5="$820.00", f6="24-08-2018 14:12:77", f7="Michael K. Ledford")
    db.tdashboardXsales0.insert(f0="4", f1="<div class=\"m-r-10\"><img alt=\"user\" class=\"rounded\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"45\"/></div>", f2="Product #4", f3="id000004", f4="34", f5="$340.00", f6="23-08-2018 09:12:35", f7="Michael K. Ledford")
    db.tdashboardXsales0.insert(f0="<a class=\"btn btn-outline-light float-right\" href=\"#\"> View Details </a>")
    db.commit()

if not db(db.tdashboardXinfluencer0).count():
    db.tdashboardXinfluencer0.insert(f0="<div class=\"m-r-10\"><img alt=\"user\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"35\"/></div>", f1="Fashion E Commerce", f2="<div class=\"avatar-group\"><span><a href=\"#\"><i class=\"fab fa-fw fa-facebook-square facebook-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-twitter-square twitter-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-instagram instagram-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-pinterest-square pinterest-color\"></i></a></span></div>", f3="1,00,000 / 1,50,000", f4="70%", f5="7 Aug,2018", f6="<div class=\"dropdown float-right\"><a aria-expanded=\"true\" class=\"dropdown-toggle card-drop\" data-toggle=\"dropdown\" href=\"#\"><i class=\"mdi mdi-dots-vertical\"></i></a><div class=\"dropdown-menu dropdown-menu-right\"><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Sales Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Export Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Profit </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Action </a></div></div>")
    db.tdashboardXinfluencer0.insert(f0="<div class=\"m-r-10\"><img alt=\"user\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"35\"/></div>", f1="Fitness Products", f2="<div class=\"avatar-group\"><span><a href=\"#\"><i class=\"fab fa-fw fa-facebook-square facebook-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-twitter-square twitter-color\"></i></a></span></div>", f3="2,50,000 / 3,50,000", f4="70%", f5="10 Aug,2018", f6="<div class=\"dropdown float-right\"><a aria-expanded=\"true\" class=\"dropdown-toggle card-drop\" data-toggle=\"dropdown\" href=\"#\"><i class=\"mdi mdi-dots-vertical\"></i></a><div class=\"dropdown-menu dropdown-menu-right\"><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Sales Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Export Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Profit </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Action </a></div></div>")
    db.tdashboardXinfluencer0.insert(f0="<div class=\"m-r-10\"><img alt=\"user\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"35\"/></div>", f1="Gym Trainer Program", f2="<div class=\"avatar-group\"><span><a href=\"#\"><i class=\"fab fa-fw fa-facebook-square facebook-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-pinterest-square pinterest-color\"></i></a></span></div>", f3="3,50,000 / 4,50,000", f4="70%", f5="22 Aug,2018", f6="<div class=\"dropdown float-right\"><a aria-expanded=\"true\" class=\"dropdown-toggle card-drop\" data-toggle=\"dropdown\" href=\"#\"><i class=\"mdi mdi-dots-vertical\"></i></a><div class=\"dropdown-menu dropdown-menu-right\"><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Sales Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Export Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Profit </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Action </a></div></div>")
    db.tdashboardXinfluencer0.insert(f0="<div class=\"m-r-10\"><img alt=\"user\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"30\"/></div>", f1="2018 Top Product", f2="<div class=\"avatar-group\"><span><a href=\"#\"><i class=\"fab fa-fw fa-pinterest-square pinterest-color\"></i></a></span></div>", f3="4,50,000 / 5,50,000", f4="70%", f5="25 Aug,2018", f6="<div class=\"dropdown float-right\"><a aria-expanded=\"true\" class=\"dropdown-toggle card-drop\" data-toggle=\"dropdown\" href=\"#\"><i class=\"mdi mdi-dots-vertical\"></i></a><div class=\"dropdown-menu dropdown-menu-right\"><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Sales Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Export Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Profit </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Action </a></div></div>")
    db.tdashboardXinfluencer0.insert(f0="<div class=\"m-r-10\"><img alt=\"user\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\" width=\"30\"/></div>", f1="Top Dashboard Sale 2018", f2="<div class=\"avatar-group\"><span><a href=\"#\"><i class=\"fab fa-fw fa-facebook-square facebook-color\"></i></a></span><span><a href=\"#\"><i class=\"fab fa-fw fa-pinterest-square pinterest-color\"></i></a></span></div>", f3="5,50,000 / 6,50,000", f4="70%", f5="27 Aug,2018", f6="<div class=\"dropdown float-right\"><a aria-expanded=\"true\" class=\"dropdown-toggle card-drop\" data-toggle=\"dropdown\" href=\"#\"><i class=\"mdi mdi-dots-vertical\"></i></a><div class=\"dropdown-menu dropdown-menu-right\"><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Sales Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Export Report </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Profit </a><!-- item--><a class=\"dropdown-item\" href=\"javascript:void(0);\"> Action </a></div></div>")
    db.commit()

if not db(db.tgeneralXtable0).count():
    db.tgeneralXtable0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tgeneralXtable1).count():
    db.tgeneralXtable1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tgeneralXtable2).count():
    db.tgeneralXtable2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable2.insert(f0="3", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tgeneralXtable3).count():
    db.tgeneralXtable3.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable3.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable3.insert(f0="3", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tgeneralXtable4).count():
    db.tgeneralXtable4.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable4.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable4.insert(f0="3", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tgeneralXtable5).count():
    db.tgeneralXtable5.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tgeneralXtable5.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tgeneralXtable5.insert(f0="3", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tdataXtables0).count():
    db.tdataXtables0.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtables0.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtables0.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtables0.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtables0.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtables0.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtables0.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtables0.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtables0.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtables0.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtables0.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtables0.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtables0.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtables0.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtables0.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtables0.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtables0.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtables0.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtables0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtables0.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtables0.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtables0.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtables0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtables0.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtables0.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtables0.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtables0.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtables0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtables0.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtables0.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtables0.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtables0.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtables0.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtables0.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtables0.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtables0.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtables0.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtables0.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtables0.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtables0.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtables0.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtables0.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtables0.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtables0.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtables0.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtables0.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtables0.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtables0.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtables0.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtables0.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtables0.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtables0.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtables0.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtables0.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtables0.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtables0.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtables0.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtables0.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tdataXtables1).count():
    db.tdataXtables1.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtables1.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtables1.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtables1.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtables1.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtables1.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtables1.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtables1.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtables1.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtables1.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtables1.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtables1.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtables1.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtables1.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtables1.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtables1.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtables1.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtables1.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtables1.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtables1.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtables1.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtables1.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtables1.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtables1.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtables1.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtables1.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtables1.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtables1.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtables1.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtables1.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtables1.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtables1.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtables1.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtables1.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtables1.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtables1.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtables1.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtables1.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtables1.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtables1.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtables1.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtables1.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtables1.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtables1.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtables1.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtables1.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtables1.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtables1.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtables1.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtables1.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtables1.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtables1.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtables1.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtables1.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtables1.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtables1.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtables1.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtables1.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tdataXtables2).count():
    db.tdataXtables2.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtables2.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtables2.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtables2.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtables2.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtables2.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtables2.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtables2.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtables2.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtables2.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtables2.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtables2.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtables2.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtables2.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtables2.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtables2.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtables2.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtables2.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtables2.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtables2.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtables2.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtables2.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtables2.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtables2.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtables2.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtables2.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtables2.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtables2.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtables2.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtables2.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtables2.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtables2.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtables2.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtables2.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtables2.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtables2.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtables2.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtables2.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtables2.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtables2.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtables2.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtables2.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtables2.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtables2.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtables2.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtables2.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtables2.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtables2.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtables2.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtables2.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtables2.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtables2.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtables2.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtables2.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtables2.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtables2.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtables2.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtables2.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tdataXtables3).count():
    db.tdataXtables3.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtables3.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtables3.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtables3.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtables3.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtables3.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtables3.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtables3.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtables3.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtables3.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtables3.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtables3.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtables3.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtables3.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtables3.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtables3.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtables3.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtables3.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtables3.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtables3.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtables3.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtables3.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtables3.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtables3.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtables3.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtables3.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtables3.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtables3.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtables3.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtables3.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtables3.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtables3.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtables3.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtables3.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtables3.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtables3.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtables3.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtables3.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtables3.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtables3.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtables3.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtables3.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtables3.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtables3.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtables3.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtables3.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtables3.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtables3.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtables3.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtables3.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtables3.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtables3.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtables3.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtables3.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtables3.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtables3.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtables3.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtables3.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tdataXtables4).count():
    db.tdataXtables4.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdataXtables4.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdataXtables4.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdataXtables4.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdataXtables4.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdataXtables4.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdataXtables4.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdataXtables4.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdataXtables4.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdataXtables4.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdataXtables4.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdataXtables4.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdataXtables4.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdataXtables4.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdataXtables4.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdataXtables4.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdataXtables4.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdataXtables4.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdataXtables4.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdataXtables4.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdataXtables4.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdataXtables4.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdataXtables4.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdataXtables4.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdataXtables4.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdataXtables4.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdataXtables4.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdataXtables4.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdataXtables4.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdataXtables4.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdataXtables4.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdataXtables4.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdataXtables4.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdataXtables4.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdataXtables4.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdataXtables4.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdataXtables4.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdataXtables4.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdataXtables4.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdataXtables4.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdataXtables4.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdataXtables4.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdataXtables4.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdataXtables4.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdataXtables4.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdataXtables4.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdataXtables4.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdataXtables4.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdataXtables4.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdataXtables4.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdataXtables4.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdataXtables4.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdataXtables4.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdataXtables4.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdataXtables4.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdataXtables4.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdataXtables4.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.tdataXtables4.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="1", f1="Origin License", f2="Extended License", f3="$1500,00", f4="1", f5="$1500,00")
    db.tinvoice0.insert(f0="2", f1="Custom Services", f2="Instalation and Customization (cost per hour)", f3="$110,00", f4="20", f5="$22.000,00")
    db.tinvoice0.insert(f0="3", f1="Hosting", f2="1 year subcription", f3="$309,00", f4="1", f5="$309,00")
    db.tinvoice0.insert(f0="4", f1="Platinum Support", f2="1 year subcription 24/7", f3="$5.000,00", f4="1", f5="$5.000,00")
    db.commit()

if not db(db.tinvoice1).count():
    db.tinvoice1.insert(f0="<strong class=\"text-dark\"> Discount (20%) </strong>", f1="$5,761,00")
    db.tinvoice1.insert(f0="<strong class=\"text-dark\"> VAT (10%) </strong>", f1="$2,304,00")
    db.tinvoice1.insert(f0="<strong class=\"text-dark\"> Total </strong>", f1="<strong class=\"text-dark\"> $20,744,00 </strong>")
    db.commit()
