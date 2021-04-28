#
# py4web app, AI-biorex ported 25.11.2020 16:43:07 msk, src: https://github.com/ColorlibHQ/gentelella
# py4web apps https://github.com/ali96343/facep4w
# 

import os, json
import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore

from yatl.helpers import INPUT, H1, HTML, BODY, A
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

def prn_form_vars(myform, mydb,):

        id_db = None; row_db = None; f0_fld = None; inserted = False

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

        f0_fld = myform.vars.get('f0', None )
        if (not f0_fld is None) and len(f0_fld):
            id_db = mydb.insert(**mydb._filter_fields(myform.vars))
            db.commit()

            if not id_db is None:
                row_db = mydb(id_db )

                if not row_db is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{myform.vars.f0}\" into {mydb.f0}, id = {id_db}' )
                         print(f"     select  : \"{row_db.f0}\" from {mydb.f0}, id = {id_db}" )
                         print ()
                    inserted =True
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
                print()

        return inserted
            
def put_json_messages(mess='mymess'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}'})
    

@action('form', method=["GET", "POST"] )
@action.uses(Template('form.html', delimiters='[%[ ]]',), db, session, T,)

def form():
    ctrl_info= "ctrl: form, view: form.html"
    page_url = "\'" + URL('form' ) + "\'"
    messages = []

    fform0= Form(db.dfform0, dbio=False, formstyle=FormStyleBulma)

    if fform0.accepted:
        prn_form_vars( fform0, db.dfform0 )
        return put_json_messages('accepted: ' + str( fform0.form_name ))
    elif fform0.errors:
        print("fform0 has errors: %s" % (fform0.errors))
        return put_json_messages('error: ' + str( fform0.form_name ))
 

    fform1= Form(db.dfform1, dbio=False, formstyle=FormStyleBulma)

    if fform1.accepted:
        prn_form_vars( fform1, db.dfform1 )
        return put_json_messages('accepted: ' + str( fform1.form_name ))
    elif fform1.errors:
        print("fform1 has errors: %s" % (fform1.errors))
        return put_json_messages('error: ' + str( fform1.form_name ))
 

    fform2= Form(db.dfform2, dbio=False, formstyle=FormStyleBulma)

    if fform2.accepted:
        prn_form_vars( fform2, db.dfform2 )
        return put_json_messages('accepted: ' + str( fform2.form_name ))
    elif fform2.errors:
        print("fform2 has errors: %s" % (fform2.errors))
        return put_json_messages('error: ' + str( fform2.form_name ))
 

    fform3= Form(db.dfform3, dbio=False, formstyle=FormStyleBulma)

    if fform3.accepted:
        prn_form_vars( fform3, db.dfform3 )
        return put_json_messages('accepted: ' + str( fform3.form_name ))
    elif fform3.errors:
        print("fform3 has errors: %s" % (fform3.errors))
        return put_json_messages('error: ' + str( fform3.form_name ))
 

    fform4= Form(db.dfform4, dbio=False, formstyle=FormStyleBulma)

    if fform4.accepted:
        prn_form_vars( fform4, db.dfform4 )
        return put_json_messages('accepted: ' + str( fform4.form_name ))
    elif fform4.errors:
        print("fform4 has errors: %s" % (fform4.errors))
        return put_json_messages('error: ' + str( fform4.form_name ))
 

    fform5= Form(db.dfform5, dbio=False, formstyle=FormStyleBulma)

    if fform5.accepted:
        prn_form_vars( fform5, db.dfform5 )
        return put_json_messages('accepted: ' + str( fform5.form_name ))
    elif fform5.errors:
        print("fform5 has errors: %s" % (fform5.errors))
        return put_json_messages('error: ' + str( fform5.form_name ))
 

    fform6= Form(db.dfform6, dbio=False, formstyle=FormStyleBulma)

    if fform6.accepted:
        prn_form_vars( fform6, db.dfform6 )
        return put_json_messages('accepted: ' + str( fform6.form_name ))
    elif fform6.errors:
        print("fform6 has errors: %s" % (fform6.errors))
        return put_json_messages('error: ' + str( fform6.form_name ))
 

    fform7= Form(db.dfform7, dbio=False, formstyle=FormStyleBulma)

    if fform7.accepted:
        prn_form_vars( fform7, db.dfform7 )
        return put_json_messages('accepted: ' + str( fform7.form_name ))
    elif fform7.errors:
        print("fform7 has errors: %s" % (fform7.errors))
        return put_json_messages('error: ' + str( fform7.form_name ))
 

    return locals()

