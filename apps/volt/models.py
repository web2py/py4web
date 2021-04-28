import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 26.04.2021 14:45:45 UTC+3, src: https://github.com/themesberg/volt-bootstrap-5-dashboard


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
    db.app_images.insert(f0='assets/img/favicon/apple-touch-icon.png', )
    db.app_images.insert(f0='assets/img/favicon/favicon-32x32.png', )
    db.app_images.insert(f0='assets/img/favicon/favicon-16x16.png', )
    db.app_images.insert(f0='assets/img/favicon/safari-pinned-tab.svg', )
    db.app_images.insert(f0='assets/img/brand/light.svg', )
    db.app_images.insert(f0='assets/img/themesberg.svg', )
    db.app_images.insert(f0='assets/img/mockup-presentation.png', )
    db.app_images.insert(f0='assets/img/illustrations/bs5-illustrations.svg', )
    db.app_images.insert(f0='assets/img/mockup-kanban-presentation.png', )
    db.app_images.insert(f0='assets/img/mockup-map-presentation.png', )
    db.app_images.insert(f0='assets/img/mockup-calendar-presentation.png', )
    db.app_images.insert(f0='assets/img/pages/overview.jpg', )
    db.app_images.insert(f0='assets/img/pages/transactions.jpg', )
    db.app_images.insert(f0='assets/img/pages/settings.jpg', )
    db.app_images.insert(f0='assets/img/pages/sign-in.jpg', )
    db.app_images.insert(f0='assets/img/pages/sign-up.jpg', )
    db.app_images.insert(f0='assets/img/pages/lock.jpg', )
    db.app_images.insert(f0='assets/img/pages/forgot-password.jpg', )
    db.app_images.insert(f0='assets/img/pages/reset-password.jpg', )
    db.app_images.insert(f0='assets/img/pages/404.jpg', )
    db.app_images.insert(f0='assets/img/pages/500.jpg', )
    db.app_images.insert(f0='assets/img/technologies/bootstrap-5-logo.svg', )
    db.app_images.insert(f0='assets/img/technologies/react-logo.svg', )
    db.app_images.insert(f0='assets/img/themesberg-logo-alt.svg', )
    db.app_images.insert(f0='assets/img/brand/dark.svg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-3.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-1.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-2.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-4.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-5.jpg', )
    db.app_images.insert(f0='assets/img/illustrations/signin.svg', )
    db.app_images.insert(f0='assets/img/profile-cover.jpg', )
    db.app_images.insert(f0='assets/img/illustrations/404.svg', )
    db.app_images.insert(f0='assets/img/illustrations/500.svg', )
    db.app_images.insert(f0='assets/img/flags/united-states-of-america.svg', )
    db.app_images.insert(f0='assets/img/flags/canada.svg', )
    db.app_images.insert(f0='assets/img/flags/united-kingdom.svg', )
    db.app_images.insert(f0='assets/img/flags/france.svg', )
    db.app_images.insert(f0='assets/img/flags/japan.svg', )
    db.app_images.insert(f0='assets/img/flags/germany.svg', )

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
    'dfdashboard0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsignXin0',
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
    Field('f3','boolean',  ),
    )
db.commit()

db.define_table(
    'dflock0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftransactions0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsettings0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsettings1',
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

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfresetXpassword0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbootstrapXtables0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbuttons0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfnotifications0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms0',
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
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfmodals2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','boolean',  ),
    )
db.commit()

db.define_table(
    'dftypography0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdashboard0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttransactions0',
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
    'tbootstrapXtables0',
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
    'tbootstrapXtables1',
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
    'tupgradeXtoXpro0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

if not db(db.tdashboard0).count():
    db.tdashboard0.insert(f0="/demo/admin/index.html", f1="3,225", f2="$20", f3="<span class=\"fas fa-arrow-up text-danger me-3\"></span>")
    db.tdashboard0.insert(f0="/demo/admin/forms.html", f1="2,987", f2="0", f3="<span class=\"fas fa-arrow-down text-success me-3\"></span>")
    db.tdashboard0.insert(f0="/demo/admin/util.html", f1="2,844", f2="294", f3="<span class=\"fas fa-arrow-down text-success me-3\"></span>")
    db.tdashboard0.insert(f0="/demo/admin/validation.html", f1="2,050", f2="$147", f3="<span class=\"fas fa-arrow-up text-danger me-3\"></span>")
    db.tdashboard0.insert(f0="/demo/admin/modals.html", f1="1,483", f2="$19", f3="<span class=\"fas fa-arrow-down text-success me-3\"></span>")
    db.commit()

if not db(db.ttransactions0).count():
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 May 2020</span>", f3="<span class=\"fw-normal\">1 Jun 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-warning\">Due</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456423 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Apr 2020</span>", f3="<span class=\"fw-normal\">1 May 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456420 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Mar 2020</span>", f3="<span class=\"fw-normal\">1 Apr 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456421 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Feb 2020</span>", f3="<span class=\"fw-normal\">1 Mar 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456420 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Jan 2020</span>", f3="<span class=\"fw-normal\">1 Feb 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456479 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Dec 2019</span>", f3="<span class=\"fw-normal\">1 Jan 2020</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\">Platinum Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Nov 2019</span>", f3="<span class=\"fw-normal\">1 Dec 2019</span>", f4="<span class=\"fw-bold\">$799,00</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 453673 </a>", f1="<span class=\"fw-normal\">Gold Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Oct 2019</span>", f3="<span class=\"fw-normal\">1 Nov 2019</span>", f4="<span class=\"fw-bold\">$533,42</span>", f5="<span class=\"fw-bold text-danger\">Canceled</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456468 </a>", f1="<span class=\"fw-normal\">Gold Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Sep 2019</span>", f3="<span class=\"fw-normal\">1 Oct 2019</span>", f4="<span class=\"fw-bold\">$533,42</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\">Flexible Subscription Plan</span>", f2="<span class=\"fw-normal\">1 Aug 2019</span>", f3="<span class=\"fw-normal\">1 Sep 2019</span>", f4="<span class=\"fw-bold\">$233,42</span>", f5="<span class=\"fw-bold text-success\">Paid</span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"sr-only\">Toggle Dropdown</span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span>View Details</a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span>Edit</a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span>Remove</a></div></div>")
    db.commit()

