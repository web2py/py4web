#
# py4web app, AI-biorex ported 01.12.2020 12:08:01 UTC+3
# https://github.com/ali96343/facep4w
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

#from yatl.helpers import INPUT, H1, HTML, BODY, A
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME


 
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

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
    
# ---------------------- Controllers  ------------------------------------------------

@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session, T,)

def X404():
    ctrl_info= "ctrl: X404, view: 404.html"
    page_url = "\'" + URL('X404' ) + "\'"
    messages = []

    return locals()

@action('tabs', method=["GET", "POST"] )
@action.uses(Template('tabs.html', delimiters='[%[ ]]',), db, session, T,)

def tabs():
    ctrl_info= "ctrl: tabs, view: tabs.html"
    page_url = "\'" + URL('tabs' ) + "\'"
    messages = []

    ftabs0= Form(db.dftabs0, dbio=False, formstyle=FormStyleBulma)

    if ftabs0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftabs0, db.dftabs0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftabs0.form_name ))
    elif ftabs0.errors:
        print("ftabs0 has errors: %s" % (ftabs0.errors))
        return put_json_messages('error: ' + str( ftabs0.form_name ))
 

    ftabs1= Form(db.dftabs1, dbio=False, formstyle=FormStyleBulma)

    if ftabs1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftabs1, db.dftabs1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftabs1.form_name ))
    elif ftabs1.errors:
        print("ftabs1 has errors: %s" % (ftabs1.errors))
        return put_json_messages('error: ' + str( ftabs1.form_name ))
 

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T,)

def inbox():
    ctrl_info= "ctrl: inbox, view: inbox.html"
    page_url = "\'" + URL('inbox' ) + "\'"
    messages = []

    rows_tinbox0= db(db.tinbox0).select()
    finbox0= Form(db.dfinbox0, dbio=False, formstyle=FormStyleBulma)

    if finbox0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox0, db.dfinbox0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox0.form_name ))
    elif finbox0.errors:
        print("finbox0 has errors: %s" % (finbox0.errors))
        return put_json_messages('error: ' + str( finbox0.form_name ))
 

    finbox1= Form(db.dfinbox1, dbio=False, formstyle=FormStyleBulma)

    if finbox1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox1, db.dfinbox1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox1.form_name ))
    elif finbox1.errors:
        print("finbox1 has errors: %s" % (finbox1.errors))
        return put_json_messages('error: ' + str( finbox1.form_name ))
 

    finbox2= Form(db.dfinbox2, dbio=False, formstyle=FormStyleBulma)

    if finbox2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox2, db.dfinbox2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox2.form_name ))
    elif finbox2.errors:
        print("finbox2 has errors: %s" % (finbox2.errors))
        return put_json_messages('error: ' + str( finbox2.form_name ))
 

    finbox3= Form(db.dfinbox3, dbio=False, formstyle=FormStyleBulma)

    if finbox3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox3, db.dfinbox3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox3.form_name ))
    elif finbox3.errors:
        print("finbox3 has errors: %s" % (finbox3.errors))
        return put_json_messages('error: ' + str( finbox3.form_name ))
 

    finbox4= Form(db.dfinbox4, dbio=False, formstyle=FormStyleBulma)

    if finbox4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox4, db.dfinbox4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox4.form_name ))
    elif finbox4.errors:
        print("finbox4 has errors: %s" % (finbox4.errors))
        return put_json_messages('error: ' + str( finbox4.form_name ))
 

    finbox5= Form(db.dfinbox5, dbio=False, formstyle=FormStyleBulma)

    if finbox5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox5, db.dfinbox5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox5.form_name ))
    elif finbox5.errors:
        print("finbox5 has errors: %s" % (finbox5.errors))
        return put_json_messages('error: ' + str( finbox5.form_name ))
 

    finbox6= Form(db.dfinbox6, dbio=False, formstyle=FormStyleBulma)

    if finbox6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox6, db.dfinbox6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox6.form_name ))
    elif finbox6.errors:
        print("finbox6 has errors: %s" % (finbox6.errors))
        return put_json_messages('error: ' + str( finbox6.form_name ))
 

    finbox7= Form(db.dfinbox7, dbio=False, formstyle=FormStyleBulma)

    if finbox7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox7, db.dfinbox7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox7.form_name ))
    elif finbox7.errors:
        print("finbox7 has errors: %s" % (finbox7.errors))
        return put_json_messages('error: ' + str( finbox7.form_name ))
 

    finbox8= Form(db.dfinbox8, dbio=False, formstyle=FormStyleBulma)

    if finbox8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox8, db.dfinbox8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox8.form_name ))
    elif finbox8.errors:
        print("finbox8 has errors: %s" % (finbox8.errors))
        return put_json_messages('error: ' + str( finbox8.form_name ))
 

    finbox9= Form(db.dfinbox9, dbio=False, formstyle=FormStyleBulma)

    if finbox9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox9, db.dfinbox9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox9.form_name ))
    elif finbox9.errors:
        print("finbox9 has errors: %s" % (finbox9.errors))
        return put_json_messages('error: ' + str( finbox9.form_name ))
 

    finbox10= Form(db.dfinbox10, dbio=False, formstyle=FormStyleBulma)

    if finbox10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finbox10, db.dfinbox10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finbox10.form_name ))
    elif finbox10.errors:
        print("finbox10 has errors: %s" % (finbox10.errors))
        return put_json_messages('error: ' + str( finbox10.form_name ))
 

    return locals()

@action('alert', method=["GET", "POST"] )
@action.uses(Template('alert.html', delimiters='[%[ ]]',), db, session, T,)

def alert():
    ctrl_info= "ctrl: alert, view: alert.html"
    page_url = "\'" + URL('alert' ) + "\'"
    messages = []

    falert0= Form(db.dfalert0, dbio=False, formstyle=FormStyleBulma)

    if falert0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( falert0, db.dfalert0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( falert0.form_name ))
    elif falert0.errors:
        print("falert0 has errors: %s" % (falert0.errors))
        return put_json_messages('error: ' + str( falert0.form_name ))
 

    falert1= Form(db.dfalert1, dbio=False, formstyle=FormStyleBulma)

    if falert1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( falert1, db.dfalert1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( falert1.form_name ))
    elif falert1.errors:
        print("falert1 has errors: %s" % (falert1.errors))
        return put_json_messages('error: ' + str( falert1.form_name ))
 

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    rows_tindex0= db(db.tindex0).select()
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)

    if findex0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex0, db.dfindex0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex0.form_name ))
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return put_json_messages('error: ' + str( findex0.form_name ))
 

    findex1= Form(db.dfindex1, dbio=False, formstyle=FormStyleBulma)

    if findex1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex1, db.dfindex1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex1.form_name ))
    elif findex1.errors:
        print("findex1 has errors: %s" % (findex1.errors))
        return put_json_messages('error: ' + str( findex1.form_name ))
 

    findex2= Form(db.dfindex2, dbio=False, formstyle=FormStyleBulma)

    if findex2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex2, db.dfindex2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex2.form_name ))
    elif findex2.errors:
        print("findex2 has errors: %s" % (findex2.errors))
        return put_json_messages('error: ' + str( findex2.form_name ))
 

    findex3= Form(db.dfindex3, dbio=False, formstyle=FormStyleBulma)

    if findex3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex3, db.dfindex3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex3.form_name ))
    elif findex3.errors:
        print("findex3 has errors: %s" % (findex3.errors))
        return put_json_messages('error: ' + str( findex3.form_name ))
 

    findex4= Form(db.dfindex4, dbio=False, formstyle=FormStyleBulma)

    if findex4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex4, db.dfindex4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex4.form_name ))
    elif findex4.errors:
        print("findex4 has errors: %s" % (findex4.errors))
        return put_json_messages('error: ' + str( findex4.form_name ))
 

    findex5= Form(db.dfindex5, dbio=False, formstyle=FormStyleBulma)

    if findex5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex5, db.dfindex5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex5.form_name ))
    elif findex5.errors:
        print("findex5 has errors: %s" % (findex5.errors))
        return put_json_messages('error: ' + str( findex5.form_name ))
 

    findex6= Form(db.dfindex6, dbio=False, formstyle=FormStyleBulma)

    if findex6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex6, db.dfindex6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex6.form_name ))
    elif findex6.errors:
        print("findex6 has errors: %s" % (findex6.errors))
        return put_json_messages('error: ' + str( findex6.form_name ))
 

    findex7= Form(db.dfindex7, dbio=False, formstyle=FormStyleBulma)

    if findex7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex7, db.dfindex7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex7.form_name ))
    elif findex7.errors:
        print("findex7 has errors: %s" % (findex7.errors))
        return put_json_messages('error: ' + str( findex7.form_name ))
 

    return locals()