@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T,)

def login():
    ctrl_info= "ctrl: login, view: login.html"
    page_url = "\'" + URL('login' ) + "\'"
    messages = []

    flogin0= Form(db.dflogin0, dbio=False, formstyle=FormStyleBulma)

    if flogin0.accepted:
        prn_form_vars( flogin0, db.dflogin0 )
        return put_json_messages('accepted: ' + str( flogin0.form_name ))
    elif flogin0.errors:
        print("flogin0 has errors: %s" % (flogin0.errors))
        return put_json_messages('error: ' + str( flogin0.form_name ))
 

    flogin1= Form(db.dflogin1, dbio=False, formstyle=FormStyleBulma)

    if flogin1.accepted:
        prn_form_vars( flogin1, db.dflogin1 )
        return put_json_messages('accepted: ' + str( flogin1.form_name ))
    elif flogin1.errors:
        print("flogin1 has errors: %s" % (flogin1.errors))
        return put_json_messages('error: ' + str( flogin1.form_name ))
 

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T,)

def inbox():
    ctrl_info= "ctrl: inbox, view: inbox.html"
    page_url = "\'" + URL('inbox' ) + "\'"
    messages = []

    return locals()

@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',), db, session, T,)

def icons():
    ctrl_info= "ctrl: icons, view: icons.html"
    page_url = "\'" + URL('icons' ) + "\'"
    messages = []

    return locals()

@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session, T,)

def tables():
    ctrl_info= "ctrl: tables, view: tables.html"
    page_url = "\'" + URL('tables' ) + "\'"
    messages = []

    rows_ttables0= db(db.ttables0).select()
    rows_ttables1= db(db.ttables1).select()
    rows_ttables2= db(db.ttables2).select()
    rows_ttables3= db(db.ttables3).select()
    rows_ttables4= db(db.ttables4).select()
    return locals()

@action('level2', method=["GET", "POST"] )
@action.uses(Template('level2.html', delimiters='[%[ ]]',), db, session, T,)

def level2():
    ctrl_info= "ctrl: level2, view: level2.html"
    page_url = "\'" + URL('level2' ) + "\'"
    messages = []

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session, T,)

def index3():
    ctrl_info= "ctrl: index3, view: index3.html"
    page_url = "\'" + URL('index3' ) + "\'"
    messages = []

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session, T,)

def index2():
    ctrl_info= "ctrl: index2, view: index2.html"
    page_url = "\'" + URL('index2' ) + "\'"
    messages = []

    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session, T,)

def widgets():
    ctrl_info= "ctrl: widgets, view: widgets.html"
    page_url = "\'" + URL('widgets' ) + "\'"
    messages = []

    return locals()

@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session, T,)

def profile():
    ctrl_info= "ctrl: profile, view: profile.html"
    page_url = "\'" + URL('profile' ) + "\'"
    messages = []

    rows_tprofile0= db(db.tprofile0).select()
    return locals()

@action('morisjs', method=["GET", "POST"] )
@action.uses(Template('morisjs.html', delimiters='[%[ ]]',), db, session, T,)

def morisjs():
    ctrl_info= "ctrl: morisjs, view: morisjs.html"
    page_url = "\'" + URL('morisjs' ) + "\'"
    messages = []

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session, T,)

def invoice():
    ctrl_info= "ctrl: invoice, view: invoice.html"
    page_url = "\'" + URL('invoice' ) + "\'"
    messages = []

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    return locals()

@action('echarts', method=["GET", "POST"] )
@action.uses(Template('echarts.html', delimiters='[%[ ]]',), db, session, T,)

def echarts():
    ctrl_info= "ctrl: echarts, view: echarts.html"
    page_url = "\'" + URL('echarts' ) + "\'"
    messages = []

    return locals()

@action('chartjs', method=["GET", "POST"] )
@action.uses(Template('chartjs.html', delimiters='[%[ ]]',), db, session, T,)

def chartjs():
    ctrl_info= "ctrl: chartjs, view: chartjs.html"
    page_url = "\'" + URL('chartjs' ) + "\'"
    messages = []

    return locals()

