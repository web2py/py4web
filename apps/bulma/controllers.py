#
# py4web app, AI-biorex ported 08.12.2020 08:51:34 UTC+3, src: https://github.com/BulmaTemplates/bulma-templates

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

@action('hero', method=["GET", "POST"] )
@action.uses(Template('hero.html', delimiters='[%[ ]]',), db, session, T,)

def hero():
    ctrl_info= "ctrl: hero, view: hero.html"
    page_url = "\'" + URL('hero' ) + "\'"
    messages = []

    return locals()

@action('tabs', method=["GET", "POST"] )
@action.uses(Template('tabs.html', delimiters='[%[ ]]',), db, session, T,)

def tabs():
    ctrl_info= "ctrl: tabs, view: tabs.html"
    page_url = "\'" + URL('tabs' ) + "\'"
    messages = []

    rows_ttabs0= db(db.ttabs0).select()
    return locals()

@action('blog', method=["GET", "POST"] )
@action.uses(Template('blog.html', delimiters='[%[ ]]',), db, session, T,)

def blog():
    ctrl_info= "ctrl: blog, view: blog.html"
    page_url = "\'" + URL('blog' ) + "\'"
    messages = []

    return locals()

@action('band', method=["GET", "POST"] )
@action.uses(Template('band.html', delimiters='[%[ ]]',), db, session, T,)