@action('color', method=["GET", "POST"] )
@action.uses(Template('color.html', delimiters='[%[ ]]',), db, session, T,)

def color():
    ctrl_info= "ctrl: color, view: color.html"
    page_url = "\'" + URL('color' ) + "\'"
    messages = []

    fcolor0= Form(db.dfcolor0, dbio=False, formstyle=FormStyleBulma)

    if fcolor0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcolor0, db.dfcolor0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcolor0.form_name ))
    elif fcolor0.errors:
        print("fcolor0 has errors: %s" % (fcolor0.errors))
        return put_json_messages('error: ' + str( fcolor0.form_name ))
 

    fcolor1= Form(db.dfcolor1, dbio=False, formstyle=FormStyleBulma)

    if fcolor1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcolor1, db.dfcolor1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcolor1.form_name ))
    elif fcolor1.errors:
        print("fcolor1 has errors: %s" % (fcolor1.errors))
        return put_json_messages('error: ' + str( fcolor1.form_name ))
 

    return locals()

@action('wizard', method=["GET", "POST"] )
@action.uses(Template('wizard.html', delimiters='[%[ ]]',), db, session, T,)

def wizard():
    ctrl_info= "ctrl: wizard, view: wizard.html"
    page_url = "\'" + URL('wizard' ) + "\'"
    messages = []

    fwizard0= Form(db.dfwizard0, dbio=False, formstyle=FormStyleBulma)

    if fwizard0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwizard0, db.dfwizard0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwizard0.form_name ))
    elif fwizard0.errors:
        print("fwizard0 has errors: %s" % (fwizard0.errors))
        return put_json_messages('error: ' + str( fwizard0.form_name ))
 

    fwizard1= Form(db.dfwizard1, dbio=False, formstyle=FormStyleBulma)

    if fwizard1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwizard1, db.dfwizard1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwizard1.form_name ))
    elif fwizard1.errors:
        print("fwizard1 has errors: %s" % (fwizard1.errors))
        return put_json_messages('error: ' + str( fwizard1.form_name ))
 

    return locals()

@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session, T,)

def modals():
    ctrl_info= "ctrl: modals, view: modals.html"
    page_url = "\'" + URL('modals' ) + "\'"
    messages = []

    fmodals0= Form(db.dfmodals0, dbio=False, formstyle=FormStyleBulma)

    if fmodals0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals0, db.dfmodals0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals0.form_name ))
    elif fmodals0.errors:
        print("fmodals0 has errors: %s" % (fmodals0.errors))
        return put_json_messages('error: ' + str( fmodals0.form_name ))
 

    fmodals1= Form(db.dfmodals1, dbio=False, formstyle=FormStyleBulma)

    if fmodals1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals1, db.dfmodals1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals1.form_name ))
    elif fmodals1.errors:
        print("fmodals1 has errors: %s" % (fmodals1.errors))
        return put_json_messages('error: ' + str( fmodals1.form_name ))
 

    return locals()

@action('dialog', method=["GET", "POST"] )
@action.uses(Template('dialog.html', delimiters='[%[ ]]',), db, session, T,)

def dialog():
    ctrl_info= "ctrl: dialog, view: dialog.html"
    page_url = "\'" + URL('dialog' ) + "\'"
    messages = []

    fdialog0= Form(db.dfdialog0, dbio=False, formstyle=FormStyleBulma)

    if fdialog0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdialog0, db.dfdialog0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdialog0.form_name ))
    elif fdialog0.errors:
        print("fdialog0 has errors: %s" % (fdialog0.errors))
        return put_json_messages('error: ' + str( fdialog0.form_name ))
 

    fdialog1= Form(db.dfdialog1, dbio=False, formstyle=FormStyleBulma)

    if fdialog1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdialog1, db.dfdialog1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdialog1.form_name ))
    elif fdialog1.errors:
        print("fdialog1 has errors: %s" % (fdialog1.errors))
        return put_json_messages('error: ' + str( fdialog1.form_name ))
 

    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session, T,)

def widgets():
    ctrl_info= "ctrl: widgets, view: widgets.html"
    page_url = "\'" + URL('widgets' ) + "\'"
    messages = []

    fwidgets0= Form(db.dfwidgets0, dbio=False, formstyle=FormStyleBulma)

    if fwidgets0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets0, db.dfwidgets0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets0.form_name ))
    elif fwidgets0.errors:
        print("fwidgets0 has errors: %s" % (fwidgets0.errors))
        return put_json_messages('error: ' + str( fwidgets0.form_name ))
 

    fwidgets1= Form(db.dfwidgets1, dbio=False, formstyle=FormStyleBulma)

    if fwidgets1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets1, db.dfwidgets1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets1.form_name ))
    elif fwidgets1.errors:
        print("fwidgets1 has errors: %s" % (fwidgets1.errors))
        return put_json_messages('error: ' + str( fwidgets1.form_name ))
 

    fwidgets2= Form(db.dfwidgets2, dbio=False, formstyle=FormStyleBulma)

    if fwidgets2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets2, db.dfwidgets2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets2.form_name ))
    elif fwidgets2.errors:
        print("fwidgets2 has errors: %s" % (fwidgets2.errors))
        return put_json_messages('error: ' + str( fwidgets2.form_name ))
 

    fwidgets3= Form(db.dfwidgets3, dbio=False, formstyle=FormStyleBulma)

    if fwidgets3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets3, db.dfwidgets3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets3.form_name ))
    elif fwidgets3.errors:
        print("fwidgets3 has errors: %s" % (fwidgets3.errors))
        return put_json_messages('error: ' + str( fwidgets3.form_name ))
 

    fwidgets4= Form(db.dfwidgets4, dbio=False, formstyle=FormStyleBulma)

    if fwidgets4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets4, db.dfwidgets4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets4.form_name ))
    elif fwidgets4.errors:
        print("fwidgets4 has errors: %s" % (fwidgets4.errors))
        return put_json_messages('error: ' + str( fwidgets4.form_name ))
 

    fwidgets5= Form(db.dfwidgets5, dbio=False, formstyle=FormStyleBulma)

    if fwidgets5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets5, db.dfwidgets5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets5.form_name ))
    elif fwidgets5.errors:
        print("fwidgets5 has errors: %s" % (fwidgets5.errors))
        return put_json_messages('error: ' + str( fwidgets5.form_name ))
 

    fwidgets6= Form(db.dfwidgets6, dbio=False, formstyle=FormStyleBulma)

    if fwidgets6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fwidgets6, db.dfwidgets6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fwidgets6.form_name ))
    elif fwidgets6.errors:
        print("fwidgets6 has errors: %s" % (fwidgets6.errors))
        return put_json_messages('error: ' + str( fwidgets6.form_name ))
 

    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session, T,)

def buttons():
    ctrl_info= "ctrl: buttons, view: buttons.html"
    page_url = "\'" + URL('buttons' ) + "\'"
    messages = []

    fbuttons0= Form(db.dfbuttons0, dbio=False, formstyle=FormStyleBulma)

    if fbuttons0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbuttons0, db.dfbuttons0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbuttons0.form_name ))
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s" % (fbuttons0.errors))
        return put_json_messages('error: ' + str( fbuttons0.form_name ))
 

    fbuttons1= Form(db.dfbuttons1, dbio=False, formstyle=FormStyleBulma)

    if fbuttons1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbuttons1, db.dfbuttons1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbuttons1.form_name ))
    elif fbuttons1.errors:
        print("fbuttons1 has errors: %s" % (fbuttons1.errors))
        return put_json_messages('error: ' + str( fbuttons1.form_name ))
 

    return locals()

@action('indexX3', method=["GET", "POST"] )
@action.uses(Template('index-3.html', delimiters='[%[ ]]',), db, session, T,)

