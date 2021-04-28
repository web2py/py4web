#
# py4web app, AI-biorex ported 02.01.2021 13:24:58 UTC+3, src: https://github.com/dropways/deskapp

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

def prn_form_vars(myform, mytable):

    id_db = None; row_db = None; f0_fld = None; inserted = False

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_fld = myform.vars.get('f0', None )
    if (not f0_fld is None) and len(f0_fld):
        id_db = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if not id_db is None:
            row_db = mytable(id_db )

            if not row_db is None:
                if Glb['debug'] == True:
                     print( f'     inserted: \"{myform.vars.f0}\" into {mytable.f0}, id = {id_db}' )
                     print( f"     select  : \"{row_db.f0}\" from {mytable.f0}, id = {id_db}" )
                     print ()
                inserted =True
    else:
        if Glb['debug'] == True:
            print( f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
            print()

    return inserted
        
def put_json_messages(mess='mymess'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}'})

def if_accepted(myform, mytable):
    if myform.accepted:
        mess1 = 'inserted: ' if prn_form_vars( myform, mytable ) else 'accepted: '
        return put_json_messages(mess1 + str( myform.form_name ))
    elif myform.errors:
        print( f"{myform.form_name} has errors: {myform.errors}")
        return put_json_messages('error: ' + str( myform.form_name ))
    return None

# ---------------------- Controllers  ------------------------------------------------

@action('faq', method=["GET", "POST"] )
@action.uses(Template('faq.html', delimiters='[%[ ]]',), db, session, T,)

def faq():
    ctrl_info= { 'c':'faq', 'v':'faq.html' }
    page_url = "\'" + URL('faq' ) + "\'"
    messages = ['faq', 'faq.html']

    # 
    ffaq0= Form(db.dffaq0, dbio=False, formstyle=FormStyleBulma)
    if ffaq0.accepted:
        mess1='inserted: ' if prn_form_vars(ffaq0, db.dffaq0) else 'acceptd: '
        return put_json_messages(mess1 + str( ffaq0.form_name ))
    elif ffaq0.errors:
        print("ffaq0 has errors: %s" % (ffaq0.errors))
        return put_json_messages('error: ' + str( ffaq0.form_name ))

    return locals()

@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session, T,)

def X404():
    ctrl_info= { 'c':'X404', 'v':'404.html' }
    page_url = "\'" + URL('X404' ) + "\'"
    messages = ['X404', '404.html']

    return locals()

@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session, T,)

def X500():
    ctrl_info= { 'c':'X500', 'v':'500.html' }
    page_url = "\'" + URL('X500' ) + "\'"
    messages = ['X500', '500.html']

    return locals()

@action('X403', method=["GET", "POST"] )
@action.uses(Template('403.html', delimiters='[%[ ]]',), db, session, T,)

def X403():
    ctrl_info= { 'c':'X403', 'v':'403.html' }
    page_url = "\'" + URL('X403' ) + "\'"
    messages = ['X403', '403.html']

    return locals()

@action('X400', method=["GET", "POST"] )
@action.uses(Template('400.html', delimiters='[%[ ]]',), db, session, T,)

def X400():
    ctrl_info= { 'c':'X400', 'v':'400.html' }
    page_url = "\'" + URL('X400' ) + "\'"
    messages = ['X400', '400.html']

    return locals()

@action('X503', method=["GET", "POST"] )
@action.uses(Template('503.html', delimiters='[%[ ]]',), db, session, T,)

def X503():
    ctrl_info= { 'c':'X503', 'v':'503.html' }
    page_url = "\'" + URL('X503' ) + "\'"
    messages = ['X503', '503.html']

    return locals()

@action('chat', method=["GET", "POST"] )
@action.uses(Template('chat.html', delimiters='[%[ ]]',), db, session, T,)

def chat():
    ctrl_info= { 'c':'chat', 'v':'chat.html' }
    page_url = "\'" + URL('chat' ) + "\'"
    messages = ['chat', 'chat.html']

    # 
    fchat0= Form(db.dfchat0, dbio=False, formstyle=FormStyleBulma)
    if fchat0.accepted:
        mess1='inserted: ' if prn_form_vars(fchat0, db.dfchat0) else 'acceptd: '
        return put_json_messages(mess1 + str( fchat0.form_name ))
    elif fchat0.errors:
        print("fchat0 has errors: %s" % (fchat0.errors))
        return put_json_messages('error: ' + str( fchat0.form_name ))

    return locals()

@action('blog', method=["GET", "POST"] )
@action.uses(Template('blog.html', delimiters='[%[ ]]',), db, session, T,)

def blog():
    ctrl_info= { 'c':'blog', 'v':'blog.html' }
    page_url = "\'" + URL('blog' ) + "\'"
    messages = ['blog', 'blog.html']

    # 
    fblog0= Form(db.dfblog0, dbio=False, formstyle=FormStyleBulma)
    if fblog0.accepted:
        mess1='inserted: ' if prn_form_vars(fblog0, db.dfblog0) else 'acceptd: '
        return put_json_messages(mess1 + str( fblog0.form_name ))
    elif fblog0.errors:
        print("fblog0 has errors: %s" % (fblog0.errors))
        return put_json_messages('error: ' + str( fblog0.form_name ))

    return locals()

@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T,)

def login():
    ctrl_info= { 'c':'login', 'v':'login.html' }
    page_url = "\'" + URL('login' ) + "\'"
    messages = ['login', 'login.html']

    # 
    flogin0= Form(db.dflogin0, dbio=False, formstyle=FormStyleBulma)
    if flogin0.accepted:
        mess1='inserted: ' if prn_form_vars(flogin0, db.dflogin0) else 'acceptd: '
        return put_json_messages(mess1 + str( flogin0.form_name ))
    elif flogin0.errors:
        print("flogin0 has errors: %s" % (flogin0.errors))
        return put_json_messages('error: ' + str( flogin0.form_name ))

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    page_url = "\'" + URL('index' ) + "\'"
    messages = ['index', 'index.html']

    rows_tindex0= db(db.tindex0).select()
    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        mess1='inserted: ' if prn_form_vars(findex0, db.dfindex0) else 'acceptd: '
        return put_json_messages(mess1 + str( findex0.form_name ))
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return put_json_messages('error: ' + str( findex0.form_name ))

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(Template('blank.html', delimiters='[%[ ]]',), db, session, T,)

def blank():
    ctrl_info= { 'c':'blank', 'v':'blank.html' }
    page_url = "\'" + URL('blank' ) + "\'"
    messages = ['blank', 'blank.html']

    # 
    fblank0= Form(db.dfblank0, dbio=False, formstyle=FormStyleBulma)
    if fblank0.accepted:
        mess1='inserted: ' if prn_form_vars(fblank0, db.dfblank0) else 'acceptd: '
        return put_json_messages(mess1 + str( fblank0.form_name ))
    elif fblank0.errors:
        print("fblank0 has errors: %s" % (fblank0.errors))
        return put_json_messages('error: ' + str( fblank0.form_name ))

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session, T,)

def index3():
    ctrl_info= { 'c':'index3', 'v':'index3.html' }
    page_url = "\'" + URL('index3' ) + "\'"
    messages = ['index3', 'index3.html']

    rows_tindex30= db(db.tindex30).select()
    # 
    findex30= Form(db.dfindex30, dbio=False, formstyle=FormStyleBulma)
    if findex30.accepted:
        mess1='inserted: ' if prn_form_vars(findex30, db.dfindex30) else 'acceptd: '
        return put_json_messages(mess1 + str( findex30.form_name ))
    elif findex30.errors:
        print("findex30 has errors: %s" % (findex30.errors))
        return put_json_messages('error: ' + str( findex30.form_name ))

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session, T,)

