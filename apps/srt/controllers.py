#
# py4web app, AI-biorex ported 21.12.2020 09:47:13 UTC+3, src: https://github.com/puikinsh/srtdash-admin-dashboard

# https://github.com/ali96343/facep4w
#

import os, json
from py4web.core import bottle

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

@action('tab', method=["GET", "POST"] )
@action.uses(Template('tab.html', delimiters='[%[ ]]',), db, session, T,)

def tab():
    ctrl_info= "ctrl: tab, view: tab.html"
    page_url = "\'" + URL('tab' ) + "\'"
    messages = []

    ftab0= Form(db.dftab0, dbio=False, formstyle=FormStyleBulma)

    if ftab0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftab0, db.dftab0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftab0.form_name ))
    elif ftab0.errors:
        print("ftab0 has errors: %s" % (ftab0.errors))
        return put_json_messages('error: ' + str( ftab0.form_name ))
 

    return locals()

@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session, T,)

def X404():
    ctrl_info= "ctrl: X404, view: 404.html"
    page_url = "\'" + URL('X404' ) + "\'"
    messages = []

    return locals()

@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session, T,)

def X500():
    ctrl_info= "ctrl: X500, view: 500.html"
    page_url = "\'" + URL('X500' ) + "\'"
    messages = []

    return locals()

@action('X403', method=["GET", "POST"] )
@action.uses(Template('403.html', delimiters='[%[ ]]',), db, session, T,)

def X403():
    ctrl_info= "ctrl: X403, view: 403.html"
    page_url = "\'" + URL('X403' ) + "\'"
    messages = []

    return locals()

@action('form', method=["GET", "POST"] )
@action.uses(Template('form.html', delimiters='[%[ ]]',), db, session, T,)

def form():
    ctrl_info= "ctrl: form, view: form.html"
    page_url = "\'" + URL('form' ) + "\'"
    messages = []

    fform0= Form(db.dfform0, dbio=False, formstyle=FormStyleBulma)

    if fform0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform0, db.dfform0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform0.form_name ))
    elif fform0.errors:
        print("fform0 has errors: %s" % (fform0.errors))
        return put_json_messages('error: ' + str( fform0.form_name ))
 

    fform1= Form(db.dfform1, dbio=False, formstyle=FormStyleBulma)

    if fform1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform1, db.dfform1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform1.form_name ))
    elif fform1.errors:
        print("fform1 has errors: %s" % (fform1.errors))
        return put_json_messages('error: ' + str( fform1.form_name ))
 

    fform2= Form(db.dfform2, dbio=False, formstyle=FormStyleBulma)

    if fform2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform2, db.dfform2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform2.form_name ))
    elif fform2.errors:
        print("fform2 has errors: %s" % (fform2.errors))
        return put_json_messages('error: ' + str( fform2.form_name ))
 

    fform3= Form(db.dfform3, dbio=False, formstyle=FormStyleBulma)

    if fform3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform3, db.dfform3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform3.form_name ))
    elif fform3.errors:
        print("fform3 has errors: %s" % (fform3.errors))
        return put_json_messages('error: ' + str( fform3.form_name ))
 

    fform4= Form(db.dfform4, dbio=False, formstyle=FormStyleBulma)

    if fform4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform4, db.dfform4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform4.form_name ))
    elif fform4.errors:
        print("fform4 has errors: %s" % (fform4.errors))
        return put_json_messages('error: ' + str( fform4.form_name ))
 

    fform5= Form(db.dfform5, dbio=False, formstyle=FormStyleBulma)

    if fform5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform5, db.dfform5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform5.form_name ))
    elif fform5.errors:
        print("fform5 has errors: %s" % (fform5.errors))
        return put_json_messages('error: ' + str( fform5.form_name ))
 

    fform6= Form(db.dfform6, dbio=False, formstyle=FormStyleBulma)

    if fform6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform6, db.dfform6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform6.form_name ))
    elif fform6.errors:
        print("fform6 has errors: %s" % (fform6.errors))
        return put_json_messages('error: ' + str( fform6.form_name ))
 

    fform7= Form(db.dfform7, dbio=False, formstyle=FormStyleBulma)

    if fform7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform7, db.dfform7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform7.form_name ))
    elif fform7.errors:
        print("fform7 has errors: %s" % (fform7.errors))
        return put_json_messages('error: ' + str( fform7.form_name ))
 

    fform8= Form(db.dfform8, dbio=False, formstyle=FormStyleBulma)

    if fform8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform8, db.dfform8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform8.form_name ))
    elif fform8.errors:
        print("fform8 has errors: %s" % (fform8.errors))
        return put_json_messages('error: ' + str( fform8.form_name ))
 

    fform9= Form(db.dfform9, dbio=False, formstyle=FormStyleBulma)

    if fform9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform9, db.dfform9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform9.form_name ))
    elif fform9.errors:
        print("fform9 has errors: %s" % (fform9.errors))
        return put_json_messages('error: ' + str( fform9.form_name ))
 

    fform10= Form(db.dfform10, dbio=False, formstyle=FormStyleBulma)

    if fform10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fform10, db.dfform10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fform10.form_name ))
    elif fform10.errors:
        print("fform10 has errors: %s" % (fform10.errors))
        return put_json_messages('error: ' + str( fform10.form_name ))
 

    return locals()

