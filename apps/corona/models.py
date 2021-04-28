import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 26.04.2021 17:49:16 UTC+3, src: https://github.com/BootstrapDash/corona-free-dark-bootstrap-admin-template

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
    db.app_images.insert(f0='assets/images/favicon.png', )
    db.app_images.insert(f0='assets/images/logo.svg', )
    db.app_images.insert(f0='assets/images/logo-mini.svg', )
    db.app_images.insert(f0='assets/images/faces/face15.jpg', )
    db.app_images.insert(f0='assets/images/faces/face4.jpg', )
    db.app_images.insert(f0='assets/images/faces/face2.jpg', )
    db.app_images.insert(f0='assets/images/faces/face3.jpg', )
    db.app_images.insert(f0='assets/images/dashboard/Group126@2x.png', )
    db.app_images.insert(f0='assets/images/faces/face1.jpg', )
    db.app_images.insert(f0='assets/images/faces/face5.jpg', )
    db.app_images.insert(f0='assets/images/faces/face6.jpg', )
    db.app_images.insert(f0='assets/images/faces/face8.jpg', )
    db.app_images.insert(f0='assets/images/faces/face9.jpg', )
    db.app_images.insert(f0='assets/images/faces/face11.jpg', )
    db.app_images.insert(f0='assets/images/dashboard/Rectangle.jpg', )
    db.app_images.insert(f0='assets/images/dashboard/Img_5.jpg', )
    db.app_images.insert(f0='assets/images/dashboard/img_6.jpg', )
    db.app_images.insert(f0='assets/images/faces/face12.jpg', )
    db.app_images.insert(f0='assets/images/faces-clipart/pic-1.png', )
    db.app_images.insert(f0='assets/images/faces-clipart/pic-2.png', )
    db.app_images.insert(f0='assets/images/faces-clipart/pic-3.png', )
    db.app_images.insert(f0='assets/images/faces-clipart/pic-4.png', )

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
    'dfbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfdropdowns0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXelements0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXelements1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','boolean',  ),
    )
db.commit()

db.define_table(
    'dfbasicXelements2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','boolean',  ),
    )
db.commit()

db.define_table(
    'dfbasicXelements3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXelements4',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXelements5',
    Field('f0','boolean',  ),
    Field('f1','boolean',  ),
    Field('f2','boolean',  ),
    Field('f3','boolean',  ),
    Field('f4','boolean',  ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbasicXelements6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfbasicXelements7',
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
    )
db.commit()

db.define_table(
    'dfbasicXtable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfchartjs0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmdi0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfblankXpage0',
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
    Field('f3','boolean',  ),
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
    )
db.commit()

db.define_table(
    'tindex1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
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
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="<div class=\"form-check form-check-muted m-0\"><label class=\"form-check-label\"><input class=\"form-check-input\" type=\"checkbox\"/></label></div>", f1="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"pl-2\">Henry Klein</span>", f2="02312", f3="$14,500", f4="Dashboard", f5="Credit card", f6="04 Dec 2019", f7="<div class=\"badge badge-outline-success\">Approved</div>")
    db.tindex0.insert(f0="<div class=\"form-check form-check-muted m-0\"><label class=\"form-check-label\"><input class=\"form-check-input\" type=\"checkbox\"/></label></div>", f1="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"pl-2\">Estella Bryan</span>", f2="02312", f3="$14,500", f4="Website", f5="Cash on delivered", f6="04 Dec 2019", f7="<div class=\"badge badge-outline-warning\">Pending</div>")
    db.tindex0.insert(f0="<div class=\"form-check form-check-muted m-0\"><label class=\"form-check-label\"><input class=\"form-check-input\" type=\"checkbox\"/></label></div>", f1="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"pl-2\">Lucy Abbott</span>", f2="02312", f3="$14,500", f4="App design", f5="Credit card", f6="04 Dec 2019", f7="<div class=\"badge badge-outline-danger\">Rejected</div>")
    db.tindex0.insert(f0="<div class=\"form-check form-check-muted m-0\"><label class=\"form-check-label\"><input class=\"form-check-input\" type=\"checkbox\"/></label></div>", f1="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"pl-2\">Peter Gill</span>", f2="02312", f3="$14,500", f4="Development", f5="Online Payment", f6="04 Dec 2019", f7="<div class=\"badge badge-outline-success\">Approved</div>")
    db.tindex0.insert(f0="<div class=\"form-check form-check-muted m-0\"><label class=\"form-check-label\"><input class=\"form-check-input\" type=\"checkbox\"/></label></div>", f1="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/> <span class=\"pl-2\">Sallie Reyes</span>", f2="02312", f3="$14,500", f4="Website", f5="Credit card", f6="04 Dec 2019", f7="<div class=\"badge badge-outline-success\">Approved</div>")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="<i class=\"flag-icon flag-icon-de\"></i>", f1="Germany", f2="800", f3="33.25%")
    db.tindex1.insert(f0="<i class=\"flag-icon flag-icon-au\"></i>", f1="Australia", f2="760", f3="15.45%")
    db.tindex1.insert(f0="<i class=\"flag-icon flag-icon-gb\"></i>", f1="United Kingdom", f2="450", f3="25.00%")
    db.tindex1.insert(f0="<i class=\"flag-icon flag-icon-ro\"></i>", f1="Romania", f2="620", f3="10.25%")
    db.tindex1.insert(f0="<i class=\"flag-icon flag-icon-br\"></i>", f1="Brasil", f2="230", f3="75.00%")
    db.commit()