def index2():
    ctrl_info= { 'c':'index2', 'v':'index2.html' }
    page_url = "\'" + URL('index2' ) + "\'"
    messages = ['index2', 'index2.html']

    # 
    findex20= Form(db.dfindex20, dbio=False, formstyle=FormStyleBulma)
    if findex20.accepted:
        mess1='inserted: ' if prn_form_vars(findex20, db.dfindex20) else 'acceptd: '
        return put_json_messages(mess1 + str( findex20.form_name ))
    elif findex20.errors:
        print("findex20 has errors: %s" % (findex20.errors))
        return put_json_messages('error: ' + str( findex20.form_name ))

    return locals()

@action('themify', method=["GET", "POST"] )
@action.uses(Template('themify.html', delimiters='[%[ ]]',), db, session, T,)

def themify():
    ctrl_info= { 'c':'themify', 'v':'themify.html' }
    page_url = "\'" + URL('themify' ) + "\'"
    messages = ['themify', 'themify.html']

    # 
    fthemify0= Form(db.dfthemify0, dbio=False, formstyle=FormStyleBulma)
    if fthemify0.accepted:
        mess1='inserted: ' if prn_form_vars(fthemify0, db.dfthemify0) else 'acceptd: '
        return put_json_messages(mess1 + str( fthemify0.form_name ))
    elif fthemify0.errors:
        print("fthemify0 has errors: %s" % (fthemify0.errors))
        return put_json_messages('error: ' + str( fthemify0.form_name ))

    return locals()

@action('uiXtabs', method=["GET", "POST"] )
@action.uses(Template('ui-tabs.html', delimiters='[%[ ]]',), db, session, T,)

def uiXtabs():
    ctrl_info= { 'c':'uiXtabs', 'v':'ui-tabs.html' }
    page_url = "\'" + URL('uiXtabs' ) + "\'"
    messages = ['uiXtabs', 'ui-tabs.html']

    # 
    fuiXtabs0= Form(db.dfuiXtabs0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtabs0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXtabs0, db.dfuiXtabs0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXtabs0.form_name ))
    elif fuiXtabs0.errors:
        print("fuiXtabs0 has errors: %s" % (fuiXtabs0.errors))
        return put_json_messages('error: ' + str( fuiXtabs0.form_name ))

    return locals()

@action('sitemap', method=["GET", "POST"] )
@action.uses(Template('sitemap.html', delimiters='[%[ ]]',), db, session, T,)

def sitemap():
    ctrl_info= { 'c':'sitemap', 'v':'sitemap.html' }
    page_url = "\'" + URL('sitemap' ) + "\'"
    messages = ['sitemap', 'sitemap.html']

    # 
    fsitemap0= Form(db.dfsitemap0, dbio=False, formstyle=FormStyleBulma)
    if fsitemap0.accepted:
        mess1='inserted: ' if prn_form_vars(fsitemap0, db.dfsitemap0) else 'acceptd: '
        return put_json_messages(mess1 + str( fsitemap0.form_name ))
    elif fsitemap0.errors:
        print("fsitemap0 has errors: %s" % (fsitemap0.errors))
        return put_json_messages('error: ' + str( fsitemap0.form_name ))

    return locals()

@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session, T,)

def profile():
    ctrl_info= { 'c':'profile', 'v':'profile.html' }
    page_url = "\'" + URL('profile' ) + "\'"
    messages = ['profile', 'profile.html']

    # 
    fprofile0= Form(db.dfprofile0, dbio=False, formstyle=FormStyleBulma)
    if fprofile0.accepted:
        mess1='inserted: ' if prn_form_vars(fprofile0, db.dfprofile0) else 'acceptd: '
        return put_json_messages(mess1 + str( fprofile0.form_name ))
    elif fprofile0.errors:
        print("fprofile0 has errors: %s" % (fprofile0.errors))
        return put_json_messages('error: ' + str( fprofile0.form_name ))

    # 
    fprofile1= Form(db.dfprofile1, dbio=False, formstyle=FormStyleBulma)
    if fprofile1.accepted:
        mess1='inserted: ' if prn_form_vars(fprofile1, db.dfprofile1) else 'acceptd: '
        return put_json_messages(mess1 + str( fprofile1.form_name ))
    elif fprofile1.errors:
        print("fprofile1 has errors: %s" % (fprofile1.errors))
        return put_json_messages('error: ' + str( fprofile1.form_name ))

    # 
    fprofile2= Form(db.dfprofile2, dbio=False, formstyle=FormStyleBulma)
    if fprofile2.accepted:
        mess1='inserted: ' if prn_form_vars(fprofile2, db.dfprofile2) else 'acceptd: '
        return put_json_messages(mess1 + str( fprofile2.form_name ))
    elif fprofile2.errors:
        print("fprofile2 has errors: %s" % (fprofile2.errors))
        return put_json_messages('error: ' + str( fprofile2.form_name ))

    # 
    fprofile3= Form(db.dfprofile3, dbio=False, formstyle=FormStyleBulma)
    if fprofile3.accepted:
        mess1='inserted: ' if prn_form_vars(fprofile3, db.dfprofile3) else 'acceptd: '
        return put_json_messages(mess1 + str( fprofile3.form_name ))
    elif fprofile3.errors:
        print("fprofile3 has errors: %s" % (fprofile3.errors))
        return put_json_messages('error: ' + str( fprofile3.form_name ))

    return locals()

@action('product', method=["GET", "POST"] )
@action.uses(Template('product.html', delimiters='[%[ ]]',), db, session, T,)

def product():
    ctrl_info= { 'c':'product', 'v':'product.html' }
    page_url = "\'" + URL('product' ) + "\'"
    messages = ['product', 'product.html']

    # 
    fproduct0= Form(db.dfproduct0, dbio=False, formstyle=FormStyleBulma)
    if fproduct0.accepted:
        mess1='inserted: ' if prn_form_vars(fproduct0, db.dfproduct0) else 'acceptd: '
        return put_json_messages(mess1 + str( fproduct0.form_name ))
    elif fproduct0.errors:
        print("fproduct0 has errors: %s" % (fproduct0.errors))
        return put_json_messages('error: ' + str( fproduct0.form_name ))

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session, T,)

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    page_url = "\'" + URL('invoice' ) + "\'"
    messages = ['invoice', 'invoice.html']

    # 
    finvoice0= Form(db.dfinvoice0, dbio=False, formstyle=FormStyleBulma)
    if finvoice0.accepted:
        mess1='inserted: ' if prn_form_vars(finvoice0, db.dfinvoice0) else 'acceptd: '
        return put_json_messages(mess1 + str( finvoice0.form_name ))
    elif finvoice0.errors:
        print("finvoice0 has errors: %s" % (finvoice0.errors))
        return put_json_messages('error: ' + str( finvoice0.form_name ))

    return locals()

@action('gallery', method=["GET", "POST"] )
@action.uses(Template('gallery.html', delimiters='[%[ ]]',), db, session, T,)

def gallery():
    ctrl_info= { 'c':'gallery', 'v':'gallery.html' }
    page_url = "\'" + URL('gallery' ) + "\'"
    messages = ['gallery', 'gallery.html']

    # 
    fgallery0= Form(db.dfgallery0, dbio=False, formstyle=FormStyleBulma)
    if fgallery0.accepted:
        mess1='inserted: ' if prn_form_vars(fgallery0, db.dfgallery0) else 'acceptd: '
        return put_json_messages(mess1 + str( fgallery0.form_name ))
    elif fgallery0.errors:
        print("fgallery0 has errors: %s" % (fgallery0.errors))
        return put_json_messages('error: ' + str( fgallery0.form_name ))

    return locals()

@action('ionicons', method=["GET", "POST"] )
@action.uses(Template('ionicons.html', delimiters='[%[ ]]',), db, session, T,)

def ionicons():
    ctrl_info= { 'c':'ionicons', 'v':'ionicons.html' }
    page_url = "\'" + URL('ionicons' ) + "\'"
    messages = ['ionicons', 'ionicons.html']

    # 
    fionicons0= Form(db.dfionicons0, dbio=False, formstyle=FormStyleBulma)
    if fionicons0.accepted:
        mess1='inserted: ' if prn_form_vars(fionicons0, db.dfionicons0) else 'acceptd: '
        return put_json_messages(mess1 + str( fionicons0.form_name ))
    elif fionicons0.errors:
        print("fionicons0 has errors: %s" % (fionicons0.errors))
        return put_json_messages('error: ' + str( fionicons0.form_name ))

    return locals()