@action('maps', method=["GET", "POST"] )
@action.uses(Template('maps.html', delimiters='[%[ ]]',), db, session, T,)

def maps():
    ctrl_info= "ctrl: maps, view: maps.html"
    page_url = "\'" + URL('maps' ) + "\'"
    messages = []

    fmaps0= Form(db.dfmaps0, dbio=False, formstyle=FormStyleBulma)

    if fmaps0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmaps0, db.dfmaps0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmaps0.form_name ))
    elif fmaps0.errors:
        print("fmaps0 has errors: %s" % (fmaps0.errors))
        return put_json_messages('error: ' + str( fmaps0.form_name ))
 

    return locals()

@action('grid', method=["GET", "POST"] )
@action.uses(Template('grid.html', delimiters='[%[ ]]',), db, session, T,)

def grid():
    ctrl_info= "ctrl: grid, view: grid.html"
    page_url = "\'" + URL('grid' ) + "\'"
    messages = []

    fgrid0= Form(db.dfgrid0, dbio=False, formstyle=FormStyleBulma)

    if fgrid0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fgrid0, db.dfgrid0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fgrid0.form_name ))
    elif fgrid0.errors:
        print("fgrid0 has errors: %s" % (fgrid0.errors))
        return put_json_messages('error: ' + str( fgrid0.form_name ))
 

    return locals()

@action('modal', method=["GET", "POST"] )
@action.uses(Template('modal.html', delimiters='[%[ ]]',), db, session, T,)

def modal():
    ctrl_info= "ctrl: modal, view: modal.html"
    page_url = "\'" + URL('modal' ) + "\'"
    messages = []

    fmodal0= Form(db.dfmodal0, dbio=False, formstyle=FormStyleBulma)

    if fmodal0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodal0, db.dfmodal0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodal0.form_name ))
    elif fmodal0.errors:
        print("fmodal0 has errors: %s" % (fmodal0.errors))
        return put_json_messages('error: ' + str( fmodal0.form_name ))
 

    return locals()

@action('cards', method=["GET", "POST"] )
@action.uses(Template('cards.html', delimiters='[%[ ]]',), db, session, T,)

def cards():
    ctrl_info= "ctrl: cards, view: cards.html"
    page_url = "\'" + URL('cards' ) + "\'"
    messages = []

    fcards0= Form(db.dfcards0, dbio=False, formstyle=FormStyleBulma)

    if fcards0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fcards0, db.dfcards0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fcards0.form_name ))
    elif fcards0.errors:
        print("fcards0 has errors: %s" % (fcards0.errors))
        return put_json_messages('error: ' + str( fcards0.form_name ))
 

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
 

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    rows_tindex2= db(db.tindex2).select()
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

@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T,)

def login():
    ctrl_info= "ctrl: login, view: login.html"
    page_url = "\'" + URL('login' ) + "\'"
    messages = []

    flogin0= Form(db.dflogin0, dbio=False, formstyle=FormStyleBulma)

    if flogin0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flogin0, db.dflogin0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flogin0.form_name ))
    elif flogin0.errors:
        print("flogin0 has errors: %s" % (flogin0.errors))
        return put_json_messages('error: ' + str( flogin0.form_name ))
 

    return locals()

@action('badge', method=["GET", "POST"] )
@action.uses(Template('badge.html', delimiters='[%[ ]]',), db, session, T,)

