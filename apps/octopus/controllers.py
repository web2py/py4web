#
# py4web app, AI-biorex ported 01.12.2020 12:03:27 UTC+3
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
 

    return locals()

@action('pagesX500', method=["GET", "POST"] )
@action.uses(Template('pages-500.html', delimiters='[%[ ]]',), db, session, T,)

def pagesX500():
    ctrl_info= "ctrl: pagesX500, view: pages-500.html"
    page_url = "\'" + URL('pagesX500' ) + "\'"
    messages = []

    return locals()

@action('pagesX404', method=["GET", "POST"] )
@action.uses(Template('pages-404.html', delimiters='[%[ ]]',), db, session, T,)

def pagesX404():
    ctrl_info= "ctrl: pagesX404, view: pages-404.html"
    page_url = "\'" + URL('pagesX404' ) + "\'"
    messages = []

    fpagesX4040= Form(db.dfpagesX4040, dbio=False, formstyle=FormStyleBulma)

    if fpagesX4040.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesX4040, db.dfpagesX4040 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesX4040.form_name ))
    elif fpagesX4040.errors:
        print("fpagesX4040 has errors: %s" % (fpagesX4040.errors))
        return put_json_messages('error: ' + str( fpagesX4040.form_name ))
 

    return locals()

@action('mapsXvector', method=["GET", "POST"] )
@action.uses(Template('maps-vector.html', delimiters='[%[ ]]',), db, session, T,)

def mapsXvector():
    ctrl_info= "ctrl: mapsXvector, view: maps-vector.html"
    page_url = "\'" + URL('mapsXvector' ) + "\'"
    messages = []

    fmapsXvector0= Form(db.dfmapsXvector0, dbio=False, formstyle=FormStyleBulma)

    if fmapsXvector0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmapsXvector0, db.dfmapsXvector0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmapsXvector0.form_name ))
    elif fmapsXvector0.errors:
        print("fmapsXvector0 has errors: %s" % (fmapsXvector0.errors))
        return put_json_messages('error: ' + str( fmapsXvector0.form_name ))
 

    return locals()

@action('formsXbasic', method=["GET", "POST"] )
@action.uses(Template('forms-basic.html', delimiters='[%[ ]]',), db, session, T,)

def formsXbasic():
    ctrl_info= "ctrl: formsXbasic, view: forms-basic.html"
    page_url = "\'" + URL('formsXbasic' ) + "\'"
    messages = []

    fformsXbasic0= Form(db.dfformsXbasic0, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic0, db.dfformsXbasic0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic0.form_name ))
    elif fformsXbasic0.errors:
        print("fformsXbasic0 has errors: %s" % (fformsXbasic0.errors))
        return put_json_messages('error: ' + str( fformsXbasic0.form_name ))
 

    fformsXbasic1= Form(db.dfformsXbasic1, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic1, db.dfformsXbasic1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic1.form_name ))
    elif fformsXbasic1.errors:
        print("fformsXbasic1 has errors: %s" % (fformsXbasic1.errors))
        return put_json_messages('error: ' + str( fformsXbasic1.form_name ))
 

    fformsXbasic2= Form(db.dfformsXbasic2, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic2, db.dfformsXbasic2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic2.form_name ))
    elif fformsXbasic2.errors:
        print("fformsXbasic2 has errors: %s" % (fformsXbasic2.errors))
        return put_json_messages('error: ' + str( fformsXbasic2.form_name ))
 

    fformsXbasic3= Form(db.dfformsXbasic3, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic3, db.dfformsXbasic3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic3.form_name ))
    elif fformsXbasic3.errors:
        print("fformsXbasic3 has errors: %s" % (fformsXbasic3.errors))
        return put_json_messages('error: ' + str( fformsXbasic3.form_name ))
 

    fformsXbasic4= Form(db.dfformsXbasic4, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic4, db.dfformsXbasic4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic4.form_name ))
    elif fformsXbasic4.errors:
        print("fformsXbasic4 has errors: %s" % (fformsXbasic4.errors))
        return put_json_messages('error: ' + str( fformsXbasic4.form_name ))
 

    fformsXbasic5= Form(db.dfformsXbasic5, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic5, db.dfformsXbasic5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic5.form_name ))
    elif fformsXbasic5.errors:
        print("fformsXbasic5 has errors: %s" % (fformsXbasic5.errors))
        return put_json_messages('error: ' + str( fformsXbasic5.form_name ))
 

    fformsXbasic6= Form(db.dfformsXbasic6, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic6, db.dfformsXbasic6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic6.form_name ))
    elif fformsXbasic6.errors:
        print("fformsXbasic6 has errors: %s" % (fformsXbasic6.errors))
        return put_json_messages('error: ' + str( fformsXbasic6.form_name ))
 

    fformsXbasic7= Form(db.dfformsXbasic7, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasic7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasic7, db.dfformsXbasic7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasic7.form_name ))
    elif fformsXbasic7.errors:
        print("fformsXbasic7 has errors: %s" % (fformsXbasic7.errors))
        return put_json_messages('error: ' + str( fformsXbasic7.form_name ))
 

    return locals()

