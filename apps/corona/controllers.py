#
# py4web app, AI-biorex ported 26.04.2021 17:49:16 UTC+3, src: https://github.com/BootstrapDash/corona-free-dark-bootstrap-admin-template
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

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']
    #
    ctrl_template_url = "\'" + URL('index' ) + "\'"

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        icon_type ='success' if insert_form_vars(findex0, db.dfindex0) else 'info'
        return json2user(mess = str( findex0.form_name ), icon_type=icon_type )
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return json2user(mess = str(findex0.form_name), icon_type = 'error')

    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('buttons.html', delimiters='[%[ ]]',))

def buttons():
    ctrl_info= { 'c':'buttons', 'v':'buttons.html' }
    messages = ['buttons', 'buttons.html']
    #
    ctrl_template_url = "\'" + URL('buttons' ) + "\'"

    # 
    fbuttons0= Form(db.dfbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fbuttons0.accepted:
        icon_type ='success' if insert_form_vars(fbuttons0, db.dfbuttons0) else 'info'
        return json2user(mess = str( fbuttons0.form_name ), icon_type=icon_type )
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s" % (fbuttons0.errors))
        return json2user(mess = str(fbuttons0.form_name), icon_type = 'error')

    return locals()

@action('dropdowns', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dropdowns.html', delimiters='[%[ ]]',))

def dropdowns():
    ctrl_info= { 'c':'dropdowns', 'v':'dropdowns.html' }
    messages = ['dropdowns', 'dropdowns.html']
    #
    ctrl_template_url = "\'" + URL('dropdowns' ) + "\'"

    # 
    fdropdowns0= Form(db.dfdropdowns0, dbio=False, formstyle=FormStyleBulma)
    if fdropdowns0.accepted:
        icon_type ='success' if insert_form_vars(fdropdowns0, db.dfdropdowns0) else 'info'
        return json2user(mess = str( fdropdowns0.form_name ), icon_type=icon_type )
    elif fdropdowns0.errors:
        print("fdropdowns0 has errors: %s" % (fdropdowns0.errors))
        return json2user(mess = str(fdropdowns0.form_name), icon_type = 'error')

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typography.html', delimiters='[%[ ]]',))

def typography():
    ctrl_info= { 'c':'typography', 'v':'typography.html' }
    messages = ['typography', 'typography.html']
    #
    ctrl_template_url = "\'" + URL('typography' ) + "\'"

    # 
    ftypography0= Form(db.dftypography0, dbio=False, formstyle=FormStyleBulma)
    if ftypography0.accepted:
        icon_type ='success' if insert_form_vars(ftypography0, db.dftypography0) else 'info'
        return json2user(mess = str( ftypography0.form_name ), icon_type=icon_type )
    elif ftypography0.errors:
        print("ftypography0 has errors: %s" % (ftypography0.errors))
        return json2user(mess = str(ftypography0.form_name), icon_type = 'error')

    return locals()

@action('basicXelements', method=["GET", "POST"] )
@action.uses(db, session, T, Template('basic_elements.html', delimiters='[%[ ]]',))

def basicXelements():
    ctrl_info= { 'c':'basicXelements', 'v':'basic_elements.html' }
    messages = ['basicXelements', 'basic_elements.html']
    #
    ctrl_template_url = "\'" + URL('basicXelements' ) + "\'"

    # 
    fbasicXelements0= Form(db.dfbasicXelements0, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements0.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements0, db.dfbasicXelements0) else 'info'
        return json2user(mess = str( fbasicXelements0.form_name ), icon_type=icon_type )
    elif fbasicXelements0.errors:
        print("fbasicXelements0 has errors: %s" % (fbasicXelements0.errors))
        return json2user(mess = str(fbasicXelements0.form_name), icon_type = 'error')

    # 
    fbasicXelements1= Form(db.dfbasicXelements1, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements1.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements1, db.dfbasicXelements1) else 'info'
        return json2user(mess = str( fbasicXelements1.form_name ), icon_type=icon_type )
    elif fbasicXelements1.errors:
        print("fbasicXelements1 has errors: %s" % (fbasicXelements1.errors))
        return json2user(mess = str(fbasicXelements1.form_name), icon_type = 'error')

    # 
    fbasicXelements2= Form(db.dfbasicXelements2, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements2.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements2, db.dfbasicXelements2) else 'info'
        return json2user(mess = str( fbasicXelements2.form_name ), icon_type=icon_type )
    elif fbasicXelements2.errors:
        print("fbasicXelements2 has errors: %s" % (fbasicXelements2.errors))
        return json2user(mess = str(fbasicXelements2.form_name), icon_type = 'error')

    # 
    fbasicXelements3= Form(db.dfbasicXelements3, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements3.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements3, db.dfbasicXelements3) else 'info'
        return json2user(mess = str( fbasicXelements3.form_name ), icon_type=icon_type )
    elif fbasicXelements3.errors:
        print("fbasicXelements3 has errors: %s" % (fbasicXelements3.errors))
        return json2user(mess = str(fbasicXelements3.form_name), icon_type = 'error')

    # 
    fbasicXelements4= Form(db.dfbasicXelements4, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements4.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements4, db.dfbasicXelements4) else 'info'
        return json2user(mess = str( fbasicXelements4.form_name ), icon_type=icon_type )
    elif fbasicXelements4.errors:
        print("fbasicXelements4 has errors: %s" % (fbasicXelements4.errors))
        return json2user(mess = str(fbasicXelements4.form_name), icon_type = 'error')

    # 
    fbasicXelements5= Form(db.dfbasicXelements5, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements5.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements5, db.dfbasicXelements5) else 'info'
        return json2user(mess = str( fbasicXelements5.form_name ), icon_type=icon_type )
    elif fbasicXelements5.errors:
        print("fbasicXelements5 has errors: %s" % (fbasicXelements5.errors))
        return json2user(mess = str(fbasicXelements5.form_name), icon_type = 'error')

    # 
    fbasicXelements6= Form(db.dfbasicXelements6, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements6.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements6, db.dfbasicXelements6) else 'info'
        return json2user(mess = str( fbasicXelements6.form_name ), icon_type=icon_type )
    elif fbasicXelements6.errors:
        print("fbasicXelements6 has errors: %s" % (fbasicXelements6.errors))
        return json2user(mess = str(fbasicXelements6.form_name), icon_type = 'error')

    # 
    fbasicXelements7= Form(db.dfbasicXelements7, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements7.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements7, db.dfbasicXelements7) else 'info'
        return json2user(mess = str( fbasicXelements7.form_name ), icon_type=icon_type )
    elif fbasicXelements7.errors:
        print("fbasicXelements7 has errors: %s" % (fbasicXelements7.errors))
        return json2user(mess = str(fbasicXelements7.form_name), icon_type = 'error')

    return locals()

@action('basicXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('basic-table.html', delimiters='[%[ ]]',))

def basicXtable():
    ctrl_info= { 'c':'basicXtable', 'v':'basic-table.html' }
    messages = ['basicXtable', 'basic-table.html']
    #
    ctrl_template_url = "\'" + URL('basicXtable' ) + "\'"

    rows_tbasicXtable0= db(db.tbasicXtable0).select()
    rows_tbasicXtable1= db(db.tbasicXtable1).select()
    rows_tbasicXtable2= db(db.tbasicXtable2).select()
    rows_tbasicXtable3= db(db.tbasicXtable3).select()
    rows_tbasicXtable4= db(db.tbasicXtable4).select()
    rows_tbasicXtable5= db(db.tbasicXtable5).select()
    # 
    fbasicXtable0= Form(db.dfbasicXtable0, dbio=False, formstyle=FormStyleBulma)
    if fbasicXtable0.accepted:
        icon_type ='success' if insert_form_vars(fbasicXtable0, db.dfbasicXtable0) else 'info'
        return json2user(mess = str( fbasicXtable0.form_name ), icon_type=icon_type )
    elif fbasicXtable0.errors:
        print("fbasicXtable0 has errors: %s" % (fbasicXtable0.errors))
        return json2user(mess = str(fbasicXtable0.form_name), icon_type = 'error')

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

@action('mdi', method=["GET", "POST"] )
@action.uses(db, session, T, Template('mdi.html', delimiters='[%[ ]]',))

def mdi():
    ctrl_info= { 'c':'mdi', 'v':'mdi.html' }
    messages = ['mdi', 'mdi.html']
    #
    ctrl_template_url = "\'" + URL('mdi' ) + "\'"

    # 
    fmdi0= Form(db.dfmdi0, dbio=False, formstyle=FormStyleBulma)
    if fmdi0.accepted:
        icon_type ='success' if insert_form_vars(fmdi0, db.dfmdi0) else 'info'
        return json2user(mess = str( fmdi0.form_name ), icon_type=icon_type )
    elif fmdi0.errors:
        print("fmdi0 has errors: %s" % (fmdi0.errors))
        return json2user(mess = str(fmdi0.form_name), icon_type = 'error')

    return locals()

@action('blankXpage', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank-page.html', delimiters='[%[ ]]',))

def blankXpage():
    ctrl_info= { 'c':'blankXpage', 'v':'blank-page.html' }
    messages = ['blankXpage', 'blank-page.html']
    #
    ctrl_template_url = "\'" + URL('blankXpage' ) + "\'"

    # 
    fblankXpage0= Form(db.dfblankXpage0, dbio=False, formstyle=FormStyleBulma)
    if fblankXpage0.accepted:
        icon_type ='success' if insert_form_vars(fblankXpage0, db.dfblankXpage0) else 'info'
        return json2user(mess = str( fblankXpage0.form_name ), icon_type=icon_type )
    elif fblankXpage0.errors:
        print("fblankXpage0 has errors: %s" % (fblankXpage0.errors))
        return json2user(mess = str(fblankXpage0.form_name), icon_type = 'error')

    return locals()

@action('errorX404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('error-404.html', delimiters='[%[ ]]',))

def errorX404():
    ctrl_info= { 'c':'errorX404', 'v':'error-404.html' }
    messages = ['errorX404', 'error-404.html']
    #
    ctrl_template_url = "\'" + URL('errorX404' ) + "\'"

    return locals()

@action('errorX500', method=["GET", "POST"] )
@action.uses(db, session, T, Template('error-500.html', delimiters='[%[ ]]',))

def errorX500():
    ctrl_info= { 'c':'errorX500', 'v':'error-500.html' }
    messages = ['errorX500', 'error-500.html']
    #
    ctrl_template_url = "\'" + URL('errorX500' ) + "\'"

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
# curl -X  GET   http://localhost:8000/corona/api/test_table/
# curl -X  GET   http://localhost:8000/corona/api/test_table/9
# curl -X DELETE  http://localhost:8000/corona/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/corona/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/corona/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/corona/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/corona/api/test_table/
#  http         localhost:8000/corona/api/test_table/9
#  http -f POST localhost:8000/corona/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/corona/api/test_table/2
#  http -f PUT localhost:8000/corona/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