def indexX3():
    ctrl_info= "ctrl: indexX3, view: index-3.html"
    page_url = "\'" + URL('indexX3' ) + "\'"
    messages = []

    rows_tindexX30= db(db.tindexX30).select()
    findexX30= Form(db.dfindexX30, dbio=False, formstyle=FormStyleBulma)

    if findexX30.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX30, db.dfindexX30 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX30.form_name ))
    elif findexX30.errors:
        print("findexX30 has errors: %s" % (findexX30.errors))
        return put_json_messages('error: ' + str( findexX30.form_name ))
 

    findexX31= Form(db.dfindexX31, dbio=False, formstyle=FormStyleBulma)

    if findexX31.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX31, db.dfindexX31 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX31.form_name ))
    elif findexX31.errors:
        print("findexX31 has errors: %s" % (findexX31.errors))
        return put_json_messages('error: ' + str( findexX31.form_name ))
 

    findexX32= Form(db.dfindexX32, dbio=False, formstyle=FormStyleBulma)

    if findexX32.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX32, db.dfindexX32 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX32.form_name ))
    elif findexX32.errors:
        print("findexX32 has errors: %s" % (findexX32.errors))
        return put_json_messages('error: ' + str( findexX32.form_name ))
 

    findexX33= Form(db.dfindexX33, dbio=False, formstyle=FormStyleBulma)

    if findexX33.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX33, db.dfindexX33 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX33.form_name ))
    elif findexX33.errors:
        print("findexX33 has errors: %s" % (findexX33.errors))
        return put_json_messages('error: ' + str( findexX33.form_name ))
 

    findexX34= Form(db.dfindexX34, dbio=False, formstyle=FormStyleBulma)

    if findexX34.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX34, db.dfindexX34 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX34.form_name ))
    elif findexX34.errors:
        print("findexX34 has errors: %s" % (findexX34.errors))
        return put_json_messages('error: ' + str( findexX34.form_name ))
 

    findexX35= Form(db.dfindexX35, dbio=False, formstyle=FormStyleBulma)

    if findexX35.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX35, db.dfindexX35 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX35.form_name ))
    elif findexX35.errors:
        print("findexX35 has errors: %s" % (findexX35.errors))
        return put_json_messages('error: ' + str( findexX35.form_name ))
 

    findexX36= Form(db.dfindexX36, dbio=False, formstyle=FormStyleBulma)

    if findexX36.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX36, db.dfindexX36 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX36.form_name ))
    elif findexX36.errors:
        print("findexX36 has errors: %s" % (findexX36.errors))
        return put_json_messages('error: ' + str( findexX36.form_name ))
 

    findexX37= Form(db.dfindexX37, dbio=False, formstyle=FormStyleBulma)

    if findexX37.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX37, db.dfindexX37 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX37.form_name ))
    elif findexX37.errors:
        print("findexX37 has errors: %s" % (findexX37.errors))
        return put_json_messages('error: ' + str( findexX37.form_name ))
 

    return locals()

@action('contact', method=["GET", "POST"] )
@action.uses(Template('contact.html', delimiters='[%[ ]]',), db, session, T,)

def contact():
    ctrl_info= "ctrl: contact, view: contact.html"
    page_url = "\'" + URL('contact' ) + "\'"
    messages = []

    fcontact0= Form(db.dfcontact0, dbio=False, formstyle=FormStyleBulma)

    if fcontact0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcontact0, db.dfcontact0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcontact0.form_name ))
    elif fcontact0.errors:
        print("fcontact0 has errors: %s" % (fcontact0.errors))
        return put_json_messages('error: ' + str( fcontact0.form_name ))
 

    fcontact1= Form(db.dfcontact1, dbio=False, formstyle=FormStyleBulma)

    if fcontact1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcontact1, db.dfcontact1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcontact1.form_name ))
    elif fcontact1.errors:
        print("fcontact1 has errors: %s" % (fcontact1.errors))
        return put_json_messages('error: ' + str( fcontact1.form_name ))
 

    return locals()

@action('indexX4', method=["GET", "POST"] )
@action.uses(Template('index-4.html', delimiters='[%[ ]]',), db, session, T,)

def indexX4():
    ctrl_info= "ctrl: indexX4, view: index-4.html"
    page_url = "\'" + URL('indexX4' ) + "\'"
    messages = []

    rows_tindexX40= db(db.tindexX40).select()
    findexX40= Form(db.dfindexX40, dbio=False, formstyle=FormStyleBulma)

    if findexX40.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX40, db.dfindexX40 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX40.form_name ))
    elif findexX40.errors:
        print("findexX40 has errors: %s" % (findexX40.errors))
        return put_json_messages('error: ' + str( findexX40.form_name ))
 

    findexX41= Form(db.dfindexX41, dbio=False, formstyle=FormStyleBulma)

    if findexX41.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX41, db.dfindexX41 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX41.form_name ))
    elif findexX41.errors:
        print("findexX41 has errors: %s" % (findexX41.errors))
        return put_json_messages('error: ' + str( findexX41.form_name ))
 

    findexX42= Form(db.dfindexX42, dbio=False, formstyle=FormStyleBulma)

    if findexX42.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX42, db.dfindexX42 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX42.form_name ))
    elif findexX42.errors:
        print("findexX42 has errors: %s" % (findexX42.errors))
        return put_json_messages('error: ' + str( findexX42.form_name ))
 

    findexX43= Form(db.dfindexX43, dbio=False, formstyle=FormStyleBulma)

    if findexX43.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX43, db.dfindexX43 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX43.form_name ))
    elif findexX43.errors:
        print("findexX43 has errors: %s" % (findexX43.errors))
        return put_json_messages('error: ' + str( findexX43.form_name ))
 

    findexX44= Form(db.dfindexX44, dbio=False, formstyle=FormStyleBulma)

    if findexX44.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX44, db.dfindexX44 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX44.form_name ))
    elif findexX44.errors:
        print("findexX44 has errors: %s" % (findexX44.errors))
        return put_json_messages('error: ' + str( findexX44.form_name ))
 

    findexX45= Form(db.dfindexX45, dbio=False, formstyle=FormStyleBulma)

    if findexX45.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX45, db.dfindexX45 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX45.form_name ))
    elif findexX45.errors:
        print("findexX45 has errors: %s" % (findexX45.errors))
        return put_json_messages('error: ' + str( findexX45.form_name ))
 

    findexX46= Form(db.dfindexX46, dbio=False, formstyle=FormStyleBulma)

    if findexX46.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX46, db.dfindexX46 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX46.form_name ))
    elif findexX46.errors:
        print("findexX46 has errors: %s" % (findexX46.errors))
        return put_json_messages('error: ' + str( findexX46.form_name ))
 

    findexX47= Form(db.dfindexX47, dbio=False, formstyle=FormStyleBulma)

    if findexX47.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX47, db.dfindexX47 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX47.form_name ))
    elif findexX47.errors:
        print("findexX47 has errors: %s" % (findexX47.errors))
        return put_json_messages('error: ' + str( findexX47.form_name ))
 

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session, T,)

def invoice():
    ctrl_info= "ctrl: invoice, view: invoice.html"
    page_url = "\'" + URL('invoice' ) + "\'"
    messages = []

    rows_tinvoice0= db(db.tinvoice0).select()
    finvoice0= Form(db.dfinvoice0, dbio=False, formstyle=FormStyleBulma)

    if finvoice0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finvoice0, db.dfinvoice0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finvoice0.form_name ))
    elif finvoice0.errors:
        print("finvoice0 has errors: %s" % (finvoice0.errors))
        return put_json_messages('error: ' + str( finvoice0.form_name ))
 

    finvoice1= Form(db.dfinvoice1, dbio=False, formstyle=FormStyleBulma)

    if finvoice1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( finvoice1, db.dfinvoice1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( finvoice1.form_name ))
    elif finvoice1.errors:
        print("finvoice1 has errors: %s" % (finvoice1.errors))
        return put_json_messages('error: ' + str( finvoice1.form_name ))
 

    return locals()

@action('indexX2', method=["GET", "POST"] )
@action.uses(Template('index-2.html', delimiters='[%[ ]]',), db, session, T,)