@action('pagesXblank', method=["GET", "POST"] )
@action.uses(Template('pages-blank.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXblank():
    ctrl_info= "ctrl: pagesXblank, view: pages-blank.html"
    page_url = "\'" + URL('pagesXblank' ) + "\'"
    messages = []

    fpagesXblank0= Form(db.dfpagesXblank0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXblank0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXblank0, db.dfpagesXblank0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXblank0.form_name ))
    elif fpagesXblank0.errors:
        print("fpagesXblank0 has errors: %s" % (fpagesXblank0.errors))
        return put_json_messages('error: ' + str( fpagesXblank0.form_name ))
 

    return locals()

@action('tablesXajax', method=["GET", "POST"] )
@action.uses(Template('tables-ajax.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXajax():
    ctrl_info= "ctrl: tablesXajax, view: tables-ajax.html"
    page_url = "\'" + URL('tablesXajax' ) + "\'"
    messages = []

    rows_ttablesXajax0= db(db.ttablesXajax0).select()
    ftablesXajax0= Form(db.dftablesXajax0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXajax0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXajax0, db.dftablesXajax0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXajax0.form_name ))
    elif ftablesXajax0.errors:
        print("ftablesXajax0 has errors: %s" % (ftablesXajax0.errors))
        return put_json_messages('error: ' + str( ftablesXajax0.form_name ))
 

    return locals()

@action('pagesXsignin', method=["GET", "POST"] )
@action.uses(Template('pages-signin.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsignin():
    ctrl_info= "ctrl: pagesXsignin, view: pages-signin.html"
    page_url = "\'" + URL('pagesXsignin' ) + "\'"
    messages = []

    fpagesXsignin0= Form(db.dfpagesXsignin0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsignin0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsignin0, db.dfpagesXsignin0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsignin0.form_name ))
    elif fpagesXsignin0.errors:
        print("fpagesXsignin0 has errors: %s" % (fpagesXsignin0.errors))
        return put_json_messages('error: ' + str( fpagesXsignin0.form_name ))
 

    return locals()

@action('pagesXsignup', method=["GET", "POST"] )
@action.uses(Template('pages-signup.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsignup():
    ctrl_info= "ctrl: pagesXsignup, view: pages-signup.html"
    page_url = "\'" + URL('pagesXsignup' ) + "\'"
    messages = []

    fpagesXsignup0= Form(db.dfpagesXsignup0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsignup0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsignup0, db.dfpagesXsignup0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsignup0.form_name ))
    elif fpagesXsignup0.errors:
        print("fpagesXsignup0 has errors: %s" % (fpagesXsignup0.errors))
        return put_json_messages('error: ' + str( fpagesXsignup0.form_name ))
 

    return locals()

@action('tablesXbasic', method=["GET", "POST"] )
@action.uses(Template('tables-basic.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXbasic():
    ctrl_info= "ctrl: tablesXbasic, view: tables-basic.html"
    page_url = "\'" + URL('tablesXbasic' ) + "\'"
    messages = []

    rows_ttablesXbasic0= db(db.ttablesXbasic0).select()
    rows_ttablesXbasic1= db(db.ttablesXbasic1).select()
    rows_ttablesXbasic2= db(db.ttablesXbasic2).select()
    rows_ttablesXbasic3= db(db.ttablesXbasic3).select()
    rows_ttablesXbasic4= db(db.ttablesXbasic4).select()
    rows_ttablesXbasic5= db(db.ttablesXbasic5).select()
    rows_ttablesXbasic6= db(db.ttablesXbasic6).select()
    rows_ttablesXbasic7= db(db.ttablesXbasic7).select()
    rows_ttablesXbasic8= db(db.ttablesXbasic8).select()
    rows_ttablesXbasic9= db(db.ttablesXbasic9).select()
    ftablesXbasic0= Form(db.dftablesXbasic0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXbasic0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXbasic0, db.dftablesXbasic0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXbasic0.form_name ))
    elif ftablesXbasic0.errors:
        print("ftablesXbasic0 has errors: %s" % (ftablesXbasic0.errors))
        return put_json_messages('error: ' + str( ftablesXbasic0.form_name ))
 

    return locals()

@action('formsXwizard', method=["GET", "POST"] )
@action.uses(Template('forms-wizard.html', delimiters='[%[ ]]',), db, session, T,)

def formsXwizard():
    ctrl_info= "ctrl: formsXwizard, view: forms-wizard.html"
    page_url = "\'" + URL('formsXwizard' ) + "\'"
    messages = []

    fformsXwizard0= Form(db.dfformsXwizard0, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard0, db.dfformsXwizard0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard0.form_name ))
    elif fformsXwizard0.errors:
        print("fformsXwizard0 has errors: %s" % (fformsXwizard0.errors))
        return put_json_messages('error: ' + str( fformsXwizard0.form_name ))
 

    fformsXwizard1= Form(db.dfformsXwizard1, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard1, db.dfformsXwizard1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard1.form_name ))
    elif fformsXwizard1.errors:
        print("fformsXwizard1 has errors: %s" % (fformsXwizard1.errors))
        return put_json_messages('error: ' + str( fformsXwizard1.form_name ))
 

    fformsXwizard2= Form(db.dfformsXwizard2, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard2, db.dfformsXwizard2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard2.form_name ))
    elif fformsXwizard2.errors:
        print("fformsXwizard2 has errors: %s" % (fformsXwizard2.errors))
        return put_json_messages('error: ' + str( fformsXwizard2.form_name ))
 

    fformsXwizard3= Form(db.dfformsXwizard3, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard3, db.dfformsXwizard3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard3.form_name ))
    elif fformsXwizard3.errors:
        print("fformsXwizard3 has errors: %s" % (fformsXwizard3.errors))
        return put_json_messages('error: ' + str( fformsXwizard3.form_name ))
 

    fformsXwizard4= Form(db.dfformsXwizard4, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard4, db.dfformsXwizard4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard4.form_name ))
    elif fformsXwizard4.errors:
        print("fformsXwizard4 has errors: %s" % (fformsXwizard4.errors))
        return put_json_messages('error: ' + str( fformsXwizard4.form_name ))
 

    fformsXwizard5= Form(db.dfformsXwizard5, dbio=False, formstyle=FormStyleBulma)

    if fformsXwizard5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXwizard5, db.dfformsXwizard5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXwizard5.form_name ))
    elif fformsXwizard5.errors:
        print("fformsXwizard5 has errors: %s" % (fformsXwizard5.errors))
        return put_json_messages('error: ' + str( fformsXwizard5.form_name ))
 

    return locals()

@action('layoutsXboxed', method=["GET", "POST"] )
@action.uses(Template('layouts-boxed.html', delimiters='[%[ ]]',), db, session, T,)

def layoutsXboxed():
    ctrl_info= "ctrl: layoutsXboxed, view: layouts-boxed.html"
    page_url = "\'" + URL('layoutsXboxed' ) + "\'"
    messages = []

    flayoutsXboxed0= Form(db.dflayoutsXboxed0, dbio=False, formstyle=FormStyleBulma)

    if flayoutsXboxed0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flayoutsXboxed0, db.dflayoutsXboxed0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flayoutsXboxed0.form_name ))
    elif flayoutsXboxed0.errors:
        print("flayoutsXboxed0 has errors: %s" % (flayoutsXboxed0.errors))
        return put_json_messages('error: ' + str( flayoutsXboxed0.form_name ))
 

    return locals()

@action('formsXlayouts', method=["GET", "POST"] )
@action.uses(Template('forms-layouts.html', delimiters='[%[ ]]',), db, session, T,)

def formsXlayouts():
    ctrl_info= "ctrl: formsXlayouts, view: forms-layouts.html"
    page_url = "\'" + URL('formsXlayouts' ) + "\'"
    messages = []

    fformsXlayouts0= Form(db.dfformsXlayouts0, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts0, db.dfformsXlayouts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts0.form_name ))
    elif fformsXlayouts0.errors:
        print("fformsXlayouts0 has errors: %s" % (fformsXlayouts0.errors))
        return put_json_messages('error: ' + str( fformsXlayouts0.form_name ))
 

    fformsXlayouts1= Form(db.dfformsXlayouts1, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts1, db.dfformsXlayouts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts1.form_name ))
    elif fformsXlayouts1.errors:
        print("fformsXlayouts1 has errors: %s" % (fformsXlayouts1.errors))
        return put_json_messages('error: ' + str( fformsXlayouts1.form_name ))
 

    fformsXlayouts2= Form(db.dfformsXlayouts2, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts2, db.dfformsXlayouts2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts2.form_name ))
    elif fformsXlayouts2.errors:
        print("fformsXlayouts2 has errors: %s" % (fformsXlayouts2.errors))
        return put_json_messages('error: ' + str( fformsXlayouts2.form_name ))
 

    fformsXlayouts3= Form(db.dfformsXlayouts3, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts3, db.dfformsXlayouts3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts3.form_name ))
    elif fformsXlayouts3.errors:
        print("fformsXlayouts3 has errors: %s" % (fformsXlayouts3.errors))
        return put_json_messages('error: ' + str( fformsXlayouts3.form_name ))
 

    fformsXlayouts4= Form(db.dfformsXlayouts4, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts4, db.dfformsXlayouts4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts4.form_name ))
    elif fformsXlayouts4.errors:
        print("fformsXlayouts4 has errors: %s" % (fformsXlayouts4.errors))
        return put_json_messages('error: ' + str( fformsXlayouts4.form_name ))
 

    return locals()

@action('pagesXinvoice', method=["GET", "POST"] )
@action.uses(Template('pages-invoice.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXinvoice():
    ctrl_info= "ctrl: pagesXinvoice, view: pages-invoice.html"
    page_url = "\'" + URL('pagesXinvoice' ) + "\'"
    messages = []

    rows_tpagesXinvoice0= db(db.tpagesXinvoice0).select()
    rows_tpagesXinvoice1= db(db.tpagesXinvoice1).select()
    fpagesXinvoice0= Form(db.dfpagesXinvoice0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXinvoice0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXinvoice0, db.dfpagesXinvoice0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXinvoice0.form_name ))
    elif fpagesXinvoice0.errors:
        print("fpagesXinvoice0 has errors: %s" % (fpagesXinvoice0.errors))
        return put_json_messages('error: ' + str( fpagesXinvoice0.form_name ))
 

    return locals()

@action('mailboxXemail', method=["GET", "POST"] )
@action.uses(Template('mailbox-email.html', delimiters='[%[ ]]',), db, session, T,)

def mailboxXemail():
    ctrl_info= "ctrl: mailboxXemail, view: mailbox-email.html"
    page_url = "\'" + URL('mailboxXemail' ) + "\'"
    messages = []

    fmailboxXemail0= Form(db.dfmailboxXemail0, dbio=False, formstyle=FormStyleBulma)

    if fmailboxXemail0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmailboxXemail0, db.dfmailboxXemail0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmailboxXemail0.form_name ))
    elif fmailboxXemail0.errors:
        print("fmailboxXemail0 has errors: %s" % (fmailboxXemail0.errors))
        return put_json_messages('error: ' + str( fmailboxXemail0.form_name ))
 

    return locals()