if not db(db.tbootstrapXtables0).count():
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\">1</a>", f1="<span class=\"icon icon-xs icon-gray w-30\"><span class=\"fas fa-globe-europe\"></span></span>", f2="Direct", f3="-", f4="--", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\">51%</div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"51\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 51%;\"></div></div></div></div>", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">2.45%</span>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\">2</a>", f1="<span class=\"icon icon-xs icon-info w-30\"><span class=\"fab fa-google\"></span></span>", f2="Search / Organic", f3="-", f4="--", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\">18%</div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"18\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 18%;\"></div></div></div></div>", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">17.67%</span>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\">3</a>", f1="<span class=\"icon icon-xs icon-danger w-30\"><span class=\"fab fa-youtube\"></span></span>", f2="Social", f3="<a class=\"small fw-bold\" href=\"#\">Arts and Entertainment</a>", f4="#2", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\">18%</div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"18\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 18%;\"></div></div></div></div>", f6="-")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\">4</a>", f1="<span class=\"icon icon-xs icon-purple w-30\"><span class=\"fab fa-yahoo\"></span></span>", f2="Referral", f3="<a class=\"small fw-bold\" href=\"#\">News and Media</a>", f4="#11", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\">8%</div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"8\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 8%;\"></div></div></div></div>", f6="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">9.30%</span>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\">5</a>", f1="<span class=\"icon icon-xs icon-info w-30\"><span class=\"fab fa-twitter\"></span></span>", f2="Social", f3="<a class=\"small fw-bold\" href=\"#\">Social Networks</a>", f4="#4", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\">4%</div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"4\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 4%;\"></div></div></div></div>", f6="-")
    db.commit()

if not db(db.tbootstrapXtables1).count():
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">United States</span></div></a>", f1="106", f2="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">5</span>", f3="3", f4="=", f5="32", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">3</span>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">Canada</span></div></a>", f1="76", f2="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">17</span>", f3="4", f4="=", f5="30", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">3</span>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">United Kingdom</span></div></a>", f1="147", f2="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">10</span>", f3="5", f4="=", f5="34", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">7</span>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">France</span></div></a>", f1="112", f2="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">3</span>", f3="5", f4="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">1</span>", f5="34", f6="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">2</span>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">Japan</span></div></a>", f1="115", f2="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">12</span>", f3="6", f4="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">1</span>", f5="37", f6="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">5</span>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\">Germany</span></div></a>", f1="220", f2="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">56</span>", f3="7", f4="<span class=\"fas fa-angle-down\"></span> <span class=\"fw-bold\">3</span>", f5="30", f6="<span class=\"fas fa-angle-up\"></span> <span class=\"fw-bold\">2</span>")
    db.commit()

if not db(db.tupgradeXtoXpro0).count():
    db.tupgradeXtoXpro0.insert(f0="Elements", f1="100 BS5 components", f2="800+ BS5 components")
    db.tupgradeXtoXpro0.insert(f0="Plugins", f1="3 plugins", f2="10 plugins")
    db.tupgradeXtoXpro0.insert(f0="Examples Pages", f1="11 pages", f2="21 pages")
    db.tupgradeXtoXpro0.insert(f0="Toggleable sidebar (icons only)", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="Kanban Drag & Drop Board", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="Kanban Board", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="Full Calendar", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="MapBox", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="SASS Files", f1="<i class=\"fa fa-check text-success\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="Documentation", f1="<i class=\"fa fa-check text-success\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="6 Months Premium Support", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="Free updates", f1="<i class=\"fa fa-times text-danger\"></i>", f2="<i class=\"fa fa-check text-success\"></i>")
    db.tupgradeXtoXpro0.insert(f0="==0", f1="<a class=\"btn btn-dark\" href=\"https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard\" target=\"_blank\"><i class=\"fas fa-download me-2\"></i>Download</a>", f2="<a class=\"btn btn-secondary\" href=\"https://demo.themesberg.com/volt-pro/pages/dashboard/dashboard.html\" target=\"_blank\">Live Demo PRO <span class=\"fas fa-external-link-alt ms-2\"></span></a> <a class=\"btn btn-outline-dark ms-3\" href=\"https://themesberg.com/product/admin-dashboard/volt-premium-bootstrap-5-dashboard\" target=\"_blank\"><span class=\"fas fa-shopping-cart me-2\"></span> Purchase - $69</a>")
    db.commit()