@action('uiXcards', method=["GET", "POST"] )
@action.uses(Template('ui-cards.html', delimiters='[%[ ]]',), db, session, T,)

def uiXcards():
    ctrl_info= { 'c':'uiXcards', 'v':'ui-cards.html' }
    page_url = "\'" + URL('uiXcards' ) + "\'"
    messages = ['uiXcards', 'ui-cards.html']

    # 
    fuiXcards0= Form(db.dfuiXcards0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcards0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXcards0, db.dfuiXcards0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXcards0.form_name ))
    elif fuiXcards0.errors:
        print("fuiXcards0 has errors: %s" % (fuiXcards0.errors))
        return put_json_messages('error: ' + str( fuiXcards0.form_name ))

    return locals()

@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session, T,)

def register():
    ctrl_info= { 'c':'register', 'v':'register.html' }
    page_url = "\'" + URL('register' ) + "\'"
    messages = ['register', 'register.html']

    # 
    fregister0= Form(db.dfregister0, dbio=False, formstyle=FormStyleBulma)
    if fregister0.accepted:
        mess1='inserted: ' if prn_form_vars(fregister0, db.dfregister0) else 'acceptd: '
        return put_json_messages(mess1 + str( fregister0.form_name ))
    elif fregister0.errors:
        print("fregister0 has errors: %s" % (fregister0.errors))
        return put_json_messages('error: ' + str( fregister0.form_name ))

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(Template('calendar.html', delimiters='[%[ ]]',), db, session, T,)

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    page_url = "\'" + URL('calendar' ) + "\'"
    messages = ['calendar', 'calendar.html']

    # 
    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)
    if fcalendar0.accepted:
        mess1='inserted: ' if prn_form_vars(fcalendar0, db.dfcalendar0) else 'acceptd: '
        return put_json_messages(mess1 + str( fcalendar0.form_name ))
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s" % (fcalendar0.errors))
        return put_json_messages('error: ' + str( fcalendar0.form_name ))

    # 
    fcalendar1= Form(db.dfcalendar1, dbio=False, formstyle=FormStyleBulma)
    if fcalendar1.accepted:
        mess1='inserted: ' if prn_form_vars(fcalendar1, db.dfcalendar1) else 'acceptd: '
        return put_json_messages(mess1 + str( fcalendar1.form_name ))
    elif fcalendar1.errors:
        print("fcalendar1 has errors: %s" % (fcalendar1.errors))
        return put_json_messages('error: ' + str( fcalendar1.form_name ))

    return locals()

@action('uiXmodals', method=["GET", "POST"] )
@action.uses(Template('ui-modals.html', delimiters='[%[ ]]',), db, session, T,)

def uiXmodals():
    ctrl_info= { 'c':'uiXmodals', 'v':'ui-modals.html' }
    page_url = "\'" + URL('uiXmodals' ) + "\'"
    messages = ['uiXmodals', 'ui-modals.html']

    # 
    fuiXmodals0= Form(db.dfuiXmodals0, dbio=False, formstyle=FormStyleBulma)
    if fuiXmodals0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXmodals0, db.dfuiXmodals0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXmodals0.form_name ))
    elif fuiXmodals0.errors:
        print("fuiXmodals0 has errors: %s" % (fuiXmodals0.errors))
        return put_json_messages('error: ' + str( fuiXmodals0.form_name ))

    # 
    fuiXmodals1= Form(db.dfuiXmodals1, dbio=False, formstyle=FormStyleBulma)
    if fuiXmodals1.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXmodals1, db.dfuiXmodals1) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXmodals1.form_name ))
    elif fuiXmodals1.errors:
        print("fuiXmodals1 has errors: %s" % (fuiXmodals1.errors))
        return put_json_messages('error: ' + str( fuiXmodals1.form_name ))

    return locals()

@action('highchart', method=["GET", "POST"] )
@action.uses(Template('highchart.html', delimiters='[%[ ]]',), db, session, T,)

def highchart():
    ctrl_info= { 'c':'highchart', 'v':'highchart.html' }
    page_url = "\'" + URL('highchart' ) + "\'"
    messages = ['highchart', 'highchart.html']

    # 
    fhighchart0= Form(db.dfhighchart0, dbio=False, formstyle=FormStyleBulma)
    if fhighchart0.accepted:
        mess1='inserted: ' if prn_form_vars(fhighchart0, db.dfhighchart0) else 'acceptd: '
        return put_json_messages(mess1 + str( fhighchart0.form_name ))
    elif fhighchart0.errors:
        print("fhighchart0 has errors: %s" % (fhighchart0.errors))
        return put_json_messages('error: ' + str( fhighchart0.form_name ))

    return locals()

@action('datatable', method=["GET", "POST"] )
@action.uses(Template('datatable.html', delimiters='[%[ ]]',), db, session, T,)

def datatable():
    ctrl_info= { 'c':'datatable', 'v':'datatable.html' }
    page_url = "\'" + URL('datatable' ) + "\'"
    messages = ['datatable', 'datatable.html']

    rows_tdatatable0= db(db.tdatatable0).select()
    rows_tdatatable1= db(db.tdatatable1).select()
    rows_tdatatable2= db(db.tdatatable2).select()
    rows_tdatatable3= db(db.tdatatable3).select()
    # 
    fdatatable0= Form(db.dfdatatable0, dbio=False, formstyle=FormStyleBulma)
    if fdatatable0.accepted:
        mess1='inserted: ' if prn_form_vars(fdatatable0, db.dfdatatable0) else 'acceptd: '
        return put_json_messages(mess1 + str( fdatatable0.form_name ))
    elif fdatatable0.errors:
        print("fdatatable0 has errors: %s" % (fdatatable0.errors))
        return put_json_messages('error: ' + str( fdatatable0.form_name ))

    return locals()

@action('foundation', method=["GET", "POST"] )
@action.uses(Template('foundation.html', delimiters='[%[ ]]',), db, session, T,)

def foundation():
    ctrl_info= { 'c':'foundation', 'v':'foundation.html' }
    page_url = "\'" + URL('foundation' ) + "\'"
    messages = ['foundation', 'foundation.html']

    # 
    ffoundation0= Form(db.dffoundation0, dbio=False, formstyle=FormStyleBulma)
    if ffoundation0.accepted:
        mess1='inserted: ' if prn_form_vars(ffoundation0, db.dffoundation0) else 'acceptd: '
        return put_json_messages(mess1 + str( ffoundation0.form_name ))
    elif ffoundation0.errors:
        print("ffoundation0 has errors: %s" % (ffoundation0.errors))
        return put_json_messages('error: ' + str( ffoundation0.form_name ))

    return locals()

@action('uiXbuttons', method=["GET", "POST"] )
@action.uses(Template('ui-buttons.html', delimiters='[%[ ]]',), db, session, T,)

def uiXbuttons():
    ctrl_info= { 'c':'uiXbuttons', 'v':'ui-buttons.html' }
    page_url = "\'" + URL('uiXbuttons' ) + "\'"
    messages = ['uiXbuttons', 'ui-buttons.html']

    # 
    fuiXbuttons0= Form(db.dfuiXbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fuiXbuttons0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXbuttons0, db.dfuiXbuttons0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXbuttons0.form_name ))
    elif fuiXbuttons0.errors:
        print("fuiXbuttons0 has errors: %s" % (fuiXbuttons0.errors))
        return put_json_messages('error: ' + str( fuiXbuttons0.form_name ))

    return locals()

@action('knobXchart', method=["GET", "POST"] )
@action.uses(Template('knob-chart.html', delimiters='[%[ ]]',), db, session, T,)