def badge():
    ctrl_info= "ctrl: badge, view: badge.html"
    page_url = "\'" + URL('badge' ) + "\'"
    messages = []

    fbadge0= Form(db.dfbadge0, dbio=False, formstyle=FormStyleBulma)

    if fbadge0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbadge0, db.dfbadge0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbadge0.form_name ))
    elif fbadge0.errors:
        print("fbadge0 has errors: %s" % (fbadge0.errors))
        return put_json_messages('error: ' + str( fbadge0.form_name ))
 

    return locals()

@action('button', method=["GET", "POST"] )
@action.uses(Template('button.html', delimiters='[%[ ]]',), db, session, T,)

def button():
    ctrl_info= "ctrl: button, view: button.html"
    page_url = "\'" + URL('button' ) + "\'"
    messages = []

    fbutton0= Form(db.dfbutton0, dbio=False, formstyle=FormStyleBulma)

    if fbutton0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbutton0, db.dfbutton0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbutton0.form_name ))
    elif fbutton0.errors:
        print("fbutton0 has errors: %s" % (fbutton0.errors))
        return put_json_messages('error: ' + str( fbutton0.form_name ))
 

    return locals()

@action('login3', method=["GET", "POST"] )
@action.uses(Template('login3.html', delimiters='[%[ ]]',), db, session, T,)

def login3():
    ctrl_info= "ctrl: login3, view: login3.html"
    page_url = "\'" + URL('login3' ) + "\'"
    messages = []

    flogin30= Form(db.dflogin30, dbio=False, formstyle=FormStyleBulma)

    if flogin30.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flogin30, db.dflogin30 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flogin30.form_name ))
    elif flogin30.errors:
        print("flogin30 has errors: %s" % (flogin30.errors))
        return put_json_messages('error: ' + str( flogin30.form_name ))
 

    return locals()

@action('login2', method=["GET", "POST"] )
@action.uses(Template('login2.html', delimiters='[%[ ]]',), db, session, T,)

def login2():
    ctrl_info= "ctrl: login2, view: login2.html"
    page_url = "\'" + URL('login2' ) + "\'"
    messages = []

    flogin20= Form(db.dflogin20, dbio=False, formstyle=FormStyleBulma)

    if flogin20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flogin20, db.dflogin20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flogin20.form_name ))
    elif flogin20.errors:
        print("flogin20 has errors: %s" % (flogin20.errors))
        return put_json_messages('error: ' + str( flogin20.form_name ))
 

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session, T,)

def index3():
    ctrl_info= "ctrl: index3, view: index3.html"
    page_url = "\'" + URL('index3' ) + "\'"
    messages = []

    findex30= Form(db.dfindex30, dbio=False, formstyle=FormStyleBulma)

    if findex30.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex30, db.dfindex30 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex30.form_name ))
    elif findex30.errors:
        print("findex30 has errors: %s" % (findex30.errors))
        return put_json_messages('error: ' + str( findex30.form_name ))
 

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session, T,)

def index2():
    ctrl_info= "ctrl: index2, view: index2.html"
    page_url = "\'" + URL('index2' ) + "\'"
    messages = []

    rows_tindex20= db(db.tindex20).select()
    rows_tindex21= db(db.tindex21).select()
    findex20= Form(db.dfindex20, dbio=False, formstyle=FormStyleBulma)

    if findex20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex20, db.dfindex20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex20.form_name ))
    elif findex20.errors:
        print("findex20 has errors: %s" % (findex20.errors))
        return put_json_messages('error: ' + str( findex20.form_name ))
 

    findex21= Form(db.dfindex21, dbio=False, formstyle=FormStyleBulma)

    if findex21.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex21, db.dfindex21 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex21.form_name ))
    elif findex21.errors:
        print("findex21 has errors: %s" % (findex21.errors))
        return put_json_messages('error: ' + str( findex21.form_name ))
 

    return locals()

@action('themify', method=["GET", "POST"] )
@action.uses(Template('themify.html', delimiters='[%[ ]]',), db, session, T,)

def themify():
    ctrl_info= "ctrl: themify, view: themify.html"
    page_url = "\'" + URL('themify' ) + "\'"
    messages = []

    fthemify0= Form(db.dfthemify0, dbio=False, formstyle=FormStyleBulma)

    if fthemify0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fthemify0, db.dfthemify0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fthemify0.form_name ))
    elif fthemify0.errors:
        print("fthemify0 has errors: %s" % (fthemify0.errors))
        return put_json_messages('error: ' + str( fthemify0.form_name ))
 

    return locals()