def indexX2():
    ctrl_info= "ctrl: indexX2, view: index-2.html"
    page_url = "\'" + URL('indexX2' ) + "\'"
    messages = []

    rows_tindexX20= db(db.tindexX20).select()
    findexX20= Form(db.dfindexX20, dbio=False, formstyle=FormStyleBulma)

    if findexX20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX20, db.dfindexX20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX20.form_name ))
    elif findexX20.errors:
        print("findexX20 has errors: %s" % (findexX20.errors))
        return put_json_messages('error: ' + str( findexX20.form_name ))
 

    findexX21= Form(db.dfindexX21, dbio=False, formstyle=FormStyleBulma)

    if findexX21.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX21, db.dfindexX21 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX21.form_name ))
    elif findexX21.errors:
        print("findexX21 has errors: %s" % (findexX21.errors))
        return put_json_messages('error: ' + str( findexX21.form_name ))
 

    findexX22= Form(db.dfindexX22, dbio=False, formstyle=FormStyleBulma)

    if findexX22.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX22, db.dfindexX22 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX22.form_name ))
    elif findexX22.errors:
        print("findexX22 has errors: %s" % (findexX22.errors))
        return put_json_messages('error: ' + str( findexX22.form_name ))
 

    findexX23= Form(db.dfindexX23, dbio=False, formstyle=FormStyleBulma)

    if findexX23.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX23, db.dfindexX23 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX23.form_name ))
    elif findexX23.errors:
        print("findexX23 has errors: %s" % (findexX23.errors))
        return put_json_messages('error: ' + str( findexX23.form_name ))
 

    findexX24= Form(db.dfindexX24, dbio=False, formstyle=FormStyleBulma)

    if findexX24.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX24, db.dfindexX24 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX24.form_name ))
    elif findexX24.errors:
        print("findexX24 has errors: %s" % (findexX24.errors))
        return put_json_messages('error: ' + str( findexX24.form_name ))
 

    findexX25= Form(db.dfindexX25, dbio=False, formstyle=FormStyleBulma)

    if findexX25.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX25, db.dfindexX25 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX25.form_name ))
    elif findexX25.errors:
        print("findexX25 has errors: %s" % (findexX25.errors))
        return put_json_messages('error: ' + str( findexX25.form_name ))
 

    findexX26= Form(db.dfindexX26, dbio=False, formstyle=FormStyleBulma)

    if findexX26.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX26, db.dfindexX26 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX26.form_name ))
    elif findexX26.errors:
        print("findexX26 has errors: %s" % (findexX26.errors))
        return put_json_messages('error: ' + str( findexX26.form_name ))
 

    findexX27= Form(db.dfindexX27, dbio=False, formstyle=FormStyleBulma)

    if findexX27.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findexX27, db.dfindexX27 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findexX27.form_name ))
    elif findexX27.errors:
        print("findexX27 has errors: %s" % (findexX27.errors))
        return put_json_messages('error: ' + str( findexX27.form_name ))
 

    return locals()

@action('tooltips', method=["GET", "POST"] )
@action.uses(Template('tooltips.html', delimiters='[%[ ]]',), db, session, T,)

def tooltips():
    ctrl_info= "ctrl: tooltips, view: tooltips.html"
    page_url = "\'" + URL('tooltips' ) + "\'"
    messages = []

    ftooltips0= Form(db.dftooltips0, dbio=False, formstyle=FormStyleBulma)

    if ftooltips0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftooltips0, db.dftooltips0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftooltips0.form_name ))
    elif ftooltips0.errors:
        print("ftooltips0 has errors: %s" % (ftooltips0.errors))
        return put_json_messages('error: ' + str( ftooltips0.form_name ))
 

    ftooltips1= Form(db.dftooltips1, dbio=False, formstyle=FormStyleBulma)

    if ftooltips1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftooltips1, db.dftooltips1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftooltips1.form_name ))
    elif ftooltips1.errors:
        print("ftooltips1 has errors: %s" % (ftooltips1.errors))
        return put_json_messages('error: ' + str( ftooltips1.form_name ))
 

    return locals()

@action('popovers', method=["GET", "POST"] )
@action.uses(Template('popovers.html', delimiters='[%[ ]]',), db, session, T,)

def popovers():
    ctrl_info= "ctrl: popovers, view: popovers.html"
    page_url = "\'" + URL('popovers' ) + "\'"
    messages = []

    fpopovers0= Form(db.dfpopovers0, dbio=False, formstyle=FormStyleBulma)

    if fpopovers0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpopovers0, db.dfpopovers0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpopovers0.form_name ))
    elif fpopovers0.errors:
        print("fpopovers0 has errors: %s" % (fpopovers0.errors))
        return put_json_messages('error: ' + str( fpopovers0.form_name ))
 

    fpopovers1= Form(db.dfpopovers1, dbio=False, formstyle=FormStyleBulma)

    if fpopovers1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpopovers1, db.dfpopovers1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpopovers1.form_name ))
    elif fpopovers1.errors:
        print("fpopovers1 has errors: %s" % (fpopovers1.errors))
        return put_json_messages('error: ' + str( fpopovers1.form_name ))
 

    return locals()

@action('dropdown', method=["GET", "POST"] )
@action.uses(Template('dropdown.html', delimiters='[%[ ]]',), db, session, T,)

def dropdown():
    ctrl_info= "ctrl: dropdown, view: dropdown.html"
    page_url = "\'" + URL('dropdown' ) + "\'"
    messages = []

    fdropdown0= Form(db.dfdropdown0, dbio=False, formstyle=FormStyleBulma)

    if fdropdown0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdropdown0, db.dfdropdown0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdropdown0.form_name ))
    elif fdropdown0.errors:
        print("fdropdown0 has errors: %s" % (fdropdown0.errors))
        return put_json_messages('error: ' + str( fdropdown0.form_name ))
 

    fdropdown1= Form(db.dfdropdown1, dbio=False, formstyle=FormStyleBulma)

    if fdropdown1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdropdown1, db.dfdropdown1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdropdown1.form_name ))
    elif fdropdown1.errors:
        print("fdropdown1 has errors: %s" % (fdropdown1.errors))
        return put_json_messages('error: ' + str( fdropdown1.form_name ))
 

    return locals()

@action('dataXmap', method=["GET", "POST"] )
@action.uses(Template('data-map.html', delimiters='[%[ ]]',), db, session, T,)

def dataXmap():
    ctrl_info= "ctrl: dataXmap, view: data-map.html"
    page_url = "\'" + URL('dataXmap' ) + "\'"
    messages = []

    fdataXmap0= Form(db.dfdataXmap0, dbio=False, formstyle=FormStyleBulma)

    if fdataXmap0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdataXmap0, db.dfdataXmap0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdataXmap0.form_name ))
    elif fdataXmap0.errors:
        print("fdataXmap0 has errors: %s" % (fdataXmap0.errors))
        return put_json_messages('error: ' + str( fdataXmap0.form_name ))
 

    fdataXmap1= Form(db.dfdataXmap1, dbio=False, formstyle=FormStyleBulma)

    if fdataXmap1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdataXmap1, db.dfdataXmap1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdataXmap1.form_name ))
    elif fdataXmap1.errors:
        print("fdataXmap1 has errors: %s" % (fdataXmap1.errors))
        return put_json_messages('error: ' + str( fdataXmap1.form_name ))
 

    return locals()

@action('accordion', method=["GET", "POST"] )
@action.uses(Template('accordion.html', delimiters='[%[ ]]',), db, session, T,)

def accordion():
    ctrl_info= "ctrl: accordion, view: accordion.html"
    page_url = "\'" + URL('accordion' ) + "\'"
    messages = []

    faccordion0= Form(db.dfaccordion0, dbio=False, formstyle=FormStyleBulma)

    if faccordion0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( faccordion0, db.dfaccordion0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( faccordion0.form_name ))
    elif faccordion0.errors:
        print("faccordion0 has errors: %s" % (faccordion0.errors))
        return put_json_messages('error: ' + str( faccordion0.form_name ))
 

    faccordion1= Form(db.dfaccordion1, dbio=False, formstyle=FormStyleBulma)

    if faccordion1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( faccordion1, db.dfaccordion1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( faccordion1.form_name ))
    elif faccordion1.errors:
        print("faccordion1 has errors: %s" % (faccordion1.errors))
        return put_json_messages('error: ' + str( faccordion1.form_name ))
 

    return locals()

@action('analytics', method=["GET", "POST"] )
@action.uses(Template('analytics.html', delimiters='[%[ ]]',), db, session, T,)

def analytics():
    ctrl_info= "ctrl: analytics, view: analytics.html"
    page_url = "\'" + URL('analytics' ) + "\'"
    messages = []

    rows_tanalytics0= db(db.tanalytics0).select()
    rows_tanalytics1= db(db.tanalytics1).select()
    rows_tanalytics2= db(db.tanalytics2).select()
    fanalytics0= Form(db.dfanalytics0, dbio=False, formstyle=FormStyleBulma)

    if fanalytics0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fanalytics0, db.dfanalytics0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fanalytics0.form_name ))
    elif fanalytics0.errors:
        print("fanalytics0 has errors: %s" % (fanalytics0.errors))
        return put_json_messages('error: ' + str( fanalytics0.form_name ))
 

    fanalytics1= Form(db.dfanalytics1, dbio=False, formstyle=FormStyleBulma)

    if fanalytics1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fanalytics1, db.dfanalytics1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fanalytics1.form_name ))
    elif fanalytics1.errors:
        print("fanalytics1 has errors: %s" % (fanalytics1.errors))
        return put_json_messages('error: ' + str( fanalytics1.form_name ))
 

    return locals()

@action('viewXemail', method=["GET", "POST"] )
@action.uses(Template('view-email.html', delimiters='[%[ ]]',), db, session, T,)

