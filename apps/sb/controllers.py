#
# py4web app, AI-biorex ported 26.11.2020 10:31:08 UTC+3
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

    fX4040= Form(db.dfX4040, dbio=False, formstyle=FormStyleBulma)

    if fX4040.accepted:
        prn_form_vars( fX4040, db.dfX4040 )
        return put_json_messages('accepted: ' + str( fX4040.form_name ))
    elif fX4040.errors:
        print("fX4040 has errors: %s" % (fX4040.errors))
        return put_json_messages('error: ' + str( fX4040.form_name ))
 

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(Template('blank.html', delimiters='[%[ ]]',), db, session, T,)

def blank():
    ctrl_info= "ctrl: blank, view: blank.html"
    page_url = "\'" + URL('blank' ) + "\'"
    messages = []

    fblank0= Form(db.dfblank0, dbio=False, formstyle=FormStyleBulma)

    if fblank0.accepted:
        prn_form_vars( fblank0, db.dfblank0 )
        return put_json_messages('accepted: ' + str( fblank0.form_name ))
    elif fblank0.errors:
        print("fblank0 has errors: %s" % (fblank0.errors))
        return put_json_messages('error: ' + str( fblank0.form_name ))
 

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
        prn_form_vars( findex0, db.dfindex0 )
        return put_json_messages('accepted: ' + str( findex0.form_name ))
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return put_json_messages('error: ' + str( findex0.form_name ))
 

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
 

    return locals()

@action('charts', method=["GET", "POST"] )
@action.uses(Template('charts.html', delimiters='[%[ ]]',), db, session, T,)

def charts():
    ctrl_info= "ctrl: charts, view: charts.html"
    page_url = "\'" + URL('charts' ) + "\'"
    messages = []

    fcharts0= Form(db.dfcharts0, dbio=False, formstyle=FormStyleBulma)

    if fcharts0.accepted:
        prn_form_vars( fcharts0, db.dfcharts0 )
        return put_json_messages('accepted: ' + str( fcharts0.form_name ))
    elif fcharts0.errors:
        print("fcharts0 has errors: %s" % (fcharts0.errors))
        return put_json_messages('error: ' + str( fcharts0.form_name ))
 

    return locals()

@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session, T,)

def tables():
    ctrl_info= "ctrl: tables, view: tables.html"
    page_url = "\'" + URL('tables' ) + "\'"
    messages = []

    rows_ttables0= db(db.ttables0).select()
    ftables0= Form(db.dftables0, dbio=False, formstyle=FormStyleBulma)

    if ftables0.accepted:
        prn_form_vars( ftables0, db.dftables0 )
        return put_json_messages('accepted: ' + str( ftables0.form_name ))
    elif ftables0.errors:
        print("ftables0 has errors: %s" % (ftables0.errors))
        return put_json_messages('error: ' + str( ftables0.form_name ))
 

    return locals()

@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session, T,)

def register():
    ctrl_info= "ctrl: register, view: register.html"
    page_url = "\'" + URL('register' ) + "\'"
    messages = []

    fregister0= Form(db.dfregister0, dbio=False, formstyle=FormStyleBulma)

    if fregister0.accepted:
        prn_form_vars( fregister0, db.dfregister0 )
        return put_json_messages('accepted: ' + str( fregister0.form_name ))
    elif fregister0.errors:
        print("fregister0 has errors: %s" % (fregister0.errors))
        return put_json_messages('error: ' + str( fregister0.form_name ))
 

    return locals()

@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session, T,)

def forgotXpassword():
    ctrl_info= "ctrl: forgotXpassword, view: forgot-password.html"
    page_url = "\'" + URL('forgotXpassword' ) + "\'"
    messages = []

    fforgotXpassword0= Form(db.dfforgotXpassword0, dbio=False, formstyle=FormStyleBulma)

    if fforgotXpassword0.accepted:
        prn_form_vars( fforgotXpassword0, db.dfforgotXpassword0 )
        return put_json_messages('accepted: ' + str( fforgotXpassword0.form_name ))
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s" % (fforgotXpassword0.errors))
        return put_json_messages('error: ' + str( fforgotXpassword0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/sb/api/test_table/
# curl -X  GET   http://localhost:8000/sb/api/test_table/9
# curl -X DELETE  http://localhost:8000/sb/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/sb/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/sb/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/sb/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/sb/api/test_table/
#  http         localhost:8000/sb/api/test_table/9
#  http -f POST localhost:8000/sb/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/sb/api/test_table/2
#  http -f PUT localhost:8000/sb/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