@action('pricing', method=["GET", "POST"] )
@action.uses(Template('pricing.html', delimiters='[%[ ]]',), db, session, T,)

def pricing():
    ctrl_info= "ctrl: pricing, view: pricing.html"
    page_url = "\'" + URL('pricing' ) + "\'"
    messages = []

    fpricing0= Form(db.dfpricing0, dbio=False, formstyle=FormStyleBulma)

    if fpricing0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpricing0, db.dfpricing0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpricing0.form_name ))
    elif fpricing0.errors:
        print("fpricing0 has errors: %s" % (fpricing0.errors))
        return put_json_messages('error: ' + str( fpricing0.form_name ))
 

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
 

    return locals()

@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session, T,)

def register():
    ctrl_info= "ctrl: register, view: register.html"
    page_url = "\'" + URL('register' ) + "\'"
    messages = []

    fregister0= Form(db.dfregister0, dbio=False, formstyle=FormStyleBulma)

    if fregister0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fregister0, db.dfregister0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fregister0.form_name ))
    elif fregister0.errors:
        print("fregister0 has errors: %s" % (fregister0.errors))
        return put_json_messages('error: ' + str( fregister0.form_name ))
 

    return locals()

@action('piechart', method=["GET", "POST"] )
@action.uses(Template('piechart.html', delimiters='[%[ ]]',), db, session, T,)

def piechart():
    ctrl_info= "ctrl: piechart, view: piechart.html"
    page_url = "\'" + URL('piechart' ) + "\'"
    messages = []

    fpiechart0= Form(db.dfpiechart0, dbio=False, formstyle=FormStyleBulma)

    if fpiechart0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpiechart0, db.dfpiechart0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpiechart0.form_name ))
    elif fpiechart0.errors:
        print("fpiechart0 has errors: %s" % (fpiechart0.errors))
        return put_json_messages('error: ' + str( fpiechart0.form_name ))
 

    return locals()

@action('barchart', method=["GET", "POST"] )
@action.uses(Template('barchart.html', delimiters='[%[ ]]',), db, session, T,)

def barchart():
    ctrl_info= "ctrl: barchart, view: barchart.html"
    page_url = "\'" + URL('barchart' ) + "\'"
    messages = []

    fbarchart0= Form(db.dfbarchart0, dbio=False, formstyle=FormStyleBulma)

    if fbarchart0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbarchart0, db.dfbarchart0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbarchart0.form_name ))
    elif fbarchart0.errors:
        print("fbarchart0 has errors: %s" % (fbarchart0.errors))
        return put_json_messages('error: ' + str( fbarchart0.form_name ))
 

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
 

    return locals()

@action('register3', method=["GET", "POST"] )
@action.uses(Template('register3.html', delimiters='[%[ ]]',), db, session, T,)

def register3():
    ctrl_info= "ctrl: register3, view: register3.html"
    page_url = "\'" + URL('register3' ) + "\'"
    messages = []

    fregister30= Form(db.dfregister30, dbio=False, formstyle=FormStyleBulma)

    if fregister30.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fregister30, db.dfregister30 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fregister30.form_name ))
    elif fregister30.errors:
        print("fregister30 has errors: %s" % (fregister30.errors))
        return put_json_messages('error: ' + str( fregister30.form_name ))
 

    return locals()

@action('register4', method=["GET", "POST"] )
@action.uses(Template('register4.html', delimiters='[%[ ]]',), db, session, T,)

def register4():
    ctrl_info= "ctrl: register4, view: register4.html"
    page_url = "\'" + URL('register4' ) + "\'"
    messages = []

    fregister40= Form(db.dfregister40, dbio=False, formstyle=FormStyleBulma)

    if fregister40.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fregister40, db.dfregister40 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fregister40.form_name ))
    elif fregister40.errors:
        print("fregister40 has errors: %s" % (fregister40.errors))
        return put_json_messages('error: ' + str( fregister40.form_name ))
 

    return locals()

@action('register2', method=["GET", "POST"] )
@action.uses(Template('register2.html', delimiters='[%[ ]]',), db, session, T,)