@action('formsXadvanced', method=["GET", "POST"] )
@action.uses(Template('forms-advanced.html', delimiters='[%[ ]]',), db, session, T,)

def formsXadvanced():
    ctrl_info= "ctrl: formsXadvanced, view: forms-advanced.html"
    page_url = "\'" + URL('formsXadvanced' ) + "\'"
    messages = []

    fformsXadvanced0= Form(db.dfformsXadvanced0, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced0, db.dfformsXadvanced0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced0.form_name ))
    elif fformsXadvanced0.errors:
        print("fformsXadvanced0 has errors: %s" % (fformsXadvanced0.errors))
        return put_json_messages('error: ' + str( fformsXadvanced0.form_name ))
 

    fformsXadvanced1= Form(db.dfformsXadvanced1, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced1, db.dfformsXadvanced1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced1.form_name ))
    elif fformsXadvanced1.errors:
        print("fformsXadvanced1 has errors: %s" % (fformsXadvanced1.errors))
        return put_json_messages('error: ' + str( fformsXadvanced1.form_name ))
 

    fformsXadvanced2= Form(db.dfformsXadvanced2, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced2, db.dfformsXadvanced2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced2.form_name ))
    elif fformsXadvanced2.errors:
        print("fformsXadvanced2 has errors: %s" % (fformsXadvanced2.errors))
        return put_json_messages('error: ' + str( fformsXadvanced2.form_name ))
 

    fformsXadvanced3= Form(db.dfformsXadvanced3, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced3, db.dfformsXadvanced3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced3.form_name ))
    elif fformsXadvanced3.errors:
        print("fformsXadvanced3 has errors: %s" % (fformsXadvanced3.errors))
        return put_json_messages('error: ' + str( fformsXadvanced3.form_name ))
 

    fformsXadvanced4= Form(db.dfformsXadvanced4, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced4, db.dfformsXadvanced4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced4.form_name ))
    elif fformsXadvanced4.errors:
        print("fformsXadvanced4 has errors: %s" % (fformsXadvanced4.errors))
        return put_json_messages('error: ' + str( fformsXadvanced4.form_name ))
 

    fformsXadvanced5= Form(db.dfformsXadvanced5, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced5, db.dfformsXadvanced5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced5.form_name ))
    elif fformsXadvanced5.errors:
        print("fformsXadvanced5 has errors: %s" % (fformsXadvanced5.errors))
        return put_json_messages('error: ' + str( fformsXadvanced5.form_name ))
 

    fformsXadvanced6= Form(db.dfformsXadvanced6, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced6, db.dfformsXadvanced6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced6.form_name ))
    elif fformsXadvanced6.errors:
        print("fformsXadvanced6 has errors: %s" % (fformsXadvanced6.errors))
        return put_json_messages('error: ' + str( fformsXadvanced6.form_name ))
 

    fformsXadvanced7= Form(db.dfformsXadvanced7, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced7, db.dfformsXadvanced7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced7.form_name ))
    elif fformsXadvanced7.errors:
        print("fformsXadvanced7 has errors: %s" % (fformsXadvanced7.errors))
        return put_json_messages('error: ' + str( fformsXadvanced7.form_name ))
 

    fformsXadvanced8= Form(db.dfformsXadvanced8, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced8, db.dfformsXadvanced8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced8.form_name ))
    elif fformsXadvanced8.errors:
        print("fformsXadvanced8 has errors: %s" % (fformsXadvanced8.errors))
        return put_json_messages('error: ' + str( fformsXadvanced8.form_name ))
 

    fformsXadvanced9= Form(db.dfformsXadvanced9, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced9, db.dfformsXadvanced9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced9.form_name ))
    elif fformsXadvanced9.errors:
        print("fformsXadvanced9 has errors: %s" % (fformsXadvanced9.errors))
        return put_json_messages('error: ' + str( fformsXadvanced9.form_name ))
 

    fformsXadvanced10= Form(db.dfformsXadvanced10, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced10, db.dfformsXadvanced10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced10.form_name ))
    elif fformsXadvanced10.errors:
        print("fformsXadvanced10 has errors: %s" % (fformsXadvanced10.errors))
        return put_json_messages('error: ' + str( fformsXadvanced10.form_name ))
 

    fformsXadvanced11= Form(db.dfformsXadvanced11, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced11.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced11, db.dfformsXadvanced11 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced11.form_name ))
    elif fformsXadvanced11.errors:
        print("fformsXadvanced11 has errors: %s" % (fformsXadvanced11.errors))
        return put_json_messages('error: ' + str( fformsXadvanced11.form_name ))
 

    fformsXadvanced12= Form(db.dfformsXadvanced12, dbio=False, formstyle=FormStyleBulma)

    if fformsXadvanced12.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXadvanced12, db.dfformsXadvanced12 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXadvanced12.form_name ))
    elif fformsXadvanced12.errors:
        print("fformsXadvanced12 has errors: %s" % (fformsXadvanced12.errors))
        return put_json_messages('error: ' + str( fformsXadvanced12.form_name ))
 

    return locals()

@action('layoutsXscroll', method=["GET", "POST"] )
@action.uses(Template('layouts-scroll.html', delimiters='[%[ ]]',), db, session, T,)

def layoutsXscroll():
    ctrl_info= "ctrl: layoutsXscroll, view: layouts-scroll.html"
    page_url = "\'" + URL('layoutsXscroll' ) + "\'"
    messages = []

    flayoutsXscroll0= Form(db.dflayoutsXscroll0, dbio=False, formstyle=FormStyleBulma)

    if flayoutsXscroll0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flayoutsXscroll0, db.dflayoutsXscroll0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flayoutsXscroll0.form_name ))
    elif flayoutsXscroll0.errors:
        print("flayoutsXscroll0 has errors: %s" % (flayoutsXscroll0.errors))
        return put_json_messages('error: ' + str( flayoutsXscroll0.form_name ))
 

    return locals()

@action('pagesXtimeline', method=["GET", "POST"] )
@action.uses(Template('pages-timeline.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXtimeline():
    ctrl_info= "ctrl: pagesXtimeline, view: pages-timeline.html"
    page_url = "\'" + URL('pagesXtimeline' ) + "\'"
    messages = []

    fpagesXtimeline0= Form(db.dfpagesXtimeline0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXtimeline0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXtimeline0, db.dfpagesXtimeline0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXtimeline0.form_name ))
    elif fpagesXtimeline0.errors:
        print("fpagesXtimeline0 has errors: %s" % (fpagesXtimeline0.errors))
        return put_json_messages('error: ' + str( fpagesXtimeline0.form_name ))
 

    return locals()

@action('pagesXcalendar', method=["GET", "POST"] )
@action.uses(Template('pages-calendar.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXcalendar():
    ctrl_info= "ctrl: pagesXcalendar, view: pages-calendar.html"
    page_url = "\'" + URL('pagesXcalendar' ) + "\'"
    messages = []

    fpagesXcalendar0= Form(db.dfpagesXcalendar0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXcalendar0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXcalendar0, db.dfpagesXcalendar0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXcalendar0.form_name ))
    elif fpagesXcalendar0.errors:
        print("fpagesXcalendar0 has errors: %s" % (fpagesXcalendar0.errors))
        return put_json_messages('error: ' + str( fpagesXcalendar0.form_name ))
 

    return locals()

@action('mailboxXfolder', method=["GET", "POST"] )
@action.uses(Template('mailbox-folder.html', delimiters='[%[ ]]',), db, session, T,)

def mailboxXfolder():
    ctrl_info= "ctrl: mailboxXfolder, view: mailbox-folder.html"
    page_url = "\'" + URL('mailboxXfolder' ) + "\'"
    messages = []

    fmailboxXfolder0= Form(db.dfmailboxXfolder0, dbio=False, formstyle=FormStyleBulma)

    if fmailboxXfolder0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmailboxXfolder0, db.dfmailboxXfolder0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmailboxXfolder0.form_name ))
    elif fmailboxXfolder0.errors:
        print("fmailboxXfolder0 has errors: %s" % (fmailboxXfolder0.errors))
        return put_json_messages('error: ' + str( fmailboxXfolder0.form_name ))
 

    return locals()