def band():
    ctrl_info= "ctrl: band, view: band.html"
    page_url = "\'" + URL('band' ) + "\'"
    messages = []

    fband0= Form(db.dfband0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fband0.accepted:
        prn_form_vars( fband0, db.dfband0 )
    elif fband0.errors:
        print("fband0 has errors: %s " % (fband0.errors))
 

    return locals()

@action('admin', method=["GET", "POST"] )
@action.uses(Template('admin.html', delimiters='[%[ ]]',), db, session, T,)

def admin():
    ctrl_info= "ctrl: admin, view: admin.html"
    page_url = "\'" + URL('admin' ) + "\'"
    messages = []

    rows_tadmin0= db(db.tadmin0).select()
    fadmin0= Form(db.dfadmin0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fadmin0.accepted:
        prn_form_vars( fadmin0, db.dfadmin0 )
    elif fadmin0.errors:
        print("fadmin0 has errors: %s " % (fadmin0.errors))
 

    fadmin1= Form(db.dfadmin1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fadmin1.accepted:
        prn_form_vars( fadmin1, db.dfadmin1 )
    elif fadmin1.errors:
        print("fadmin1 has errors: %s " % (fadmin1.errors))
 

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T,)

def inbox():
    ctrl_info= "ctrl: inbox, view: inbox.html"
    page_url = "\'" + URL('inbox' ) + "\'"
    messages = []

    return locals()

@action('forum', method=["GET", "POST"] )
@action.uses(Template('forum.html', delimiters='[%[ ]]',), db, session, T,)

def forum():
    ctrl_info= "ctrl: forum, view: forum.html"
    page_url = "\'" + URL('forum' ) + "\'"
    messages = []

    fforum0= Form(db.dfforum0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fforum0.accepted:
        prn_form_vars( fforum0, db.dfforum0 )
    elif fforum0.errors:
        print("fforum0 has errors: %s " % (fforum0.errors))
 

    return locals()

@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T,)

def login():
    ctrl_info= "ctrl: login, view: login.html"
    page_url = "\'" + URL('login' ) + "\'"
    messages = []

    flogin0= Form(db.dflogin0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if flogin0.accepted:
        prn_form_vars( flogin0, db.dflogin0 )
    elif flogin0.errors:
        print("flogin0 has errors: %s " % (flogin0.errors))
 

    return locals()

@action('cards', method=["GET", "POST"] )
@action.uses(Template('cards.html', delimiters='[%[ ]]',), db, session, T,)

def cards():
    ctrl_info= "ctrl: cards, view: cards.html"
    page_url = "\'" + URL('cards' ) + "\'"
    messages = []

    return locals()

@action('cover', method=["GET", "POST"] )
@action.uses(Template('cover.html', delimiters='[%[ ]]',), db, session, T,)

def cover():
    ctrl_info= "ctrl: cover, view: cover.html"
    page_url = "\'" + URL('cover' ) + "\'"
    messages = []

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    return locals()

@action('kanban', method=["GET", "POST"] )
@action.uses(Template('kanban.html', delimiters='[%[ ]]',), db, session, T,)

def kanban():
    ctrl_info= "ctrl: kanban, view: kanban.html"
    page_url = "\'" + URL('kanban' ) + "\'"
    messages = []

    fkanban0= Form(db.dfkanban0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fkanban0.accepted:
        prn_form_vars( fkanban0, db.dfkanban0 )
    elif fkanban0.errors:
        print("fkanban0 has errors: %s " % (fkanban0.errors))
 

    return locals()

@action('search', method=["GET", "POST"] )
@action.uses(Template('search.html', delimiters='[%[ ]]',), db, session, T,)

def search():
    ctrl_info= "ctrl: search, view: search.html"
    page_url = "\'" + URL('search' ) + "\'"
    messages = []

    fsearch0= Form(db.dfsearch0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fsearch0.accepted:
        prn_form_vars( fsearch0, db.dfsearch0 )
    elif fsearch0.errors:
        print("fsearch0 has errors: %s " % (fsearch0.errors))
 

    return locals()

@action('absurd', method=["GET", "POST"] )
@action.uses(Template('absurd.html', delimiters='[%[ ]]',), db, session, T,)

def absurd():
    ctrl_info= "ctrl: absurd, view: absurd.html"
    page_url = "\'" + URL('absurd' ) + "\'"
    messages = []

    return locals()

@action('landing', method=["GET", "POST"] )
@action.uses(Template('landing.html', delimiters='[%[ ]]',), db, session, T,)

def landing():
    ctrl_info= "ctrl: landing, view: landing.html"
    page_url = "\'" + URL('landing' ) + "\'"
    messages = []

    flanding0= Form(db.dflanding0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if flanding0.accepted:
        prn_form_vars( flanding0, db.dflanding0 )
    elif flanding0.errors:
        print("flanding0 has errors: %s " % (flanding0.errors))
 

    return locals()

@action('contact', method=["GET", "POST"] )
@action.uses(Template('contact.html', delimiters='[%[ ]]',), db, session, T,)

def contact():
    ctrl_info= "ctrl: contact, view: contact.html"
    page_url = "\'" + URL('contact' ) + "\'"
    messages = []

    fcontact0= Form(db.dfcontact0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fcontact0.accepted:
        prn_form_vars( fcontact0, db.dfcontact0 )
    elif fcontact0.errors:
        print("fcontact0 has errors: %s " % (fcontact0.errors))
 

    fcontact1= Form(db.dfcontact1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fcontact1.accepted:
        prn_form_vars( fcontact1, db.dfcontact1 )
    elif fcontact1.errors:
        print("fcontact1 has errors: %s " % (fcontact1.errors))
 

    fcontact2= Form(db.dfcontact2, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fcontact2.accepted:
        prn_form_vars( fcontact2, db.dfcontact2 )
    elif fcontact2.errors:
        print("fcontact2 has errors: %s " % (fcontact2.errors))
 

    return locals()

@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session, T,)

def register():
    ctrl_info= "ctrl: register, view: register.html"
    page_url = "\'" + URL('register' ) + "\'"
    messages = []

    fregister0= Form(db.dfregister0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fregister0.accepted:
        prn_form_vars( fregister0, db.dfregister0 )
    elif fregister0.errors:
        print("fregister0 has errors: %s " % (fregister0.errors))
 

    return locals()

@action('personal', method=["GET", "POST"] )
@action.uses(Template('personal.html', delimiters='[%[ ]]',), db, session, T,)

def personal():
    ctrl_info= "ctrl: personal, view: personal.html"
    page_url = "\'" + URL('personal' ) + "\'"
    messages = []

    rows_tpersonal0= db(db.tpersonal0).select()
    fpersonal0= Form(db.dfpersonal0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fpersonal0.accepted:
        prn_form_vars( fpersonal0, db.dfpersonal0 )
    elif fpersonal0.errors:
        print("fpersonal0 has errors: %s " % (fpersonal0.errors))
 

    fpersonal1= Form(db.dfpersonal1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fpersonal1.accepted:
        prn_form_vars( fpersonal1, db.dfpersonal1 )
    elif fpersonal1.errors:
        print("fpersonal1 has errors: %s " % (fpersonal1.errors))
 

    fpersonal2= Form(db.dfpersonal2, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fpersonal2.accepted:
        prn_form_vars( fpersonal2, db.dfpersonal2 )
    elif fpersonal2.errors:
        print("fpersonal2 has errors: %s " % (fpersonal2.errors))
 

    return locals()

@action('showcase', method=["GET", "POST"] )
@action.uses(Template('showcase.html', delimiters='[%[ ]]',), db, session, T,)

def showcase():
    ctrl_info= "ctrl: showcase, view: showcase.html"
    page_url = "\'" + URL('showcase' ) + "\'"
    messages = []

    fshowcase0= Form(db.dfshowcase0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fshowcase0.accepted:
        prn_form_vars( fshowcase0, db.dfshowcase0 )
    elif fshowcase0.errors:
        print("fshowcase0 has errors: %s " % (fshowcase0.errors))
 

    fshowcase1= Form(db.dfshowcase1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fshowcase1.accepted:
        prn_form_vars( fshowcase1, db.dfshowcase1 )
    elif fshowcase1.errors:
        print("fshowcase1 has errors: %s " % (fshowcase1.errors))
 

    fshowcase2= Form(db.dfshowcase2, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fshowcase2.accepted:
        prn_form_vars( fshowcase2, db.dfshowcase2 )
    elif fshowcase2.errors:
        print("fshowcase2 has errors: %s " % (fshowcase2.errors))
 

    return locals()

@action('cheatsheet', method=["GET", "POST"] )
@action.uses(Template('cheatsheet.html', delimiters='[%[ ]]',), db, session, T,)

def cheatsheet():
    ctrl_info= "ctrl: cheatsheet, view: cheatsheet.html"
    page_url = "\'" + URL('cheatsheet' ) + "\'"
    messages = []

    return locals()

@action('instaAlbum', method=["GET", "POST"] )
@action.uses(Template('instaAlbum.html', delimiters='[%[ ]]',), db, session, T,)

def instaAlbum():
    ctrl_info= "ctrl: instaAlbum, view: instaAlbum.html"
    page_url = "\'" + URL('instaAlbum' ) + "\'"
    messages = []

    finstaAlbum0= Form(db.dfinstaAlbum0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if finstaAlbum0.accepted:
        prn_form_vars( finstaAlbum0, db.dfinstaAlbum0 )
    elif finstaAlbum0.errors:
        print("finstaAlbum0 has errors: %s " % (finstaAlbum0.errors))
 

    finstaAlbum1= Form(db.dfinstaAlbum1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if finstaAlbum1.accepted:
        prn_form_vars( finstaAlbum1, db.dfinstaAlbum1 )
    elif finstaAlbum1.errors:
        print("finstaAlbum1 has errors: %s " % (finstaAlbum1.errors))
 

    finstaAlbum2= Form(db.dfinstaAlbum2, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if finstaAlbum2.accepted:
        prn_form_vars( finstaAlbum2, db.dfinstaAlbum2 )
    elif finstaAlbum2.errors:
        print("finstaAlbum2 has errors: %s " % (finstaAlbum2.errors))
 

    finstaAlbum3= Form(db.dfinstaAlbum3, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if finstaAlbum3.accepted:
        prn_form_vars( finstaAlbum3, db.dfinstaAlbum3 )
    elif finstaAlbum3.errors:
        print("finstaAlbum3 has errors: %s " % (finstaAlbum3.errors))
 

    return locals()

@action('ghostXblog', method=["GET", "POST"] )
@action.uses(Template('ghost-blog.html', delimiters='[%[ ]]',), db, session, T,)

def ghostXblog():
    ctrl_info= "ctrl: ghostXblog, view: ghost-blog.html"
    page_url = "\'" + URL('ghostXblog' ) + "\'"
    messages = []

    return locals()

@action('modalXcards', method=["GET", "POST"] )
@action.uses(Template('modal-cards.html', delimiters='[%[ ]]',), db, session, T,)

def modalXcards():
    ctrl_info= "ctrl: modalXcards, view: modal-cards.html"
    page_url = "\'" + URL('modalXcards' ) + "\'"
    messages = []

    return locals()

@action('blogXtailsaw', method=["GET", "POST"] )
@action.uses(Template('blog-tailsaw.html', delimiters='[%[ ]]',), db, session, T,)

def blogXtailsaw():
    ctrl_info= "ctrl: blogXtailsaw, view: blog-tailsaw.html"
    page_url = "\'" + URL('blogXtailsaw' ) + "\'"
    messages = []

    fblogXtailsaw0= Form(db.dfblogXtailsaw0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fblogXtailsaw0.accepted:
        prn_form_vars( fblogXtailsaw0, db.dfblogXtailsaw0 )
    elif fblogXtailsaw0.errors:
        print("fblogXtailsaw0 has errors: %s " % (fblogXtailsaw0.errors))
 

    fblogXtailsaw1= Form(db.dfblogXtailsaw1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fblogXtailsaw1.accepted:
        prn_form_vars( fblogXtailsaw1, db.dfblogXtailsaw1 )
    elif fblogXtailsaw1.errors:
        print("fblogXtailsaw1 has errors: %s " % (fblogXtailsaw1.errors))
 

    return locals()

@action('kanbanXsearchX', method=["GET", "POST"] )
@action.uses(Template('kanban[search].html', delimiters='[%[ ]]',), db, session, T,)

def kanbanXsearchX():
    ctrl_info= "ctrl: kanbanXsearchX, view: kanban[search].html"
    page_url = "\'" + URL('kanbanXsearchX' ) + "\'"
    messages = []

    fkanbanXsearchX0= Form(db.dfkanbanXsearchX0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fkanbanXsearchX0.accepted:
        prn_form_vars( fkanbanXsearchX0, db.dfkanbanXsearchX0 )
    elif fkanbanXsearchX0.errors:
        print("fkanbanXsearchX0 has errors: %s " % (fkanbanXsearchX0.errors))
 

    return locals()

@action('helloXparallax', method=["GET", "POST"] )
@action.uses(Template('hello-parallax.html', delimiters='[%[ ]]',), db, session, T,)

def helloXparallax():
    ctrl_info= "ctrl: helloXparallax, view: hello-parallax.html"
    page_url = "\'" + URL('helloXparallax' ) + "\'"
    messages = []

    fhelloXparallax0= Form(db.dfhelloXparallax0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fhelloXparallax0.accepted:
        prn_form_vars( fhelloXparallax0, db.dfhelloXparallax0 )
    elif fhelloXparallax0.errors:
        print("fhelloXparallax0 has errors: %s " % (fhelloXparallax0.errors))
 

    fhelloXparallax1= Form(db.dfhelloXparallax1, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fhelloXparallax1.accepted:
        prn_form_vars( fhelloXparallax1, db.dfhelloXparallax1 )
    elif fhelloXparallax1.errors:
        print("fhelloXparallax1 has errors: %s " % (fhelloXparallax1.errors))
 

    return locals()

@action('neumorphicXlogin', method=["GET", "POST"] )
@action.uses(Template('neumorphic-login.html', delimiters='[%[ ]]',), db, session, T,)

def neumorphicXlogin():
    ctrl_info= "ctrl: neumorphicXlogin, view: neumorphic-login.html"
    page_url = "\'" + URL('neumorphicXlogin' ) + "\'"
    messages = []

    fneumorphicXlogin0= Form(db.dfneumorphicXlogin0, dbio=False, keep_values=True, formstyle=FormStyleBulma)

    if fneumorphicXlogin0.accepted:
        prn_form_vars( fneumorphicXlogin0, db.dfneumorphicXlogin0 )
    elif fneumorphicXlogin0.errors:
        print("fneumorphicXlogin0 has errors: %s " % (fneumorphicXlogin0.errors))
 

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
# curl -X  GET   http://localhost:8000/bulma/api/test_table/
# curl -X  GET   http://localhost:8000/bulma/api/test_table/9
# curl -X DELETE  http://localhost:8000/bulma/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/bulma/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/bulma/api/test_table/
#  http         localhost:8000/bulma/api/test_table/9
#  http -f POST localhost:8000/bulma/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/bulma/api/test_table/2
#  http -f PUT localhost:8000/bulma/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