def register2():
    ctrl_info= "ctrl: register2, view: register2.html"
    page_url = "\'" + URL('register2' ) + "\'"
    messages = []

    fregister20= Form(db.dfregister20, dbio=False, formstyle=FormStyleBulma)

    if fregister20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fregister20, db.dfregister20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fregister20.form_name ))
    elif fregister20.errors:
        print("fregister20 has errors: %s" % (fregister20.errors))
        return put_json_messages('error: ' + str( fregister20.form_name ))
 

    return locals()

@action('linechart', method=["GET", "POST"] )
@action.uses(Template('linechart.html', delimiters='[%[ ]]',), db, session, T,)

def linechart():
    ctrl_info= "ctrl: linechart, view: linechart.html"
    page_url = "\'" + URL('linechart' ) + "\'"
    messages = []

    flinechart0= Form(db.dflinechart0, dbio=False, formstyle=FormStyleBulma)

    if flinechart0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flinechart0, db.dflinechart0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flinechart0.form_name ))
    elif flinechart0.errors:
        print("flinechart0 has errors: %s" % (flinechart0.errors))
        return put_json_messages('error: ' + str( flinechart0.form_name ))
 

    return locals()

@action('datatable', method=["GET", "POST"] )
@action.uses(Template('datatable.html', delimiters='[%[ ]]',), db, session, T,)

def datatable():
    ctrl_info= "ctrl: datatable, view: datatable.html"
    page_url = "\'" + URL('datatable' ) + "\'"
    messages = []

    rows_tdatatable0= db(db.tdatatable0).select()
    rows_tdatatable1= db(db.tdatatable1).select()
    rows_tdatatable2= db(db.tdatatable2).select()
    fdatatable0= Form(db.dfdatatable0, dbio=False, formstyle=FormStyleBulma)

    if fdatatable0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdatatable0, db.dfdatatable0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdatatable0.form_name ))
    elif fdatatable0.errors:
        print("fdatatable0 has errors: %s" % (fdatatable0.errors))
        return put_json_messages('error: ' + str( fdatatable0.form_name ))
 

    return locals()

@action('listXgroup', method=["GET", "POST"] )
@action.uses(Template('list-group.html', delimiters='[%[ ]]',), db, session, T,)

def listXgroup():
    ctrl_info= "ctrl: listXgroup, view: list-group.html"
    page_url = "\'" + URL('listXgroup' ) + "\'"
    messages = []

    flistXgroup0= Form(db.dflistXgroup0, dbio=False, formstyle=FormStyleBulma)

    if flistXgroup0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flistXgroup0, db.dflistXgroup0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flistXgroup0.form_name ))
    elif flistXgroup0.errors:
        print("flistXgroup0 has errors: %s" % (flistXgroup0.errors))
        return put_json_messages('error: ' + str( flistXgroup0.form_name ))
 

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
 

    return locals()

@action('screenlock', method=["GET", "POST"] )
@action.uses(Template('screenlock.html', delimiters='[%[ ]]',), db, session, T,)

def screenlock():
    ctrl_info= "ctrl: screenlock, view: screenlock.html"
    page_url = "\'" + URL('screenlock' ) + "\'"
    messages = []

    fscreenlock0= Form(db.dfscreenlock0, dbio=False, formstyle=FormStyleBulma)

    if fscreenlock0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fscreenlock0, db.dfscreenlock0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fscreenlock0.form_name ))
    elif fscreenlock0.errors:
        print("fscreenlock0 has errors: %s" % (fscreenlock0.errors))
        return put_json_messages('error: ' + str( fscreenlock0.form_name ))
 

    return locals()

@action('resetXpass', method=["GET", "POST"] )
@action.uses(Template('reset-pass.html', delimiters='[%[ ]]',), db, session, T,)

def resetXpass():
    ctrl_info= "ctrl: resetXpass, view: reset-pass.html"
    page_url = "\'" + URL('resetXpass' ) + "\'"
    messages = []

    fresetXpass0= Form(db.dfresetXpass0, dbio=False, formstyle=FormStyleBulma)

    if fresetXpass0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fresetXpass0, db.dfresetXpass0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fresetXpass0.form_name ))
    elif fresetXpass0.errors:
        print("fresetXpass0 has errors: %s" % (fresetXpass0.errors))
        return put_json_messages('error: ' + str( fresetXpass0.form_name ))
 

    return locals()