def knobXchart():
    ctrl_info= { 'c':'knobXchart', 'v':'knob-chart.html' }
    page_url = "\'" + URL('knobXchart' ) + "\'"
    messages = ['knobXchart', 'knob-chart.html']

    # 
    fknobXchart0= Form(db.dfknobXchart0, dbio=False, formstyle=FormStyleBulma)
    if fknobXchart0.accepted:
        mess1='inserted: ' if prn_form_vars(fknobXchart0, db.dfknobXchart0) else 'acceptd: '
        return put_json_messages(mess1 + str( fknobXchart0.form_name ))
    elif fknobXchart0.errors:
        print("fknobXchart0 has errors: %s" % (fknobXchart0.errors))
        return put_json_messages('error: ' + str( fknobXchart0.form_name ))

    return locals()

@action('jvectormap', method=["GET", "POST"] )
@action.uses(Template('jvectormap.html', delimiters='[%[ ]]',), db, session, T,)

def jvectormap():
    ctrl_info= { 'c':'jvectormap', 'v':'jvectormap.html' }
    page_url = "\'" + URL('jvectormap' ) + "\'"
    messages = ['jvectormap', 'jvectormap.html']

    # 
    fjvectormap0= Form(db.dfjvectormap0, dbio=False, formstyle=FormStyleBulma)
    if fjvectormap0.accepted:
        mess1='inserted: ' if prn_form_vars(fjvectormap0, db.dfjvectormap0) else 'acceptd: '
        return put_json_messages(mess1 + str( fjvectormap0.form_name ))
    elif fjvectormap0.errors:
        print("fjvectormap0 has errors: %s" % (fjvectormap0.errors))
        return put_json_messages('error: ' + str( fjvectormap0.form_name ))

    return locals()

@action('formXbasic', method=["GET", "POST"] )
@action.uses(Template('form-basic.html', delimiters='[%[ ]]',), db, session, T,)

def formXbasic():
    ctrl_info= { 'c':'formXbasic', 'v':'form-basic.html' }
    page_url = "\'" + URL('formXbasic' ) + "\'"
    messages = ['formXbasic', 'form-basic.html']

    # 
    fformXbasic0= Form(db.dfformXbasic0, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic0.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic0, db.dfformXbasic0) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic0.form_name ))
    elif fformXbasic0.errors:
        print("fformXbasic0 has errors: %s" % (fformXbasic0.errors))
        return put_json_messages('error: ' + str( fformXbasic0.form_name ))

    # 
    fformXbasic1= Form(db.dfformXbasic1, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic1.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic1, db.dfformXbasic1) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic1.form_name ))
    elif fformXbasic1.errors:
        print("fformXbasic1 has errors: %s" % (fformXbasic1.errors))
        return put_json_messages('error: ' + str( fformXbasic1.form_name ))

    # 
    fformXbasic2= Form(db.dfformXbasic2, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic2.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic2, db.dfformXbasic2) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic2.form_name ))
    elif fformXbasic2.errors:
        print("fformXbasic2 has errors: %s" % (fformXbasic2.errors))
        return put_json_messages('error: ' + str( fformXbasic2.form_name ))

    # 
    fformXbasic3= Form(db.dfformXbasic3, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic3.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic3, db.dfformXbasic3) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic3.form_name ))
    elif fformXbasic3.errors:
        print("fformXbasic3 has errors: %s" % (fformXbasic3.errors))
        return put_json_messages('error: ' + str( fformXbasic3.form_name ))

    # 
    fformXbasic4= Form(db.dfformXbasic4, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic4.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic4, db.dfformXbasic4) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic4.form_name ))
    elif fformXbasic4.errors:
        print("fformXbasic4 has errors: %s" % (fformXbasic4.errors))
        return put_json_messages('error: ' + str( fformXbasic4.form_name ))

    # 
    fformXbasic5= Form(db.dfformXbasic5, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic5.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic5, db.dfformXbasic5) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic5.form_name ))
    elif fformXbasic5.errors:
        print("fformXbasic5 has errors: %s" % (fformXbasic5.errors))
        return put_json_messages('error: ' + str( fformXbasic5.form_name ))

    # 
    fformXbasic6= Form(db.dfformXbasic6, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic6.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic6, db.dfformXbasic6) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic6.form_name ))
    elif fformXbasic6.errors:
        print("fformXbasic6 has errors: %s" % (fformXbasic6.errors))
        return put_json_messages('error: ' + str( fformXbasic6.form_name ))

    # 
    fformXbasic7= Form(db.dfformXbasic7, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic7.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic7, db.dfformXbasic7) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic7.form_name ))
    elif fformXbasic7.errors:
        print("fformXbasic7 has errors: %s" % (fformXbasic7.errors))
        return put_json_messages('error: ' + str( fformXbasic7.form_name ))

    # 
    fformXbasic8= Form(db.dfformXbasic8, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic8.accepted:
        mess1='inserted: ' if prn_form_vars(fformXbasic8, db.dfformXbasic8) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXbasic8.form_name ))
    elif fformXbasic8.errors:
        print("fformXbasic8 has errors: %s" % (fformXbasic8.errors))
        return put_json_messages('error: ' + str( fformXbasic8.form_name ))

    return locals()

@action('apexcharts', method=["GET", "POST"] )
@action.uses(Template('apexcharts.html', delimiters='[%[ ]]',), db, session, T,)

def apexcharts():
    ctrl_info= { 'c':'apexcharts', 'v':'apexcharts.html' }
    page_url = "\'" + URL('apexcharts' ) + "\'"
    messages = ['apexcharts', 'apexcharts.html']

    # 
    fapexcharts0= Form(db.dfapexcharts0, dbio=False, formstyle=FormStyleBulma)
    if fapexcharts0.accepted:
        mess1='inserted: ' if prn_form_vars(fapexcharts0, db.dfapexcharts0) else 'acceptd: '
        return put_json_messages(mess1 + str( fapexcharts0.form_name ))
    elif fapexcharts0.errors:
        print("fapexcharts0 has errors: %s" % (fapexcharts0.errors))
        return put_json_messages('error: ' + str( fapexcharts0.form_name ))

    return locals()

@action('uiXtimeline', method=["GET", "POST"] )
@action.uses(Template('ui-timeline.html', delimiters='[%[ ]]',), db, session, T,)

def uiXtimeline():
    ctrl_info= { 'c':'uiXtimeline', 'v':'ui-timeline.html' }
    page_url = "\'" + URL('uiXtimeline' ) + "\'"
    messages = ['uiXtimeline', 'ui-timeline.html']

    # 
    fuiXtimeline0= Form(db.dfuiXtimeline0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtimeline0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXtimeline0, db.dfuiXtimeline0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXtimeline0.form_name ))
    elif fuiXtimeline0.errors:
        print("fuiXtimeline0 has errors: %s" % (fuiXtimeline0.errors))
        return put_json_messages('error: ' + str( fuiXtimeline0.form_name ))

    return locals()

@action('uiXcarousel', method=["GET", "POST"] )
@action.uses(Template('ui-carousel.html', delimiters='[%[ ]]',), db, session, T,)

def uiXcarousel():
    ctrl_info= { 'c':'uiXcarousel', 'v':'ui-carousel.html' }
    page_url = "\'" + URL('uiXcarousel' ) + "\'"
    messages = ['uiXcarousel', 'ui-carousel.html']

    # 
    fuiXcarousel0= Form(db.dfuiXcarousel0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcarousel0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXcarousel0, db.dfuiXcarousel0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXcarousel0.form_name ))
    elif fuiXcarousel0.errors:
        print("fuiXcarousel0 has errors: %s" % (fuiXcarousel0.errors))
        return put_json_messages('error: ' + str( fuiXcarousel0.form_name ))

    return locals()

@action('formXwizard', method=["GET", "POST"] )
@action.uses(Template('form-wizard.html', delimiters='[%[ ]]',), db, session, T,)