@action('projects', method=["GET", "POST"] )
@action.uses(Template('projects.html', delimiters='[%[ ]]',), db, session, T,)

def projects():
    ctrl_info= "ctrl: projects, view: projects.html"
    page_url = "\'" + URL('projects' ) + "\'"
    messages = []

    rows_tprojects0= db(db.tprojects0).select()
    return locals()

@action('pageX500', method=["GET", "POST"] )
@action.uses(Template('page_500.html', delimiters='[%[ ]]',), db, session, T,)

def pageX500():
    ctrl_info= "ctrl: pageX500, view: page_500.html"
    page_url = "\'" + URL('pageX500' ) + "\'"
    messages = []

    fpageX5000= Form(db.dfpageX5000, dbio=False, formstyle=FormStyleBulma)

    if fpageX5000.accepted:
        prn_form_vars( fpageX5000, db.dfpageX5000 )
        return put_json_messages('accepted: ' + str( fpageX5000.form_name ))
    elif fpageX5000.errors:
        print("fpageX5000 has errors: %s" % (fpageX5000.errors))
        return put_json_messages('error: ' + str( fpageX5000.form_name ))
 

    return locals()

@action('pageX404', method=["GET", "POST"] )
@action.uses(Template('page_404.html', delimiters='[%[ ]]',), db, session, T,)

def pageX404():
    ctrl_info= "ctrl: pageX404, view: page_404.html"
    page_url = "\'" + URL('pageX404' ) + "\'"
    messages = []

    fpageX4040= Form(db.dfpageX4040, dbio=False, formstyle=FormStyleBulma)

    if fpageX4040.accepted:
        prn_form_vars( fpageX4040, db.dfpageX4040 )
        return put_json_messages('accepted: ' + str( fpageX4040.form_name ))
    elif fpageX4040.errors:
        print("fpageX4040 has errors: %s" % (fpageX4040.errors))
        return put_json_messages('error: ' + str( fpageX4040.form_name ))
 

    return locals()

@action('pageX403', method=["GET", "POST"] )
@action.uses(Template('page_403.html', delimiters='[%[ ]]',), db, session, T,)

def pageX403():
    ctrl_info= "ctrl: pageX403, view: page_403.html"
    page_url = "\'" + URL('pageX403' ) + "\'"
    messages = []

    fpageX4030= Form(db.dfpageX4030, dbio=False, formstyle=FormStyleBulma)

    if fpageX4030.accepted:
        prn_form_vars( fpageX4030, db.dfpageX4030 )
        return put_json_messages('accepted: ' + str( fpageX4030.form_name ))
    elif fpageX4030.errors:
        print("fpageX4030 has errors: %s" % (fpageX4030.errors))
        return put_json_messages('error: ' + str( fpageX4030.form_name ))
 

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(Template('calendar.html', delimiters='[%[ ]]',), db, session, T,)

def calendar():
    ctrl_info= "ctrl: calendar, view: calendar.html"
    page_url = "\'" + URL('calendar' ) + "\'"
    messages = []

    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)

    if fcalendar0.accepted:
        prn_form_vars( fcalendar0, db.dfcalendar0 )
        return put_json_messages('accepted: ' + str( fcalendar0.form_name ))
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s" % (fcalendar0.errors))
        return put_json_messages('error: ' + str( fcalendar0.form_name ))
 

    fcalendar1= Form(db.dfcalendar1, dbio=False, formstyle=FormStyleBulma)

    if fcalendar1.accepted:
        prn_form_vars( fcalendar1, db.dfcalendar1 )
        return put_json_messages('accepted: ' + str( fcalendar1.form_name ))
    elif fcalendar1.errors:
        print("fcalendar1 has errors: %s" % (fcalendar1.errors))
        return put_json_messages('error: ' + str( fcalendar1.form_name ))
 

    return locals()

@action('contacts', method=["GET", "POST"] )
@action.uses(Template('contacts.html', delimiters='[%[ ]]',), db, session, T,)

def contacts():
    ctrl_info= "ctrl: contacts, view: contacts.html"
    page_url = "\'" + URL('contacts' ) + "\'"
    messages = []

    return locals()

@action('chartjs2', method=["GET", "POST"] )
@action.uses(Template('chartjs2.html', delimiters='[%[ ]]',), db, session, T,)