@action('pagination', method=["GET", "POST"] )
@action.uses(Template('pagination.html', delimiters='[%[ ]]',), db, session, T,)

def pagination():
    ctrl_info= "ctrl: pagination, view: pagination.html"
    page_url = "\'" + URL('pagination' ) + "\'"
    messages = []

    fpagination0= Form(db.dfpagination0, dbio=False, formstyle=FormStyleBulma)

    if fpagination0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagination0, db.dfpagination0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagination0.form_name ))
    elif fpagination0.errors:
        print("fpagination0 has errors: %s" % (fpagination0.errors))
        return put_json_messages('error: ' + str( fpagination0.form_name ))
 

    return locals()

@action('tableXbasic', method=["GET", "POST"] )
@action.uses(Template('table-basic.html', delimiters='[%[ ]]',), db, session, T,)

def tableXbasic():
    ctrl_info= "ctrl: tableXbasic, view: table-basic.html"
    page_url = "\'" + URL('tableXbasic' ) + "\'"
    messages = []

    rows_ttableXbasic0= db(db.ttableXbasic0).select()
    rows_ttableXbasic1= db(db.ttableXbasic1).select()
    rows_ttableXbasic2= db(db.ttableXbasic2).select()
    rows_ttableXbasic3= db(db.ttableXbasic3).select()
    rows_ttableXbasic4= db(db.ttableXbasic4).select()
    rows_ttableXbasic5= db(db.ttableXbasic5).select()
    rows_ttableXbasic6= db(db.ttableXbasic6).select()
    rows_ttableXbasic7= db(db.ttableXbasic7).select()
    rows_ttableXbasic8= db(db.ttableXbasic8).select()
    rows_ttableXbasic9= db(db.ttableXbasic9).select()
    ftableXbasic0= Form(db.dftableXbasic0, dbio=False, formstyle=FormStyleBulma)

    if ftableXbasic0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftableXbasic0, db.dftableXbasic0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftableXbasic0.form_name ))
    elif ftableXbasic0.errors:
        print("ftableXbasic0 has errors: %s" % (ftableXbasic0.errors))
        return put_json_messages('error: ' + str( ftableXbasic0.form_name ))
 

    return locals()

@action('fontawesome', method=["GET", "POST"] )
@action.uses(Template('fontawesome.html', delimiters='[%[ ]]',), db, session, T,)

def fontawesome():
    ctrl_info= "ctrl: fontawesome, view: fontawesome.html"
    page_url = "\'" + URL('fontawesome' ) + "\'"
    messages = []

    ffontawesome0= Form(db.dffontawesome0, dbio=False, formstyle=FormStyleBulma)

    if ffontawesome0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ffontawesome0, db.dffontawesome0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ffontawesome0.form_name ))
    elif ffontawesome0.errors:
        print("ffontawesome0 has errors: %s" % (ffontawesome0.errors))
        return put_json_messages('error: ' + str( ffontawesome0.form_name ))
 

    return locals()

@action('progressbar', method=["GET", "POST"] )
@action.uses(Template('progressbar.html', delimiters='[%[ ]]',), db, session, T,)

def progressbar():
    ctrl_info= "ctrl: progressbar, view: progressbar.html"
    page_url = "\'" + URL('progressbar' ) + "\'"
    messages = []

    fprogressbar0= Form(db.dfprogressbar0, dbio=False, formstyle=FormStyleBulma)

    if fprogressbar0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fprogressbar0, db.dfprogressbar0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fprogressbar0.form_name ))
    elif fprogressbar0.errors:
        print("fprogressbar0 has errors: %s" % (fprogressbar0.errors))
        return put_json_messages('error: ' + str( fprogressbar0.form_name ))
 

    return locals()

@action('screenlock2', method=["GET", "POST"] )
@action.uses(Template('screenlock2.html', delimiters='[%[ ]]',), db, session, T,)

def screenlock2():
    ctrl_info= "ctrl: screenlock2, view: screenlock2.html"
    page_url = "\'" + URL('screenlock2' ) + "\'"
    messages = []

    fscreenlock20= Form(db.dfscreenlock20, dbio=False, formstyle=FormStyleBulma)

    if fscreenlock20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fscreenlock20, db.dfscreenlock20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fscreenlock20.form_name ))
    elif fscreenlock20.errors:
        print("fscreenlock20 has errors: %s" % (fscreenlock20.errors))
        return put_json_messages('error: ' + str( fscreenlock20.form_name ))
 

    return locals()