if not db(db.tbasicXtable0).count():
    db.tbasicXtable0.insert(f0="Jacob", f1="53275531", f2="12 May 2017", f3="<label class=\"badge badge-danger\">Pending</label>")
    db.tbasicXtable0.insert(f0="Messsy", f1="53275532", f2="15 May 2017", f3="<label class=\"badge badge-warning\">In progress</label>")
    db.tbasicXtable0.insert(f0="John", f1="53275533", f2="14 May 2017", f3="<label class=\"badge badge-info\">Fixed</label>")
    db.tbasicXtable0.insert(f0="Peter", f1="53275534", f2="16 May 2017", f3="<label class=\"badge badge-success\">Completed</label>")
    db.tbasicXtable0.insert(f0="Dave", f1="53275535", f2="20 May 2017", f3="<label class=\"badge badge-warning\">In progress</label>")
    db.commit()

if not db(db.tbasicXtable1).count():
    db.tbasicXtable1.insert(f0="Jacob", f1="Photoshop", f2="<i class=\"mdi mdi-arrow-down\"></i>", f3="<label class=\"badge badge-danger\">Pending</label>")
    db.tbasicXtable1.insert(f0="Messsy", f1="Flash", f2="<i class=\"mdi mdi-arrow-down\"></i>", f3="<label class=\"badge badge-warning\">In progress</label>")
    db.tbasicXtable1.insert(f0="John", f1="Premier", f2="<i class=\"mdi mdi-arrow-down\"></i>", f3="<label class=\"badge badge-info\">Fixed</label>")
    db.tbasicXtable1.insert(f0="Peter", f1="After effects", f2="<i class=\"mdi mdi-arrow-up\"></i>", f3="<label class=\"badge badge-success\">Completed</label>")
    db.tbasicXtable1.insert(f0="Dave", f1="53275535", f2="<i class=\"mdi mdi-arrow-up\"></i>", f3="<label class=\"badge badge-warning\">In progress</label>")
    db.commit()

