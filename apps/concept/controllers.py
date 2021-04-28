#
# py4web app, AI-biorex ported 28.04.2021 08:47:33 UTC+3, src: https://github.com/puikinsh/concept

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

@action('tabs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tabs.html', delimiters='[%[ ]]',))

def tabs():
    ctrl_info= { 'c':'tabs', 'v':'tabs.html' }
    messages = ['tabs', 'tabs.html']
    #
    ctrl_template_url = "\'" + URL('tabs' ) + "\'"

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inbox.html', delimiters='[%[ ]]',))

def inbox():
    ctrl_info= { 'c':'inbox', 'v':'inbox.html' }
    messages = ['inbox', 'inbox.html']
    #
    ctrl_template_url = "\'" + URL('inbox' ) + "\'"

    return locals()

@action('cards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('cards.html', delimiters='[%[ ]]',))

def cards():
    ctrl_info= { 'c':'cards', 'v':'cards.html' }
    messages = ['cards', 'cards.html']
    #
    ctrl_template_url = "\'" + URL('cards' ) + "\'"

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']
    #
    ctrl_template_url = "\'" + URL('index' ) + "\'"

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
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

@action('invoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice.html', delimiters='[%[ ]]',))

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    messages = ['invoice', 'invoice.html']
    #
    ctrl_template_url = "\'" + URL('invoice' ) + "\'"

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(db, session, T, Template('widgets.html', delimiters='[%[ ]]',))

def widgets():
    ctrl_info= { 'c':'widgets', 'v':'widgets.html' }
    messages = ['widgets', 'widgets.html']
    #
    ctrl_template_url = "\'" + URL('widgets' ) + "\'"

    return locals()