@action('tableXlayout', method=["GET", "POST"] )
@action.uses(Template('table-layout.html', delimiters='[%[ ]]',), db, session, T,)

def tableXlayout():
    ctrl_info= "ctrl: tableXlayout, view: table-layout.html"
    page_url = "\'" + URL('tableXlayout' ) + "\'"
    messages = []

    rows_ttableXlayout0= db(db.ttableXlayout0).select()
    rows_ttableXlayout1= db(db.ttableXlayout1).select()
    rows_ttableXlayout2= db(db.ttableXlayout2).select()
    rows_ttableXlayout3= db(db.ttableXlayout3).select()
    rows_ttableXlayout4= db(db.ttableXlayout4).select()
    ftableXlayout0= Form(db.dftableXlayout0, dbio=False, formstyle=FormStyleBulma)

    if ftableXlayout0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftableXlayout0, db.dftableXlayout0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftableXlayout0.form_name ))
    elif ftableXlayout0.errors:
        print("ftableXlayout0 has errors: %s" % (ftableXlayout0.errors))
        return put_json_messages('error: ' + str( ftableXlayout0.form_name ))
 

    return locals()

@action('mediaXobject', method=["GET", "POST"] )
@action.uses(Template('media-object.html', delimiters='[%[ ]]',), db, session, T,)

def mediaXobject():
    ctrl_info= "ctrl: mediaXobject, view: media-object.html"
    page_url = "\'" + URL('mediaXobject' ) + "\'"
    messages = []

    fmediaXobject0= Form(db.dfmediaXobject0, dbio=False, formstyle=FormStyleBulma)

    if fmediaXobject0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmediaXobject0, db.dfmediaXobject0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmediaXobject0.form_name ))
    elif fmediaXobject0.errors:
        print("fmediaXobject0 has errors: %s" % (fmediaXobject0.errors))
        return put_json_messages('error: ' + str( fmediaXobject0.form_name ))
 

    return locals()

@action('buttonXgroup', method=["GET", "POST"] )
@action.uses(Template('button-group.html', delimiters='[%[ ]]',), db, session, T,)

def buttonXgroup():
    ctrl_info= "ctrl: buttonXgroup, view: button-group.html"
    page_url = "\'" + URL('buttonXgroup' ) + "\'"
    messages = []

    fbuttonXgroup0= Form(db.dfbuttonXgroup0, dbio=False, formstyle=FormStyleBulma)

    if fbuttonXgroup0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbuttonXgroup0, db.dfbuttonXgroup0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbuttonXgroup0.form_name ))
    elif fbuttonXgroup0.errors:
        print("fbuttonXgroup0 has errors: %s" % (fbuttonXgroup0.errors))
        return put_json_messages('error: ' + str( fbuttonXgroup0.form_name ))
 

    return locals()

@action('index3Xhorizontalmenu', method=["GET", "POST"] )
@action.uses(Template('index3-horizontalmenu.html', delimiters='[%[ ]]',), db, session, T,)

def index3Xhorizontalmenu():
    ctrl_info= "ctrl: index3Xhorizontalmenu, view: index3-horizontalmenu.html"
    page_url = "\'" + URL('index3Xhorizontalmenu' ) + "\'"
    messages = []

    findex3Xhorizontalmenu0= Form(db.dfindex3Xhorizontalmenu0, dbio=False, formstyle=FormStyleBulma)

    if findex3Xhorizontalmenu0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex3Xhorizontalmenu0, db.dfindex3Xhorizontalmenu0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex3Xhorizontalmenu0.form_name ))
    elif findex3Xhorizontalmenu0.errors:
        print("findex3Xhorizontalmenu0 has errors: %s" % (findex3Xhorizontalmenu0.errors))
        return put_json_messages('error: ' + str( findex3Xhorizontalmenu0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/srt/api/test_table/
# curl -X  GET   http://localhost:8000/srt/api/test_table/9
# curl -X DELETE  http://localhost:8000/srt/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/srt/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/srt/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/srt/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/srt/api/test_table/
#  http         localhost:8000/srt/api/test_table/9
#  http -f POST localhost:8000/srt/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/srt/api/test_table/2
#  http -f PUT localhost:8000/srt/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