@action('tablesXpricing', method=["GET", "POST"] )
@action.uses(Template('tables-pricing.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXpricing():
    ctrl_info= "ctrl: tablesXpricing, view: tables-pricing.html"
    page_url = "\'" + URL('tablesXpricing' ) + "\'"
    messages = []

    ftablesXpricing0= Form(db.dftablesXpricing0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXpricing0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXpricing0, db.dftablesXpricing0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXpricing0.form_name ))
    elif ftablesXpricing0.errors:
        print("ftablesXpricing0 has errors: %s" % (ftablesXpricing0.errors))
        return put_json_messages('error: ' + str( ftablesXpricing0.form_name ))
 

    return locals()

@action('layoutsXdefault', method=["GET", "POST"] )
@action.uses(Template('layouts-default.html', delimiters='[%[ ]]',), db, session, T,)

def layoutsXdefault():
    ctrl_info= "ctrl: layoutsXdefault, view: layouts-default.html"
    page_url = "\'" + URL('layoutsXdefault' ) + "\'"
    messages = []

    flayoutsXdefault0= Form(db.dflayoutsXdefault0, dbio=False, formstyle=FormStyleBulma)

    if flayoutsXdefault0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flayoutsXdefault0, db.dflayoutsXdefault0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flayoutsXdefault0.form_name ))
    elif flayoutsXdefault0.errors:
        print("flayoutsXdefault0 has errors: %s" % (flayoutsXdefault0.errors))
        return put_json_messages('error: ' + str( flayoutsXdefault0.form_name ))
 

    return locals()

@action('tablesXeditable', method=["GET", "POST"] )
@action.uses(Template('tables-editable.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXeditable():
    ctrl_info= "ctrl: tablesXeditable, view: tables-editable.html"
    page_url = "\'" + URL('tablesXeditable' ) + "\'"
    messages = []

    rows_ttablesXeditable0= db(db.ttablesXeditable0).select()
    ftablesXeditable0= Form(db.dftablesXeditable0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXeditable0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXeditable0, db.dftablesXeditable0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXeditable0.form_name ))
    elif ftablesXeditable0.errors:
        print("ftablesXeditable0 has errors: %s" % (ftablesXeditable0.errors))
        return put_json_messages('error: ' + str( ftablesXeditable0.form_name ))
 

    return locals()

@action('mailboxXcompose', method=["GET", "POST"] )
@action.uses(Template('mailbox-compose.html', delimiters='[%[ ]]',), db, session, T,)

def mailboxXcompose():
    ctrl_info= "ctrl: mailboxXcompose, view: mailbox-compose.html"
    page_url = "\'" + URL('mailboxXcompose' ) + "\'"
    messages = []

    fmailboxXcompose0= Form(db.dfmailboxXcompose0, dbio=False, formstyle=FormStyleBulma)

    if fmailboxXcompose0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmailboxXcompose0, db.dfmailboxXcompose0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmailboxXcompose0.form_name ))
    elif fmailboxXcompose0.errors:
        print("fmailboxXcompose0 has errors: %s" % (fmailboxXcompose0.errors))
        return put_json_messages('error: ' + str( fmailboxXcompose0.form_name ))
 

    fmailboxXcompose1= Form(db.dfmailboxXcompose1, dbio=False, formstyle=FormStyleBulma)

    if fmailboxXcompose1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmailboxXcompose1, db.dfmailboxXcompose1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmailboxXcompose1.form_name ))
    elif fmailboxXcompose1.errors:
        print("fmailboxXcompose1 has errors: %s" % (fmailboxXcompose1.errors))
        return put_json_messages('error: ' + str( fmailboxXcompose1.form_name ))
 

    return locals()

@action('tablesXadvanced', method=["GET", "POST"] )
@action.uses(Template('tables-advanced.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXadvanced():
    ctrl_info= "ctrl: tablesXadvanced, view: tables-advanced.html"
    page_url = "\'" + URL('tablesXadvanced' ) + "\'"
    messages = []

    rows_ttablesXadvanced0= db(db.ttablesXadvanced0).select()
    rows_ttablesXadvanced1= db(db.ttablesXadvanced1).select()
    rows_ttablesXadvanced2= db(db.ttablesXadvanced2).select()
    ftablesXadvanced0= Form(db.dftablesXadvanced0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXadvanced0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXadvanced0, db.dftablesXadvanced0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXadvanced0.form_name ))
    elif ftablesXadvanced0.errors:
        print("ftablesXadvanced0 has errors: %s" % (ftablesXadvanced0.errors))
        return put_json_messages('error: ' + str( ftablesXadvanced0.form_name ))
 

    return locals()

@action('formsXvalidation', method=["GET", "POST"] )
@action.uses(Template('forms-validation.html', delimiters='[%[ ]]',), db, session, T,)

def formsXvalidation():
    ctrl_info= "ctrl: formsXvalidation, view: forms-validation.html"
    page_url = "\'" + URL('formsXvalidation' ) + "\'"
    messages = []

    fformsXvalidation0= Form(db.dfformsXvalidation0, dbio=False, formstyle=FormStyleBulma)

    if fformsXvalidation0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXvalidation0, db.dfformsXvalidation0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXvalidation0.form_name ))
    elif fformsXvalidation0.errors:
        print("fformsXvalidation0 has errors: %s" % (fformsXvalidation0.errors))
        return put_json_messages('error: ' + str( fformsXvalidation0.form_name ))
 

    fformsXvalidation1= Form(db.dfformsXvalidation1, dbio=False, formstyle=FormStyleBulma)

    if fformsXvalidation1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXvalidation1, db.dfformsXvalidation1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXvalidation1.form_name ))
    elif fformsXvalidation1.errors:
        print("fformsXvalidation1 has errors: %s" % (fformsXvalidation1.errors))
        return put_json_messages('error: ' + str( fformsXvalidation1.form_name ))
 

    fformsXvalidation2= Form(db.dfformsXvalidation2, dbio=False, formstyle=FormStyleBulma)

    if fformsXvalidation2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXvalidation2, db.dfformsXvalidation2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXvalidation2.form_name ))
    elif fformsXvalidation2.errors:
        print("fformsXvalidation2 has errors: %s" % (fformsXvalidation2.errors))
        return put_json_messages('error: ' + str( fformsXvalidation2.form_name ))
 

    fformsXvalidation3= Form(db.dfformsXvalidation3, dbio=False, formstyle=FormStyleBulma)

    if fformsXvalidation3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXvalidation3, db.dfformsXvalidation3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXvalidation3.form_name ))
    elif fformsXvalidation3.errors:
        print("fformsXvalidation3 has errors: %s" % (fformsXvalidation3.errors))
        return put_json_messages('error: ' + str( fformsXvalidation3.form_name ))
 

    fformsXvalidation4= Form(db.dfformsXvalidation4, dbio=False, formstyle=FormStyleBulma)

    if fformsXvalidation4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXvalidation4, db.dfformsXvalidation4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXvalidation4.form_name ))
    elif fformsXvalidation4.errors:
        print("fformsXvalidation4 has errors: %s" % (fformsXvalidation4.errors))
        return put_json_messages('error: ' + str( fformsXvalidation4.form_name ))
 

    return locals()