def formXwizard():
    ctrl_info= { 'c':'formXwizard', 'v':'form-wizard.html' }
    page_url = "\'" + URL('formXwizard' ) + "\'"
    messages = ['formXwizard', 'form-wizard.html']

    # 
    fformXwizard0= Form(db.dfformXwizard0, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard0.accepted:
        mess1='inserted: ' if prn_form_vars(fformXwizard0, db.dfformXwizard0) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXwizard0.form_name ))
    elif fformXwizard0.errors:
        print("fformXwizard0 has errors: %s" % (fformXwizard0.errors))
        return put_json_messages('error: ' + str( fformXwizard0.form_name ))

    # 
    fformXwizard1= Form(db.dfformXwizard1, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard1.accepted:
        mess1='inserted: ' if prn_form_vars(fformXwizard1, db.dfformXwizard1) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXwizard1.form_name ))
    elif fformXwizard1.errors:
        print("fformXwizard1 has errors: %s" % (fformXwizard1.errors))
        return put_json_messages('error: ' + str( fformXwizard1.form_name ))

    # 
    fformXwizard2= Form(db.dfformXwizard2, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard2.accepted:
        mess1='inserted: ' if prn_form_vars(fformXwizard2, db.dfformXwizard2) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXwizard2.form_name ))
    elif fformXwizard2.errors:
        print("fformXwizard2 has errors: %s" % (fformXwizard2.errors))
        return put_json_messages('error: ' + str( fformXwizard2.form_name ))

    return locals()

@action('customXicon', method=["GET", "POST"] )
@action.uses(Template('custom-icon.html', delimiters='[%[ ]]',), db, session, T,)

def customXicon():
    ctrl_info= { 'c':'customXicon', 'v':'custom-icon.html' }
    page_url = "\'" + URL('customXicon' ) + "\'"
    messages = ['customXicon', 'custom-icon.html']

    # 
    fcustomXicon0= Form(db.dfcustomXicon0, dbio=False, formstyle=FormStyleBulma)
    if fcustomXicon0.accepted:
        mess1='inserted: ' if prn_form_vars(fcustomXicon0, db.dfcustomXicon0) else 'acceptd: '
        return put_json_messages(mess1 + str( fcustomXicon0.form_name ))
    elif fcustomXicon0.errors:
        print("fcustomXicon0 has errors: %s" % (fcustomXicon0.errors))
        return put_json_messages('error: ' + str( fcustomXicon0.form_name ))

    return locals()

@action('basicXtable', method=["GET", "POST"] )
@action.uses(Template('basic-table.html', delimiters='[%[ ]]',), db, session, T,)

def basicXtable():
    ctrl_info= { 'c':'basicXtable', 'v':'basic-table.html' }
    page_url = "\'" + URL('basicXtable' ) + "\'"
    messages = ['basicXtable', 'basic-table.html']

    rows_tbasicXtable0= db(db.tbasicXtable0).select()
    rows_tbasicXtable1= db(db.tbasicXtable1).select()
    rows_tbasicXtable2= db(db.tbasicXtable2).select()
    rows_tbasicXtable3= db(db.tbasicXtable3).select()
    rows_tbasicXtable4= db(db.tbasicXtable4).select()
    rows_tbasicXtable5= db(db.tbasicXtable5).select()
    rows_tbasicXtable6= db(db.tbasicXtable6).select()
    rows_tbasicXtable7= db(db.tbasicXtable7).select()
    rows_tbasicXtable8= db(db.tbasicXtable8).select()
    rows_tbasicXtable9= db(db.tbasicXtable9).select()
    # 
    fbasicXtable0= Form(db.dfbasicXtable0, dbio=False, formstyle=FormStyleBulma)
    if fbasicXtable0.accepted:
        mess1='inserted: ' if prn_form_vars(fbasicXtable0, db.dfbasicXtable0) else 'acceptd: '
        return put_json_messages(mess1 + str( fbasicXtable0.form_name ))
    elif fbasicXtable0.errors:
        print("fbasicXtable0 has errors: %s" % (fbasicXtable0.errors))
        return put_json_messages('error: ' + str( fbasicXtable0.form_name ))

    return locals()

@action('blogXdetail', method=["GET", "POST"] )
@action.uses(Template('blog-detail.html', delimiters='[%[ ]]',), db, session, T,)

def blogXdetail():
    ctrl_info= { 'c':'blogXdetail', 'v':'blog-detail.html' }
    page_url = "\'" + URL('blogXdetail' ) + "\'"
    messages = ['blogXdetail', 'blog-detail.html']

    # 
    fblogXdetail0= Form(db.dfblogXdetail0, dbio=False, formstyle=FormStyleBulma)
    if fblogXdetail0.accepted:
        mess1='inserted: ' if prn_form_vars(fblogXdetail0, db.dfblogXdetail0) else 'acceptd: '
        return put_json_messages(mess1 + str( fblogXdetail0.form_name ))
    elif fblogXdetail0.errors:
        print("fblogXdetail0 has errors: %s" % (fblogXdetail0.errors))
        return put_json_messages('error: ' + str( fblogXdetail0.form_name ))

    return locals()

@action('fontXawesome', method=["GET", "POST"] )
@action.uses(Template('font-awesome.html', delimiters='[%[ ]]',), db, session, T,)

def fontXawesome():
    ctrl_info= { 'c':'fontXawesome', 'v':'font-awesome.html' }
    page_url = "\'" + URL('fontXawesome' ) + "\'"
    messages = ['fontXawesome', 'font-awesome.html']

    # 
    ffontXawesome0= Form(db.dffontXawesome0, dbio=False, formstyle=FormStyleBulma)
    if ffontXawesome0.accepted:
        mess1='inserted: ' if prn_form_vars(ffontXawesome0, db.dffontXawesome0) else 'acceptd: '
        return put_json_messages(mess1 + str( ffontXawesome0.form_name ))
    elif ffontXawesome0.errors:
        print("ffontXawesome0 has errors: %s" % (ffontXawesome0.errors))
        return put_json_messages('error: ' + str( ffontXawesome0.form_name ))

    return locals()

@action('videoXplayer', method=["GET", "POST"] )
@action.uses(Template('video-player.html', delimiters='[%[ ]]',), db, session, T,)

def videoXplayer():
    ctrl_info= { 'c':'videoXplayer', 'v':'video-player.html' }
    page_url = "\'" + URL('videoXplayer' ) + "\'"
    messages = ['videoXplayer', 'video-player.html']

    # 
    fvideoXplayer0= Form(db.dfvideoXplayer0, dbio=False, formstyle=FormStyleBulma)
    if fvideoXplayer0.accepted:
        mess1='inserted: ' if prn_form_vars(fvideoXplayer0, db.dfvideoXplayer0) else 'acceptd: '
        return put_json_messages(mess1 + str( fvideoXplayer0.form_name ))
    elif fvideoXplayer0.errors:
        print("fvideoXplayer0 has errors: %s" % (fvideoXplayer0.errors))
        return put_json_messages('error: ' + str( fvideoXplayer0.form_name ))

    return locals()

@action('introduction', method=["GET", "POST"] )
@action.uses(Template('introduction.html', delimiters='[%[ ]]',), db, session, T,)

def introduction():
    ctrl_info= { 'c':'introduction', 'v':'introduction.html' }
    page_url = "\'" + URL('introduction' ) + "\'"
    messages = ['introduction', 'introduction.html']

    # 
    fintroduction0= Form(db.dfintroduction0, dbio=False, formstyle=FormStyleBulma)
    if fintroduction0.accepted:
        mess1='inserted: ' if prn_form_vars(fintroduction0, db.dfintroduction0) else 'acceptd: '
        return put_json_messages(mess1 + str( fintroduction0.form_name ))
    elif fintroduction0.errors:
        print("fintroduction0 has errors: %s" % (fintroduction0.errors))
        return put_json_messages('error: ' + str( fintroduction0.form_name ))

    return locals()

@action('html5Xeditor', method=["GET", "POST"] )
@action.uses(Template('html5-editor.html', delimiters='[%[ ]]',), db, session, T,)