@action('pricing', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pricing.html', delimiters='[%[ ]]',))

def pricing():
    ctrl_info= { 'c':'pricing', 'v':'pricing.html' }
    messages = ['pricing', 'pricing.html']
    #
    ctrl_template_url = "\'" + URL('pricing' ) + "\'"

    return locals()

@action('general', method=["GET", "POST"] )
@action.uses(db, session, T, Template('general.html', delimiters='[%[ ]]',))

def general():
    ctrl_info= { 'c':'general', 'v':'general.html' }
    messages = ['general', 'general.html']
    #
    ctrl_template_url = "\'" + URL('general' ) + "\'"

    return locals()

@action('signXup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('sign-up.html', delimiters='[%[ ]]',))

def signXup():
    ctrl_info= { 'c':'signXup', 'v':'sign-up.html' }
    messages = ['signXup', 'sign-up.html']
    #
    ctrl_template_url = "\'" + URL('signXup' ) + "\'"

    # 
    fsignXup0= Form(db.dfsignXup0, dbio=False, formstyle=FormStyleBulma)
    if fsignXup0.accepted:
        icon_type ='success' if insert_form_vars(fsignXup0, db.dfsignXup0) else 'info'
        return json2user(mess = str( fsignXup0.form_name ), icon_type=icon_type )
    elif fsignXup0.errors:
        print("fsignXup0 has errors: %s" % (fsignXup0.errors))
        return json2user(mess = str(fsignXup0.form_name), icon_type = 'error')

    return locals()

@action('morrisjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('morrisjs.html', delimiters='[%[ ]]',))

def morrisjs():
    ctrl_info= { 'c':'morrisjs', 'v':'morrisjs.html' }
    messages = ['morrisjs', 'morrisjs.html']
    #
    ctrl_template_url = "\'" + URL('morrisjs' ) + "\'"

    # 
    fmorrisjs0= Form(db.dfmorrisjs0, dbio=False, formstyle=FormStyleBulma)
    if fmorrisjs0.accepted:
        icon_type ='success' if insert_form_vars(fmorrisjs0, db.dfmorrisjs0) else 'info'
        return json2user(mess = str( fmorrisjs0.form_name ), icon_type=icon_type )
    elif fmorrisjs0.errors:
        print("fmorrisjs0 has errors: %s" % (fmorrisjs0.errors))
        return json2user(mess = str(fmorrisjs0.form_name), icon_type = 'error')

    # 
    fmorrisjs1= Form(db.dfmorrisjs1, dbio=False, formstyle=FormStyleBulma)
    if fmorrisjs1.accepted:
        icon_type ='success' if insert_form_vars(fmorrisjs1, db.dfmorrisjs1) else 'info'
        return json2user(mess = str( fmorrisjs1.form_name ), icon_type=icon_type )
    elif fmorrisjs1.errors:
        print("fmorrisjs1 has errors: %s" % (fmorrisjs1.errors))
        return json2user(mess = str(fmorrisjs1.form_name), icon_type = 'error')

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']
    #
    ctrl_template_url = "\'" + URL('calendar' ) + "\'"

    return locals()

@action('timeline', method=["GET", "POST"] )
@action.uses(db, session, T, Template('timeline.html', delimiters='[%[ ]]',))

def timeline():
    ctrl_info= { 'c':'timeline', 'v':'timeline.html' }
    messages = ['timeline', 'timeline.html']
    #
    ctrl_template_url = "\'" + URL('timeline' ) + "\'"

    return locals()

@action('chartXc3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-c3.html', delimiters='[%[ ]]',))

def chartXc3():
    ctrl_info= { 'c':'chartXc3', 'v':'chart-c3.html' }
    messages = ['chartXc3', 'chart-c3.html']
    #
    ctrl_template_url = "\'" + URL('chartXc3' ) + "\'"

    return locals()

@action('carousel', method=["GET", "POST"] )
@action.uses(db, session, T, Template('carousel.html', delimiters='[%[ ]]',))

def carousel():
    ctrl_info= { 'c':'carousel', 'v':'carousel.html' }
    messages = ['carousel', 'carousel.html']
    #
    ctrl_template_url = "\'" + URL('carousel' ) + "\'"

    return locals()

@action('X404Xpage', method=["GET", "POST"] )
@action.uses(db, session, T, Template('404-page.html', delimiters='[%[ ]]',))

def X404Xpage():
    ctrl_info= { 'c':'X404Xpage', 'v':'404-page.html' }
    messages = ['X404Xpage', '404-page.html']
    #
    ctrl_template_url = "\'" + URL('X404Xpage' ) + "\'"

    return locals()

@action('pagesXapp', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-app.html', delimiters='[%[ ]]',))

def pagesXapp():
    ctrl_info= { 'c':'pagesXapp', 'v':'pages-app.html' }
    messages = ['pagesXapp', 'pages-app.html']
    #
    ctrl_template_url = "\'" + URL('pagesXapp' ) + "\'"

    # 
    fpagesXapp0= Form(db.dfpagesXapp0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXapp0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXapp0, db.dfpagesXapp0) else 'info'
        return json2user(mess = str( fpagesXapp0.form_name ), icon_type=icon_type )
    elif fpagesXapp0.errors:
        print("fpagesXapp0 has errors: %s" % (fpagesXapp0.errors))
        return json2user(mess = str(fpagesXapp0.form_name), icon_type = 'error')

    # 
    fpagesXapp1= Form(db.dfpagesXapp1, dbio=False, formstyle=FormStyleBulma)
    if fpagesXapp1.accepted:
        icon_type ='success' if insert_form_vars(fpagesXapp1, db.dfpagesXapp1) else 'info'
        return json2user(mess = str( fpagesXapp1.form_name ), icon_type=icon_type )
    elif fpagesXapp1.errors:
        print("fpagesXapp1 has errors: %s" % (fpagesXapp1.errors))
        return json2user(mess = str(fpagesXapp1.form_name), icon_type = 'error')

    return locals()

@action('iconXflag', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-flag.html', delimiters='[%[ ]]',))

def iconXflag():
    ctrl_info= { 'c':'iconXflag', 'v':'icon-flag.html' }
    messages = ['iconXflag', 'icon-flag.html']
    #
    ctrl_template_url = "\'" + URL('iconXflag' ) + "\'"

    return locals()

@action('listgroup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('listgroup.html', delimiters='[%[ ]]',))

def listgroup():
    ctrl_info= { 'c':'listgroup', 'v':'listgroup.html' }
    messages = ['listgroup', 'listgroup.html']
    #
    ctrl_template_url = "\'" + URL('listgroup' ) + "\'"

    return locals()

@action('mapXvector', method=["GET", "POST"] )
@action.uses(db, session, T, Template('map-vector.html', delimiters='[%[ ]]',))

def mapXvector():
    ctrl_info= { 'c':'mapXvector', 'v':'map-vector.html' }
    messages = ['mapXvector', 'map-vector.html']
    #
    ctrl_template_url = "\'" + URL('mapXvector' ) + "\'"

    return locals()

@action('mapXgoogle', method=["GET", "POST"] )
@action.uses(db, session, T, Template('map-google.html', delimiters='[%[ ]]',))

def mapXgoogle():
    ctrl_info= { 'c':'mapXgoogle', 'v':'map-google.html' }
    messages = ['mapXgoogle', 'map-google.html']
    #
    ctrl_template_url = "\'" + URL('mapXgoogle' ) + "\'"

    return locals()

@action('blankXpage', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank-page.html', delimiters='[%[ ]]',))

def blankXpage():
    ctrl_info= { 'c':'blankXpage', 'v':'blank-page.html' }
    messages = ['blankXpage', 'blank-page.html']
    #
    ctrl_template_url = "\'" + URL('blankXpage' ) + "\'"

    return locals()

@action('datepicker', method=["GET", "POST"] )
@action.uses(db, session, T, Template('datepicker.html', delimiters='[%[ ]]',))

def datepicker():
    ctrl_info= { 'c':'datepicker', 'v':'datepicker.html' }
    messages = ['datepicker', 'datepicker.html']
    #
    ctrl_template_url = "\'" + URL('datepicker' ) + "\'"

    return locals()

@action('accordions', method=["GET", "POST"] )
@action.uses(db, session, T, Template('accordions.html', delimiters='[%[ ]]',))

def accordions():
    ctrl_info= { 'c':'accordions', 'v':'accordions.html' }
    messages = ['accordions', 'accordions.html']
    #
    ctrl_template_url = "\'" + URL('accordions' ) + "\'"

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typography.html', delimiters='[%[ ]]',))

def typography():
    ctrl_info= { 'c':'typography', 'v':'typography.html' }
    messages = ['typography', 'typography.html']
    #
    ctrl_template_url = "\'" + URL('typography' ) + "\'"

    return locals()

@action('dataXtables', method=["GET", "POST"] )
@action.uses(db, session, T, Template('data-tables.html', delimiters='[%[ ]]',))

def dataXtables():
    ctrl_info= { 'c':'dataXtables', 'v':'data-tables.html' }
    messages = ['dataXtables', 'data-tables.html']
    #
    ctrl_template_url = "\'" + URL('dataXtables' ) + "\'"

    rows_tdataXtables0= db(db.tdataXtables0).select()
    rows_tdataXtables1= db(db.tdataXtables1).select()
    rows_tdataXtables2= db(db.tdataXtables2).select()
    rows_tdataXtables3= db(db.tdataXtables3).select()
    rows_tdataXtables4= db(db.tdataXtables4).select()
    return locals()

@action('multiselect', method=["GET", "POST"] )
@action.uses(db, session, T, Template('multiselect.html', delimiters='[%[ ]]',))

def multiselect():
    ctrl_info= { 'c':'multiselect', 'v':'multiselect.html' }
    messages = ['multiselect', 'multiselect.html']
    #
    ctrl_template_url = "\'" + URL('multiselect' ) + "\'"

    return locals()

@action('chartXgauge', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-gauge.html', delimiters='[%[ ]]',))

def chartXgauge():
    ctrl_info= { 'c':'chartXgauge', 'v':'chart-gauge.html' }
    messages = ['chartXgauge', 'chart-gauge.html']
    #
    ctrl_template_url = "\'" + URL('chartXgauge' ) + "\'"

    return locals()

@action('userXprofile', method=["GET", "POST"] )
@action.uses(db, session, T, Template('user-profile.html', delimiters='[%[ ]]',))

def userXprofile():
    ctrl_info= { 'c':'userXprofile', 'v':'user-profile.html' }
    messages = ['userXprofile', 'user-profile.html']
    #
    ctrl_template_url = "\'" + URL('userXprofile' ) + "\'"

    # 
    fuserXprofile0= Form(db.dfuserXprofile0, dbio=False, formstyle=FormStyleBulma)
    if fuserXprofile0.accepted:
        icon_type ='success' if insert_form_vars(fuserXprofile0, db.dfuserXprofile0) else 'info'
        return json2user(mess = str( fuserXprofile0.form_name ), icon_type=icon_type )
    elif fuserXprofile0.errors:
        print("fuserXprofile0 has errors: %s" % (fuserXprofile0.errors))
        return json2user(mess = str(fuserXprofile0.form_name), icon_type = 'error')

    # 
    fuserXprofile1= Form(db.dfuserXprofile1, dbio=False, formstyle=FormStyleBulma)
    if fuserXprofile1.accepted:
        icon_type ='success' if insert_form_vars(fuserXprofile1, db.dfuserXprofile1) else 'info'
        return json2user(mess = str( fuserXprofile1.form_name ), icon_type=icon_type )
    elif fuserXprofile1.errors:
        print("fuserXprofile1 has errors: %s" % (fuserXprofile1.errors))
        return json2user(mess = str(fuserXprofile1.form_name), icon_type = 'error')

    return locals()

@action('iconXweather', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-weather.html', delimiters='[%[ ]]',))

def iconXweather():
    ctrl_info= { 'c':'iconXweather', 'v':'icon-weather.html' }
    messages = ['iconXweather', 'icon-weather.html']
    #
    ctrl_template_url = "\'" + URL('iconXweather' ) + "\'"

    return locals()

@action('iconXthemify', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-themify.html', delimiters='[%[ ]]',))

def iconXthemify():
    ctrl_info= { 'c':'iconXthemify', 'v':'icon-themify.html' }
    messages = ['iconXthemify', 'icon-themify.html']
    #
    ctrl_template_url = "\'" + URL('iconXthemify' ) + "\'"

    return locals()

@action('messageXchat', method=["GET", "POST"] )
@action.uses(db, session, T, Template('message-chat.html', delimiters='[%[ ]]',))

def messageXchat():
    ctrl_info= { 'c':'messageXchat', 'v':'message-chat.html' }
    messages = ['messageXchat', 'message-chat.html']
    #
    ctrl_template_url = "\'" + URL('messageXchat' ) + "\'"

    # 
    fmessageXchat0= Form(db.dfmessageXchat0, dbio=False, formstyle=FormStyleBulma)
    if fmessageXchat0.accepted:
        icon_type ='success' if insert_form_vars(fmessageXchat0, db.dfmessageXchat0) else 'info'
        return json2user(mess = str( fmessageXchat0.form_name ), icon_type=icon_type )
    elif fmessageXchat0.errors:
        print("fmessageXchat0 has errors: %s" % (fmessageXchat0.errors))
        return json2user(mess = str(fmessageXchat0.form_name), icon_type = 'error')

    # 
    fmessageXchat1= Form(db.dfmessageXchat1, dbio=False, formstyle=FormStyleBulma)
    if fmessageXchat1.accepted:
        icon_type ='success' if insert_form_vars(fmessageXchat1, db.dfmessageXchat1) else 'info'
        return json2user(mess = str( fmessageXchat1.form_name ), icon_type=icon_type )
    elif fmessageXchat1.errors:
        print("fmessageXchat1 has errors: %s" % (fmessageXchat1.errors))
        return json2user(mess = str(fmessageXchat1.form_name), icon_type = 'error')

    # 
    fmessageXchat2= Form(db.dfmessageXchat2, dbio=False, formstyle=FormStyleBulma)
    if fmessageXchat2.accepted:
        icon_type ='success' if insert_form_vars(fmessageXchat2, db.dfmessageXchat2) else 'info'
        return json2user(mess = str( fmessageXchat2.form_name ), icon_type=icon_type )
    elif fmessageXchat2.errors:
        print("fmessageXchat2 has errors: %s" % (fmessageXchat2.errors))
        return json2user(mess = str(fmessageXchat2.form_name), icon_type = 'error')

    # 
    fmessageXchat3= Form(db.dfmessageXchat3, dbio=False, formstyle=FormStyleBulma)
    if fmessageXchat3.accepted:
        icon_type ='success' if insert_form_vars(fmessageXchat3, db.dfmessageXchat3) else 'info'
        return json2user(mess = str( fmessageXchat3.form_name ), icon_type=icon_type )
    elif fmessageXchat3.errors:
        print("fmessageXchat3 has errors: %s" % (fmessageXchat3.errors))
        return json2user(mess = str(fmessageXchat3.form_name), icon_type = 'error')

    # 
    fmessageXchat4= Form(db.dfmessageXchat4, dbio=False, formstyle=FormStyleBulma)
    if fmessageXchat4.accepted:
        icon_type ='success' if insert_form_vars(fmessageXchat4, db.dfmessageXchat4) else 'info'
        return json2user(mess = str( fmessageXchat4.form_name ), icon_type=icon_type )
    elif fmessageXchat4.errors:
        print("fmessageXchat4 has errors: %s" % (fmessageXchat4.errors))
        return json2user(mess = str(fmessageXchat4.form_name), icon_type = 'error')

    return locals()

@action('colorXpicker', method=["GET", "POST"] )
@action.uses(db, session, T, Template('color-picker.html', delimiters='[%[ ]]',))

def colorXpicker():
    ctrl_info= { 'c':'colorXpicker', 'v':'color-picker.html' }
    messages = ['colorXpicker', 'color-picker.html']
    #
    ctrl_template_url = "\'" + URL('colorXpicker' ) + "\'"

    return locals()

@action('mediaXobject', method=["GET", "POST"] )
@action.uses(db, session, T, Template('media-object.html', delimiters='[%[ ]]',))

def mediaXobject():
    ctrl_info= { 'c':'mediaXobject', 'v':'media-object.html' }
    messages = ['mediaXobject', 'media-object.html']
    #
    ctrl_template_url = "\'" + URL('mediaXobject' ) + "\'"

    return locals()

@action('chartXmorris', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-morris.html', delimiters='[%[ ]]',))

def chartXmorris():
    ctrl_info= { 'c':'chartXmorris', 'v':'chart-morris.html' }
    messages = ['chartXmorris', 'chart-morris.html']
    #
    ctrl_template_url = "\'" + URL('chartXmorris' ) + "\'"

    return locals()

@action('chartXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-charts.html', delimiters='[%[ ]]',))

def chartXcharts():
    ctrl_info= { 'c':'chartXcharts', 'v':'chart-charts.html' }
    messages = ['chartXcharts', 'chart-charts.html']
    #
    ctrl_template_url = "\'" + URL('chartXcharts' ) + "\'"

    return locals()

@action('pagesXsignXup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-sign-up.html', delimiters='[%[ ]]',))

def pagesXsignXup():
    ctrl_info= { 'c':'pagesXsignXup', 'v':'pages-sign-up.html' }
    messages = ['pagesXsignXup', 'pages-sign-up.html']
    #
    ctrl_template_url = "\'" + URL('pagesXsignXup' ) + "\'"

    # 
    fpagesXsignXup0= Form(db.dfpagesXsignXup0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsignXup0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsignXup0, db.dfpagesXsignXup0) else 'info'
        return json2user(mess = str( fpagesXsignXup0.form_name ), icon_type=icon_type )
    elif fpagesXsignXup0.errors:
        print("fpagesXsignXup0 has errors: %s" % (fpagesXsignXup0.errors))
        return json2user(mess = str(fpagesXsignXup0.form_name), icon_type = 'error')

    # 
    fpagesXsignXup1= Form(db.dfpagesXsignXup1, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsignXup1.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsignXup1, db.dfpagesXsignXup1) else 'info'
        return json2user(mess = str( fpagesXsignXup1.form_name ), icon_type=icon_type )
    elif fpagesXsignXup1.errors:
        print("fpagesXsignXup1 has errors: %s" % (fpagesXsignXup1.errors))
        return json2user(mess = str(fpagesXsignXup1.form_name), icon_type = 'error')

    return locals()

@action('iconXmaterial', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-material.html', delimiters='[%[ ]]',))

def iconXmaterial():
    ctrl_info= { 'c':'iconXmaterial', 'v':'icon-material.html' }
    messages = ['iconXmaterial', 'icon-material.html']
    #
    ctrl_template_url = "\'" + URL('iconXmaterial' ) + "\'"

    return locals()

@action('emailXcompose', method=["GET", "POST"] )
@action.uses(db, session, T, Template('email-compose.html', delimiters='[%[ ]]',))

def emailXcompose():
    ctrl_info= { 'c':'emailXcompose', 'v':'email-compose.html' }
    messages = ['emailXcompose', 'email-compose.html']
    #
    ctrl_template_url = "\'" + URL('emailXcompose' ) + "\'"

    return locals()

@action('emailXdetails', method=["GET", "POST"] )
@action.uses(db, session, T, Template('email-details.html', delimiters='[%[ ]]',))

def emailXdetails():
    ctrl_info= { 'c':'emailXdetails', 'v':'email-details.html' }
    messages = ['emailXdetails', 'email-details.html']
    #
    ctrl_template_url = "\'" + URL('emailXdetails' ) + "\'"

    return locals()

@action('cropperXimage', method=["GET", "POST"] )
@action.uses(db, session, T, Template('cropper-image.html', delimiters='[%[ ]]',))

def cropperXimage():
    ctrl_info= { 'c':'cropperXimage', 'v':'cropper-image.html' }
    messages = ['cropperXimage', 'cropper-image.html']
    #
    ctrl_template_url = "\'" + URL('cropperXimage' ) + "\'"

    return locals()

@action('generalXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('general-table.html', delimiters='[%[ ]]',))

def generalXtable():
    ctrl_info= { 'c':'generalXtable', 'v':'general-table.html' }
    messages = ['generalXtable', 'general-table.html']
    #
    ctrl_template_url = "\'" + URL('generalXtable' ) + "\'"

    rows_tgeneralXtable0= db(db.tgeneralXtable0).select()
    rows_tgeneralXtable1= db(db.tgeneralXtable1).select()
    rows_tgeneralXtable2= db(db.tgeneralXtable2).select()
    rows_tgeneralXtable3= db(db.tgeneralXtable3).select()
    rows_tgeneralXtable4= db(db.tgeneralXtable4).select()
    rows_tgeneralXtable5= db(db.tgeneralXtable5).select()
    return locals()

@action('formXelements', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-elements.html', delimiters='[%[ ]]',))

def formXelements():
    ctrl_info= { 'c':'formXelements', 'v':'form-elements.html' }
    messages = ['formXelements', 'form-elements.html']
    #
    ctrl_template_url = "\'" + URL('formXelements' ) + "\'"

    # 
    fformXelements0= Form(db.dfformXelements0, dbio=False, formstyle=FormStyleBulma)
    if fformXelements0.accepted:
        icon_type ='success' if insert_form_vars(fformXelements0, db.dfformXelements0) else 'info'
        return json2user(mess = str( fformXelements0.form_name ), icon_type=icon_type )
    elif fformXelements0.errors:
        print("fformXelements0 has errors: %s" % (fformXelements0.errors))
        return json2user(mess = str(fformXelements0.form_name), icon_type = 'error')

    # 
    fformXelements1= Form(db.dfformXelements1, dbio=False, formstyle=FormStyleBulma)
    if fformXelements1.accepted:
        icon_type ='success' if insert_form_vars(fformXelements1, db.dfformXelements1) else 'info'
        return json2user(mess = str( fformXelements1.form_name ), icon_type=icon_type )
    elif fformXelements1.errors:
        print("fformXelements1 has errors: %s" % (fformXelements1.errors))
        return json2user(mess = str(fformXelements1.form_name), icon_type = 'error')

    # 
    fformXelements2= Form(db.dfformXelements2, dbio=False, formstyle=FormStyleBulma)
    if fformXelements2.accepted:
        icon_type ='success' if insert_form_vars(fformXelements2, db.dfformXelements2) else 'info'
        return json2user(mess = str( fformXelements2.form_name ), icon_type=icon_type )
    elif fformXelements2.errors:
        print("fformXelements2 has errors: %s" % (fformXelements2.errors))
        return json2user(mess = str(fformXelements2.form_name), icon_type = 'error')

    # 
    fformXelements3= Form(db.dfformXelements3, dbio=False, formstyle=FormStyleBulma)
    if fformXelements3.accepted:
        icon_type ='success' if insert_form_vars(fformXelements3, db.dfformXelements3) else 'info'
        return json2user(mess = str( fformXelements3.form_name ), icon_type=icon_type )
    elif fformXelements3.errors:
        print("fformXelements3 has errors: %s" % (fformXelements3.errors))
        return json2user(mess = str(fformXelements3.form_name), icon_type = 'error')

    # 
    fformXelements4= Form(db.dfformXelements4, dbio=False, formstyle=FormStyleBulma)
    if fformXelements4.accepted:
        icon_type ='success' if insert_form_vars(fformXelements4, db.dfformXelements4) else 'info'
        return json2user(mess = str( fformXelements4.form_name ), icon_type=icon_type )
    elif fformXelements4.errors:
        print("fformXelements4 has errors: %s" % (fformXelements4.errors))
        return json2user(mess = str(fformXelements4.form_name), icon_type = 'error')

    # 
    fformXelements5= Form(db.dfformXelements5, dbio=False, formstyle=FormStyleBulma)
    if fformXelements5.accepted:
        icon_type ='success' if insert_form_vars(fformXelements5, db.dfformXelements5) else 'info'
        return json2user(mess = str( fformXelements5.form_name ), icon_type=icon_type )
    elif fformXelements5.errors:
        print("fformXelements5 has errors: %s" % (fformXelements5.errors))
        return json2user(mess = str(fformXelements5.form_name), icon_type = 'error')

    # 
    fformXelements6= Form(db.dfformXelements6, dbio=False, formstyle=FormStyleBulma)
    if fformXelements6.accepted:
        icon_type ='success' if insert_form_vars(fformXelements6, db.dfformXelements6) else 'info'
        return json2user(mess = str( fformXelements6.form_name ), icon_type=icon_type )
    elif fformXelements6.errors:
        print("fformXelements6 has errors: %s" % (fformXelements6.errors))
        return json2user(mess = str(fformXelements6.form_name), icon_type = 'error')

    # 
    fformXelements7= Form(db.dfformXelements7, dbio=False, formstyle=FormStyleBulma)
    if fformXelements7.accepted:
        icon_type ='success' if insert_form_vars(fformXelements7, db.dfformXelements7) else 'info'
        return json2user(mess = str( fformXelements7.form_name ), icon_type=icon_type )
    elif fformXelements7.errors:
        print("fformXelements7 has errors: %s" % (fformXelements7.errors))
        return json2user(mess = str(fformXelements7.form_name), icon_type = 'error')

    # 
    fformXelements8= Form(db.dfformXelements8, dbio=False, formstyle=FormStyleBulma)
    if fformXelements8.accepted:
        icon_type ='success' if insert_form_vars(fformXelements8, db.dfformXelements8) else 'info'
        return json2user(mess = str( fformXelements8.form_name ), icon_type=icon_type )
    elif fformXelements8.errors:
        print("fformXelements8 has errors: %s" % (fformXelements8.errors))
        return json2user(mess = str(fformXelements8.form_name), icon_type = 'error')

    return locals()

@action('chartXchartist', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-chartist.html', delimiters='[%[ ]]',))

def chartXchartist():
    ctrl_info= { 'c':'chartXchartist', 'v':'chart-chartist.html' }
    messages = ['chartXchartist', 'chart-chartist.html']
    #
    ctrl_template_url = "\'" + URL('chartXchartist' ) + "\'"

    return locals()

@action('formXvalidation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-validation.html', delimiters='[%[ ]]',))

def formXvalidation():
    ctrl_info= { 'c':'formXvalidation', 'v':'form-validation.html' }
    messages = ['formXvalidation', 'form-validation.html']
    #
    ctrl_template_url = "\'" + URL('formXvalidation' ) + "\'"

    # 
    fformXvalidation0= Form(db.dfformXvalidation0, dbio=False, formstyle=FormStyleBulma)
    if fformXvalidation0.accepted:
        icon_type ='success' if insert_form_vars(fformXvalidation0, db.dfformXvalidation0) else 'info'
        return json2user(mess = str( fformXvalidation0.form_name ), icon_type=icon_type )
    elif fformXvalidation0.errors:
        print("fformXvalidation0 has errors: %s" % (fformXvalidation0.errors))
        return json2user(mess = str(fformXvalidation0.form_name), icon_type = 'error')

    # 
    fformXvalidation1= Form(db.dfformXvalidation1, dbio=False, formstyle=FormStyleBulma)
    if fformXvalidation1.accepted:
        icon_type ='success' if insert_form_vars(fformXvalidation1, db.dfformXvalidation1) else 'info'
        return json2user(mess = str( fformXvalidation1.form_name ), icon_type=icon_type )
    elif fformXvalidation1.errors:
        print("fformXvalidation1 has errors: %s" % (fformXvalidation1.errors))
        return json2user(mess = str(fformXvalidation1.form_name), icon_type = 'error')

    # 
    fformXvalidation2= Form(db.dfformXvalidation2, dbio=False, formstyle=FormStyleBulma)
    if fformXvalidation2.accepted:
        icon_type ='success' if insert_form_vars(fformXvalidation2, db.dfformXvalidation2) else 'info'
        return json2user(mess = str( fformXvalidation2.form_name ), icon_type=icon_type )
    elif fformXvalidation2.errors:
        print("fformXvalidation2 has errors: %s" % (fformXvalidation2.errors))
        return json2user(mess = str(fformXvalidation2.form_name), icon_type = 'error')

    # 
    fformXvalidation3= Form(db.dfformXvalidation3, dbio=False, formstyle=FormStyleBulma)
    if fformXvalidation3.accepted:
        icon_type ='success' if insert_form_vars(fformXvalidation3, db.dfformXvalidation3) else 'info'
        return json2user(mess = str( fformXvalidation3.form_name ), icon_type=icon_type )
    elif fformXvalidation3.errors:
        print("fformXvalidation3 has errors: %s" % (fformXvalidation3.errors))
        return json2user(mess = str(fformXvalidation3.form_name), icon_type = 'error')

    return locals()

@action('chartXsparkline', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart-sparkline.html', delimiters='[%[ ]]',))

def chartXsparkline():
    ctrl_info= { 'c':'chartXsparkline', 'v':'chart-sparkline.html' }
    messages = ['chartXsparkline', 'chart-sparkline.html']
    #
    ctrl_template_url = "\'" + URL('chartXsparkline' ) + "\'"

    return locals()

@action('dashboardXsales', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dashboard-sales.html', delimiters='[%[ ]]',))

def dashboardXsales():
    ctrl_info= { 'c':'dashboardXsales', 'v':'dashboard-sales.html' }
    messages = ['dashboardXsales', 'dashboard-sales.html']
    #
    ctrl_template_url = "\'" + URL('dashboardXsales' ) + "\'"

    rows_tdashboardXsales0= db(db.tdashboardXsales0).select()
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

@action('iconXfontawesome', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-fontawesome.html', delimiters='[%[ ]]',))

def iconXfontawesome():
    ctrl_info= { 'c':'iconXfontawesome', 'v':'icon-fontawesome.html' }
    messages = ['iconXfontawesome', 'icon-fontawesome.html']
    #
    ctrl_template_url = "\'" + URL('iconXfontawesome' ) + "\'"

    return locals()

@action('bootstrapXselect', method=["GET", "POST"] )
@action.uses(db, session, T, Template('bootstrap-select.html', delimiters='[%[ ]]',))

def bootstrapXselect():
    ctrl_info= { 'c':'bootstrapXselect', 'v':'bootstrap-select.html' }
    messages = ['bootstrapXselect', 'bootstrap-select.html']
    #
    ctrl_template_url = "\'" + URL('bootstrapXselect' ) + "\'"

    return locals()

@action('blankXpageXheader', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank-page-header.html', delimiters='[%[ ]]',))

def blankXpageXheader():
    ctrl_info= { 'c':'blankXpageXheader', 'v':'blank-page-header.html' }
    messages = ['blankXpageXheader', 'blank-page-header.html']
    #
    ctrl_template_url = "\'" + URL('blankXpageXheader' ) + "\'"

    return locals()

@action('influencerXfinder', method=["GET", "POST"] )
@action.uses(db, session, T, Template('influencer-finder.html', delimiters='[%[ ]]',))

def influencerXfinder():
    ctrl_info= { 'c':'influencerXfinder', 'v':'influencer-finder.html' }
    messages = ['influencerXfinder', 'influencer-finder.html']
    #
    ctrl_template_url = "\'" + URL('influencerXfinder' ) + "\'"

    # 
    finfluencerXfinder0= Form(db.dfinfluencerXfinder0, dbio=False, formstyle=FormStyleBulma)
    if finfluencerXfinder0.accepted:
        icon_type ='success' if insert_form_vars(finfluencerXfinder0, db.dfinfluencerXfinder0) else 'info'
        return json2user(mess = str( finfluencerXfinder0.form_name ), icon_type=icon_type )
    elif finfluencerXfinder0.errors:
        print("finfluencerXfinder0 has errors: %s" % (finfluencerXfinder0.errors))
        return json2user(mess = str(finfluencerXfinder0.form_name), icon_type = 'error')

    return locals()

@action('dashboardXfinance', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dashboard-finance.html', delimiters='[%[ ]]',))

def dashboardXfinance():
    ctrl_info= { 'c':'dashboardXfinance', 'v':'dashboard-finance.html' }
    messages = ['dashboardXfinance', 'dashboard-finance.html']
    #
    ctrl_template_url = "\'" + URL('dashboardXfinance' ) + "\'"

    # 
    fdashboardXfinance0= Form(db.dfdashboardXfinance0, dbio=False, formstyle=FormStyleBulma)
    if fdashboardXfinance0.accepted:
        icon_type ='success' if insert_form_vars(fdashboardXfinance0, db.dfdashboardXfinance0) else 'info'
        return json2user(mess = str( fdashboardXfinance0.form_name ), icon_type=icon_type )
    elif fdashboardXfinance0.errors:
        print("fdashboardXfinance0 has errors: %s" % (fdashboardXfinance0.errors))
        return json2user(mess = str(fdashboardXfinance0.form_name), icon_type = 'error')

    return locals()

@action('ecommerceXproduct', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ecommerce-product.html', delimiters='[%[ ]]',))

def ecommerceXproduct():
    ctrl_info= { 'c':'ecommerceXproduct', 'v':'ecommerce-product.html' }
    messages = ['ecommerceXproduct', 'ecommerce-product.html']
    #
    ctrl_template_url = "\'" + URL('ecommerceXproduct' ) + "\'"

    return locals()

@action('influencerXprofile', method=["GET", "POST"] )
@action.uses(db, session, T, Template('influencer-profile.html', delimiters='[%[ ]]',))

def influencerXprofile():
    ctrl_info= { 'c':'influencerXprofile', 'v':'influencer-profile.html' }
    messages = ['influencerXprofile', 'influencer-profile.html']
    #
    ctrl_template_url = "\'" + URL('influencerXprofile' ) + "\'"

    # 
    finfluencerXprofile0= Form(db.dfinfluencerXprofile0, dbio=False, formstyle=FormStyleBulma)
    if finfluencerXprofile0.accepted:
        icon_type ='success' if insert_form_vars(finfluencerXprofile0, db.dfinfluencerXprofile0) else 'info'
        return json2user(mess = str( finfluencerXprofile0.form_name ), icon_type=icon_type )
    elif finfluencerXprofile0.errors:
        print("finfluencerXprofile0 has errors: %s" % (finfluencerXprofile0.errors))
        return json2user(mess = str(finfluencerXprofile0.form_name), icon_type = 'error')

    return locals()

@action('jqueryXmultiXselect', method=["GET", "POST"] )
@action.uses(db, session, T, Template('jquery.multi-select.html', delimiters='[%[ ]]',))

def jqueryXmultiXselect():
    ctrl_info= { 'c':'jqueryXmultiXselect', 'v':'jquery.multi-select.html' }
    messages = ['jqueryXmultiXselect', 'jquery.multi-select.html']
    #
    ctrl_template_url = "\'" + URL('jqueryXmultiXselect' ) + "\'"

    # 
    fjqueryXmultiXselect0= Form(db.dfjqueryXmultiXselect0, dbio=False, formstyle=FormStyleBulma)
    if fjqueryXmultiXselect0.accepted:
        icon_type ='success' if insert_form_vars(fjqueryXmultiXselect0, db.dfjqueryXmultiXselect0) else 'info'
        return json2user(mess = str( fjqueryXmultiXselect0.form_name ), icon_type=icon_type )
    elif fjqueryXmultiXselect0.errors:
        print("fjqueryXmultiXselect0 has errors: %s" % (fjqueryXmultiXselect0.errors))
        return json2user(mess = str(fjqueryXmultiXselect0.form_name), icon_type = 'error')

    # 
    fjqueryXmultiXselect1= Form(db.dfjqueryXmultiXselect1, dbio=False, formstyle=FormStyleBulma)
    if fjqueryXmultiXselect1.accepted:
        icon_type ='success' if insert_form_vars(fjqueryXmultiXselect1, db.dfjqueryXmultiXselect1) else 'info'
        return json2user(mess = str( fjqueryXmultiXselect1.form_name ), icon_type=icon_type )
    elif fjqueryXmultiXselect1.errors:
        print("fjqueryXmultiXselect1 has errors: %s" % (fjqueryXmultiXselect1.errors))
        return json2user(mess = str(fjqueryXmultiXselect1.form_name), icon_type = 'error')

    return locals()

@action('iconXsimpleXlineicon', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icon-simple-lineicon.html', delimiters='[%[ ]]',))

def iconXsimpleXlineicon():
    ctrl_info= { 'c':'iconXsimpleXlineicon', 'v':'icon-simple-lineicon.html' }
    messages = ['iconXsimpleXlineicon', 'icon-simple-lineicon.html']
    #
    ctrl_template_url = "\'" + URL('iconXsimpleXlineicon' ) + "\'"

    return locals()

@action('dashboardXinfluencer', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dashboard-influencer.html', delimiters='[%[ ]]',))

def dashboardXinfluencer():
    ctrl_info= { 'c':'dashboardXinfluencer', 'v':'dashboard-influencer.html' }
    messages = ['dashboardXinfluencer', 'dashboard-influencer.html']
    #
    ctrl_template_url = "\'" + URL('dashboardXinfluencer' ) + "\'"

    rows_tdashboardXinfluencer0= db(db.tdashboardXinfluencer0).select()
    return locals()

@action('sortableXnestableXlists', method=["GET", "POST"] )
@action.uses(db, session, T, Template('sortable-nestable-lists.html', delimiters='[%[ ]]',))

def sortableXnestableXlists():
    ctrl_info= { 'c':'sortableXnestableXlists', 'v':'sortable-nestable-lists.html' }
    messages = ['sortableXnestableXlists', 'sortable-nestable-lists.html']
    #
    ctrl_template_url = "\'" + URL('sortableXnestableXlists' ) + "\'"

    return locals()

@action('ecommerceXproductXsingle', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ecommerce-product-single.html', delimiters='[%[ ]]',))

def ecommerceXproductXsingle():
    ctrl_info= { 'c':'ecommerceXproductXsingle', 'v':'ecommerce-product-single.html' }
    messages = ['ecommerceXproductXsingle', 'ecommerce-product-single.html']
    #
    ctrl_template_url = "\'" + URL('ecommerceXproductXsingle' ) + "\'"

    return locals()

@action('ecommerceXproductXcheckout', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ecommerce-product-checkout.html', delimiters='[%[ ]]',))

def ecommerceXproductXcheckout():
    ctrl_info= { 'c':'ecommerceXproductXcheckout', 'v':'ecommerce-product-checkout.html' }
    messages = ['ecommerceXproductXcheckout', 'ecommerce-product-checkout.html']
    #
    ctrl_template_url = "\'" + URL('ecommerceXproductXcheckout' ) + "\'"

    # 
    fecommerceXproductXcheckout0= Form(db.dfecommerceXproductXcheckout0, dbio=False, formstyle=FormStyleBulma)
    if fecommerceXproductXcheckout0.accepted:
        icon_type ='success' if insert_form_vars(fecommerceXproductXcheckout0, db.dfecommerceXproductXcheckout0) else 'info'
        return json2user(mess = str( fecommerceXproductXcheckout0.form_name ), icon_type=icon_type )
    elif fecommerceXproductXcheckout0.errors:
        print("fecommerceXproductXcheckout0 has errors: %s" % (fecommerceXproductXcheckout0.errors))
        return json2user(mess = str(fecommerceXproductXcheckout0.form_name), icon_type = 'error')

    # 
    fecommerceXproductXcheckout1= Form(db.dfecommerceXproductXcheckout1, dbio=False, formstyle=FormStyleBulma)
    if fecommerceXproductXcheckout1.accepted:
        icon_type ='success' if insert_form_vars(fecommerceXproductXcheckout1, db.dfecommerceXproductXcheckout1) else 'info'
        return json2user(mess = str( fecommerceXproductXcheckout1.form_name ), icon_type=icon_type )
    elif fecommerceXproductXcheckout1.errors:
        print("fecommerceXproductXcheckout1 has errors: %s" % (fecommerceXproductXcheckout1.errors))
        return json2user(mess = str(fecommerceXproductXcheckout1.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/concept/api/test_table/
# curl -X  GET   http://localhost:8000/concept/api/test_table/9
# curl -X DELETE  http://localhost:8000/concept/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/concept/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/concept/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/concept/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/concept/api/test_table/
#  http         localhost:8000/concept/api/test_table/9
#  http -f POST localhost:8000/concept/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/concept/api/test_table/2
#  http -f PUT localhost:8000/concept/api/test_table/2 f0=111111 f1=2222222 f2=333333

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
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    menu = DIV(
               P( "backand-admin-panel"),
               A( "sql2table", _role="button", _href=URL('mytab_grid', ),) ,
               A( "p4wupload_file", _role="button", _href=URL('p4wupload_file', ),) ,
               A( "tlist", _role="button", _href=URL('tlist', ),) ,
               A( "app_images", _role="button", _href=URL('ima_grid', ),) ,
              )
    return dict(message=message, menu=menu)