def viewXemail():
    ctrl_info= "ctrl: viewXemail, view: view-email.html"
    page_url = "\'" + URL('viewXemail' ) + "\'"
    messages = []

    fviewXemail0= Form(db.dfviewXemail0, dbio=False, formstyle=FormStyleBulma)

    if fviewXemail0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fviewXemail0, db.dfviewXemail0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fviewXemail0.form_name ))
    elif fviewXemail0.errors:
        print("fviewXemail0 has errors: %s" % (fviewXemail0.errors))
        return put_json_messages('error: ' + str( fviewXemail0.form_name ))
 

    fviewXemail1= Form(db.dfviewXemail1, dbio=False, formstyle=FormStyleBulma)

    if fviewXemail1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fviewXemail1, db.dfviewXemail1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fviewXemail1.form_name ))
    elif fviewXemail1.errors:
        print("fviewXemail1 has errors: %s" % (fviewXemail1.errors))
        return put_json_messages('error: ' + str( fviewXemail1.form_name ))
 

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session, T,)

def typography():
    ctrl_info= "ctrl: typography, view: typography.html"
    page_url = "\'" + URL('typography' ) + "\'"
    messages = []

    ftypography0= Form(db.dftypography0, dbio=False, formstyle=FormStyleBulma)

    if ftypography0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftypography0, db.dftypography0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftypography0.form_name ))
    elif ftypography0.errors:
        print("ftypography0 has errors: %s" % (ftypography0.errors))
        return put_json_messages('error: ' + str( ftypography0.form_name ))
 

    ftypography1= Form(db.dftypography1, dbio=False, formstyle=FormStyleBulma)

    if ftypography1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftypography1, db.dftypography1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftypography1.form_name ))
    elif ftypography1.errors:
        print("ftypography1 has errors: %s" % (ftypography1.errors))
        return put_json_messages('error: ' + str( ftypography1.form_name ))
 

    return locals()

@action('dataXtable', method=["GET", "POST"] )
@action.uses(Template('data-table.html', delimiters='[%[ ]]',), db, session, T,)

def dataXtable():
    ctrl_info= "ctrl: dataXtable, view: data-table.html"
    page_url = "\'" + URL('dataXtable' ) + "\'"
    messages = []

    rows_tdataXtable0= db(db.tdataXtable0).select()
    fdataXtable0= Form(db.dfdataXtable0, dbio=False, formstyle=FormStyleBulma)

    if fdataXtable0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdataXtable0, db.dfdataXtable0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdataXtable0.form_name ))
    elif fdataXtable0.errors:
        print("fdataXtable0 has errors: %s" % (fdataXtable0.errors))
        return put_json_messages('error: ' + str( fdataXtable0.form_name ))
 

    fdataXtable1= Form(db.dfdataXtable1, dbio=False, formstyle=FormStyleBulma)

    if fdataXtable1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdataXtable1, db.dfdataXtable1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdataXtable1.form_name ))
    elif fdataXtable1.errors:
        print("fdataXtable1 has errors: %s" % (fdataXtable1.errors))
        return put_json_messages('error: ' + str( fdataXtable1.form_name ))
 

    return locals()

@action('googleXmap', method=["GET", "POST"] )
@action.uses(Template('google-map.html', delimiters='[%[ ]]',), db, session, T,)

def googleXmap():
    ctrl_info= "ctrl: googleXmap, view: google-map.html"
    page_url = "\'" + URL('googleXmap' ) + "\'"
    messages = []

    fgoogleXmap0= Form(db.dfgoogleXmap0, dbio=False, formstyle=FormStyleBulma)

    if fgoogleXmap0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fgoogleXmap0, db.dfgoogleXmap0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fgoogleXmap0.form_name ))
    elif fgoogleXmap0.errors:
        print("fgoogleXmap0 has errors: %s" % (fgoogleXmap0.errors))
        return put_json_messages('error: ' + str( fgoogleXmap0.form_name ))
 

    fgoogleXmap1= Form(db.dfgoogleXmap1, dbio=False, formstyle=FormStyleBulma)

    if fgoogleXmap1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fgoogleXmap1, db.dfgoogleXmap1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fgoogleXmap1.form_name ))
    elif fgoogleXmap1.errors:
        print("fgoogleXmap1 has errors: %s" % (fgoogleXmap1.errors))
        return put_json_messages('error: ' + str( fgoogleXmap1.form_name ))
 

    return locals()

@action('barXcharts', method=["GET", "POST"] )
@action.uses(Template('bar-charts.html', delimiters='[%[ ]]',), db, session, T,)

def barXcharts():
    ctrl_info= "ctrl: barXcharts, view: bar-charts.html"
    page_url = "\'" + URL('barXcharts' ) + "\'"
    messages = []

    fbarXcharts0= Form(db.dfbarXcharts0, dbio=False, formstyle=FormStyleBulma)

    if fbarXcharts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbarXcharts0, db.dfbarXcharts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbarXcharts0.form_name ))
    elif fbarXcharts0.errors:
        print("fbarXcharts0 has errors: %s" % (fbarXcharts0.errors))
        return put_json_messages('error: ' + str( fbarXcharts0.form_name ))
 

    fbarXcharts1= Form(db.dfbarXcharts1, dbio=False, formstyle=FormStyleBulma)

    if fbarXcharts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbarXcharts1, db.dfbarXcharts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbarXcharts1.form_name ))
    elif fbarXcharts1.errors:
        print("fbarXcharts1 has errors: %s" % (fbarXcharts1.errors))
        return put_json_messages('error: ' + str( fbarXcharts1.form_name ))
 

    return locals()

@action('animations', method=["GET", "POST"] )
@action.uses(Template('animations.html', delimiters='[%[ ]]',), db, session, T,)

def animations():
    ctrl_info= "ctrl: animations, view: animations.html"
    page_url = "\'" + URL('animations' ) + "\'"
    messages = []

    fanimations0= Form(db.dfanimations0, dbio=False, formstyle=FormStyleBulma)

    if fanimations0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fanimations0, db.dfanimations0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fanimations0.form_name ))
    elif fanimations0.errors:
        print("fanimations0 has errors: %s" % (fanimations0.errors))
        return put_json_messages('error: ' + str( fanimations0.form_name ))
 

    fanimations1= Form(db.dfanimations1, dbio=False, formstyle=FormStyleBulma)

    if fanimations1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fanimations1, db.dfanimations1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fanimations1.form_name ))
    elif fanimations1.errors:
        print("fanimations1 has errors: %s" % (fanimations1.errors))
        return put_json_messages('error: ' + str( fanimations1.form_name ))
 

    return locals()

@action('lineXcharts', method=["GET", "POST"] )
@action.uses(Template('line-charts.html', delimiters='[%[ ]]',), db, session, T,)

def lineXcharts():
    ctrl_info= "ctrl: lineXcharts, view: line-charts.html"
    page_url = "\'" + URL('lineXcharts' ) + "\'"
    messages = []

    flineXcharts0= Form(db.dflineXcharts0, dbio=False, formstyle=FormStyleBulma)

    if flineXcharts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flineXcharts0, db.dflineXcharts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flineXcharts0.form_name ))
    elif flineXcharts0.errors:
        print("flineXcharts0 has errors: %s" % (flineXcharts0.errors))
        return put_json_messages('error: ' + str( flineXcharts0.form_name ))
 

    flineXcharts1= Form(db.dflineXcharts1, dbio=False, formstyle=FormStyleBulma)

    if flineXcharts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flineXcharts1, db.dflineXcharts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flineXcharts1.form_name ))
    elif flineXcharts1.errors:
        print("flineXcharts1 has errors: %s" % (flineXcharts1.errors))
        return put_json_messages('error: ' + str( flineXcharts1.form_name ))
 

    return locals()

@action('areaXcharts', method=["GET", "POST"] )
@action.uses(Template('area-charts.html', delimiters='[%[ ]]',), db, session, T,)

def areaXcharts():
    ctrl_info= "ctrl: areaXcharts, view: area-charts.html"
    page_url = "\'" + URL('areaXcharts' ) + "\'"
    messages = []

    fareaXcharts0= Form(db.dfareaXcharts0, dbio=False, formstyle=FormStyleBulma)

    if fareaXcharts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fareaXcharts0, db.dfareaXcharts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fareaXcharts0.form_name ))
    elif fareaXcharts0.errors:
        print("fareaXcharts0 has errors: %s" % (fareaXcharts0.errors))
        return put_json_messages('error: ' + str( fareaXcharts0.form_name ))
 

    fareaXcharts1= Form(db.dfareaXcharts1, dbio=False, formstyle=FormStyleBulma)

    if fareaXcharts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fareaXcharts1, db.dfareaXcharts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fareaXcharts1.form_name ))
    elif fareaXcharts1.errors:
        print("fareaXcharts1 has errors: %s" % (fareaXcharts1.errors))
        return put_json_messages('error: ' + str( fareaXcharts1.form_name ))
 

    return locals()