def html5Xeditor():
    ctrl_info= { 'c':'html5Xeditor', 'v':'html5-editor.html' }
    page_url = "\'" + URL('html5Xeditor' ) + "\'"
    messages = ['html5Xeditor', 'html5-editor.html']

    # 
    fhtml5Xeditor0= Form(db.dfhtml5Xeditor0, dbio=False, formstyle=FormStyleBulma)
    if fhtml5Xeditor0.accepted:
        mess1='inserted: ' if prn_form_vars(fhtml5Xeditor0, db.dfhtml5Xeditor0) else 'acceptd: '
        return put_json_messages(mess1 + str( fhtml5Xeditor0.form_name ))
    elif fhtml5Xeditor0.errors:
        print("fhtml5Xeditor0 has errors: %s" % (fhtml5Xeditor0.errors))
        return put_json_messages('error: ' + str( fhtml5Xeditor0.form_name ))

    return locals()

@action('formXpickers', method=["GET", "POST"] )
@action.uses(Template('form-pickers.html', delimiters='[%[ ]]',), db, session, T,)

def formXpickers():
    ctrl_info= { 'c':'formXpickers', 'v':'form-pickers.html' }
    page_url = "\'" + URL('formXpickers' ) + "\'"
    messages = ['formXpickers', 'form-pickers.html']

    # 
    fformXpickers0= Form(db.dfformXpickers0, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers0.accepted:
        mess1='inserted: ' if prn_form_vars(fformXpickers0, db.dfformXpickers0) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXpickers0.form_name ))
    elif fformXpickers0.errors:
        print("fformXpickers0 has errors: %s" % (fformXpickers0.errors))
        return put_json_messages('error: ' + str( fformXpickers0.form_name ))

    # 
    fformXpickers1= Form(db.dfformXpickers1, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers1.accepted:
        mess1='inserted: ' if prn_form_vars(fformXpickers1, db.dfformXpickers1) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXpickers1.form_name ))
    elif fformXpickers1.errors:
        print("fformXpickers1 has errors: %s" % (fformXpickers1.errors))
        return put_json_messages('error: ' + str( fformXpickers1.form_name ))

    # 
    fformXpickers2= Form(db.dfformXpickers2, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers2.accepted:
        mess1='inserted: ' if prn_form_vars(fformXpickers2, db.dfformXpickers2) else 'acceptd: '
        return put_json_messages(mess1 + str( fformXpickers2.form_name ))
    elif fformXpickers2.errors:
        print("fformXpickers2 has errors: %s" % (fformXpickers2.errors))
        return put_json_messages('error: ' + str( fformXpickers2.form_name ))

    return locals()

@action('uiXtypography', method=["GET", "POST"] )
@action.uses(Template('ui-typography.html', delimiters='[%[ ]]',), db, session, T,)

def uiXtypography():
    ctrl_info= { 'c':'uiXtypography', 'v':'ui-typography.html' }
    page_url = "\'" + URL('uiXtypography' ) + "\'"
    messages = ['uiXtypography', 'ui-typography.html']

    # 
    fuiXtypography0= Form(db.dfuiXtypography0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtypography0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXtypography0, db.dfuiXtypography0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXtypography0.form_name ))
    elif fuiXtypography0.errors:
        print("fuiXtypography0 has errors: %s" % (fuiXtypography0.errors))
        return put_json_messages('error: ' + str( fuiXtypography0.form_name ))

    return locals()

@action('uiXlistXgroup', method=["GET", "POST"] )
@action.uses(Template('ui-list-group.html', delimiters='[%[ ]]',), db, session, T,)

def uiXlistXgroup():
    ctrl_info= { 'c':'uiXlistXgroup', 'v':'ui-list-group.html' }
    page_url = "\'" + URL('uiXlistXgroup' ) + "\'"
    messages = ['uiXlistXgroup', 'ui-list-group.html']

    # 
    fuiXlistXgroup0= Form(db.dfuiXlistXgroup0, dbio=False, formstyle=FormStyleBulma)
    if fuiXlistXgroup0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXlistXgroup0, db.dfuiXlistXgroup0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXlistXgroup0.form_name ))
    elif fuiXlistXgroup0.errors:
        print("fuiXlistXgroup0 has errors: %s" % (fuiXlistXgroup0.errors))
        return put_json_messages('error: ' + str( fuiXlistXgroup0.form_name ))

    return locals()

@action('pricingXtable', method=["GET", "POST"] )
@action.uses(Template('pricing-table.html', delimiters='[%[ ]]',), db, session, T,)

def pricingXtable():
    ctrl_info= { 'c':'pricingXtable', 'v':'pricing-table.html' }
    page_url = "\'" + URL('pricingXtable' ) + "\'"
    messages = ['pricingXtable', 'pricing-table.html']

    # 
    fpricingXtable0= Form(db.dfpricingXtable0, dbio=False, formstyle=FormStyleBulma)
    if fpricingXtable0.accepted:
        mess1='inserted: ' if prn_form_vars(fpricingXtable0, db.dfpricingXtable0) else 'acceptd: '
        return put_json_messages(mess1 + str( fpricingXtable0.form_name ))
    elif fpricingXtable0.errors:
        print("fpricingXtable0 has errors: %s" % (fpricingXtable0.errors))
        return put_json_messages('error: ' + str( fpricingXtable0.form_name ))

    return locals()

@action('imageXcropper', method=["GET", "POST"] )
@action.uses(Template('image-cropper.html', delimiters='[%[ ]]',), db, session, T,)

def imageXcropper():
    ctrl_info= { 'c':'imageXcropper', 'v':'image-cropper.html' }
    page_url = "\'" + URL('imageXcropper' ) + "\'"
    messages = ['imageXcropper', 'image-cropper.html']

    # 
    fimageXcropper0= Form(db.dfimageXcropper0, dbio=False, formstyle=FormStyleBulma)
    if fimageXcropper0.accepted:
        mess1='inserted: ' if prn_form_vars(fimageXcropper0, db.dfimageXcropper0) else 'acceptd: '
        return put_json_messages(mess1 + str( fimageXcropper0.form_name ))
    elif fimageXcropper0.errors:
        print("fimageXcropper0 has errors: %s" % (fimageXcropper0.errors))
        return put_json_messages('error: ' + str( fimageXcropper0.form_name ))

    return locals()

@action('uiXsweetXalert', method=["GET", "POST"] )
@action.uses(Template('ui-sweet-alert.html', delimiters='[%[ ]]',), db, session, T,)

def uiXsweetXalert():
    ctrl_info= { 'c':'uiXsweetXalert', 'v':'ui-sweet-alert.html' }
    page_url = "\'" + URL('uiXsweetXalert' ) + "\'"
    messages = ['uiXsweetXalert', 'ui-sweet-alert.html']

    # 
    fuiXsweetXalert0= Form(db.dfuiXsweetXalert0, dbio=False, formstyle=FormStyleBulma)
    if fuiXsweetXalert0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXsweetXalert0, db.dfuiXsweetXalert0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXsweetXalert0.form_name ))
    elif fuiXsweetXalert0.errors:
        print("fuiXsweetXalert0 has errors: %s" % (fuiXsweetXalert0.errors))
        return put_json_messages('error: ' + str( fuiXsweetXalert0.form_name ))

    return locals()

@action('uiXprogressbar', method=["GET", "POST"] )
@action.uses(Template('ui-progressbar.html', delimiters='[%[ ]]',), db, session, T,)

def uiXprogressbar():
    ctrl_info= { 'c':'uiXprogressbar', 'v':'ui-progressbar.html' }
    page_url = "\'" + URL('uiXprogressbar' ) + "\'"
    messages = ['uiXprogressbar', 'ui-progressbar.html']

    # 
    fuiXprogressbar0= Form(db.dfuiXprogressbar0, dbio=False, formstyle=FormStyleBulma)
    if fuiXprogressbar0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXprogressbar0, db.dfuiXprogressbar0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXprogressbar0.form_name ))
    elif fuiXprogressbar0.errors:
        print("fuiXprogressbar0 has errors: %s" % (fuiXprogressbar0.errors))
        return put_json_messages('error: ' + str( fuiXprogressbar0.form_name ))

    return locals()

