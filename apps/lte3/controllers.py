#
# py4web app, AI-biorex ported 26.04.2021 15:09:02 UTC+3
# https://github.com/ali96343/facep4w
#

import os, json, uuid
from py4web.core import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore
from py4web import Session, Cache, Translator, Flash, DAL

from py4web.utils.url_signer import URLSigner

from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV, SPAN, P
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME

 
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)
url_signer = URLSigner(session)

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

def insert_form_vars(myform, mytable):

    row_id, table_row, f0_fld = None, None, None

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_fld = myform.vars.get('f0', None )
    if (not f0_fld is None) and len(f0_fld):
        row_id = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if not row_id is None:
            table_row = mytable(row_id )

            if not table_row is None:
                if Glb['debug'] == True:
                     print( f'     inserted: \"{myform.vars.f0}\" into {mytable.f0}, id = {row_id}' )
                     print( f"     select  : \"{table_row.f0}\" from {mytable.f0}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug'] == True:
            print( f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
            print()

    return row_id 



@action('callback', method="GET")
# Note that we do not use a template.  This is a JSON API, not a "web page".
@action.uses(url_signer.verify())
def callback():
     print("Called with:", dict(request.params))
     return dict(messages=request.params.echo)

#
def json2user(mess='mymess', icon_type = 'warning', js_alert='sweet2'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}', 'icon_type': icon_type, 'js_alert': js_alert})

# ---------------------- Controllers  ------------------------------------------------

@action('X500', method=["GET", "POST"] )
@action.uses(db, session, T, Template('500.html', delimiters='[%[ ]]',))

def X500():
    ctrl_info= { 'c':'X500', 'v':'500.html' }
    messages = ['X500', '500.html']
    #
    ctrl_template_url = "\'" + URL('X500' ) + "\'"

    # 
    fX5000= Form(db.dfX5000, dbio=False, formstyle=FormStyleBulma)
    if fX5000.accepted:
        icon_type ='success' if insert_form_vars(fX5000, db.dfX5000) else 'info'
        return json2user(mess = str( fX5000.form_name ), icon_type=icon_type )
    elif fX5000.errors:
        print("fX5000 has errors: %s" % (fX5000.errors))
        return json2user(mess = str(fX5000.form_name), icon_type = 'error')

    # 
    fX5001= Form(db.dfX5001, dbio=False, formstyle=FormStyleBulma)
    if fX5001.accepted:
        icon_type ='success' if insert_form_vars(fX5001, db.dfX5001) else 'info'
        return json2user(mess = str( fX5001.form_name ), icon_type=icon_type )
    elif fX5001.errors:
        print("fX5001 has errors: %s" % (fX5001.errors))
        return json2user(mess = str(fX5001.form_name), icon_type = 'error')

    return locals()

@action('X404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('404.html', delimiters='[%[ ]]',))

def X404():
    ctrl_info= { 'c':'X404', 'v':'404.html' }
    messages = ['X404', '404.html']
    #
    ctrl_template_url = "\'" + URL('X404' ) + "\'"

    return locals()

@action('faq', method=["GET", "POST"] )
@action.uses(db, session, T, Template('faq.html', delimiters='[%[ ]]',))

def faq():
    ctrl_info= { 'c':'faq', 'v':'faq.html' }
    messages = ['faq', 'faq.html']
    #
    ctrl_template_url = "\'" + URL('faq' ) + "\'"

    # 
    ffaq0= Form(db.dffaq0, dbio=False, formstyle=FormStyleBulma)
    if ffaq0.accepted:
        icon_type ='success' if insert_form_vars(ffaq0, db.dffaq0) else 'info'
        return json2user(mess = str( ffaq0.form_name ), icon_type=icon_type )
    elif ffaq0.errors:
        print("ffaq0 has errors: %s" % (ffaq0.errors))
        return json2user(mess = str(ffaq0.form_name), icon_type = 'error')

    return locals()

@action('pace', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pace.html', delimiters='[%[ ]]',))

def pace():
    ctrl_info= { 'c':'pace', 'v':'pace.html' }
    messages = ['pace', 'pace.html']
    #
    ctrl_template_url = "\'" + URL('pace' ) + "\'"

    # 
    fpace0= Form(db.dfpace0, dbio=False, formstyle=FormStyleBulma)
    if fpace0.accepted:
        icon_type ='success' if insert_form_vars(fpace0, db.dfpace0) else 'info'
        return json2user(mess = str( fpace0.form_name ), icon_type=icon_type )
    elif fpace0.errors:
        print("fpace0 has errors: %s" % (fpace0.errors))
        return json2user(mess = str(fpace0.form_name), icon_type = 'error')

    return locals()

@action('data', method=["GET", "POST"] )
@action.uses(db, session, T, Template('data.html', delimiters='[%[ ]]',))

def data():
    ctrl_info= { 'c':'data', 'v':'data.html' }
    messages = ['data', 'data.html']
    #
    ctrl_template_url = "\'" + URL('data' ) + "\'"

    rows_tdata0= db(db.tdata0).select()
    rows_tdata1= db(db.tdata1).select()
    # 
    fdata0= Form(db.dfdata0, dbio=False, formstyle=FormStyleBulma)
    if fdata0.accepted:
        icon_type ='success' if insert_form_vars(fdata0, db.dfdata0) else 'info'
        return json2user(mess = str( fdata0.form_name ), icon_type=icon_type )
    elif fdata0.errors:
        print("fdata0 has errors: %s" % (fdata0.errors))
        return json2user(mess = str(fdata0.form_name), icon_type = 'error')

    return locals()

@action('flot', method=["GET", "POST"] )
@action.uses(db, session, T, Template('flot.html', delimiters='[%[ ]]',))

def flot():
    ctrl_info= { 'c':'flot', 'v':'flot.html' }
    messages = ['flot', 'flot.html']
    #
    ctrl_template_url = "\'" + URL('flot' ) + "\'"

    # 
    fflot0= Form(db.dfflot0, dbio=False, formstyle=FormStyleBulma)
    if fflot0.accepted:
        icon_type ='success' if insert_form_vars(fflot0, db.dfflot0) else 'info'
        return json2user(mess = str( fflot0.form_name ), icon_type=icon_type )
    elif fflot0.errors:
        print("fflot0 has errors: %s" % (fflot0.errors))
        return json2user(mess = str(fflot0.form_name), icon_type = 'error')

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank.html', delimiters='[%[ ]]',))

def blank():
    ctrl_info= { 'c':'blank', 'v':'blank.html' }
    messages = ['blank', 'blank.html']
    #
    ctrl_template_url = "\'" + URL('blank' ) + "\'"

    # 
    fblank0= Form(db.dfblank0, dbio=False, formstyle=FormStyleBulma)
    if fblank0.accepted:
        icon_type ='success' if insert_form_vars(fblank0, db.dfblank0) else 'info'
        return json2user(mess = str( fblank0.form_name ), icon_type=icon_type )
    elif fblank0.errors:
        print("fblank0 has errors: %s" % (fblank0.errors))
        return json2user(mess = str(fblank0.form_name), icon_type = 'error')

    return locals()

@action('loginA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login.html', delimiters='[%[ ]]',))

def loginA():
    ctrl_info= { 'c':'loginA', 'v':'login.html' }
    messages = ['loginA', 'login.html']
    #
    ctrl_template_url = "\'" + URL('loginA' ) + "\'"

    # 
    floginA0= Form(db.dfloginA0, dbio=False, formstyle=FormStyleBulma)
    if floginA0.accepted:
        icon_type ='success' if insert_form_vars(floginA0, db.dfloginA0) else 'info'
        return json2user(mess = str( floginA0.form_name ), icon_type=icon_type )
    elif floginA0.errors:
        print("floginA0 has errors: %s" % (floginA0.errors))
        return json2user(mess = str(floginA0.form_name), icon_type = 'error')

    return locals()

@action('icons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icons.html', delimiters='[%[ ]]',))

def icons():
    ctrl_info= { 'c':'icons', 'v':'icons.html' }
    messages = ['icons', 'icons.html']
    #
    ctrl_template_url = "\'" + URL('icons' ) + "\'"

    # 
    ficons0= Form(db.dficons0, dbio=False, formstyle=FormStyleBulma)
    if ficons0.accepted:
        icon_type ='success' if insert_form_vars(ficons0, db.dficons0) else 'info'
        return json2user(mess = str( ficons0.form_name ), icon_type=icon_type )
    elif ficons0.errors:
        print("ficons0 has errors: %s" % (ficons0.errors))
        return json2user(mess = str(ficons0.form_name), icon_type = 'error')

    return locals()

@action('uplot', method=["GET", "POST"] )
@action.uses(db, session, T, Template('uplot.html', delimiters='[%[ ]]',))

def uplot():
    ctrl_info= { 'c':'uplot', 'v':'uplot.html' }
    messages = ['uplot', 'uplot.html']
    #
    ctrl_template_url = "\'" + URL('uplot' ) + "\'"

    # 
    fuplot0= Form(db.dfuplot0, dbio=False, formstyle=FormStyleBulma)
    if fuplot0.accepted:
        icon_type ='success' if insert_form_vars(fuplot0, db.dfuplot0) else 'info'
        return json2user(mess = str( fuplot0.form_name ), icon_type=icon_type )
    elif fuplot0.errors:
        print("fuplot0 has errors: %s" % (fuplot0.errors))
        return json2user(mess = str(fuplot0.form_name), icon_type = 'error')

    return locals()

@action('boxed', method=["GET", "POST"] )
@action.uses(db, session, T, Template('boxed.html', delimiters='[%[ ]]',))

def boxed():
    ctrl_info= { 'c':'boxed', 'v':'boxed.html' }
    messages = ['boxed', 'boxed.html']
    #
    ctrl_template_url = "\'" + URL('boxed' ) + "\'"

    # 
    fboxed0= Form(db.dfboxed0, dbio=False, formstyle=FormStyleBulma)
    if fboxed0.accepted:
        icon_type ='success' if insert_form_vars(fboxed0, db.dfboxed0) else 'info'
        return json2user(mess = str( fboxed0.form_name ), icon_type=icon_type )
    elif fboxed0.errors:
        print("fboxed0 has errors: %s" % (fboxed0.errors))
        return json2user(mess = str(fboxed0.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']
    #
    ctrl_template_url = "\'" + URL('index' ) + "\'"

    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        icon_type ='success' if insert_form_vars(findex0, db.dfindex0) else 'info'
        return json2user(mess = str( findex0.form_name ), icon_type=icon_type )
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return json2user(mess = str(findex0.form_name), icon_type = 'error')

    # 
    findex1= Form(db.dfindex1, dbio=False, formstyle=FormStyleBulma)
    if findex1.accepted:
        icon_type ='success' if insert_form_vars(findex1, db.dfindex1) else 'info'
        return json2user(mess = str( findex1.form_name ), icon_type=icon_type )
    elif findex1.errors:
        print("findex1 has errors: %s" % (findex1.errors))
        return json2user(mess = str(findex1.form_name), icon_type = 'error')

    return locals()

@action('navbar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('navbar.html', delimiters='[%[ ]]',))

def navbar():
    ctrl_info= { 'c':'navbar', 'v':'navbar.html' }
    messages = ['navbar', 'navbar.html']
    #
    ctrl_template_url = "\'" + URL('navbar' ) + "\'"

    # 
    fnavbar0= Form(db.dfnavbar0, dbio=False, formstyle=FormStyleBulma)
    if fnavbar0.accepted:
        icon_type ='success' if insert_form_vars(fnavbar0, db.dfnavbar0) else 'info'
        return json2user(mess = str( fnavbar0.form_name ), icon_type=icon_type )
    elif fnavbar0.errors:
        print("fnavbar0 has errors: %s" % (fnavbar0.errors))
        return json2user(mess = str(fnavbar0.form_name), icon_type = 'error')

    # 
    fnavbar1= Form(db.dfnavbar1, dbio=False, formstyle=FormStyleBulma)
    if fnavbar1.accepted:
        icon_type ='success' if insert_form_vars(fnavbar1, db.dfnavbar1) else 'info'
        return json2user(mess = str( fnavbar1.form_name ), icon_type=icon_type )
    elif fnavbar1.errors:
        print("fnavbar1 has errors: %s" % (fnavbar1.errors))
        return json2user(mess = str(fnavbar1.form_name), icon_type = 'error')

    # 
    fnavbar2= Form(db.dfnavbar2, dbio=False, formstyle=FormStyleBulma)
    if fnavbar2.accepted:
        icon_type ='success' if insert_form_vars(fnavbar2, db.dfnavbar2) else 'info'
        return json2user(mess = str( fnavbar2.form_name ), icon_type=icon_type )
    elif fnavbar2.errors:
        print("fnavbar2 has errors: %s" % (fnavbar2.errors))
        return json2user(mess = str(fnavbar2.form_name), icon_type = 'error')

    # 
    fnavbar3= Form(db.dfnavbar3, dbio=False, formstyle=FormStyleBulma)
    if fnavbar3.accepted:
        icon_type ='success' if insert_form_vars(fnavbar3, db.dfnavbar3) else 'info'
        return json2user(mess = str( fnavbar3.form_name ), icon_type=icon_type )
    elif fnavbar3.errors:
        print("fnavbar3 has errors: %s" % (fnavbar3.errors))
        return json2user(mess = str(fnavbar3.form_name), icon_type = 'error')

    # 
    fnavbar4= Form(db.dfnavbar4, dbio=False, formstyle=FormStyleBulma)
    if fnavbar4.accepted:
        icon_type ='success' if insert_form_vars(fnavbar4, db.dfnavbar4) else 'info'
        return json2user(mess = str( fnavbar4.form_name ), icon_type=icon_type )
    elif fnavbar4.errors:
        print("fnavbar4 has errors: %s" % (fnavbar4.errors))
        return json2user(mess = str(fnavbar4.form_name), icon_type = 'error')

    # 
    fnavbar5= Form(db.dfnavbar5, dbio=False, formstyle=FormStyleBulma)
    if fnavbar5.accepted:
        icon_type ='success' if insert_form_vars(fnavbar5, db.dfnavbar5) else 'info'
        return json2user(mess = str( fnavbar5.form_name ), icon_type=icon_type )
    elif fnavbar5.errors:
        print("fnavbar5 has errors: %s" % (fnavbar5.errors))
        return json2user(mess = str(fnavbar5.form_name), icon_type = 'error')

    # 
    fnavbar6= Form(db.dfnavbar6, dbio=False, formstyle=FormStyleBulma)
    if fnavbar6.accepted:
        icon_type ='success' if insert_form_vars(fnavbar6, db.dfnavbar6) else 'info'
        return json2user(mess = str( fnavbar6.form_name ), icon_type=icon_type )
    elif fnavbar6.errors:
        print("fnavbar6 has errors: %s" % (fnavbar6.errors))
        return json2user(mess = str(fnavbar6.form_name), icon_type = 'error')

    return locals()

@action('kanban', method=["GET", "POST"] )
@action.uses(db, session, T, Template('kanban.html', delimiters='[%[ ]]',))

def kanban():
    ctrl_info= { 'c':'kanban', 'v':'kanban.html' }
    messages = ['kanban', 'kanban.html']
    #
    ctrl_template_url = "\'" + URL('kanban' ) + "\'"

    # 
    fkanban0= Form(db.dfkanban0, dbio=False, formstyle=FormStyleBulma)
    if fkanban0.accepted:
        icon_type ='success' if insert_form_vars(fkanban0, db.dfkanban0) else 'info'
        return json2user(mess = str( fkanban0.form_name ), icon_type=icon_type )
    elif fkanban0.errors:
        print("fkanban0 has errors: %s" % (fkanban0.errors))
        return json2user(mess = str(fkanban0.form_name), icon_type = 'error')

    return locals()

@action('simple', method=["GET", "POST"] )
@action.uses(db, session, T, Template('simple.html', delimiters='[%[ ]]',))

def simple():
    ctrl_info= { 'c':'simple', 'v':'simple.html' }
    messages = ['simple', 'simple.html']
    #
    ctrl_template_url = "\'" + URL('simple' ) + "\'"

    # 
    fsimple0= Form(db.dfsimple0, dbio=False, formstyle=FormStyleBulma)
    if fsimple0.accepted:
        icon_type ='success' if insert_form_vars(fsimple0, db.dfsimple0) else 'info'
        return json2user(mess = str( fsimple0.form_name ), icon_type=icon_type )
    elif fsimple0.errors:
        print("fsimple0 has errors: %s" % (fsimple0.errors))
        return json2user(mess = str(fsimple0.form_name), icon_type = 'error')

    # 
    fsimple1= Form(db.dfsimple1, dbio=False, formstyle=FormStyleBulma)
    if fsimple1.accepted:
        icon_type ='success' if insert_form_vars(fsimple1, db.dfsimple1) else 'info'
        return json2user(mess = str( fsimple1.form_name ), icon_type=icon_type )
    elif fsimple1.errors:
        print("fsimple1 has errors: %s" % (fsimple1.errors))
        return json2user(mess = str(fsimple1.form_name), icon_type = 'error')

    return locals()

@action('jsgrid', method=["GET", "POST"] )
@action.uses(db, session, T, Template('jsgrid.html', delimiters='[%[ ]]',))

def jsgrid():
    ctrl_info= { 'c':'jsgrid', 'v':'jsgrid.html' }
    messages = ['jsgrid', 'jsgrid.html']
    #
    ctrl_template_url = "\'" + URL('jsgrid' ) + "\'"

    # 
    fjsgrid0= Form(db.dfjsgrid0, dbio=False, formstyle=FormStyleBulma)
    if fjsgrid0.accepted:
        icon_type ='success' if insert_form_vars(fjsgrid0, db.dfjsgrid0) else 'info'
        return json2user(mess = str( fjsgrid0.form_name ), icon_type=icon_type )
    elif fjsgrid0.errors:
        print("fjsgrid0 has errors: %s" % (fjsgrid0.errors))
        return json2user(mess = str(fjsgrid0.form_name), icon_type = 'error')

    return locals()

@action('modals', method=["GET", "POST"] )
@action.uses(db, session, T, Template('modals.html', delimiters='[%[ ]]',))

def modals():
    ctrl_info= { 'c':'modals', 'v':'modals.html' }
    messages = ['modals', 'modals.html']
    #
    ctrl_template_url = "\'" + URL('modals' ) + "\'"

    # 
    fmodals0= Form(db.dfmodals0, dbio=False, formstyle=FormStyleBulma)
    if fmodals0.accepted:
        icon_type ='success' if insert_form_vars(fmodals0, db.dfmodals0) else 'info'
        return json2user(mess = str( fmodals0.form_name ), icon_type=icon_type )
    elif fmodals0.errors:
        print("fmodals0 has errors: %s" % (fmodals0.errors))
        return json2user(mess = str(fmodals0.form_name), icon_type = 'error')

    return locals()

@action('inline', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inline.html', delimiters='[%[ ]]',))

def inline():
    ctrl_info= { 'c':'inline', 'v':'inline.html' }
    messages = ['inline', 'inline.html']
    #
    ctrl_template_url = "\'" + URL('inline' ) + "\'"

    # 
    finline0= Form(db.dfinline0, dbio=False, formstyle=FormStyleBulma)
    if finline0.accepted:
        icon_type ='success' if insert_form_vars(finline0, db.dfinline0) else 'info'
        return json2user(mess = str( finline0.form_name ), icon_type=icon_type )
    elif finline0.errors:
        print("finline0 has errors: %s" % (finline0.errors))
        return json2user(mess = str(finline0.form_name), icon_type = 'error')

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index3.html', delimiters='[%[ ]]',))

def index3():
    ctrl_info= { 'c':'index3', 'v':'index3.html' }
    messages = ['index3', 'index3.html']
    #
    ctrl_template_url = "\'" + URL('index3' ) + "\'"

    rows_tindex30= db(db.tindex30).select()
    # 
    findex30= Form(db.dfindex30, dbio=False, formstyle=FormStyleBulma)
    if findex30.accepted:
        icon_type ='success' if insert_form_vars(findex30, db.dfindex30) else 'info'
        return json2user(mess = str( findex30.form_name ), icon_type=icon_type )
    elif findex30.errors:
        print("findex30 has errors: %s" % (findex30.errors))
        return json2user(mess = str(findex30.form_name), icon_type = 'error')

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index2.html', delimiters='[%[ ]]',))

def index2():
    ctrl_info= { 'c':'index2', 'v':'index2.html' }
    messages = ['index2', 'index2.html']
    #
    ctrl_template_url = "\'" + URL('index2' ) + "\'"

    rows_tindex20= db(db.tindex20).select()
    # 
    findex20= Form(db.dfindex20, dbio=False, formstyle=FormStyleBulma)
    if findex20.accepted:
        icon_type ='success' if insert_form_vars(findex20, db.dfindex20) else 'info'
        return json2user(mess = str( findex20.form_name ), icon_type=icon_type )
    elif findex20.errors:
        print("findex20 has errors: %s" % (findex20.errors))
        return json2user(mess = str(findex20.form_name), icon_type = 'error')

    # 
    findex21= Form(db.dfindex21, dbio=False, formstyle=FormStyleBulma)
    if findex21.accepted:
        icon_type ='success' if insert_form_vars(findex21, db.dfindex21) else 'info'
        return json2user(mess = str( findex21.form_name ), icon_type=icon_type )
    elif findex21.errors:
        print("findex21 has errors: %s" % (findex21.errors))
        return json2user(mess = str(findex21.form_name), icon_type = 'error')

    return locals()

@action('iframe', method=["GET", "POST"] )
@action.uses(db, session, T, Template('iframe.html', delimiters='[%[ ]]',))

def iframe():
    ctrl_info= { 'c':'iframe', 'v':'iframe.html' }
    messages = ['iframe', 'iframe.html']
    #
    ctrl_template_url = "\'" + URL('iframe' ) + "\'"

    # 
    fiframe0= Form(db.dfiframe0, dbio=False, formstyle=FormStyleBulma)
    if fiframe0.accepted:
        icon_type ='success' if insert_form_vars(fiframe0, db.dfiframe0) else 'info'
        return json2user(mess = str( fiframe0.form_name ), icon_type=icon_type )
    elif fiframe0.errors:
        print("fiframe0 has errors: %s" % (fiframe0.errors))
        return json2user(mess = str(fiframe0.form_name), icon_type = 'error')

    return locals()

@action('profileA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('profile.html', delimiters='[%[ ]]',))

def profileA():
    ctrl_info= { 'c':'profileA', 'v':'profile.html' }
    messages = ['profileA', 'profile.html']
    #
    ctrl_template_url = "\'" + URL('profileA' ) + "\'"

    # 
    fprofileA0= Form(db.dfprofileA0, dbio=False, formstyle=FormStyleBulma)
    if fprofileA0.accepted:
        icon_type ='success' if insert_form_vars(fprofileA0, db.dfprofileA0) else 'info'
        return json2user(mess = str( fprofileA0.form_name ), icon_type=icon_type )
    elif fprofileA0.errors:
        print("fprofileA0 has errors: %s" % (fprofileA0.errors))
        return json2user(mess = str(fprofileA0.form_name), icon_type = 'error')

    # 
    fprofileA1= Form(db.dfprofileA1, dbio=False, formstyle=FormStyleBulma)
    if fprofileA1.accepted:
        icon_type ='success' if insert_form_vars(fprofileA1, db.dfprofileA1) else 'info'
        return json2user(mess = str( fprofileA1.form_name ), icon_type=icon_type )
    elif fprofileA1.errors:
        print("fprofileA1 has errors: %s" % (fprofileA1.errors))
        return json2user(mess = str(fprofileA1.form_name), icon_type = 'error')

    # 
    fprofileA2= Form(db.dfprofileA2, dbio=False, formstyle=FormStyleBulma)
    if fprofileA2.accepted:
        icon_type ='success' if insert_form_vars(fprofileA2, db.dfprofileA2) else 'info'
        return json2user(mess = str( fprofileA2.form_name ), icon_type=icon_type )
    elif fprofileA2.errors:
        print("fprofileA2 has errors: %s" % (fprofileA2.errors))
        return json2user(mess = str(fprofileA2.form_name), icon_type = 'error')

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice.html', delimiters='[%[ ]]',))

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    messages = ['invoice', 'invoice.html']
    #
    ctrl_template_url = "\'" + URL('invoice' ) + "\'"

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    # 
    finvoice0= Form(db.dfinvoice0, dbio=False, formstyle=FormStyleBulma)
    if finvoice0.accepted:
        icon_type ='success' if insert_form_vars(finvoice0, db.dfinvoice0) else 'info'
        return json2user(mess = str( finvoice0.form_name ), icon_type=icon_type )
    elif finvoice0.errors:
        print("finvoice0 has errors: %s" % (finvoice0.errors))
        return json2user(mess = str(finvoice0.form_name), icon_type = 'error')

    return locals()

@action('compose', method=["GET", "POST"] )
@action.uses(db, session, T, Template('compose.html', delimiters='[%[ ]]',))

def compose():
    ctrl_info= { 'c':'compose', 'v':'compose.html' }
    messages = ['compose', 'compose.html']
    #
    ctrl_template_url = "\'" + URL('compose' ) + "\'"

    # 
    fcompose0= Form(db.dfcompose0, dbio=False, formstyle=FormStyleBulma)
    if fcompose0.accepted:
        icon_type ='success' if insert_form_vars(fcompose0, db.dfcompose0) else 'info'
        return json2user(mess = str( fcompose0.form_name ), icon_type=icon_type )
    elif fcompose0.errors:
        print("fcompose0 has errors: %s" % (fcompose0.errors))
        return json2user(mess = str(fcompose0.form_name), icon_type = 'error')

    return locals()

@action('mailbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('mailbox.html', delimiters='[%[ ]]',))

def mailbox():
    ctrl_info= { 'c':'mailbox', 'v':'mailbox.html' }
    messages = ['mailbox', 'mailbox.html']
    #
    ctrl_template_url = "\'" + URL('mailbox' ) + "\'"

    rows_tmailbox0= db(db.tmailbox0).select()
    # 
    fmailbox0= Form(db.dfmailbox0, dbio=False, formstyle=FormStyleBulma)
    if fmailbox0.accepted:
        icon_type ='success' if insert_form_vars(fmailbox0, db.dfmailbox0) else 'info'
        return json2user(mess = str( fmailbox0.form_name ), icon_type=icon_type )
    elif fmailbox0.errors:
        print("fmailbox0 has errors: %s" % (fmailbox0.errors))
        return json2user(mess = str(fmailbox0.form_name), icon_type = 'error')

    return locals()

@action('gallery', method=["GET", "POST"] )
@action.uses(db, session, T, Template('gallery.html', delimiters='[%[ ]]',))

def gallery():
    ctrl_info= { 'c':'gallery', 'v':'gallery.html' }
    messages = ['gallery', 'gallery.html']
    #
    ctrl_template_url = "\'" + URL('gallery' ) + "\'"

    # 
    fgallery0= Form(db.dfgallery0, dbio=False, formstyle=FormStyleBulma)
    if fgallery0.accepted:
        icon_type ='success' if insert_form_vars(fgallery0, db.dfgallery0) else 'info'
        return json2user(mess = str( fgallery0.form_name ), icon_type=icon_type )
    elif fgallery0.errors:
        print("fgallery0 has errors: %s" % (fgallery0.errors))
        return json2user(mess = str(fgallery0.form_name), icon_type = 'error')

    return locals()

@action('ribbons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ribbons.html', delimiters='[%[ ]]',))

def ribbons():
    ctrl_info= { 'c':'ribbons', 'v':'ribbons.html' }
    messages = ['ribbons', 'ribbons.html']
    #
    ctrl_template_url = "\'" + URL('ribbons' ) + "\'"

    # 
    fribbons0= Form(db.dfribbons0, dbio=False, formstyle=FormStyleBulma)
    if fribbons0.accepted:
        icon_type ='success' if insert_form_vars(fribbons0, db.dfribbons0) else 'info'
        return json2user(mess = str( fribbons0.form_name ), icon_type=icon_type )
    elif fribbons0.errors:
        print("fribbons0 has errors: %s" % (fribbons0.errors))
        return json2user(mess = str(fribbons0.form_name), icon_type = 'error')

    return locals()

@action('editors', method=["GET", "POST"] )
@action.uses(db, session, T, Template('editors.html', delimiters='[%[ ]]',))

def editors():
    ctrl_info= { 'c':'editors', 'v':'editors.html' }
    messages = ['editors', 'editors.html']
    #
    ctrl_template_url = "\'" + URL('editors' ) + "\'"

    # 
    feditors0= Form(db.dfeditors0, dbio=False, formstyle=FormStyleBulma)
    if feditors0.accepted:
        icon_type ='success' if insert_form_vars(feditors0, db.dfeditors0) else 'info'
        return json2user(mess = str( feditors0.form_name ), icon_type=icon_type )
    elif feditors0.errors:
        print("feditors0 has errors: %s" % (feditors0.errors))
        return json2user(mess = str(feditors0.form_name), icon_type = 'error')

    return locals()

@action('sliders', method=["GET", "POST"] )
@action.uses(db, session, T, Template('sliders.html', delimiters='[%[ ]]',))

def sliders():
    ctrl_info= { 'c':'sliders', 'v':'sliders.html' }
    messages = ['sliders', 'sliders.html']
    #
    ctrl_template_url = "\'" + URL('sliders' ) + "\'"

    # 
    fsliders0= Form(db.dfsliders0, dbio=False, formstyle=FormStyleBulma)
    if fsliders0.accepted:
        icon_type ='success' if insert_form_vars(fsliders0, db.dfsliders0) else 'info'
        return json2user(mess = str( fsliders0.form_name ), icon_type=icon_type )
    elif fsliders0.errors:
        print("fsliders0 has errors: %s" % (fsliders0.errors))
        return json2user(mess = str(fsliders0.form_name), icon_type = 'error')

    return locals()

@action('general', method=["GET", "POST"] )
@action.uses(db, session, T, Template('general.html', delimiters='[%[ ]]',))

def general():
    ctrl_info= { 'c':'general', 'v':'general.html' }
    messages = ['general', 'general.html']
    #
    ctrl_template_url = "\'" + URL('general' ) + "\'"

    # 
    fgeneral0= Form(db.dfgeneral0, dbio=False, formstyle=FormStyleBulma)
    if fgeneral0.accepted:
        icon_type ='success' if insert_form_vars(fgeneral0, db.dfgeneral0) else 'info'
        return json2user(mess = str( fgeneral0.form_name ), icon_type=icon_type )
    elif fgeneral0.errors:
        print("fgeneral0 has errors: %s" % (fgeneral0.errors))
        return json2user(mess = str(fgeneral0.form_name), icon_type = 'error')

    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('buttons.html', delimiters='[%[ ]]',))

def buttons():
    ctrl_info= { 'c':'buttons', 'v':'buttons.html' }
    messages = ['buttons', 'buttons.html']
    #
    ctrl_template_url = "\'" + URL('buttons' ) + "\'"

    rows_tbuttons0= db(db.tbuttons0).select()
    rows_tbuttons1= db(db.tbuttons1).select()
    rows_tbuttons2= db(db.tbuttons2).select()
    rows_tbuttons3= db(db.tbuttons3).select()
    rows_tbuttons4= db(db.tbuttons4).select()
    # 
    fbuttons0= Form(db.dfbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fbuttons0.accepted:
        icon_type ='success' if insert_form_vars(fbuttons0, db.dfbuttons0) else 'info'
        return json2user(mess = str( fbuttons0.form_name ), icon_type=icon_type )
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s" % (fbuttons0.errors))
        return json2user(mess = str(fbuttons0.form_name), icon_type = 'error')

    return locals()

@action('chartjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chartjs.html', delimiters='[%[ ]]',))

def chartjs():
    ctrl_info= { 'c':'chartjs', 'v':'chartjs.html' }
    messages = ['chartjs', 'chartjs.html']
    #
    ctrl_template_url = "\'" + URL('chartjs' ) + "\'"

    # 
    fchartjs0= Form(db.dfchartjs0, dbio=False, formstyle=FormStyleBulma)
    if fchartjs0.accepted:
        icon_type ='success' if insert_form_vars(fchartjs0, db.dfchartjs0) else 'info'
        return json2user(mess = str( fchartjs0.form_name ), icon_type=icon_type )
    elif fchartjs0.errors:
        print("fchartjs0 has errors: %s" % (fchartjs0.errors))
        return json2user(mess = str(fchartjs0.form_name), icon_type = 'error')

    return locals()

@action('topXnav', method=["GET", "POST"] )
@action.uses(db, session, T, Template('top-nav.html', delimiters='[%[ ]]',))

def topXnav():
    ctrl_info= { 'c':'topXnav', 'v':'top-nav.html' }
    messages = ['topXnav', 'top-nav.html']
    #
    ctrl_template_url = "\'" + URL('topXnav' ) + "\'"

    # 
    ftopXnav0= Form(db.dftopXnav0, dbio=False, formstyle=FormStyleBulma)
    if ftopXnav0.accepted:
        icon_type ='success' if insert_form_vars(ftopXnav0, db.dftopXnav0) else 'info'
        return json2user(mess = str( ftopXnav0.form_name ), icon_type=icon_type )
    elif ftopXnav0.errors:
        print("ftopXnav0 has errors: %s" % (ftopXnav0.errors))
        return json2user(mess = str(ftopXnav0.form_name), icon_type = 'error')

    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(db, session, T, Template('widgets.html', delimiters='[%[ ]]',))

def widgets():
    ctrl_info= { 'c':'widgets', 'v':'widgets.html' }
    messages = ['widgets', 'widgets.html']
    #
    ctrl_template_url = "\'" + URL('widgets' ) + "\'"

    # 
    fwidgets0= Form(db.dfwidgets0, dbio=False, formstyle=FormStyleBulma)
    if fwidgets0.accepted:
        icon_type ='success' if insert_form_vars(fwidgets0, db.dfwidgets0) else 'info'
        return json2user(mess = str( fwidgets0.form_name ), icon_type=icon_type )
    elif fwidgets0.errors:
        print("fwidgets0 has errors: %s" % (fwidgets0.errors))
        return json2user(mess = str(fwidgets0.form_name), icon_type = 'error')

    # 
    fwidgets1= Form(db.dfwidgets1, dbio=False, formstyle=FormStyleBulma)
    if fwidgets1.accepted:
        icon_type ='success' if insert_form_vars(fwidgets1, db.dfwidgets1) else 'info'
        return json2user(mess = str( fwidgets1.form_name ), icon_type=icon_type )
    elif fwidgets1.errors:
        print("fwidgets1 has errors: %s" % (fwidgets1.errors))
        return json2user(mess = str(fwidgets1.form_name), icon_type = 'error')

    # 
    fwidgets2= Form(db.dfwidgets2, dbio=False, formstyle=FormStyleBulma)
    if fwidgets2.accepted:
        icon_type ='success' if insert_form_vars(fwidgets2, db.dfwidgets2) else 'info'
        return json2user(mess = str( fwidgets2.form_name ), icon_type=icon_type )
    elif fwidgets2.errors:
        print("fwidgets2 has errors: %s" % (fwidgets2.errors))
        return json2user(mess = str(fwidgets2.form_name), icon_type = 'error')

    # 
    fwidgets3= Form(db.dfwidgets3, dbio=False, formstyle=FormStyleBulma)
    if fwidgets3.accepted:
        icon_type ='success' if insert_form_vars(fwidgets3, db.dfwidgets3) else 'info'
        return json2user(mess = str( fwidgets3.form_name ), icon_type=icon_type )
    elif fwidgets3.errors:
        print("fwidgets3 has errors: %s" % (fwidgets3.errors))
        return json2user(mess = str(fwidgets3.form_name), icon_type = 'error')

    # 
    fwidgets4= Form(db.dfwidgets4, dbio=False, formstyle=FormStyleBulma)
    if fwidgets4.accepted:
        icon_type ='success' if insert_form_vars(fwidgets4, db.dfwidgets4) else 'info'
        return json2user(mess = str( fwidgets4.form_name ), icon_type=icon_type )
    elif fwidgets4.errors:
        print("fwidgets4 has errors: %s" % (fwidgets4.errors))
        return json2user(mess = str(fwidgets4.form_name), icon_type = 'error')

    # 
    fwidgets5= Form(db.dfwidgets5, dbio=False, formstyle=FormStyleBulma)
    if fwidgets5.accepted:
        icon_type ='success' if insert_form_vars(fwidgets5, db.dfwidgets5) else 'info'
        return json2user(mess = str( fwidgets5.form_name ), icon_type=icon_type )
    elif fwidgets5.errors:
        print("fwidgets5 has errors: %s" % (fwidgets5.errors))
        return json2user(mess = str(fwidgets5.form_name), icon_type = 'error')

    # 
    fwidgets6= Form(db.dfwidgets6, dbio=False, formstyle=FormStyleBulma)
    if fwidgets6.accepted:
        icon_type ='success' if insert_form_vars(fwidgets6, db.dfwidgets6) else 'info'
        return json2user(mess = str( fwidgets6.form_name ), icon_type=icon_type )
    elif fwidgets6.errors:
        print("fwidgets6 has errors: %s" % (fwidgets6.errors))
        return json2user(mess = str(fwidgets6.form_name), icon_type = 'error')

    # 
    fwidgets7= Form(db.dfwidgets7, dbio=False, formstyle=FormStyleBulma)
    if fwidgets7.accepted:
        icon_type ='success' if insert_form_vars(fwidgets7, db.dfwidgets7) else 'info'
        return json2user(mess = str( fwidgets7.form_name ), icon_type=icon_type )
    elif fwidgets7.errors:
        print("fwidgets7 has errors: %s" % (fwidgets7.errors))
        return json2user(mess = str(fwidgets7.form_name), icon_type = 'error')

    # 
    fwidgets8= Form(db.dfwidgets8, dbio=False, formstyle=FormStyleBulma)
    if fwidgets8.accepted:
        icon_type ='success' if insert_form_vars(fwidgets8, db.dfwidgets8) else 'info'
        return json2user(mess = str( fwidgets8.form_name ), icon_type=icon_type )
    elif fwidgets8.errors:
        print("fwidgets8 has errors: %s" % (fwidgets8.errors))
        return json2user(mess = str(fwidgets8.form_name), icon_type = 'error')

    # 
    fwidgets9= Form(db.dfwidgets9, dbio=False, formstyle=FormStyleBulma)
    if fwidgets9.accepted:
        icon_type ='success' if insert_form_vars(fwidgets9, db.dfwidgets9) else 'info'
        return json2user(mess = str( fwidgets9.form_name ), icon_type=icon_type )
    elif fwidgets9.errors:
        print("fwidgets9 has errors: %s" % (fwidgets9.errors))
        return json2user(mess = str(fwidgets9.form_name), icon_type = 'error')

    # 
    fwidgets10= Form(db.dfwidgets10, dbio=False, formstyle=FormStyleBulma)
    if fwidgets10.accepted:
        icon_type ='success' if insert_form_vars(fwidgets10, db.dfwidgets10) else 'info'
        return json2user(mess = str( fwidgets10.form_name ), icon_type=icon_type )
    elif fwidgets10.errors:
        print("fwidgets10 has errors: %s" % (fwidgets10.errors))
        return json2user(mess = str(fwidgets10.form_name), icon_type = 'error')

    return locals()

@action('starter', method=["GET", "POST"] )
@action.uses(db, session, T, Template('starter.html', delimiters='[%[ ]]',))

def starter():
    ctrl_info= { 'c':'starter', 'v':'starter.html' }
    messages = ['starter', 'starter.html']
    #
    ctrl_template_url = "\'" + URL('starter' ) + "\'"

    # 
    fstarter0= Form(db.dfstarter0, dbio=False, formstyle=FormStyleBulma)
    if fstarter0.accepted:
        icon_type ='success' if insert_form_vars(fstarter0, db.dfstarter0) else 'info'
        return json2user(mess = str( fstarter0.form_name ), icon_type=icon_type )
    elif fstarter0.errors:
        print("fstarter0 has errors: %s" % (fstarter0.errors))
        return json2user(mess = str(fstarter0.form_name), icon_type = 'error')

    return locals()

@action('enhanced', method=["GET", "POST"] )
@action.uses(db, session, T, Template('enhanced.html', delimiters='[%[ ]]',))

def enhanced():
    ctrl_info= { 'c':'enhanced', 'v':'enhanced.html' }
    messages = ['enhanced', 'enhanced.html']
    #
    ctrl_template_url = "\'" + URL('enhanced' ) + "\'"

    # 
    fenhanced0= Form(db.dfenhanced0, dbio=False, formstyle=FormStyleBulma)
    if fenhanced0.accepted:
        icon_type ='success' if insert_form_vars(fenhanced0, db.dfenhanced0) else 'info'
        return json2user(mess = str( fenhanced0.form_name ), icon_type=icon_type )
    elif fenhanced0.errors:
        print("fenhanced0 has errors: %s" % (fenhanced0.errors))
        return json2user(mess = str(fenhanced0.form_name), icon_type = 'error')

    # 
    fenhanced1= Form(db.dfenhanced1, dbio=False, formstyle=FormStyleBulma)
    if fenhanced1.accepted:
        icon_type ='success' if insert_form_vars(fenhanced1, db.dfenhanced1) else 'info'
        return json2user(mess = str( fenhanced1.form_name ), icon_type=icon_type )
    elif fenhanced1.errors:
        print("fenhanced1 has errors: %s" % (fenhanced1.errors))
        return json2user(mess = str(fenhanced1.form_name), icon_type = 'error')

    return locals()

@action('loginXv2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login-v2.html', delimiters='[%[ ]]',))

def loginXv2():
    ctrl_info= { 'c':'loginXv2', 'v':'login-v2.html' }
    messages = ['loginXv2', 'login-v2.html']
    #
    ctrl_template_url = "\'" + URL('loginXv2' ) + "\'"

    # 
    floginXv20= Form(db.dfloginXv20, dbio=False, formstyle=FormStyleBulma)
    if floginXv20.accepted:
        icon_type ='success' if insert_form_vars(floginXv20, db.dfloginXv20) else 'info'
        return json2user(mess = str( floginXv20.form_name ), icon_type=icon_type )
    elif floginXv20.errors:
        print("floginXv20 has errors: %s" % (floginXv20.errors))
        return json2user(mess = str(floginXv20.form_name), icon_type = 'error')

    return locals()

@action('registerA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register.html', delimiters='[%[ ]]',))

def registerA():
    ctrl_info= { 'c':'registerA', 'v':'register.html' }
    messages = ['registerA', 'register.html']
    #
    ctrl_template_url = "\'" + URL('registerA' ) + "\'"

    # 
    fregisterA0= Form(db.dfregisterA0, dbio=False, formstyle=FormStyleBulma)
    if fregisterA0.accepted:
        icon_type ='success' if insert_form_vars(fregisterA0, db.dfregisterA0) else 'info'
        return json2user(mess = str( fregisterA0.form_name ), icon_type=icon_type )
    elif fregisterA0.errors:
        print("fregisterA0 has errors: %s" % (fregisterA0.errors))
        return json2user(mess = str(fregisterA0.form_name), icon_type = 'error')

    return locals()

@action('contacts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('contacts.html', delimiters='[%[ ]]',))

def contacts():
    ctrl_info= { 'c':'contacts', 'v':'contacts.html' }
    messages = ['contacts', 'contacts.html']
    #
    ctrl_template_url = "\'" + URL('contacts' ) + "\'"

    # 
    fcontacts0= Form(db.dfcontacts0, dbio=False, formstyle=FormStyleBulma)
    if fcontacts0.accepted:
        icon_type ='success' if insert_form_vars(fcontacts0, db.dfcontacts0) else 'info'
        return json2user(mess = str( fcontacts0.form_name ), icon_type=icon_type )
    elif fcontacts0.errors:
        print("fcontacts0 has errors: %s" % (fcontacts0.errors))
        return json2user(mess = str(fcontacts0.form_name), icon_type = 'error')

    return locals()

@action('projects', method=["GET", "POST"] )
@action.uses(db, session, T, Template('projects.html', delimiters='[%[ ]]',))

def projects():
    ctrl_info= { 'c':'projects', 'v':'projects.html' }
    messages = ['projects', 'projects.html']
    #
    ctrl_template_url = "\'" + URL('projects' ) + "\'"

    rows_tprojects0= db(db.tprojects0).select()
    # 
    fprojects0= Form(db.dfprojects0, dbio=False, formstyle=FormStyleBulma)
    if fprojects0.accepted:
        icon_type ='success' if insert_form_vars(fprojects0, db.dfprojects0) else 'info'
        return json2user(mess = str( fprojects0.form_name ), icon_type=icon_type )
    elif fprojects0.errors:
        print("fprojects0 has errors: %s" % (fprojects0.errors))
        return json2user(mess = str(fprojects0.form_name), icon_type = 'error')

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']
    #
    ctrl_template_url = "\'" + URL('calendar' ) + "\'"

    # 
    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)
    if fcalendar0.accepted:
        icon_type ='success' if insert_form_vars(fcalendar0, db.dfcalendar0) else 'info'
        return json2user(mess = str( fcalendar0.form_name ), icon_type=icon_type )
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s" % (fcalendar0.errors))
        return json2user(mess = str(fcalendar0.form_name), icon_type = 'error')

    return locals()

@action('advanced', method=["GET", "POST"] )
@action.uses(db, session, T, Template('advanced.html', delimiters='[%[ ]]',))

def advanced():
    ctrl_info= { 'c':'advanced', 'v':'advanced.html' }
    messages = ['advanced', 'advanced.html']
    #
    ctrl_template_url = "\'" + URL('advanced' ) + "\'"

    # 
    fadvanced0= Form(db.dfadvanced0, dbio=False, formstyle=FormStyleBulma)
    if fadvanced0.accepted:
        icon_type ='success' if insert_form_vars(fadvanced0, db.dfadvanced0) else 'info'
        return json2user(mess = str( fadvanced0.form_name ), icon_type=icon_type )
    elif fadvanced0.errors:
        print("fadvanced0 has errors: %s" % (fadvanced0.errors))
        return json2user(mess = str(fadvanced0.form_name), icon_type = 'error')

    return locals()

@action('timeline', method=["GET", "POST"] )
@action.uses(db, session, T, Template('timeline.html', delimiters='[%[ ]]',))

def timeline():
    ctrl_info= { 'c':'timeline', 'v':'timeline.html' }
    messages = ['timeline', 'timeline.html']
    #
    ctrl_template_url = "\'" + URL('timeline' ) + "\'"

    # 
    ftimeline0= Form(db.dftimeline0, dbio=False, formstyle=FormStyleBulma)
    if ftimeline0.accepted:
        icon_type ='success' if insert_form_vars(ftimeline0, db.dftimeline0) else 'info'
        return json2user(mess = str( ftimeline0.form_name ), icon_type=icon_type )
    elif ftimeline0.errors:
        print("ftimeline0 has errors: %s" % (ftimeline0.errors))
        return json2user(mess = str(ftimeline0.form_name), icon_type = 'error')

    return locals()

@action('readXmail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('read-mail.html', delimiters='[%[ ]]',))

def readXmail():
    ctrl_info= { 'c':'readXmail', 'v':'read-mail.html' }
    messages = ['readXmail', 'read-mail.html']
    #
    ctrl_template_url = "\'" + URL('readXmail' ) + "\'"

    # 
    freadXmail0= Form(db.dfreadXmail0, dbio=False, formstyle=FormStyleBulma)
    if freadXmail0.accepted:
        icon_type ='success' if insert_form_vars(freadXmail0, db.dfreadXmail0) else 'info'
        return json2user(mess = str( freadXmail0.form_name ), icon_type=icon_type )
    elif freadXmail0.errors:
        print("freadXmail0 has errors: %s" % (freadXmail0.errors))
        return json2user(mess = str(freadXmail0.form_name), icon_type = 'error')

    return locals()

@action('lockscreen', method=["GET", "POST"] )
@action.uses(db, session, T, Template('lockscreen.html', delimiters='[%[ ]]',))

def lockscreen():
    ctrl_info= { 'c':'lockscreen', 'v':'lockscreen.html' }
    messages = ['lockscreen', 'lockscreen.html']
    #
    ctrl_template_url = "\'" + URL('lockscreen' ) + "\'"

    # 
    flockscreen0= Form(db.dflockscreen0, dbio=False, formstyle=FormStyleBulma)
    if flockscreen0.accepted:
        icon_type ='success' if insert_form_vars(flockscreen0, db.dflockscreen0) else 'info'
        return json2user(mess = str( flockscreen0.form_name ), icon_type=icon_type )
    elif flockscreen0.errors:
        print("flockscreen0 has errors: %s" % (flockscreen0.errors))
        return json2user(mess = str(flockscreen0.form_name), icon_type = 'error')

    return locals()

@action('contactXus', method=["GET", "POST"] )
@action.uses(db, session, T, Template('contact-us.html', delimiters='[%[ ]]',))

def contactXus():
    ctrl_info= { 'c':'contactXus', 'v':'contact-us.html' }
    messages = ['contactXus', 'contact-us.html']
    #
    ctrl_template_url = "\'" + URL('contactXus' ) + "\'"

    # 
    fcontactXus0= Form(db.dfcontactXus0, dbio=False, formstyle=FormStyleBulma)
    if fcontactXus0.accepted:
        icon_type ='success' if insert_form_vars(fcontactXus0, db.dfcontactXus0) else 'info'
        return json2user(mess = str( fcontactXus0.form_name ), icon_type=icon_type )
    elif fcontactXus0.errors:
        print("fcontactXus0 has errors: %s" % (fcontactXus0.errors))
        return json2user(mess = str(fcontactXus0.form_name), icon_type = 'error')

    return locals()

@action('eXcommerce', method=["GET", "POST"] )
@action.uses(db, session, T, Template('e-commerce.html', delimiters='[%[ ]]',))

def eXcommerce():
    ctrl_info= { 'c':'eXcommerce', 'v':'e-commerce.html' }
    messages = ['eXcommerce', 'e-commerce.html']
    #
    ctrl_template_url = "\'" + URL('eXcommerce' ) + "\'"

    # 
    feXcommerce0= Form(db.dfeXcommerce0, dbio=False, formstyle=FormStyleBulma)
    if feXcommerce0.accepted:
        icon_type ='success' if insert_form_vars(feXcommerce0, db.dfeXcommerce0) else 'info'
        return json2user(mess = str( feXcommerce0.form_name ), icon_type=icon_type )
    elif feXcommerce0.errors:
        print("feXcommerce0 has errors: %s" % (feXcommerce0.errors))
        return json2user(mess = str(feXcommerce0.form_name), icon_type = 'error')

    return locals()

@action('validation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('validation.html', delimiters='[%[ ]]',))

def validation():
    ctrl_info= { 'c':'validation', 'v':'validation.html' }
    messages = ['validation', 'validation.html']
    #
    ctrl_template_url = "\'" + URL('validation' ) + "\'"

    # 
    fvalidation0= Form(db.dfvalidation0, dbio=False, formstyle=FormStyleBulma)
    if fvalidation0.accepted:
        icon_type ='success' if insert_form_vars(fvalidation0, db.dfvalidation0) else 'info'
        return json2user(mess = str( fvalidation0.form_name ), icon_type=icon_type )
    elif fvalidation0.errors:
        print("fvalidation0 has errors: %s" % (fvalidation0.errors))
        return json2user(mess = str(fvalidation0.form_name), icon_type = 'error')

    # 
    fvalidation1= Form(db.dfvalidation1, dbio=False, formstyle=FormStyleBulma)
    if fvalidation1.accepted:
        icon_type ='success' if insert_form_vars(fvalidation1, db.dfvalidation1) else 'info'
        return json2user(mess = str( fvalidation1.form_name ), icon_type=icon_type )
    elif fvalidation1.errors:
        print("fvalidation1 has errors: %s" % (fvalidation1.errors))
        return json2user(mess = str(fvalidation1.form_name), icon_type = 'error')

    return locals()

@action('registerXv2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register-v2.html', delimiters='[%[ ]]',))

def registerXv2():
    ctrl_info= { 'c':'registerXv2', 'v':'register-v2.html' }
    messages = ['registerXv2', 'register-v2.html']
    #
    ctrl_template_url = "\'" + URL('registerXv2' ) + "\'"

    # 
    fregisterXv20= Form(db.dfregisterXv20, dbio=False, formstyle=FormStyleBulma)
    if fregisterXv20.accepted:
        icon_type ='success' if insert_form_vars(fregisterXv20, db.dfregisterXv20) else 'info'
        return json2user(mess = str( fregisterXv20.form_name ), icon_type=icon_type )
    elif fregisterXv20.errors:
        print("fregisterXv20 has errors: %s" % (fregisterXv20.errors))
        return json2user(mess = str(fregisterXv20.form_name), icon_type = 'error')

    return locals()

@action('projectXadd', method=["GET", "POST"] )
@action.uses(db, session, T, Template('project-add.html', delimiters='[%[ ]]',))

def projectXadd():
    ctrl_info= { 'c':'projectXadd', 'v':'project-add.html' }
    messages = ['projectXadd', 'project-add.html']
    #
    ctrl_template_url = "\'" + URL('projectXadd' ) + "\'"

    # 
    fprojectXadd0= Form(db.dfprojectXadd0, dbio=False, formstyle=FormStyleBulma)
    if fprojectXadd0.accepted:
        icon_type ='success' if insert_form_vars(fprojectXadd0, db.dfprojectXadd0) else 'info'
        return json2user(mess = str( fprojectXadd0.form_name ), icon_type=icon_type )
    elif fprojectXadd0.errors:
        print("fprojectXadd0 has errors: %s" % (fprojectXadd0.errors))
        return json2user(mess = str(fprojectXadd0.form_name), icon_type = 'error')

    return locals()

@action('projectXedit', method=["GET", "POST"] )
@action.uses(db, session, T, Template('project-edit.html', delimiters='[%[ ]]',))

def projectXedit():
    ctrl_info= { 'c':'projectXedit', 'v':'project-edit.html' }
    messages = ['projectXedit', 'project-edit.html']
    #
    ctrl_template_url = "\'" + URL('projectXedit' ) + "\'"

    rows_tprojectXedit0= db(db.tprojectXedit0).select()
    # 
    fprojectXedit0= Form(db.dfprojectXedit0, dbio=False, formstyle=FormStyleBulma)
    if fprojectXedit0.accepted:
        icon_type ='success' if insert_form_vars(fprojectXedit0, db.dfprojectXedit0) else 'info'
        return json2user(mess = str( fprojectXedit0.form_name ), icon_type=icon_type )
    elif fprojectXedit0.errors:
        print("fprojectXedit0 has errors: %s" % (fprojectXedit0.errors))
        return json2user(mess = str(fprojectXedit0.form_name), icon_type = 'error')

    return locals()

@action('fixedXtopnav', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed-topnav.html', delimiters='[%[ ]]',))

def fixedXtopnav():
    ctrl_info= { 'c':'fixedXtopnav', 'v':'fixed-topnav.html' }
    messages = ['fixedXtopnav', 'fixed-topnav.html']
    #
    ctrl_template_url = "\'" + URL('fixedXtopnav' ) + "\'"

    # 
    ffixedXtopnav0= Form(db.dffixedXtopnav0, dbio=False, formstyle=FormStyleBulma)
    if ffixedXtopnav0.accepted:
        icon_type ='success' if insert_form_vars(ffixedXtopnav0, db.dffixedXtopnav0) else 'info'
        return json2user(mess = str( ffixedXtopnav0.form_name ), icon_type=icon_type )
    elif ffixedXtopnav0.errors:
        print("ffixedXtopnav0 has errors: %s" % (ffixedXtopnav0.errors))
        return json2user(mess = str(ffixedXtopnav0.form_name), icon_type = 'error')

    return locals()

@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed-footer.html', delimiters='[%[ ]]',))

def fixedXfooter():
    ctrl_info= { 'c':'fixedXfooter', 'v':'fixed-footer.html' }
    messages = ['fixedXfooter', 'fixed-footer.html']
    #
    ctrl_template_url = "\'" + URL('fixedXfooter' ) + "\'"

    # 
    ffixedXfooter0= Form(db.dffixedXfooter0, dbio=False, formstyle=FormStyleBulma)
    if ffixedXfooter0.accepted:
        icon_type ='success' if insert_form_vars(ffixedXfooter0, db.dffixedXfooter0) else 'info'
        return json2user(mess = str( ffixedXfooter0.form_name ), icon_type=icon_type )
    elif ffixedXfooter0.errors:
        print("ffixedXfooter0 has errors: %s" % (ffixedXfooter0.errors))
        return json2user(mess = str(ffixedXfooter0.form_name), icon_type = 'error')

    return locals()

@action('invoiceXprint', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice-print.html', delimiters='[%[ ]]',))

def invoiceXprint():
    ctrl_info= { 'c':'invoiceXprint', 'v':'invoice-print.html' }
    messages = ['invoiceXprint', 'invoice-print.html']
    #
    ctrl_template_url = "\'" + URL('invoiceXprint' ) + "\'"

    rows_tinvoiceXprint0= db(db.tinvoiceXprint0).select()
    rows_tinvoiceXprint1= db(db.tinvoiceXprint1).select()
    return locals()

@action('languageXmenu', method=["GET", "POST"] )
@action.uses(db, session, T, Template('language-menu.html', delimiters='[%[ ]]',))

def languageXmenu():
    ctrl_info= { 'c':'languageXmenu', 'v':'language-menu.html' }
    messages = ['languageXmenu', 'language-menu.html']
    #
    ctrl_template_url = "\'" + URL('languageXmenu' ) + "\'"

    # 
    flanguageXmenu0= Form(db.dflanguageXmenu0, dbio=False, formstyle=FormStyleBulma)
    if flanguageXmenu0.accepted:
        icon_type ='success' if insert_form_vars(flanguageXmenu0, db.dflanguageXmenu0) else 'info'
        return json2user(mess = str( flanguageXmenu0.form_name ), icon_type=icon_type )
    elif flanguageXmenu0.errors:
        print("flanguageXmenu0 has errors: %s" % (flanguageXmenu0.errors))
        return json2user(mess = str(flanguageXmenu0.form_name), icon_type = 'error')

    return locals()

@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed-sidebar.html', delimiters='[%[ ]]',))

def fixedXsidebar():
    ctrl_info= { 'c':'fixedXsidebar', 'v':'fixed-sidebar.html' }
    messages = ['fixedXsidebar', 'fixed-sidebar.html']
    #
    ctrl_template_url = "\'" + URL('fixedXsidebar' ) + "\'"

    # 
    ffixedXsidebar0= Form(db.dffixedXsidebar0, dbio=False, formstyle=FormStyleBulma)
    if ffixedXsidebar0.accepted:
        icon_type ='success' if insert_form_vars(ffixedXsidebar0, db.dffixedXsidebar0) else 'info'
        return json2user(mess = str( ffixedXsidebar0.form_name ), icon_type=icon_type )
    elif ffixedXsidebar0.errors:
        print("ffixedXsidebar0 has errors: %s" % (ffixedXsidebar0.errors))
        return json2user(mess = str(ffixedXsidebar0.form_name), icon_type = 'error')

    return locals()

@action('simpleXresults', method=["GET", "POST"] )
@action.uses(db, session, T, Template('simple-results.html', delimiters='[%[ ]]',))

def simpleXresults():
    ctrl_info= { 'c':'simpleXresults', 'v':'simple-results.html' }
    messages = ['simpleXresults', 'simple-results.html']
    #
    ctrl_template_url = "\'" + URL('simpleXresults' ) + "\'"

    # 
    fsimpleXresults0= Form(db.dfsimpleXresults0, dbio=False, formstyle=FormStyleBulma)
    if fsimpleXresults0.accepted:
        icon_type ='success' if insert_form_vars(fsimpleXresults0, db.dfsimpleXresults0) else 'info'
        return json2user(mess = str( fsimpleXresults0.form_name ), icon_type=icon_type )
    elif fsimpleXresults0.errors:
        print("fsimpleXresults0 has errors: %s" % (fsimpleXresults0.errors))
        return json2user(mess = str(fsimpleXresults0.form_name), icon_type = 'error')

    # 
    fsimpleXresults1= Form(db.dfsimpleXresults1, dbio=False, formstyle=FormStyleBulma)
    if fsimpleXresults1.accepted:
        icon_type ='success' if insert_form_vars(fsimpleXresults1, db.dfsimpleXresults1) else 'info'
        return json2user(mess = str( fsimpleXresults1.form_name ), icon_type=icon_type )
    elif fsimpleXresults1.errors:
        print("fsimpleXresults1 has errors: %s" % (fsimpleXresults1.errors))
        return json2user(mess = str(fsimpleXresults1.form_name), icon_type = 'error')

    return locals()

@action('projectXdetail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('project-detail.html', delimiters='[%[ ]]',))

def projectXdetail():
    ctrl_info= { 'c':'projectXdetail', 'v':'project-detail.html' }
    messages = ['projectXdetail', 'project-detail.html']
    #
    ctrl_template_url = "\'" + URL('projectXdetail' ) + "\'"

    # 
    fprojectXdetail0= Form(db.dfprojectXdetail0, dbio=False, formstyle=FormStyleBulma)
    if fprojectXdetail0.accepted:
        icon_type ='success' if insert_form_vars(fprojectXdetail0, db.dfprojectXdetail0) else 'info'
        return json2user(mess = str( fprojectXdetail0.form_name ), icon_type=icon_type )
    elif fprojectXdetail0.errors:
        print("fprojectXdetail0 has errors: %s" % (fprojectXdetail0.errors))
        return json2user(mess = str(fprojectXdetail0.form_name), icon_type = 'error')

    return locals()

@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forgot-password.html', delimiters='[%[ ]]',))

def forgotXpassword():
    ctrl_info= { 'c':'forgotXpassword', 'v':'forgot-password.html' }
    messages = ['forgotXpassword', 'forgot-password.html']
    #
    ctrl_template_url = "\'" + URL('forgotXpassword' ) + "\'"

    # 
    fforgotXpassword0= Form(db.dfforgotXpassword0, dbio=False, formstyle=FormStyleBulma)
    if fforgotXpassword0.accepted:
        icon_type ='success' if insert_form_vars(fforgotXpassword0, db.dfforgotXpassword0) else 'info'
        return json2user(mess = str( fforgotXpassword0.form_name ), icon_type=icon_type )
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s" % (fforgotXpassword0.errors))
        return json2user(mess = str(fforgotXpassword0.form_name), icon_type = 'error')

    return locals()

@action('topXnavXsidebar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('top-nav-sidebar.html', delimiters='[%[ ]]',))

def topXnavXsidebar():
    ctrl_info= { 'c':'topXnavXsidebar', 'v':'top-nav-sidebar.html' }
    messages = ['topXnavXsidebar', 'top-nav-sidebar.html']
    #
    ctrl_template_url = "\'" + URL('topXnavXsidebar' ) + "\'"

    # 
    ftopXnavXsidebar0= Form(db.dftopXnavXsidebar0, dbio=False, formstyle=FormStyleBulma)
    if ftopXnavXsidebar0.accepted:
        icon_type ='success' if insert_form_vars(ftopXnavXsidebar0, db.dftopXnavXsidebar0) else 'info'
        return json2user(mess = str( ftopXnavXsidebar0.form_name ), icon_type=icon_type )
    elif ftopXnavXsidebar0.errors:
        print("ftopXnavXsidebar0 has errors: %s" % (ftopXnavXsidebar0.errors))
        return json2user(mess = str(ftopXnavXsidebar0.form_name), icon_type = 'error')

    return locals()

@action('enhancedXresults', method=["GET", "POST"] )
@action.uses(db, session, T, Template('enhanced-results.html', delimiters='[%[ ]]',))

def enhancedXresults():
    ctrl_info= { 'c':'enhancedXresults', 'v':'enhanced-results.html' }
    messages = ['enhancedXresults', 'enhanced-results.html']
    #
    ctrl_template_url = "\'" + URL('enhancedXresults' ) + "\'"

    # 
    fenhancedXresults0= Form(db.dfenhancedXresults0, dbio=False, formstyle=FormStyleBulma)
    if fenhancedXresults0.accepted:
        icon_type ='success' if insert_form_vars(fenhancedXresults0, db.dfenhancedXresults0) else 'info'
        return json2user(mess = str( fenhancedXresults0.form_name ), icon_type=icon_type )
    elif fenhancedXresults0.errors:
        print("fenhancedXresults0 has errors: %s" % (fenhancedXresults0.errors))
        return json2user(mess = str(fenhancedXresults0.form_name), icon_type = 'error')

    # 
    fenhancedXresults1= Form(db.dfenhancedXresults1, dbio=False, formstyle=FormStyleBulma)
    if fenhancedXresults1.accepted:
        icon_type ='success' if insert_form_vars(fenhancedXresults1, db.dfenhancedXresults1) else 'info'
        return json2user(mess = str( fenhancedXresults1.form_name ), icon_type=icon_type )
    elif fenhancedXresults1.errors:
        print("fenhancedXresults1 has errors: %s" % (fenhancedXresults1.errors))
        return json2user(mess = str(fenhancedXresults1.form_name), icon_type = 'error')

    return locals()

@action('legacyXuserXmenu', method=["GET", "POST"] )
@action.uses(db, session, T, Template('legacy-user-menu.html', delimiters='[%[ ]]',))

def legacyXuserXmenu():
    ctrl_info= { 'c':'legacyXuserXmenu', 'v':'legacy-user-menu.html' }
    messages = ['legacyXuserXmenu', 'legacy-user-menu.html']
    #
    ctrl_template_url = "\'" + URL('legacyXuserXmenu' ) + "\'"

    # 
    flegacyXuserXmenu0= Form(db.dflegacyXuserXmenu0, dbio=False, formstyle=FormStyleBulma)
    if flegacyXuserXmenu0.accepted:
        icon_type ='success' if insert_form_vars(flegacyXuserXmenu0, db.dflegacyXuserXmenu0) else 'info'
        return json2user(mess = str( flegacyXuserXmenu0.form_name ), icon_type=icon_type )
    elif flegacyXuserXmenu0.errors:
        print("flegacyXuserXmenu0 has errors: %s" % (flegacyXuserXmenu0.errors))
        return json2user(mess = str(flegacyXuserXmenu0.form_name), icon_type = 'error')

    return locals()

@action('recoverXpassword', method=["GET", "POST"] )
@action.uses(db, session, T, Template('recover-password.html', delimiters='[%[ ]]',))

def recoverXpassword():
    ctrl_info= { 'c':'recoverXpassword', 'v':'recover-password.html' }
    messages = ['recoverXpassword', 'recover-password.html']
    #
    ctrl_template_url = "\'" + URL('recoverXpassword' ) + "\'"

    # 
    frecoverXpassword0= Form(db.dfrecoverXpassword0, dbio=False, formstyle=FormStyleBulma)
    if frecoverXpassword0.accepted:
        icon_type ='success' if insert_form_vars(frecoverXpassword0, db.dfrecoverXpassword0) else 'info'
        return json2user(mess = str( frecoverXpassword0.form_name ), icon_type=icon_type )
    elif frecoverXpassword0.errors:
        print("frecoverXpassword0 has errors: %s" % (frecoverXpassword0.errors))
        return json2user(mess = str(frecoverXpassword0.form_name), icon_type = 'error')

    return locals()

@action('collapsedXsidebar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('collapsed-sidebar.html', delimiters='[%[ ]]',))

def collapsedXsidebar():
    ctrl_info= { 'c':'collapsedXsidebar', 'v':'collapsed-sidebar.html' }
    messages = ['collapsedXsidebar', 'collapsed-sidebar.html']
    #
    ctrl_template_url = "\'" + URL('collapsedXsidebar' ) + "\'"

    # 
    fcollapsedXsidebar0= Form(db.dfcollapsedXsidebar0, dbio=False, formstyle=FormStyleBulma)
    if fcollapsedXsidebar0.accepted:
        icon_type ='success' if insert_form_vars(fcollapsedXsidebar0, db.dfcollapsedXsidebar0) else 'info'
        return json2user(mess = str( fcollapsedXsidebar0.form_name ), icon_type=icon_type )
    elif fcollapsedXsidebar0.errors:
        print("fcollapsedXsidebar0 has errors: %s" % (fcollapsedXsidebar0.errors))
        return json2user(mess = str(fcollapsedXsidebar0.form_name), icon_type = 'error')

    return locals()

@action('forgotXpasswordXv2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forgot-password-v2.html', delimiters='[%[ ]]',))

def forgotXpasswordXv2():
    ctrl_info= { 'c':'forgotXpasswordXv2', 'v':'forgot-password-v2.html' }
    messages = ['forgotXpasswordXv2', 'forgot-password-v2.html']
    #
    ctrl_template_url = "\'" + URL('forgotXpasswordXv2' ) + "\'"

    # 
    fforgotXpasswordXv20= Form(db.dfforgotXpasswordXv20, dbio=False, formstyle=FormStyleBulma)
    if fforgotXpasswordXv20.accepted:
        icon_type ='success' if insert_form_vars(fforgotXpasswordXv20, db.dfforgotXpasswordXv20) else 'info'
        return json2user(mess = str( fforgotXpasswordXv20.form_name ), icon_type=icon_type )
    elif fforgotXpasswordXv20.errors:
        print("fforgotXpasswordXv20 has errors: %s" % (fforgotXpasswordXv20.errors))
        return json2user(mess = str(fforgotXpasswordXv20.form_name), icon_type = 'error')

    return locals()

@action('recoverXpasswordXv2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('recover-password-v2.html', delimiters='[%[ ]]',))

def recoverXpasswordXv2():
    ctrl_info= { 'c':'recoverXpasswordXv2', 'v':'recover-password-v2.html' }
    messages = ['recoverXpasswordXv2', 'recover-password-v2.html']
    #
    ctrl_template_url = "\'" + URL('recoverXpasswordXv2' ) + "\'"

    # 
    frecoverXpasswordXv20= Form(db.dfrecoverXpasswordXv20, dbio=False, formstyle=FormStyleBulma)
    if frecoverXpasswordXv20.accepted:
        icon_type ='success' if insert_form_vars(frecoverXpasswordXv20, db.dfrecoverXpasswordXv20) else 'info'
        return json2user(mess = str( frecoverXpasswordXv20.form_name ), icon_type=icon_type )
    elif frecoverXpasswordXv20.errors:
        print("frecoverXpasswordXv20 has errors: %s" % (frecoverXpasswordXv20.errors))
        return json2user(mess = str(frecoverXpasswordXv20.form_name), icon_type = 'error')

    return locals()

@action('fixedXsidebarXcustom', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed-sidebar-custom.html', delimiters='[%[ ]]',))

def fixedXsidebarXcustom():
    ctrl_info= { 'c':'fixedXsidebarXcustom', 'v':'fixed-sidebar-custom.html' }
    messages = ['fixedXsidebarXcustom', 'fixed-sidebar-custom.html']
    #
    ctrl_template_url = "\'" + URL('fixedXsidebarXcustom' ) + "\'"

    # 
    ffixedXsidebarXcustom0= Form(db.dffixedXsidebarXcustom0, dbio=False, formstyle=FormStyleBulma)
    if ffixedXsidebarXcustom0.accepted:
        icon_type ='success' if insert_form_vars(ffixedXsidebarXcustom0, db.dffixedXsidebarXcustom0) else 'info'
        return json2user(mess = str( ffixedXsidebarXcustom0.form_name ), icon_type=icon_type )
    elif ffixedXsidebarXcustom0.errors:
        print("ffixedXsidebarXcustom0 has errors: %s" % (ffixedXsidebarXcustom0.errors))
        return json2user(mess = str(ffixedXsidebarXcustom0.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/lte3/api/test_table/
# curl -X  GET   http://localhost:8000/lte3/api/test_table/9
# curl -X DELETE  http://localhost:8000/lte3/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/lte3/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/lte3/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/lte3/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/lte3/api/test_table/
#  http         localhost:8000/lte3/api/test_table/9
#  http -f POST localhost:8000/lte3/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/lte3/api/test_table/2
#  http -f PUT localhost:8000/lte3/api/test_table/2 f0=111111 f1=2222222 f2=333333

#------------------------------------------------------------------------------------
#curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
#curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584






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

# this code is not necessary for modern py4web 
#
#        files_prefix = location + Glb["tte_path"]
#
#        location_2x = location + location + "/"
#        files_prefix_2x = files_prefix + files_prefix + "/"
#
#        def rm_bad_prefix(bad_prefix):
#            new_location = bottle.request.path.replace(bad_prefix, "", 1)
#            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
#            return new_location
#
#        if bottle.request.path.startswith(files_prefix_2x):
#            if len(bottle.request.path) > len(files_prefix_2x):
#                location = rm_bad_prefix(files_prefix)
#
#        elif bottle.request.path.startswith(location_2x):
#            if len(bottle.request.path) > len(location_2x):
#                location = rm_bad_prefix(location)

    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)


# -------------------- tabinfo: my backend ------------------------------------

from .atab_utils import mytab_grid
from .images_utils import ima_grid
from .upload_utils import p4wupload_file
from .tlist_utils import tlist 

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    menu = DIV(
               P( "test-demo for sql2table ( SQLTABLE from web2py)"),
               A( "sql2table", _role="button", _href=URL('mytab_grid', ),) ,
               A( "p4wupload_file", _role="button", _href=URL('p4wupload_file', ),) ,
               A( "tlist", _role="button", _href=URL('tlist', ),) ,
               A( "app_images", _role="button", _href=URL('ima_grid', ),) ,
              )
    return dict(message=message, menu=menu)