@action('uiXelementsXtabs', method=["GET", "POST"] )
@action.uses(Template('ui-elements-tabs.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXtabs():
    ctrl_info= "ctrl: uiXelementsXtabs, view: ui-elements-tabs.html"
    page_url = "\'" + URL('uiXelementsXtabs' ) + "\'"
    messages = []

    fuiXelementsXtabs0= Form(db.dfuiXelementsXtabs0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXtabs0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXtabs0, db.dfuiXelementsXtabs0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXtabs0.form_name ))
    elif fuiXelementsXtabs0.errors:
        print("fuiXelementsXtabs0 has errors: %s" % (fuiXelementsXtabs0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXtabs0.form_name ))
 

    return locals()

@action('pagesXlogXviewer', method=["GET", "POST"] )
@action.uses(Template('pages-log-viewer.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXlogXviewer():
    ctrl_info= "ctrl: pagesXlogXviewer, view: pages-log-viewer.html"
    page_url = "\'" + URL('pagesXlogXviewer' ) + "\'"
    messages = []

    rows_tpagesXlogXviewer0= db(db.tpagesXlogXviewer0).select()
    rows_tpagesXlogXviewer1= db(db.tpagesXlogXviewer1).select()
    rows_tpagesXlogXviewer2= db(db.tpagesXlogXviewer2).select()
    fpagesXlogXviewer0= Form(db.dfpagesXlogXviewer0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXlogXviewer0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXlogXviewer0, db.dfpagesXlogXviewer0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXlogXviewer0.form_name ))
    elif fpagesXlogXviewer0.errors:
        print("fpagesXlogXviewer0 has errors: %s" % (fpagesXlogXviewer0.errors))
        return put_json_messages('error: ' + str( fpagesXlogXviewer0.form_name ))
 

    return locals()

@action('mapsXgoogleXmaps', method=["GET", "POST"] )
@action.uses(Template('maps-google-maps.html', delimiters='[%[ ]]',), db, session, T,)

def mapsXgoogleXmaps():
    ctrl_info= "ctrl: mapsXgoogleXmaps, view: maps-google-maps.html"
    page_url = "\'" + URL('mapsXgoogleXmaps' ) + "\'"
    messages = []

    fmapsXgoogleXmaps0= Form(db.dfmapsXgoogleXmaps0, dbio=False, formstyle=FormStyleBulma)

    if fmapsXgoogleXmaps0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmapsXgoogleXmaps0, db.dfmapsXgoogleXmaps0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmapsXgoogleXmaps0.form_name ))
    elif fmapsXgoogleXmaps0.errors:
        print("fmapsXgoogleXmaps0 has errors: %s" % (fmapsXgoogleXmaps0.errors))
        return put_json_messages('error: ' + str( fmapsXgoogleXmaps0.form_name ))
 

    return locals()

@action('uiXelementsXicons', method=["GET", "POST"] )
@action.uses(Template('ui-elements-icons.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXicons():
    ctrl_info= "ctrl: uiXelementsXicons, view: ui-elements-icons.html"
    page_url = "\'" + URL('uiXelementsXicons' ) + "\'"
    messages = []

    fuiXelementsXicons0= Form(db.dfuiXelementsXicons0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXicons0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXicons0, db.dfuiXelementsXicons0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXicons0.form_name ))
    elif fuiXelementsXicons0.errors:
        print("fuiXelementsXicons0 has errors: %s" % (fuiXelementsXicons0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXicons0.form_name ))
 

    return locals()

@action('formsXcodeXeditor', method=["GET", "POST"] )
@action.uses(Template('forms-code-editor.html', delimiters='[%[ ]]',), db, session, T,)

def formsXcodeXeditor():
    ctrl_info= "ctrl: formsXcodeXeditor, view: forms-code-editor.html"
    page_url = "\'" + URL('formsXcodeXeditor' ) + "\'"
    messages = []

    fformsXcodeXeditor0= Form(db.dfformsXcodeXeditor0, dbio=False, formstyle=FormStyleBulma)

    if fformsXcodeXeditor0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXcodeXeditor0, db.dfformsXcodeXeditor0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXcodeXeditor0.form_name ))
    elif fformsXcodeXeditor0.errors:
        print("fformsXcodeXeditor0 has errors: %s" % (fformsXcodeXeditor0.errors))
        return put_json_messages('error: ' + str( fformsXcodeXeditor0.form_name ))
 

    fformsXcodeXeditor1= Form(db.dfformsXcodeXeditor1, dbio=False, formstyle=FormStyleBulma)

    if fformsXcodeXeditor1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXcodeXeditor1, db.dfformsXcodeXeditor1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXcodeXeditor1.form_name ))
    elif fformsXcodeXeditor1.errors:
        print("fformsXcodeXeditor1 has errors: %s" % (fformsXcodeXeditor1.errors))
        return put_json_messages('error: ' + str( fformsXcodeXeditor1.form_name ))
 

    return locals()