@action('uiXcardsXhover', method=["GET", "POST"] )
@action.uses(Template('ui-cards-hover.html', delimiters='[%[ ]]',), db, session, T,)

def uiXcardsXhover():
    ctrl_info= { 'c':'uiXcardsXhover', 'v':'ui-cards-hover.html' }
    page_url = "\'" + URL('uiXcardsXhover' ) + "\'"
    messages = ['uiXcardsXhover', 'ui-cards-hover.html']

    # 
    fuiXcardsXhover0= Form(db.dfuiXcardsXhover0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcardsXhover0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXcardsXhover0, db.dfuiXcardsXhover0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXcardsXhover0.form_name ))
    elif fuiXcardsXhover0.errors:
        print("fuiXcardsXhover0 has errors: %s" % (fuiXcardsXhover0.errors))
        return put_json_messages('error: ' + str( fuiXcardsXhover0.form_name ))

    return locals()

@action('resetXpassword', method=["GET", "POST"] )
@action.uses(Template('reset-password.html', delimiters='[%[ ]]',), db, session, T,)

def resetXpassword():
    ctrl_info= { 'c':'resetXpassword', 'v':'reset-password.html' }
    page_url = "\'" + URL('resetXpassword' ) + "\'"
    messages = ['resetXpassword', 'reset-password.html']

    # 
    fresetXpassword0= Form(db.dfresetXpassword0, dbio=False, formstyle=FormStyleBulma)
    if fresetXpassword0.accepted:
        mess1='inserted: ' if prn_form_vars(fresetXpassword0, db.dfresetXpassword0) else 'acceptd: '
        return put_json_messages(mess1 + str( fresetXpassword0.form_name ))
    elif fresetXpassword0.errors:
        print("fresetXpassword0 has errors: %s" % (fresetXpassword0.errors))
        return put_json_messages('error: ' + str( fresetXpassword0.form_name ))

    return locals()

@action('productXdetail', method=["GET", "POST"] )
@action.uses(Template('product-detail.html', delimiters='[%[ ]]',), db, session, T,)

def productXdetail():
    ctrl_info= { 'c':'productXdetail', 'v':'product-detail.html' }
    page_url = "\'" + URL('productXdetail' ) + "\'"
    messages = ['productXdetail', 'product-detail.html']

    # 
    fproductXdetail0= Form(db.dfproductXdetail0, dbio=False, formstyle=FormStyleBulma)
    if fproductXdetail0.accepted:
        mess1='inserted: ' if prn_form_vars(fproductXdetail0, db.dfproductXdetail0) else 'acceptd: '
        return put_json_messages(mess1 + str( fproductXdetail0.form_name ))
    elif fproductXdetail0.errors:
        print("fproductXdetail0 has errors: %s" % (fproductXdetail0.errors))
        return put_json_messages('error: ' + str( fproductXdetail0.form_name ))

    return locals()

@action('imageXdropzone', method=["GET", "POST"] )
@action.uses(Template('image-dropzone.html', delimiters='[%[ ]]',), db, session, T,)

def imageXdropzone():
    ctrl_info= { 'c':'imageXdropzone', 'v':'image-dropzone.html' }
    page_url = "\'" + URL('imageXdropzone' ) + "\'"
    messages = ['imageXdropzone', 'image-dropzone.html']

    # 
    fimageXdropzone0= Form(db.dfimageXdropzone0, dbio=False, formstyle=FormStyleBulma)
    if fimageXdropzone0.accepted:
        mess1='inserted: ' if prn_form_vars(fimageXdropzone0, db.dfimageXdropzone0) else 'acceptd: '
        return put_json_messages(mess1 + str( fimageXdropzone0.form_name ))
    elif fimageXdropzone0.errors:
        print("fimageXdropzone0 has errors: %s" % (fimageXdropzone0.errors))
        return put_json_messages('error: ' + str( fimageXdropzone0.form_name ))

    # 
    fimageXdropzone1= Form(db.dfimageXdropzone1, dbio=False, formstyle=FormStyleBulma)
    if fimageXdropzone1.accepted:
        mess1='inserted: ' if prn_form_vars(fimageXdropzone1, db.dfimageXdropzone1) else 'acceptd: '
        return put_json_messages(mess1 + str( fimageXdropzone1.form_name ))
    elif fimageXdropzone1.errors:
        print("fimageXdropzone1 has errors: %s" % (fimageXdropzone1.errors))
        return put_json_messages('error: ' + str( fimageXdropzone1.form_name ))

    return locals()

@action('colorXsettings', method=["GET", "POST"] )
@action.uses(Template('color-settings.html', delimiters='[%[ ]]',), db, session, T,)

def colorXsettings():
    ctrl_info= { 'c':'colorXsettings', 'v':'color-settings.html' }
    page_url = "\'" + URL('colorXsettings' ) + "\'"
    messages = ['colorXsettings', 'color-settings.html']

    # 
    fcolorXsettings0= Form(db.dfcolorXsettings0, dbio=False, formstyle=FormStyleBulma)
    if fcolorXsettings0.accepted:
        mess1='inserted: ' if prn_form_vars(fcolorXsettings0, db.dfcolorXsettings0) else 'acceptd: '
        return put_json_messages(mess1 + str( fcolorXsettings0.form_name ))
    elif fcolorXsettings0.errors:
        print("fcolorXsettings0 has errors: %s" % (fcolorXsettings0.errors))
        return put_json_messages('error: ' + str( fcolorXsettings0.form_name ))

    return locals()

@action('uiXrangeXslider', method=["GET", "POST"] )
@action.uses(Template('ui-range-slider.html', delimiters='[%[ ]]',), db, session, T,)

def uiXrangeXslider():
    ctrl_info= { 'c':'uiXrangeXslider', 'v':'ui-range-slider.html' }
    page_url = "\'" + URL('uiXrangeXslider' ) + "\'"
    messages = ['uiXrangeXslider', 'ui-range-slider.html']

    # 
    fuiXrangeXslider0= Form(db.dfuiXrangeXslider0, dbio=False, formstyle=FormStyleBulma)
    if fuiXrangeXslider0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXrangeXslider0, db.dfuiXrangeXslider0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXrangeXslider0.form_name ))
    elif fuiXrangeXslider0.errors:
        print("fuiXrangeXslider0 has errors: %s" % (fuiXrangeXslider0.errors))
        return put_json_messages('error: ' + str( fuiXrangeXslider0.form_name ))

    return locals()

@action('uiXnotification', method=["GET", "POST"] )
@action.uses(Template('ui-notification.html', delimiters='[%[ ]]',), db, session, T,)

def uiXnotification():
    ctrl_info= { 'c':'uiXnotification', 'v':'ui-notification.html' }
    page_url = "\'" + URL('uiXnotification' ) + "\'"
    messages = ['uiXnotification', 'ui-notification.html']

    # 
    fuiXnotification0= Form(db.dfuiXnotification0, dbio=False, formstyle=FormStyleBulma)
    if fuiXnotification0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXnotification0, db.dfuiXnotification0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXnotification0.form_name ))
    elif fuiXnotification0.errors:
        print("fuiXnotification0 has errors: %s" % (fuiXnotification0.errors))
        return put_json_messages('error: ' + str( fuiXnotification0.form_name ))

    return locals()

@action('gettingXstarted', method=["GET", "POST"] )
@action.uses(Template('getting-started.html', delimiters='[%[ ]]',), db, session, T,)