def chartjs2():
    ctrl_info= "ctrl: chartjs2, view: chartjs2.html"
    page_url = "\'" + URL('chartjs2' ) + "\'"
    messages = []

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session, T,)

def typography():
    ctrl_info= "ctrl: typography, view: typography.html"
    page_url = "\'" + URL('typography' ) + "\'"
    messages = []

    return locals()

@action('plainXpage', method=["GET", "POST"] )
@action.uses(Template('plain_page.html', delimiters='[%[ ]]',), db, session, T,)

def plainXpage():
    ctrl_info= "ctrl: plainXpage, view: plain_page.html"
    page_url = "\'" + URL('plainXpage' ) + "\'"
    messages = []

    return locals()

@action('glyphicons', method=["GET", "POST"] )
@action.uses(Template('glyphicons.html', delimiters='[%[ ]]',), db, session, T,)

def glyphicons():
    ctrl_info= "ctrl: glyphicons, view: glyphicons.html"
    page_url = "\'" + URL('glyphicons' ) + "\'"
    messages = []

    return locals()

@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e_commerce.html', delimiters='[%[ ]]',), db, session, T,)

def eXcommerce():
    ctrl_info= "ctrl: eXcommerce, view: e_commerce.html"
    page_url = "\'" + URL('eXcommerce' ) + "\'"
    messages = []

    return locals()

@action('formXupload', method=["GET", "POST"] )
@action.uses(Template('form_upload.html', delimiters='[%[ ]]',), db, session, T,)

def formXupload():
    ctrl_info= "ctrl: formXupload, view: form_upload.html"
    page_url = "\'" + URL('formXupload' ) + "\'"
    messages = []

    fformXupload0= Form(db.dfformXupload0, dbio=False, formstyle=FormStyleBulma)

    if fformXupload0.accepted:
        prn_form_vars( fformXupload0, db.dfformXupload0 )
        return put_json_messages('accepted: ' + str( fformXupload0.form_name ))
    elif fformXupload0.errors:
        print("fformXupload0 has errors: %s" % (fformXupload0.errors))
        return put_json_messages('error: ' + str( fformXupload0.form_name ))
 

    return locals()

@action('otherXcharts', method=["GET", "POST"] )
@action.uses(Template('other_charts.html', delimiters='[%[ ]]',), db, session, T,)

def otherXcharts():
    ctrl_info= "ctrl: otherXcharts, view: other_charts.html"
    page_url = "\'" + URL('otherXcharts' ) + "\'"
    messages = []

    rows_totherXcharts0= db(db.totherXcharts0).select()
    return locals()

@action('formXbuttons', method=["GET", "POST"] )
@action.uses(Template('form_buttons.html', delimiters='[%[ ]]',), db, session, T,)

def formXbuttons():
    ctrl_info= "ctrl: formXbuttons, view: form_buttons.html"
    page_url = "\'" + URL('formXbuttons' ) + "\'"
    messages = []

    return locals()

@action('formXwizards', method=["GET", "POST"] )
@action.uses(Template('form_wizards.html', delimiters='[%[ ]]',), db, session, T,)

def formXwizards():
    ctrl_info= "ctrl: formXwizards, view: form_wizards.html"
    page_url = "\'" + URL('formXwizards' ) + "\'"
    messages = []

    fformXwizards0= Form(db.dfformXwizards0, dbio=False, formstyle=FormStyleBulma)

    if fformXwizards0.accepted:
        prn_form_vars( fformXwizards0, db.dfformXwizards0 )
        return put_json_messages('accepted: ' + str( fformXwizards0.form_name ))
    elif fformXwizards0.errors:
        print("fformXwizards0 has errors: %s" % (fformXwizards0.errors))
        return put_json_messages('error: ' + str( fformXwizards0.form_name ))
 

    fformXwizards1= Form(db.dfformXwizards1, dbio=False, formstyle=FormStyleBulma)

    if fformXwizards1.accepted:
        prn_form_vars( fformXwizards1, db.dfformXwizards1 )
        return put_json_messages('accepted: ' + str( fformXwizards1.form_name ))
    elif fformXwizards1.errors:
        print("fformXwizards1 has errors: %s" % (fformXwizards1.errors))
        return put_json_messages('error: ' + str( fformXwizards1.form_name ))
 

    return locals()