@action('tablesXresponsive', method=["GET", "POST"] )
@action.uses(Template('tables-responsive.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXresponsive():
    ctrl_info= "ctrl: tablesXresponsive, view: tables-responsive.html"
    page_url = "\'" + URL('tablesXresponsive' ) + "\'"
    messages = []

    rows_ttablesXresponsive0= db(db.ttablesXresponsive0).select()
    rows_ttablesXresponsive1= db(db.ttablesXresponsive1).select()
    rows_ttablesXresponsive2= db(db.ttablesXresponsive2).select()
    ftablesXresponsive0= Form(db.dftablesXresponsive0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXresponsive0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXresponsive0, db.dftablesXresponsive0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXresponsive0.form_name ))
    elif ftablesXresponsive0.errors:
        print("ftablesXresponsive0 has errors: %s" % (ftablesXresponsive0.errors))
        return put_json_messages('error: ' + str( ftablesXresponsive0.form_name ))
 

    return locals()

@action('pagesXlockXscreen', method=["GET", "POST"] )
@action.uses(Template('pages-lock-screen.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXlockXscreen():
    ctrl_info= "ctrl: pagesXlockXscreen, view: pages-lock-screen.html"
    page_url = "\'" + URL('pagesXlockXscreen' ) + "\'"
    messages = []

    fpagesXlockXscreen0= Form(db.dfpagesXlockXscreen0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXlockXscreen0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXlockXscreen0, db.dfpagesXlockXscreen0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXlockXscreen0.form_name ))
    elif fpagesXlockXscreen0.errors:
        print("fpagesXlockXscreen0 has errors: %s" % (fpagesXlockXscreen0.errors))
        return put_json_messages('error: ' + str( fpagesXlockXscreen0.form_name ))
 

    return locals()

@action('uiXelementsXextra', method=["GET", "POST"] )
@action.uses(Template('ui-elements-extra.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXextra():
    ctrl_info= "ctrl: uiXelementsXextra, view: ui-elements-extra.html"
    page_url = "\'" + URL('uiXelementsXextra' ) + "\'"
    messages = []

    fuiXelementsXextra0= Form(db.dfuiXelementsXextra0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXextra0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXextra0, db.dfuiXelementsXextra0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXextra0.form_name ))
    elif fuiXelementsXextra0.errors:
        print("fuiXelementsXextra0 has errors: %s" % (fuiXelementsXextra0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXextra0.form_name ))
 

    return locals()

@action('uiXelementsXalerts', method=["GET", "POST"] )
@action.uses(Template('ui-elements-alerts.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXalerts():
    ctrl_info= "ctrl: uiXelementsXalerts, view: ui-elements-alerts.html"
    page_url = "\'" + URL('uiXelementsXalerts' ) + "\'"
    messages = []

    fuiXelementsXalerts0= Form(db.dfuiXelementsXalerts0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXalerts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXalerts0, db.dfuiXelementsXalerts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXalerts0.form_name ))
    elif fuiXelementsXalerts0.errors:
        print("fuiXelementsXalerts0 has errors: %s" % (fuiXelementsXalerts0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXalerts0.form_name ))
 

    return locals()

@action('uiXelementsXcharts', method=["GET", "POST"] )
@action.uses(Template('ui-elements-charts.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXcharts():
    ctrl_info= "ctrl: uiXelementsXcharts, view: ui-elements-charts.html"
    page_url = "\'" + URL('uiXelementsXcharts' ) + "\'"
    messages = []

    fuiXelementsXcharts0= Form(db.dfuiXelementsXcharts0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXcharts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXcharts0, db.dfuiXelementsXcharts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXcharts0.form_name ))
    elif fuiXelementsXcharts0.errors:
        print("fuiXelementsXcharts0 has errors: %s" % (fuiXelementsXcharts0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXcharts0.form_name ))
 

    return locals()

@action('pagesXuserXprofile', method=["GET", "POST"] )
@action.uses(Template('pages-user-profile.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXuserXprofile():
    ctrl_info= "ctrl: pagesXuserXprofile, view: pages-user-profile.html"
    page_url = "\'" + URL('pagesXuserXprofile' ) + "\'"
    messages = []

    fpagesXuserXprofile0= Form(db.dfpagesXuserXprofile0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXuserXprofile0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXuserXprofile0, db.dfpagesXuserXprofile0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXuserXprofile0.form_name ))
    elif fpagesXuserXprofile0.errors:
        print("fpagesXuserXprofile0 has errors: %s" % (fpagesXuserXprofile0.errors))
        return put_json_messages('error: ' + str( fpagesXuserXprofile0.form_name ))
 

    fpagesXuserXprofile1= Form(db.dfpagesXuserXprofile1, dbio=False, formstyle=FormStyleBulma)

    if fpagesXuserXprofile1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXuserXprofile1, db.dfpagesXuserXprofile1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXuserXprofile1.form_name ))
    elif fpagesXuserXprofile1.errors:
        print("fpagesXuserXprofile1 has errors: %s" % (fpagesXuserXprofile1.errors))
        return put_json_messages('error: ' + str( fpagesXuserXprofile1.form_name ))
 

    fpagesXuserXprofile2= Form(db.dfpagesXuserXprofile2, dbio=False, formstyle=FormStyleBulma)

    if fpagesXuserXprofile2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXuserXprofile2, db.dfpagesXuserXprofile2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXuserXprofile2.form_name ))
    elif fpagesXuserXprofile2.errors:
        print("fpagesXuserXprofile2 has errors: %s" % (fpagesXuserXprofile2.errors))
        return put_json_messages('error: ' + str( fpagesXuserXprofile2.form_name ))
 

    return locals()

@action('uiXelementsXmodals', method=["GET", "POST"] )
@action.uses(Template('ui-elements-modals.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXmodals():
    ctrl_info= "ctrl: uiXelementsXmodals, view: ui-elements-modals.html"
    page_url = "\'" + URL('uiXelementsXmodals' ) + "\'"
    messages = []

    fuiXelementsXmodals0= Form(db.dfuiXelementsXmodals0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXmodals0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXmodals0, db.dfuiXelementsXmodals0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXmodals0.form_name ))
    elif fuiXelementsXmodals0.errors:
        print("fuiXelementsXmodals0 has errors: %s" % (fuiXelementsXmodals0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXmodals0.form_name ))
 

    fuiXelementsXmodals1= Form(db.dfuiXelementsXmodals1, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXmodals1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXmodals1, db.dfuiXelementsXmodals1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXmodals1.form_name ))
    elif fuiXelementsXmodals1.errors:
        print("fuiXelementsXmodals1 has errors: %s" % (fuiXelementsXmodals1.errors))
        return put_json_messages('error: ' + str( fuiXelementsXmodals1.form_name ))
 

    return locals()

@action('uiXelementsXpanels', method=["GET", "POST"] )
@action.uses(Template('ui-elements-panels.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXpanels():
    ctrl_info= "ctrl: uiXelementsXpanels, view: ui-elements-panels.html"
    page_url = "\'" + URL('uiXelementsXpanels' ) + "\'"
    messages = []

    fuiXelementsXpanels0= Form(db.dfuiXelementsXpanels0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXpanels0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXpanels0, db.dfuiXelementsXpanels0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXpanels0.form_name ))
    elif fuiXelementsXpanels0.errors:
        print("fuiXelementsXpanels0 has errors: %s" % (fuiXelementsXpanels0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXpanels0.form_name ))
 

    return locals()

@action('pagesXmediaXgallery', method=["GET", "POST"] )
@action.uses(Template('pages-media-gallery.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXmediaXgallery():
    ctrl_info= "ctrl: pagesXmediaXgallery, view: pages-media-gallery.html"
    page_url = "\'" + URL('pagesXmediaXgallery' ) + "\'"
    messages = []

    fpagesXmediaXgallery0= Form(db.dfpagesXmediaXgallery0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXmediaXgallery0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXmediaXgallery0, db.dfpagesXmediaXgallery0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXmediaXgallery0.form_name ))
    elif fpagesXmediaXgallery0.errors:
        print("fpagesXmediaXgallery0 has errors: %s" % (fpagesXmediaXgallery0.errors))
        return put_json_messages('error: ' + str( fpagesXmediaXgallery0.form_name ))
 

    return locals()

@action('pagesXinvoiceXprint', method=["GET", "POST"] )
@action.uses(Template('pages-invoice-print.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXinvoiceXprint():
    ctrl_info= "ctrl: pagesXinvoiceXprint, view: pages-invoice-print.html"
    page_url = "\'" + URL('pagesXinvoiceXprint' ) + "\'"
    messages = []

    rows_tpagesXinvoiceXprint0= db(db.tpagesXinvoiceXprint0).select()
    rows_tpagesXinvoiceXprint1= db(db.tpagesXinvoiceXprint1).select()
    return locals()

@action('uiXelementsXbuttons', method=["GET", "POST"] )
@action.uses(Template('ui-elements-buttons.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXbuttons():
    ctrl_info= "ctrl: uiXelementsXbuttons, view: ui-elements-buttons.html"
    page_url = "\'" + URL('uiXelementsXbuttons' ) + "\'"
    messages = []

    fuiXelementsXbuttons0= Form(db.dfuiXelementsXbuttons0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXbuttons0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXbuttons0, db.dfuiXelementsXbuttons0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXbuttons0.form_name ))
    elif fuiXelementsXbuttons0.errors:
        print("fuiXelementsXbuttons0 has errors: %s" % (fuiXelementsXbuttons0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXbuttons0.form_name ))
 

    return locals()

@action('uiXelementsXwidgets', method=["GET", "POST"] )
@action.uses(Template('ui-elements-widgets.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXwidgets():
    ctrl_info= "ctrl: uiXelementsXwidgets, view: ui-elements-widgets.html"
    page_url = "\'" + URL('uiXelementsXwidgets' ) + "\'"
    messages = []

    fuiXelementsXwidgets0= Form(db.dfuiXelementsXwidgets0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXwidgets0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXwidgets0, db.dfuiXelementsXwidgets0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXwidgets0.form_name ))
    elif fuiXelementsXwidgets0.errors:
        print("fuiXelementsXwidgets0 has errors: %s" % (fuiXelementsXwidgets0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXwidgets0.form_name ))
 

    return locals()

@action('uiXelementsXsliders', method=["GET", "POST"] )
@action.uses(Template('ui-elements-sliders.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXsliders():
    ctrl_info= "ctrl: uiXelementsXsliders, view: ui-elements-sliders.html"
    page_url = "\'" + URL('uiXelementsXsliders' ) + "\'"
    messages = []

    fuiXelementsXsliders0= Form(db.dfuiXelementsXsliders0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXsliders0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXsliders0, db.dfuiXelementsXsliders0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXsliders0.form_name ))
    elif fuiXelementsXsliders0.errors:
        print("fuiXelementsXsliders0 has errors: %s" % (fuiXelementsXsliders0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXsliders0.form_name ))
 

    return locals()

@action('uiXelementsXportlets', method=["GET", "POST"] )
@action.uses(Template('ui-elements-portlets.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXportlets():
    ctrl_info= "ctrl: uiXelementsXportlets, view: ui-elements-portlets.html"
    page_url = "\'" + URL('uiXelementsXportlets' ) + "\'"
    messages = []

    fuiXelementsXportlets0= Form(db.dfuiXelementsXportlets0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXportlets0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXportlets0, db.dfuiXelementsXportlets0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXportlets0.form_name ))
    elif fuiXelementsXportlets0.errors:
        print("fuiXelementsXportlets0 has errors: %s" % (fuiXelementsXportlets0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXportlets0.form_name ))
 

    return locals()

@action('uiXelementsXnestable', method=["GET", "POST"] )
@action.uses(Template('ui-elements-nestable.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXnestable():
    ctrl_info= "ctrl: uiXelementsXnestable, view: ui-elements-nestable.html"
    page_url = "\'" + URL('uiXelementsXnestable' ) + "\'"
    messages = []

    fuiXelementsXnestable0= Form(db.dfuiXelementsXnestable0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXnestable0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXnestable0, db.dfuiXelementsXnestable0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXnestable0.form_name ))
    elif fuiXelementsXnestable0.errors:
        print("fuiXelementsXnestable0 has errors: %s" % (fuiXelementsXnestable0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXnestable0.form_name ))
 

    return locals()

@action('pagesXsearchXresults', method=["GET", "POST"] )
@action.uses(Template('pages-search-results.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsearchXresults():
    ctrl_info= "ctrl: pagesXsearchXresults, view: pages-search-results.html"
    page_url = "\'" + URL('pagesXsearchXresults' ) + "\'"
    messages = []

    fpagesXsearchXresults0= Form(db.dfpagesXsearchXresults0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsearchXresults0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsearchXresults0, db.dfpagesXsearchXresults0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsearchXresults0.form_name ))
    elif fpagesXsearchXresults0.errors:
        print("fpagesXsearchXresults0 has errors: %s" % (fpagesXsearchXresults0.errors))
        return put_json_messages('error: ' + str( fpagesXsearchXresults0.form_name ))
 

    fpagesXsearchXresults1= Form(db.dfpagesXsearchXresults1, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsearchXresults1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsearchXresults1, db.dfpagesXsearchXresults1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsearchXresults1.form_name ))
    elif fpagesXsearchXresults1.errors:
        print("fpagesXsearchXresults1 has errors: %s" % (fpagesXsearchXresults1.errors))
        return put_json_messages('error: ' + str( fpagesXsearchXresults1.form_name ))
 

    return locals()

@action('uiXelementsXlightbox', method=["GET", "POST"] )
@action.uses(Template('ui-elements-lightbox.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXlightbox():
    ctrl_info= "ctrl: uiXelementsXlightbox, view: ui-elements-lightbox.html"
    page_url = "\'" + URL('uiXelementsXlightbox' ) + "\'"
    messages = []

    fuiXelementsXlightbox0= Form(db.dfuiXelementsXlightbox0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXlightbox0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXlightbox0, db.dfuiXelementsXlightbox0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXlightbox0.form_name ))
    elif fuiXelementsXlightbox0.errors:
        print("fuiXelementsXlightbox0 has errors: %s" % (fuiXelementsXlightbox0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXlightbox0.form_name ))
 

    fuiXelementsXlightbox1= Form(db.dfuiXelementsXlightbox1, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXlightbox1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXlightbox1, db.dfuiXelementsXlightbox1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXlightbox1.form_name ))
    elif fuiXelementsXlightbox1.errors:
        print("fuiXelementsXlightbox1 has errors: %s" % (fuiXelementsXlightbox1.errors))
        return put_json_messages('error: ' + str( fuiXelementsXlightbox1.form_name ))
 

    return locals()

@action('pagesXsessionXtimeout', method=["GET", "POST"] )
@action.uses(Template('pages-session-timeout.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsessionXtimeout():
    ctrl_info= "ctrl: pagesXsessionXtimeout, view: pages-session-timeout.html"
    page_url = "\'" + URL('pagesXsessionXtimeout' ) + "\'"
    messages = []

    fpagesXsessionXtimeout0= Form(db.dfpagesXsessionXtimeout0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsessionXtimeout0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsessionXtimeout0, db.dfpagesXsessionXtimeout0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsessionXtimeout0.form_name ))
    elif fpagesXsessionXtimeout0.errors:
        print("fpagesXsessionXtimeout0 has errors: %s" % (fpagesXsessionXtimeout0.errors))
        return put_json_messages('error: ' + str( fpagesXsessionXtimeout0.form_name ))
 

    return locals()

@action('uiXelementsXcarousels', method=["GET", "POST"] )
@action.uses(Template('ui-elements-carousels.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXcarousels():
    ctrl_info= "ctrl: uiXelementsXcarousels, view: ui-elements-carousels.html"
    page_url = "\'" + URL('uiXelementsXcarousels' ) + "\'"
    messages = []

    fuiXelementsXcarousels0= Form(db.dfuiXelementsXcarousels0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXcarousels0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXcarousels0, db.dfuiXelementsXcarousels0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXcarousels0.form_name ))
    elif fuiXelementsXcarousels0.errors:
        print("fuiXelementsXcarousels0 has errors: %s" % (fuiXelementsXcarousels0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXcarousels0.form_name ))
 

    return locals()

@action('uiXelementsXtreeXview', method=["GET", "POST"] )
@action.uses(Template('ui-elements-tree-view.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXtreeXview():
    ctrl_info= "ctrl: uiXelementsXtreeXview, view: ui-elements-tree-view.html"
    page_url = "\'" + URL('uiXelementsXtreeXview' ) + "\'"
    messages = []

    fuiXelementsXtreeXview0= Form(db.dfuiXelementsXtreeXview0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXtreeXview0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXtreeXview0, db.dfuiXelementsXtreeXview0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXtreeXview0.form_name ))
    elif fuiXelementsXtreeXview0.errors:
        print("fuiXelementsXtreeXview0 has errors: %s" % (fuiXelementsXtreeXview0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXtreeXview0.form_name ))
 

    return locals()

@action('uiXelementsXanimations', method=["GET", "POST"] )
@action.uses(Template('ui-elements-animations.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXanimations():
    ctrl_info= "ctrl: uiXelementsXanimations, view: ui-elements-animations.html"
    page_url = "\'" + URL('uiXelementsXanimations' ) + "\'"
    messages = []

    fuiXelementsXanimations0= Form(db.dfuiXelementsXanimations0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXanimations0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXanimations0, db.dfuiXelementsXanimations0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXanimations0.form_name ))
    elif fuiXelementsXanimations0.errors:
        print("fuiXelementsXanimations0 has errors: %s" % (fuiXelementsXanimations0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXanimations0.form_name ))
 

    return locals()

@action('layoutsXmenuXcollapsed', method=["GET", "POST"] )
@action.uses(Template('layouts-menu-collapsed.html', delimiters='[%[ ]]',), db, session, T,)

def layoutsXmenuXcollapsed():
    ctrl_info= "ctrl: layoutsXmenuXcollapsed, view: layouts-menu-collapsed.html"
    page_url = "\'" + URL('layoutsXmenuXcollapsed' ) + "\'"
    messages = []

    flayoutsXmenuXcollapsed0= Form(db.dflayoutsXmenuXcollapsed0, dbio=False, formstyle=FormStyleBulma)

    if flayoutsXmenuXcollapsed0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flayoutsXmenuXcollapsed0, db.dflayoutsXmenuXcollapsed0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flayoutsXmenuXcollapsed0.form_name ))
    elif flayoutsXmenuXcollapsed0.errors:
        print("flayoutsXmenuXcollapsed0 has errors: %s" % (flayoutsXmenuXcollapsed0.errors))
        return put_json_messages('error: ' + str( flayoutsXmenuXcollapsed0.form_name ))
 

    return locals()

@action('uiXelementsXtypography', method=["GET", "POST"] )
@action.uses(Template('ui-elements-typography.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXtypography():
    ctrl_info= "ctrl: uiXelementsXtypography, view: ui-elements-typography.html"
    page_url = "\'" + URL('uiXelementsXtypography' ) + "\'"
    messages = []

    fuiXelementsXtypography0= Form(db.dfuiXelementsXtypography0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXtypography0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXtypography0, db.dfuiXelementsXtypography0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXtypography0.form_name ))
    elif fuiXelementsXtypography0.errors:
        print("fuiXelementsXtypography0 has errors: %s" % (fuiXelementsXtypography0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXtypography0.form_name ))
 

    return locals()

@action('pagesXrecoverXpassword', method=["GET", "POST"] )
@action.uses(Template('pages-recover-password.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXrecoverXpassword():
    ctrl_info= "ctrl: pagesXrecoverXpassword, view: pages-recover-password.html"
    page_url = "\'" + URL('pagesXrecoverXpassword' ) + "\'"
    messages = []

    fpagesXrecoverXpassword0= Form(db.dfpagesXrecoverXpassword0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXrecoverXpassword0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXrecoverXpassword0, db.dfpagesXrecoverXpassword0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXrecoverXpassword0.form_name ))
    elif fpagesXrecoverXpassword0.errors:
        print("fpagesXrecoverXpassword0 has errors: %s" % (fpagesXrecoverXpassword0.errors))
        return put_json_messages('error: ' + str( fpagesXrecoverXpassword0.form_name ))
 

    return locals()

@action('uiXelementsXaccordions', method=["GET", "POST"] )
@action.uses(Template('ui-elements-accordions.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXaccordions():
    ctrl_info= "ctrl: uiXelementsXaccordions, view: ui-elements-accordions.html"
    page_url = "\'" + URL('uiXelementsXaccordions' ) + "\'"
    messages = []

    fuiXelementsXaccordions0= Form(db.dfuiXelementsXaccordions0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXaccordions0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXaccordions0, db.dfuiXelementsXaccordions0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXaccordions0.form_name ))
    elif fuiXelementsXaccordions0.errors:
        print("fuiXelementsXaccordions0 has errors: %s" % (fuiXelementsXaccordions0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXaccordions0.form_name ))
 

    return locals()

@action('uiXelementsXmodalsXajax', method=["GET", "POST"] )
@action.uses(Template('ui-elements-modals-ajax.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXmodalsXajax():
    ctrl_info= "ctrl: uiXelementsXmodalsXajax, view: ui-elements-modals-ajax.html"
    page_url = "\'" + URL('uiXelementsXmodalsXajax' ) + "\'"
    messages = []

    return locals()

@action('uiXelementsXgridXsystem', method=["GET", "POST"] )
@action.uses(Template('ui-elements-grid-system.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXgridXsystem():
    ctrl_info= "ctrl: uiXelementsXgridXsystem, view: ui-elements-grid-system.html"
    page_url = "\'" + URL('uiXelementsXgridXsystem' ) + "\'"
    messages = []

    fuiXelementsXgridXsystem0= Form(db.dfuiXelementsXgridXsystem0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXgridXsystem0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXgridXsystem0, db.dfuiXelementsXgridXsystem0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXgridXsystem0.form_name ))
    elif fuiXelementsXgridXsystem0.errors:
        print("fuiXelementsXgridXsystem0 has errors: %s" % (fuiXelementsXgridXsystem0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXgridXsystem0.form_name ))
 

    return locals()

@action('uiXelementsXprogressbars', method=["GET", "POST"] )
@action.uses(Template('ui-elements-progressbars.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXprogressbars():
    ctrl_info= "ctrl: uiXelementsXprogressbars, view: ui-elements-progressbars.html"
    page_url = "\'" + URL('uiXelementsXprogressbars' ) + "\'"
    messages = []

    fuiXelementsXprogressbars0= Form(db.dfuiXelementsXprogressbars0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXprogressbars0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXprogressbars0, db.dfuiXelementsXprogressbars0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXprogressbars0.form_name ))
    elif fuiXelementsXprogressbars0.errors:
        print("fuiXelementsXprogressbars0 has errors: %s" % (fuiXelementsXprogressbars0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXprogressbars0.form_name ))
 

    return locals()

@action('mapsXgoogleXmapsXbuilder', method=["GET", "POST"] )
@action.uses(Template('maps-google-maps-builder.html', delimiters='[%[ ]]',), db, session, T,)

def mapsXgoogleXmapsXbuilder():
    ctrl_info= "ctrl: mapsXgoogleXmapsXbuilder, view: maps-google-maps-builder.html"
    page_url = "\'" + URL('mapsXgoogleXmapsXbuilder' ) + "\'"
    messages = []

    fmapsXgoogleXmapsXbuilder0= Form(db.dfmapsXgoogleXmapsXbuilder0, dbio=False, formstyle=FormStyleBulma)

    if fmapsXgoogleXmapsXbuilder0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmapsXgoogleXmapsXbuilder0, db.dfmapsXgoogleXmapsXbuilder0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmapsXgoogleXmapsXbuilder0.form_name ))
    elif fmapsXgoogleXmapsXbuilder0.errors:
        print("fmapsXgoogleXmapsXbuilder0 has errors: %s" % (fmapsXgoogleXmapsXbuilder0.errors))
        return put_json_messages('error: ' + str( fmapsXgoogleXmapsXbuilder0.form_name ))
 

    fmapsXgoogleXmapsXbuilder1= Form(db.dfmapsXgoogleXmapsXbuilder1, dbio=False, formstyle=FormStyleBulma)

    if fmapsXgoogleXmapsXbuilder1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmapsXgoogleXmapsXbuilder1, db.dfmapsXgoogleXmapsXbuilder1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmapsXgoogleXmapsXbuilder1.form_name ))
    elif fmapsXgoogleXmapsXbuilder1.errors:
        print("fmapsXgoogleXmapsXbuilder1 has errors: %s" % (fmapsXgoogleXmapsXbuilder1.errors))
        return put_json_messages('error: ' + str( fmapsXgoogleXmapsXbuilder1.form_name ))
 

    return locals()

@action('uiXelementsXlightboxXajax', method=["GET", "POST"] )
@action.uses(Template('ui-elements-lightbox-ajax.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXlightboxXajax():
    ctrl_info= "ctrl: uiXelementsXlightboxXajax, view: ui-elements-lightbox-ajax.html"
    page_url = "\'" + URL('uiXelementsXlightboxXajax' ) + "\'"
    messages = []

    return locals()

@action('uiXelementsXnotifications', method=["GET", "POST"] )
@action.uses(Template('ui-elements-notifications.html', delimiters='[%[ ]]',), db, session, T,)

def uiXelementsXnotifications():
    ctrl_info= "ctrl: uiXelementsXnotifications, view: ui-elements-notifications.html"
    page_url = "\'" + URL('uiXelementsXnotifications' ) + "\'"
    messages = []

    fuiXelementsXnotifications0= Form(db.dfuiXelementsXnotifications0, dbio=False, formstyle=FormStyleBulma)

    if fuiXelementsXnotifications0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXelementsXnotifications0, db.dfuiXelementsXnotifications0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXelementsXnotifications0.form_name ))
    elif fuiXelementsXnotifications0.errors:
        print("fuiXelementsXnotifications0 has errors: %s" % (fuiXelementsXnotifications0.errors))
        return put_json_messages('error: ' + str( fuiXelementsXnotifications0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/octopus/api/test_table/
# curl -X  GET   http://localhost:8000/octopus/api/test_table/9
# curl -X DELETE  http://localhost:8000/octopus/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/octopus/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/octopus/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/octopus/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/octopus/api/test_table/
#  http         localhost:8000/octopus/api/test_table/9
#  http -f POST localhost:8000/octopus/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/octopus/api/test_table/2
#  http -f PUT localhost:8000/octopus/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