def gettingXstarted():
    ctrl_info= { 'c':'gettingXstarted', 'v':'getting-started.html' }
    page_url = "\'" + URL('gettingXstarted' ) + "\'"
    messages = ['gettingXstarted', 'getting-started.html']

    # 
    fgettingXstarted0= Form(db.dfgettingXstarted0, dbio=False, formstyle=FormStyleBulma)
    if fgettingXstarted0.accepted:
        mess1='inserted: ' if prn_form_vars(fgettingXstarted0, db.dfgettingXstarted0) else 'acceptd: '
        return put_json_messages(mess1 + str( fgettingXstarted0.form_name ))
    elif fgettingXstarted0.errors:
        print("fgettingXstarted0 has errors: %s" % (fgettingXstarted0.errors))
        return put_json_messages('error: ' + str( fgettingXstarted0.form_name ))

    return locals()

@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session, T,)

def forgotXpassword():
    ctrl_info= { 'c':'forgotXpassword', 'v':'forgot-password.html' }
    page_url = "\'" + URL('forgotXpassword' ) + "\'"
    messages = ['forgotXpassword', 'forgot-password.html']

    # 
    fforgotXpassword0= Form(db.dfforgotXpassword0, dbio=False, formstyle=FormStyleBulma)
    if fforgotXpassword0.accepted:
        mess1='inserted: ' if prn_form_vars(fforgotXpassword0, db.dfforgotXpassword0) else 'acceptd: '
        return put_json_messages(mess1 + str( fforgotXpassword0.form_name ))
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s" % (fforgotXpassword0.errors))
        return put_json_messages('error: ' + str( fforgotXpassword0.form_name ))

    return locals()

@action('contactXdirectory', method=["GET", "POST"] )
@action.uses(Template('contact-directory.html', delimiters='[%[ ]]',), db, session, T,)

def contactXdirectory():
    ctrl_info= { 'c':'contactXdirectory', 'v':'contact-directory.html' }
    page_url = "\'" + URL('contactXdirectory' ) + "\'"
    messages = ['contactXdirectory', 'contact-directory.html']

    # 
    fcontactXdirectory0= Form(db.dfcontactXdirectory0, dbio=False, formstyle=FormStyleBulma)
    if fcontactXdirectory0.accepted:
        mess1='inserted: ' if prn_form_vars(fcontactXdirectory0, db.dfcontactXdirectory0) else 'acceptd: '
        return put_json_messages(mess1 + str( fcontactXdirectory0.form_name ))
    elif fcontactXdirectory0.errors:
        print("fcontactXdirectory0 has errors: %s" % (fcontactXdirectory0.errors))
        return put_json_messages('error: ' + str( fcontactXdirectory0.form_name ))

    return locals()

@action('uiXtooltipXpopover', method=["GET", "POST"] )
@action.uses(Template('ui-tooltip-popover.html', delimiters='[%[ ]]',), db, session, T,)

def uiXtooltipXpopover():
    ctrl_info= { 'c':'uiXtooltipXpopover', 'v':'ui-tooltip-popover.html' }
    page_url = "\'" + URL('uiXtooltipXpopover' ) + "\'"
    messages = ['uiXtooltipXpopover', 'ui-tooltip-popover.html']

    # 
    fuiXtooltipXpopover0= Form(db.dfuiXtooltipXpopover0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtooltipXpopover0.accepted:
        mess1='inserted: ' if prn_form_vars(fuiXtooltipXpopover0, db.dfuiXtooltipXpopover0) else 'acceptd: '
        return put_json_messages(mess1 + str( fuiXtooltipXpopover0.form_name ))
    elif fuiXtooltipXpopover0.errors:
        print("fuiXtooltipXpopover0 has errors: %s" % (fuiXtooltipXpopover0.errors))
        return put_json_messages('error: ' + str( fuiXtooltipXpopover0.form_name ))

    return locals()

@action('thirdXpartyXplugins', method=["GET", "POST"] )
@action.uses(Template('third-party-plugins.html', delimiters='[%[ ]]',), db, session, T,)

def thirdXpartyXplugins():
    ctrl_info= { 'c':'thirdXpartyXplugins', 'v':'third-party-plugins.html' }
    page_url = "\'" + URL('thirdXpartyXplugins' ) + "\'"
    messages = ['thirdXpartyXplugins', 'third-party-plugins.html']

    rows_tthirdXpartyXplugins0= db(db.tthirdXpartyXplugins0).select()
    # 
    fthirdXpartyXplugins0= Form(db.dfthirdXpartyXplugins0, dbio=False, formstyle=FormStyleBulma)
    if fthirdXpartyXplugins0.accepted:
        mess1='inserted: ' if prn_form_vars(fthirdXpartyXplugins0, db.dfthirdXpartyXplugins0) else 'acceptd: '
        return put_json_messages(mess1 + str( fthirdXpartyXplugins0.form_name ))
    elif fthirdXpartyXplugins0.errors:
        print("fthirdXpartyXplugins0 has errors: %s" % (fthirdXpartyXplugins0.errors))
        return put_json_messages('error: ' + str( fthirdXpartyXplugins0.form_name ))

    return locals()

@action('advancedXcomponents', method=["GET", "POST"] )
@action.uses(Template('advanced-components.html', delimiters='[%[ ]]',), db, session, T,)

def advancedXcomponents():
    ctrl_info= { 'c':'advancedXcomponents', 'v':'advanced-components.html' }
    page_url = "\'" + URL('advancedXcomponents' ) + "\'"
    messages = ['advancedXcomponents', 'advanced-components.html']

    # 
    fadvancedXcomponents0= Form(db.dfadvancedXcomponents0, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents0.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents0, db.dfadvancedXcomponents0) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents0.form_name ))
    elif fadvancedXcomponents0.errors:
        print("fadvancedXcomponents0 has errors: %s" % (fadvancedXcomponents0.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents0.form_name ))

    # 
    fadvancedXcomponents1= Form(db.dfadvancedXcomponents1, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents1.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents1, db.dfadvancedXcomponents1) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents1.form_name ))
    elif fadvancedXcomponents1.errors:
        print("fadvancedXcomponents1 has errors: %s" % (fadvancedXcomponents1.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents1.form_name ))

    # 
    fadvancedXcomponents2= Form(db.dfadvancedXcomponents2, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents2.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents2, db.dfadvancedXcomponents2) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents2.form_name ))
    elif fadvancedXcomponents2.errors:
        print("fadvancedXcomponents2 has errors: %s" % (fadvancedXcomponents2.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents2.form_name ))

    # 
    fadvancedXcomponents3= Form(db.dfadvancedXcomponents3, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents3.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents3, db.dfadvancedXcomponents3) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents3.form_name ))
    elif fadvancedXcomponents3.errors:
        print("fadvancedXcomponents3 has errors: %s" % (fadvancedXcomponents3.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents3.form_name ))

    # 
    fadvancedXcomponents4= Form(db.dfadvancedXcomponents4, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents4.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents4, db.dfadvancedXcomponents4) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents4.form_name ))
    elif fadvancedXcomponents4.errors:
        print("fadvancedXcomponents4 has errors: %s" % (fadvancedXcomponents4.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents4.form_name ))

    # 
    fadvancedXcomponents5= Form(db.dfadvancedXcomponents5, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents5.accepted:
        mess1='inserted: ' if prn_form_vars(fadvancedXcomponents5, db.dfadvancedXcomponents5) else 'acceptd: '
        return put_json_messages(mess1 + str( fadvancedXcomponents5.form_name ))
    elif fadvancedXcomponents5.errors:
        print("fadvancedXcomponents5 has errors: %s" % (fadvancedXcomponents5.errors))
        return put_json_messages('error: ' + str( fadvancedXcomponents5.form_name ))

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
# curl -X  GET   http://localhost:8000/desk/api/test_table/
# curl -X  GET   http://localhost:8000/desk/api/test_table/9
# curl -X DELETE  http://localhost:8000/desk/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/desk/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/desk/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/desk/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/desk/api/test_table/
#  http         localhost:8000/desk/api/test_table/9
#  http -f POST localhost:8000/desk/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/desk/api/test_table/2
#  http -f PUT localhost:8000/desk/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