@action('flotXcharts', method=["GET", "POST"] )
@action.uses(Template('flot-charts.html', delimiters='[%[ ]]',), db, session, T,)

def flotXcharts():
    ctrl_info= "ctrl: flotXcharts, view: flot-charts.html"
    page_url = "\'" + URL('flotXcharts' ) + "\'"
    messages = []

    fflotXcharts0= Form(db.dfflotXcharts0, dbio=False, formstyle=FormStyleBulma)

    if fflotXcharts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fflotXcharts0, db.dfflotXcharts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fflotXcharts0.form_name ))
    elif fflotXcharts0.errors:
        print("fflotXcharts0 has errors: %s" % (fflotXcharts0.errors))
        return put_json_messages('error: ' + str( fflotXcharts0.form_name ))
 

    fflotXcharts1= Form(db.dfflotXcharts1, dbio=False, formstyle=FormStyleBulma)

    if fflotXcharts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fflotXcharts1, db.dfflotXcharts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fflotXcharts1.form_name ))
    elif fflotXcharts1.errors:
        print("fflotXcharts1 has errors: %s" % (fflotXcharts1.errors))
        return put_json_messages('error: ' + str( fflotXcharts1.form_name ))
 

    return locals()

@action('codeXeditor', method=["GET", "POST"] )
@action.uses(Template('code-editor.html', delimiters='[%[ ]]',), db, session, T,)

def codeXeditor():
    ctrl_info= "ctrl: codeXeditor, view: code-editor.html"
    page_url = "\'" + URL('codeXeditor' ) + "\'"
    messages = []

    fcodeXeditor0= Form(db.dfcodeXeditor0, dbio=False, formstyle=FormStyleBulma)

    if fcodeXeditor0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcodeXeditor0, db.dfcodeXeditor0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcodeXeditor0.form_name ))
    elif fcodeXeditor0.errors:
        print("fcodeXeditor0 has errors: %s" % (fcodeXeditor0.errors))
        return put_json_messages('error: ' + str( fcodeXeditor0.form_name ))
 

    fcodeXeditor1= Form(db.dfcodeXeditor1, dbio=False, formstyle=FormStyleBulma)

    if fcodeXeditor1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcodeXeditor1, db.dfcodeXeditor1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcodeXeditor1.form_name ))
    elif fcodeXeditor1.errors:
        print("fcodeXeditor1 has errors: %s" % (fcodeXeditor1.errors))
        return put_json_messages('error: ' + str( fcodeXeditor1.form_name ))
 

    return locals()

@action('notification', method=["GET", "POST"] )
@action.uses(Template('notification.html', delimiters='[%[ ]]',), db, session, T,)

def notification():
    ctrl_info= "ctrl: notification, view: notification.html"
    page_url = "\'" + URL('notification' ) + "\'"
    messages = []

    fnotification0= Form(db.dfnotification0, dbio=False, formstyle=FormStyleBulma)

    if fnotification0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fnotification0, db.dfnotification0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fnotification0.form_name ))
    elif fnotification0.errors:
        print("fnotification0 has errors: %s" % (fnotification0.errors))
        return put_json_messages('error: ' + str( fnotification0.form_name ))
 

    fnotification1= Form(db.dfnotification1, dbio=False, formstyle=FormStyleBulma)

    if fnotification1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fnotification1, db.dfnotification1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fnotification1.form_name ))
    elif fnotification1.errors:
        print("fnotification1 has errors: %s" % (fnotification1.errors))
        return put_json_messages('error: ' + str( fnotification1.form_name ))
 

    return locals()

@action('normalXtable', method=["GET", "POST"] )
@action.uses(Template('normal-table.html', delimiters='[%[ ]]',), db, session, T,)

def normalXtable():
    ctrl_info= "ctrl: normalXtable, view: normal-table.html"
    page_url = "\'" + URL('normalXtable' ) + "\'"
    messages = []

    rows_tnormalXtable0= db(db.tnormalXtable0).select()
    rows_tnormalXtable1= db(db.tnormalXtable1).select()
    rows_tnormalXtable2= db(db.tnormalXtable2).select()
    rows_tnormalXtable3= db(db.tnormalXtable3).select()
    rows_tnormalXtable4= db(db.tnormalXtable4).select()
    rows_tnormalXtable5= db(db.tnormalXtable5).select()
    fnormalXtable0= Form(db.dfnormalXtable0, dbio=False, formstyle=FormStyleBulma)

    if fnormalXtable0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fnormalXtable0, db.dfnormalXtable0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fnormalXtable0.form_name ))
    elif fnormalXtable0.errors:
        print("fnormalXtable0 has errors: %s" % (fnormalXtable0.errors))
        return put_json_messages('error: ' + str( fnormalXtable0.form_name ))
 

    fnormalXtable1= Form(db.dfnormalXtable1, dbio=False, formstyle=FormStyleBulma)

    if fnormalXtable1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fnormalXtable1, db.dfnormalXtable1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fnormalXtable1.form_name ))
    elif fnormalXtable1.errors:
        print("fnormalXtable1 has errors: %s" % (fnormalXtable1.errors))
        return put_json_messages('error: ' + str( fnormalXtable1.form_name ))
 

    return locals()

@action('composeXemail', method=["GET", "POST"] )
@action.uses(Template('compose-email.html', delimiters='[%[ ]]',), db, session, T,)

def composeXemail():
    ctrl_info= "ctrl: composeXemail, view: compose-email.html"
    page_url = "\'" + URL('composeXemail' ) + "\'"
    messages = []

    fcomposeXemail0= Form(db.dfcomposeXemail0, dbio=False, formstyle=FormStyleBulma)

    if fcomposeXemail0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcomposeXemail0, db.dfcomposeXemail0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcomposeXemail0.form_name ))
    elif fcomposeXemail0.errors:
        print("fcomposeXemail0 has errors: %s" % (fcomposeXemail0.errors))
        return put_json_messages('error: ' + str( fcomposeXemail0.form_name ))
 

    return locals()

@action('imageXcropper', method=["GET", "POST"] )
@action.uses(Template('image-cropper.html', delimiters='[%[ ]]',), db, session, T,)

def imageXcropper():
    ctrl_info= "ctrl: imageXcropper, view: image-cropper.html"
    page_url = "\'" + URL('imageXcropper' ) + "\'"
    messages = []

    fimageXcropper0= Form(db.dfimageXcropper0, dbio=False, formstyle=FormStyleBulma)

    if fimageXcropper0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fimageXcropper0, db.dfimageXcropper0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fimageXcropper0.form_name ))
    elif fimageXcropper0.errors:
        print("fimageXcropper0 has errors: %s" % (fimageXcropper0.errors))
        return put_json_messages('error: ' + str( fimageXcropper0.form_name ))
 

    fimageXcropper1= Form(db.dfimageXcropper1, dbio=False, formstyle=FormStyleBulma)

    if fimageXcropper1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fimageXcropper1, db.dfimageXcropper1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fimageXcropper1.form_name ))
    elif fimageXcropper1.errors:
        print("fimageXcropper1 has errors: %s" % (fimageXcropper1.errors))
        return put_json_messages('error: ' + str( fimageXcropper1.form_name ))
 

    return locals()

@action('formXexamples', method=["GET", "POST"] )
@action.uses(Template('form-examples.html', delimiters='[%[ ]]',), db, session, T,)