if not db(db.tbasicXtable2).count():
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Herman Beck", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar bg-success\" role=\"progressbar\" style=\"width: 25%\"></div></div>", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Messsy Adam", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"75\" class=\"progress-bar bg-danger\" role=\"progressbar\" style=\"width: 75%\"></div></div>", f3="$245.30", f4="July 1, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="John Richards", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"90\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 90%\"></div></div>", f3="$138.00", f4="Apr 12, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Peter Meggik", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"50\" class=\"progress-bar bg-primary\" role=\"progressbar\" style=\"width: 50%\"></div></div>", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Edward", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"35\" class=\"progress-bar bg-danger\" role=\"progressbar\" style=\"width: 35%\"></div></div>", f3="$ 160.25", f4="May 03, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="John Doe", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"65\" class=\"progress-bar bg-info\" role=\"progressbar\" style=\"width: 65%\"></div></div>", f3="$ 123.21", f4="April 05, 2015")
    db.tbasicXtable2.insert(f0="<img alt=\"image\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/>", f1="Henry Tom", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"20\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 20%\"></div></div>", f3="$ 150.00", f4="June 16, 2015")
    db.commit()

if not db(db.tbasicXtable3).count():
    db.tbasicXtable3.insert(f0="1", f1="Herman Beck", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"25\" class=\"progress-bar bg-success\" role=\"progressbar\" style=\"width: 25%\"></div></div>", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable3.insert(f0="2", f1="Messsy Adam", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"75\" class=\"progress-bar bg-danger\" role=\"progressbar\" style=\"width: 75%\"></div></div>", f3="$245.30", f4="July 1, 2015")
    db.tbasicXtable3.insert(f0="3", f1="John Richards", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"90\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 90%\"></div></div>", f3="$138.00", f4="Apr 12, 2015")
    db.tbasicXtable3.insert(f0="4", f1="Peter Meggik", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"50\" class=\"progress-bar bg-primary\" role=\"progressbar\" style=\"width: 50%\"></div></div>", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable3.insert(f0="5", f1="Edward", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"35\" class=\"progress-bar bg-danger\" role=\"progressbar\" style=\"width: 35%\"></div></div>", f3="$ 160.25", f4="May 03, 2015")
    db.tbasicXtable3.insert(f0="6", f1="John Doe", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"65\" class=\"progress-bar bg-info\" role=\"progressbar\" style=\"width: 65%\"></div></div>", f3="$ 123.21", f4="April 05, 2015")
    db.tbasicXtable3.insert(f0="7", f1="Henry Tom", f2="<div class=\"progress\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"20\" class=\"progress-bar bg-warning\" role=\"progressbar\" style=\"width: 20%\"></div></div>", f3="$ 150.00", f4="June 16, 2015")
    db.commit()

if not db(db.tbasicXtable4).count():
    db.tbasicXtable4.insert(f0="1", f1="Herman Beck", f2="$ 77.99", f3="May 15, 2015")
    db.tbasicXtable4.insert(f0="2", f1="Messsy Adam", f2="$245.30", f3="July 1, 2015")
    db.tbasicXtable4.insert(f0="3", f1="John Richards", f2="$138.00", f3="Apr 12, 2015")
    db.tbasicXtable4.insert(f0="4", f1="Peter Meggik", f2="$ 77.99", f3="May 15, 2015")
    db.tbasicXtable4.insert(f0="5", f1="Edward", f2="$ 160.25", f3="May 03, 2015")
    db.tbasicXtable4.insert(f0="6", f1="John Doe", f2="$ 123.21", f3="April 05, 2015")
    db.tbasicXtable4.insert(f0="7", f1="Henry Tom", f2="$ 150.00", f3="June 16, 2015")
    db.commit()

if not db(db.tbasicXtable5).count():
    db.tbasicXtable5.insert(f0="1", f1="Herman Beck", f2="Photoshop", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable5.insert(f0="2", f1="Messsy Adam", f2="Flash", f3="$245.30", f4="July 1, 2015")
    db.tbasicXtable5.insert(f0="3", f1="John Richards", f2="Premeire", f3="$138.00", f4="Apr 12, 2015")
    db.tbasicXtable5.insert(f0="4", f1="Peter Meggik", f2="After effects", f3="$ 77.99", f4="May 15, 2015")
    db.tbasicXtable5.insert(f0="5", f1="Edward", f2="Illustrator", f3="$ 160.25", f4="May 03, 2015")
    db.commit()