@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(Template('fixed_footer.html', delimiters='[%[ ]]',), db, session, T,)

def fixedXfooter():
    ctrl_info= "ctrl: fixedXfooter, view: fixed_footer.html"
    page_url = "\'" + URL('fixedXfooter' ) + "\'"
    messages = []

    return locals()

@action('mediaXgallery', method=["GET", "POST"] )
@action.uses(Template('media_gallery.html', delimiters='[%[ ]]',), db, session, T,)

def mediaXgallery():
    ctrl_info= "ctrl: mediaXgallery, view: media_gallery.html"
    page_url = "\'" + URL('mediaXgallery' ) + "\'"
    messages = []

    return locals()

@action('formXadvanced', method=["GET", "POST"] )
@action.uses(Template('form_advanced.html', delimiters='[%[ ]]',), db, session, T,)

def formXadvanced():
    ctrl_info= "ctrl: formXadvanced, view: form_advanced.html"
    page_url = "\'" + URL('formXadvanced' ) + "\'"
    messages = []

    rows_tformXadvanced0= db(db.tformXadvanced0).select()
    rows_tformXadvanced1= db(db.tformXadvanced1).select()
    rows_tformXadvanced2= db(db.tformXadvanced2).select()
    rows_tformXadvanced3= db(db.tformXadvanced3).select()
    rows_tformXadvanced4= db(db.tformXadvanced4).select()
    rows_tformXadvanced5= db(db.tformXadvanced5).select()
    rows_tformXadvanced6= db(db.tformXadvanced6).select()
    rows_tformXadvanced7= db(db.tformXadvanced7).select()
    fformXadvanced0= Form(db.dfformXadvanced0, dbio=False, formstyle=FormStyleBulma)

    if fformXadvanced0.accepted:
        prn_form_vars( fformXadvanced0, db.dfformXadvanced0 )
        return put_json_messages('accepted: ' + str( fformXadvanced0.form_name ))
    elif fformXadvanced0.errors:
        print("fformXadvanced0 has errors: %s" % (fformXadvanced0.errors))
        return put_json_messages('error: ' + str( fformXadvanced0.form_name ))
 

    fformXadvanced1= Form(db.dfformXadvanced1, dbio=False, formstyle=FormStyleBulma)

    if fformXadvanced1.accepted:
        prn_form_vars( fformXadvanced1, db.dfformXadvanced1 )
        return put_json_messages('accepted: ' + str( fformXadvanced1.form_name ))
    elif fformXadvanced1.errors:
        print("fformXadvanced1 has errors: %s" % (fformXadvanced1.errors))
        return put_json_messages('error: ' + str( fformXadvanced1.form_name ))
 

    fformXadvanced2= Form(db.dfformXadvanced2, dbio=False, formstyle=FormStyleBulma)

    if fformXadvanced2.accepted:
        prn_form_vars( fformXadvanced2, db.dfformXadvanced2 )
        return put_json_messages('accepted: ' + str( fformXadvanced2.form_name ))
    elif fformXadvanced2.errors:
        print("fformXadvanced2 has errors: %s" % (fformXadvanced2.errors))
        return put_json_messages('error: ' + str( fformXadvanced2.form_name ))
 

    fformXadvanced3= Form(db.dfformXadvanced3, dbio=False, formstyle=FormStyleBulma)

    if fformXadvanced3.accepted:
        prn_form_vars( fformXadvanced3, db.dfformXadvanced3 )
        return put_json_messages('accepted: ' + str( fformXadvanced3.form_name ))
    elif fformXadvanced3.errors:
        print("fformXadvanced3 has errors: %s" % (fformXadvanced3.errors))
        return put_json_messages('error: ' + str( fformXadvanced3.form_name ))
 

    return locals()

@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(Template('fixed_sidebar.html', delimiters='[%[ ]]',), db, session, T,)

def fixedXsidebar():
    ctrl_info= "ctrl: fixedXsidebar, view: fixed_sidebar.html"
    page_url = "\'" + URL('fixedXsidebar' ) + "\'"
    messages = []

    return locals()