def formXexamples():
    ctrl_info= "ctrl: formXexamples, view: form-examples.html"
    page_url = "\'" + URL('formXexamples' ) + "\'"
    messages = []

    fformXexamples0= Form(db.dfformXexamples0, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples0, db.dfformXexamples0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples0.form_name ))
    elif fformXexamples0.errors:
        print("fformXexamples0 has errors: %s" % (fformXexamples0.errors))
        return put_json_messages('error: ' + str( fformXexamples0.form_name ))
 

    fformXexamples1= Form(db.dfformXexamples1, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples1, db.dfformXexamples1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples1.form_name ))
    elif fformXexamples1.errors:
        print("fformXexamples1 has errors: %s" % (fformXexamples1.errors))
        return put_json_messages('error: ' + str( fformXexamples1.form_name ))
 

    fformXexamples2= Form(db.dfformXexamples2, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples2, db.dfformXexamples2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples2.form_name ))
    elif fformXexamples2.errors:
        print("fformXexamples2 has errors: %s" % (fformXexamples2.errors))
        return put_json_messages('error: ' + str( fformXexamples2.form_name ))
 

    fformXexamples3= Form(db.dfformXexamples3, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples3, db.dfformXexamples3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples3.form_name ))
    elif fformXexamples3.errors:
        print("fformXexamples3 has errors: %s" % (fformXexamples3.errors))
        return put_json_messages('error: ' + str( fformXexamples3.form_name ))
 

    fformXexamples4= Form(db.dfformXexamples4, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples4, db.dfformXexamples4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples4.form_name ))
    elif fformXexamples4.errors:
        print("fformXexamples4 has errors: %s" % (fformXexamples4.errors))
        return put_json_messages('error: ' + str( fformXexamples4.form_name ))
 

    fformXexamples5= Form(db.dfformXexamples5, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples5, db.dfformXexamples5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples5.form_name ))
    elif fformXexamples5.errors:
        print("fformXexamples5 has errors: %s" % (fformXexamples5.errors))
        return put_json_messages('error: ' + str( fformXexamples5.form_name ))
 

    fformXexamples6= Form(db.dfformXexamples6, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples6, db.dfformXexamples6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples6.form_name ))
    elif fformXexamples6.errors:
        print("fformXexamples6 has errors: %s" % (fformXexamples6.errors))
        return put_json_messages('error: ' + str( fformXexamples6.form_name ))
 

    fformXexamples7= Form(db.dfformXexamples7, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples7, db.dfformXexamples7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples7.form_name ))
    elif fformXexamples7.errors:
        print("fformXexamples7 has errors: %s" % (fformXexamples7.errors))
        return put_json_messages('error: ' + str( fformXexamples7.form_name ))
 

    fformXexamples8= Form(db.dfformXexamples8, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples8, db.dfformXexamples8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples8.form_name ))
    elif fformXexamples8.errors:
        print("fformXexamples8 has errors: %s" % (fformXexamples8.errors))
        return put_json_messages('error: ' + str( fformXexamples8.form_name ))
 

    fformXexamples9= Form(db.dfformXexamples9, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples9, db.dfformXexamples9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples9.form_name ))
    elif fformXexamples9.errors:
        print("fformXexamples9 has errors: %s" % (fformXexamples9.errors))
        return put_json_messages('error: ' + str( fformXexamples9.form_name ))
 

    fformXexamples10= Form(db.dfformXexamples10, dbio=False, formstyle=FormStyleBulma)

    if fformXexamples10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXexamples10, db.dfformXexamples10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXexamples10.form_name ))
    elif fformXexamples10.errors:
        print("fformXexamples10 has errors: %s" % (fformXexamples10.errors))
        return put_json_messages('error: ' + str( fformXexamples10.form_name ))
 

    return locals()

@action('formXelements', method=["GET", "POST"] )
@action.uses(Template('form-elements.html', delimiters='[%[ ]]',), db, session, T,)

def formXelements():
    ctrl_info= "ctrl: formXelements, view: form-elements.html"
    page_url = "\'" + URL('formXelements' ) + "\'"
    messages = []

    fformXelements0= Form(db.dfformXelements0, dbio=False, formstyle=FormStyleBulma)

    if fformXelements0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements0, db.dfformXelements0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements0.form_name ))
    elif fformXelements0.errors:
        print("fformXelements0 has errors: %s" % (fformXelements0.errors))
        return put_json_messages('error: ' + str( fformXelements0.form_name ))
 

    fformXelements1= Form(db.dfformXelements1, dbio=False, formstyle=FormStyleBulma)

    if fformXelements1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements1, db.dfformXelements1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements1.form_name ))
    elif fformXelements1.errors:
        print("fformXelements1 has errors: %s" % (fformXelements1.errors))
        return put_json_messages('error: ' + str( fformXelements1.form_name ))
 

    fformXelements2= Form(db.dfformXelements2, dbio=False, formstyle=FormStyleBulma)

    if fformXelements2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements2, db.dfformXelements2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements2.form_name ))
    elif fformXelements2.errors:
        print("fformXelements2 has errors: %s" % (fformXelements2.errors))
        return put_json_messages('error: ' + str( fformXelements2.form_name ))
 

    fformXelements3= Form(db.dfformXelements3, dbio=False, formstyle=FormStyleBulma)

    if fformXelements3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements3, db.dfformXelements3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements3.form_name ))
    elif fformXelements3.errors:
        print("fformXelements3 has errors: %s" % (fformXelements3.errors))
        return put_json_messages('error: ' + str( fformXelements3.form_name ))
 

    fformXelements4= Form(db.dfformXelements4, dbio=False, formstyle=FormStyleBulma)

    if fformXelements4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements4, db.dfformXelements4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements4.form_name ))
    elif fformXelements4.errors:
        print("fformXelements4 has errors: %s" % (fformXelements4.errors))
        return put_json_messages('error: ' + str( fformXelements4.form_name ))
 

    fformXelements5= Form(db.dfformXelements5, dbio=False, formstyle=FormStyleBulma)

    if fformXelements5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements5, db.dfformXelements5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements5.form_name ))
    elif fformXelements5.errors:
        print("fformXelements5 has errors: %s" % (fformXelements5.errors))
        return put_json_messages('error: ' + str( fformXelements5.form_name ))
 

    fformXelements6= Form(db.dfformXelements6, dbio=False, formstyle=FormStyleBulma)

    if fformXelements6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements6, db.dfformXelements6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements6.form_name ))
    elif fformXelements6.errors:
        print("fformXelements6 has errors: %s" % (fformXelements6.errors))
        return put_json_messages('error: ' + str( fformXelements6.form_name ))
 

    fformXelements7= Form(db.dfformXelements7, dbio=False, formstyle=FormStyleBulma)

    if fformXelements7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements7, db.dfformXelements7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements7.form_name ))
    elif fformXelements7.errors:
        print("fformXelements7 has errors: %s" % (fformXelements7.errors))
        return put_json_messages('error: ' + str( fformXelements7.form_name ))
 

    fformXelements8= Form(db.dfformXelements8, dbio=False, formstyle=FormStyleBulma)

    if fformXelements8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements8, db.dfformXelements8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements8.form_name ))
    elif fformXelements8.errors:
        print("fformXelements8 has errors: %s" % (fformXelements8.errors))
        return put_json_messages('error: ' + str( fformXelements8.form_name ))
 

    fformXelements9= Form(db.dfformXelements9, dbio=False, formstyle=FormStyleBulma)

    if fformXelements9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements9, db.dfformXelements9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements9.form_name ))
    elif fformXelements9.errors:
        print("fformXelements9 has errors: %s" % (fformXelements9.errors))
        return put_json_messages('error: ' + str( fformXelements9.form_name ))
 

    fformXelements10= Form(db.dfformXelements10, dbio=False, formstyle=FormStyleBulma)

    if fformXelements10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements10, db.dfformXelements10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements10.form_name ))
    elif fformXelements10.errors:
        print("fformXelements10 has errors: %s" % (fformXelements10.errors))
        return put_json_messages('error: ' + str( fformXelements10.form_name ))
 

    fformXelements11= Form(db.dfformXelements11, dbio=False, formstyle=FormStyleBulma)

    if fformXelements11.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements11, db.dfformXelements11 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements11.form_name ))
    elif fformXelements11.errors:
        print("fformXelements11 has errors: %s" % (fformXelements11.errors))
        return put_json_messages('error: ' + str( fformXelements11.form_name ))
 

    fformXelements12= Form(db.dfformXelements12, dbio=False, formstyle=FormStyleBulma)

    if fformXelements12.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements12, db.dfformXelements12 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements12.form_name ))
    elif fformXelements12.errors:
        print("fformXelements12 has errors: %s" % (fformXelements12.errors))
        return put_json_messages('error: ' + str( fformXelements12.form_name ))
 

    fformXelements13= Form(db.dfformXelements13, dbio=False, formstyle=FormStyleBulma)

    if fformXelements13.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements13, db.dfformXelements13 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements13.form_name ))
    elif fformXelements13.errors:
        print("fformXelements13 has errors: %s" % (fformXelements13.errors))
        return put_json_messages('error: ' + str( fformXelements13.form_name ))
 

    fformXelements14= Form(db.dfformXelements14, dbio=False, formstyle=FormStyleBulma)

    if fformXelements14.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements14, db.dfformXelements14 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements14.form_name ))
    elif fformXelements14.errors:
        print("fformXelements14 has errors: %s" % (fformXelements14.errors))
        return put_json_messages('error: ' + str( fformXelements14.form_name ))
 

    fformXelements15= Form(db.dfformXelements15, dbio=False, formstyle=FormStyleBulma)

    if fformXelements15.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements15, db.dfformXelements15 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements15.form_name ))
    elif fformXelements15.errors:
        print("fformXelements15 has errors: %s" % (fformXelements15.errors))
        return put_json_messages('error: ' + str( fformXelements15.form_name ))
 

    fformXelements16= Form(db.dfformXelements16, dbio=False, formstyle=FormStyleBulma)

    if fformXelements16.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements16, db.dfformXelements16 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements16.form_name ))
    elif fformXelements16.errors:
        print("fformXelements16 has errors: %s" % (fformXelements16.errors))
        return put_json_messages('error: ' + str( fformXelements16.form_name ))
 

    fformXelements17= Form(db.dfformXelements17, dbio=False, formstyle=FormStyleBulma)

    if fformXelements17.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements17, db.dfformXelements17 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements17.form_name ))
    elif fformXelements17.errors:
        print("fformXelements17 has errors: %s" % (fformXelements17.errors))
        return put_json_messages('error: ' + str( fformXelements17.form_name ))
 

    fformXelements18= Form(db.dfformXelements18, dbio=False, formstyle=FormStyleBulma)

    if fformXelements18.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements18, db.dfformXelements18 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements18.form_name ))
    elif fformXelements18.errors:
        print("fformXelements18 has errors: %s" % (fformXelements18.errors))
        return put_json_messages('error: ' + str( fformXelements18.form_name ))
 

    fformXelements19= Form(db.dfformXelements19, dbio=False, formstyle=FormStyleBulma)

    if fformXelements19.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements19, db.dfformXelements19 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements19.form_name ))
    elif fformXelements19.errors:
        print("fformXelements19 has errors: %s" % (fformXelements19.errors))
        return put_json_messages('error: ' + str( fformXelements19.form_name ))
 

    fformXelements20= Form(db.dfformXelements20, dbio=False, formstyle=FormStyleBulma)

    if fformXelements20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements20, db.dfformXelements20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements20.form_name ))
    elif fformXelements20.errors:
        print("fformXelements20 has errors: %s" % (fformXelements20.errors))
        return put_json_messages('error: ' + str( fformXelements20.form_name ))
 

    fformXelements21= Form(db.dfformXelements21, dbio=False, formstyle=FormStyleBulma)

    if fformXelements21.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements21, db.dfformXelements21 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements21.form_name ))
    elif fformXelements21.errors:
        print("fformXelements21 has errors: %s" % (fformXelements21.errors))
        return put_json_messages('error: ' + str( fformXelements21.form_name ))
 

    fformXelements22= Form(db.dfformXelements22, dbio=False, formstyle=FormStyleBulma)

    if fformXelements22.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements22, db.dfformXelements22 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements22.form_name ))
    elif fformXelements22.errors:
        print("fformXelements22 has errors: %s" % (fformXelements22.errors))
        return put_json_messages('error: ' + str( fformXelements22.form_name ))
 

    fformXelements23= Form(db.dfformXelements23, dbio=False, formstyle=FormStyleBulma)

    if fformXelements23.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements23, db.dfformXelements23 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements23.form_name ))
    elif fformXelements23.errors:
        print("fformXelements23 has errors: %s" % (fformXelements23.errors))
        return put_json_messages('error: ' + str( fformXelements23.form_name ))
 

    fformXelements24= Form(db.dfformXelements24, dbio=False, formstyle=FormStyleBulma)

    if fformXelements24.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements24, db.dfformXelements24 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements24.form_name ))
    elif fformXelements24.errors:
        print("fformXelements24 has errors: %s" % (fformXelements24.errors))
        return put_json_messages('error: ' + str( fformXelements24.form_name ))
 

    fformXelements25= Form(db.dfformXelements25, dbio=False, formstyle=FormStyleBulma)

    if fformXelements25.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements25, db.dfformXelements25 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements25.form_name ))
    elif fformXelements25.errors:
        print("fformXelements25 has errors: %s" % (fformXelements25.errors))
        return put_json_messages('error: ' + str( fformXelements25.form_name ))
 

    fformXelements26= Form(db.dfformXelements26, dbio=False, formstyle=FormStyleBulma)

    if fformXelements26.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements26, db.dfformXelements26 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements26.form_name ))
    elif fformXelements26.errors:
        print("fformXelements26 has errors: %s" % (fformXelements26.errors))
        return put_json_messages('error: ' + str( fformXelements26.form_name ))
 

    fformXelements27= Form(db.dfformXelements27, dbio=False, formstyle=FormStyleBulma)

    if fformXelements27.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXelements27, db.dfformXelements27 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXelements27.form_name ))
    elif fformXelements27.errors:
        print("fformXelements27 has errors: %s" % (fformXelements27.errors))
        return put_json_messages('error: ' + str( fformXelements27.form_name ))
 

    return locals()

@action('loginXregister', method=["GET", "POST"] )
@action.uses(Template('login-register.html', delimiters='[%[ ]]',), db, session, T,)

def loginXregister():
    ctrl_info= "ctrl: loginXregister, view: login-register.html"
    page_url = "\'" + URL('loginXregister' ) + "\'"
    messages = []

    floginXregister0= Form(db.dfloginXregister0, dbio=False, formstyle=FormStyleBulma)

    if floginXregister0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister0, db.dfloginXregister0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister0.form_name ))
    elif floginXregister0.errors:
        print("floginXregister0 has errors: %s" % (floginXregister0.errors))
        return put_json_messages('error: ' + str( floginXregister0.form_name ))
 

    floginXregister1= Form(db.dfloginXregister1, dbio=False, formstyle=FormStyleBulma)

    if floginXregister1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister1, db.dfloginXregister1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister1.form_name ))
    elif floginXregister1.errors:
        print("floginXregister1 has errors: %s" % (floginXregister1.errors))
        return put_json_messages('error: ' + str( floginXregister1.form_name ))
 

    floginXregister2= Form(db.dfloginXregister2, dbio=False, formstyle=FormStyleBulma)

    if floginXregister2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister2, db.dfloginXregister2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister2.form_name ))
    elif floginXregister2.errors:
        print("floginXregister2 has errors: %s" % (floginXregister2.errors))
        return put_json_messages('error: ' + str( floginXregister2.form_name ))
 

    floginXregister3= Form(db.dfloginXregister3, dbio=False, formstyle=FormStyleBulma)

    if floginXregister3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister3, db.dfloginXregister3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister3.form_name ))
    elif floginXregister3.errors:
        print("floginXregister3 has errors: %s" % (floginXregister3.errors))
        return put_json_messages('error: ' + str( floginXregister3.form_name ))
 

    floginXregister4= Form(db.dfloginXregister4, dbio=False, formstyle=FormStyleBulma)

    if floginXregister4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister4, db.dfloginXregister4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister4.form_name ))
    elif floginXregister4.errors:
        print("floginXregister4 has errors: %s" % (floginXregister4.errors))
        return put_json_messages('error: ' + str( floginXregister4.form_name ))
 

    floginXregister5= Form(db.dfloginXregister5, dbio=False, formstyle=FormStyleBulma)

    if floginXregister5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister5, db.dfloginXregister5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister5.form_name ))
    elif floginXregister5.errors:
        print("floginXregister5 has errors: %s" % (floginXregister5.errors))
        return put_json_messages('error: ' + str( floginXregister5.form_name ))
 

    floginXregister6= Form(db.dfloginXregister6, dbio=False, formstyle=FormStyleBulma)

    if floginXregister6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( floginXregister6, db.dfloginXregister6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( floginXregister6.form_name ))
    elif floginXregister6.errors:
        print("floginXregister6 has errors: %s" % (floginXregister6.errors))
        return put_json_messages('error: ' + str( floginXregister6.form_name ))
 

    return locals()

@action('formXcomponents', method=["GET", "POST"] )
@action.uses(Template('form-components.html', delimiters='[%[ ]]',), db, session, T,)

def formXcomponents():
    ctrl_info= "ctrl: formXcomponents, view: form-components.html"
    page_url = "\'" + URL('formXcomponents' ) + "\'"
    messages = []

    fformXcomponents0= Form(db.dfformXcomponents0, dbio=False, formstyle=FormStyleBulma)

    if fformXcomponents0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformXcomponents0, db.dfformXcomponents0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformXcomponents0.form_name ))
    elif fformXcomponents0.errors:
        print("fformXcomponents0 has errors: %s" % (fformXcomponents0.errors))
        return put_json_messages('error: ' + str( fformXcomponents0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/notika/api/test_table/
# curl -X  GET   http://localhost:8000/notika/api/test_table/9
# curl -X DELETE  http://localhost:8000/notika/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/notika/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/notika/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/notika/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/notika/api/test_table/
#  http         localhost:8000/notika/api/test_table/9
#  http -f POST localhost:8000/notika/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/notika/api/test_table/2
#  http -f PUT localhost:8000/notika/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