@action('tablesXdynamic', method=["GET", "POST"] )
@action.uses(Template('tables_dynamic.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXdynamic():
    ctrl_info= "ctrl: tablesXdynamic, view: tables_dynamic.html"
    page_url = "\'" + URL('tablesXdynamic' ) + "\'"
    messages = []

    rows_ttablesXdynamic0= db(db.ttablesXdynamic0).select()
    rows_ttablesXdynamic1= db(db.ttablesXdynamic1).select()
    rows_ttablesXdynamic2= db(db.ttablesXdynamic2).select()
    rows_ttablesXdynamic3= db(db.ttablesXdynamic3).select()
    rows_ttablesXdynamic4= db(db.ttablesXdynamic4).select()
    rows_ttablesXdynamic5= db(db.ttablesXdynamic5).select()
    return locals()

@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project_detail.html', delimiters='[%[ ]]',), db, session, T,)

def projectXdetail():
    ctrl_info= "ctrl: projectXdetail, view: project_detail.html"
    page_url = "\'" + URL('projectXdetail' ) + "\'"
    messages = []

    return locals()

@action('pricingXtables', method=["GET", "POST"] )
@action.uses(Template('pricing_tables.html', delimiters='[%[ ]]',), db, session, T,)

def pricingXtables():
    ctrl_info= "ctrl: pricingXtables, view: pricing_tables.html"
    page_url = "\'" + URL('pricingXtables' ) + "\'"
    messages = []

    return locals()

@action('formXvalidation', method=["GET", "POST"] )
@action.uses(Template('form_validation.html', delimiters='[%[ ]]',), db, session, T,)

def formXvalidation():
    ctrl_info= "ctrl: formXvalidation, view: form_validation.html"
    page_url = "\'" + URL('formXvalidation' ) + "\'"
    messages = []

    fformXvalidation0= Form(db.dfformXvalidation0, dbio=False, formstyle=FormStyleBulma)

    if fformXvalidation0.accepted:
        prn_form_vars( fformXvalidation0, db.dfformXvalidation0 )
        return put_json_messages('accepted: ' + str( fformXvalidation0.form_name ))
    elif fformXvalidation0.errors:
        print("fformXvalidation0 has errors: %s" % (fformXvalidation0.errors))
        return put_json_messages('error: ' + str( fformXvalidation0.form_name ))
 

    return locals()

@action('generalXelements', method=["GET", "POST"] )
@action.uses(Template('general_elements.html', delimiters='[%[ ]]',), db, session, T,)

def generalXelements():
    ctrl_info= "ctrl: generalXelements, view: general_elements.html"
    page_url = "\'" + URL('generalXelements' ) + "\'"
    messages = []

    rows_tgeneralXelements0= db(db.tgeneralXelements0).select()
    rows_tgeneralXelements1= db(db.tgeneralXelements1).select()
    return locals()


from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/', method=["GET", "POST", "PUT", "DELETE"])
@action('api/<tablename>/<rec_id>', method=["GET", "POST", "PUT", "DELETE"])
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.POST
                               )
# 
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/9
# curl -X DELETE  http://localhost:8000/gentelella/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/gentelella/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/gentelella/api/test_table/
#  http         localhost:8000/gentelella/api/test_table/9
#  http -f POST localhost:8000/gentelella/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/gentelella/api/test_table/2
#  http -f PUT localhost:8000/gentelella/api/test_table/2 f0=111111 f1=2222222 f2=333333


@bottle.error(404)
def error404(error):

    func_mess = []

    def check_rule(maybe_app_root):
        for e in Reloader.ROUTES:
            if ('rule' in e ) and ( e["rule"] == maybe_app_root) :
                Glb["debug"] and func_mess.append(f"     found_rule: {e['rule']}")
                return True
        return False

    location = "/" + Glb["my_app_name"]
    lx = bottle.request.path.split("/", 2)

    if len(lx) >= 2 and check_rule("/" + lx[1]):
        location = "/" + lx[1]
        files_prefix = location + Glb["tte_path"]

        location_2x = location + location + "/"
        files_prefix_2x = files_prefix + files_prefix + "/"

        def rm_bad_prefix(bad_prefix):
            new_location = bottle.request.path.replace(bad_prefix, "", 1)
            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
            return new_location

        if bottle.request.path.startswith(files_prefix_2x):
            if len(bottle.request.path) > len(files_prefix_2x):
                location = rm_bad_prefix(files_prefix)

        elif bottle.request.path.startswith(location_2x):
            if len(bottle.request.path) > len(location_2x):
                location = rm_bad_prefix(location)
    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)

