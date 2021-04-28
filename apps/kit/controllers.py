#
# py4web app, AI-biorex ported 28.04.2021 12:04:48 UTC+3, src: https://github.com/adminkit/adminkit

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

@action('uiXgrid', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-grid.html', delimiters='[%[ ]]',))

def uiXgrid():
    ctrl_info= { 'c':'uiXgrid', 'v':'ui-grid.html' }
    messages = ['uiXgrid', 'ui-grid.html']
    #
    ctrl_template_url = "\'" + URL('uiXgrid' ) + "\'"

    # 
    fuiXgrid0= Form(db.dfuiXgrid0, dbio=False, formstyle=FormStyleBulma)
    if fuiXgrid0.accepted:
        icon_type ='success' if insert_form_vars(fuiXgrid0, db.dfuiXgrid0) else 'info'
        return json2user(mess = str( fuiXgrid0.form_name ), icon_type=icon_type )
    elif fuiXgrid0.errors:
        print("fuiXgrid0 has errors: %s" % (fuiXgrid0.errors))
        return json2user(mess = str(fuiXgrid0.form_name), icon_type = 'error')

    return locals()

@action('uiXcards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-cards.html', delimiters='[%[ ]]',))

def uiXcards():
    ctrl_info= { 'c':'uiXcards', 'v':'ui-cards.html' }
    messages = ['uiXcards', 'ui-cards.html']
    #
    ctrl_template_url = "\'" + URL('uiXcards' ) + "\'"

    # 
    fuiXcards0= Form(db.dfuiXcards0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcards0.accepted:
        icon_type ='success' if insert_form_vars(fuiXcards0, db.dfuiXcards0) else 'info'
        return json2user(mess = str( fuiXcards0.form_name ), icon_type=icon_type )
    elif fuiXcards0.errors:
        print("fuiXcards0 has errors: %s" % (fuiXcards0.errors))
        return json2user(mess = str(fuiXcards0.form_name), icon_type = 'error')

    return locals()

@action('uiXmodals', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-modals.html', delimiters='[%[ ]]',))

def uiXmodals():
    ctrl_info= { 'c':'uiXmodals', 'v':'ui-modals.html' }
    messages = ['uiXmodals', 'ui-modals.html']
    #
    ctrl_template_url = "\'" + URL('uiXmodals' ) + "\'"

    # 
    fuiXmodals0= Form(db.dfuiXmodals0, dbio=False, formstyle=FormStyleBulma)
    if fuiXmodals0.accepted:
        icon_type ='success' if insert_form_vars(fuiXmodals0, db.dfuiXmodals0) else 'info'
        return json2user(mess = str( fuiXmodals0.form_name ), icon_type=icon_type )
    elif fuiXmodals0.errors:
        print("fuiXmodals0 has errors: %s" % (fuiXmodals0.errors))
        return json2user(mess = str(fuiXmodals0.form_name), icon_type = 'error')

    return locals()

@action('uiXalerts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-alerts.html', delimiters='[%[ ]]',))

def uiXalerts():
    ctrl_info= { 'c':'uiXalerts', 'v':'ui-alerts.html' }
    messages = ['uiXalerts', 'ui-alerts.html']
    #
    ctrl_template_url = "\'" + URL('uiXalerts' ) + "\'"

    # 
    fuiXalerts0= Form(db.dfuiXalerts0, dbio=False, formstyle=FormStyleBulma)
    if fuiXalerts0.accepted:
        icon_type ='success' if insert_form_vars(fuiXalerts0, db.dfuiXalerts0) else 'info'
        return json2user(mess = str( fuiXalerts0.form_name ), icon_type=icon_type )
    elif fuiXalerts0.errors:
        print("fuiXalerts0 has errors: %s" % (fuiXalerts0.errors))
        return json2user(mess = str(fuiXalerts0.form_name), icon_type = 'error')

    return locals()

@action('uiXbuttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-buttons.html', delimiters='[%[ ]]',))

def uiXbuttons():
    ctrl_info= { 'c':'uiXbuttons', 'v':'ui-buttons.html' }
    messages = ['uiXbuttons', 'ui-buttons.html']
    #
    ctrl_template_url = "\'" + URL('uiXbuttons' ) + "\'"

    # 
    fuiXbuttons0= Form(db.dfuiXbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fuiXbuttons0.accepted:
        icon_type ='success' if insert_form_vars(fuiXbuttons0, db.dfuiXbuttons0) else 'info'
        return json2user(mess = str( fuiXbuttons0.form_name ), icon_type=icon_type )
    elif fuiXbuttons0.errors:
        print("fuiXbuttons0 has errors: %s" % (fuiXbuttons0.errors))
        return json2user(mess = str(fuiXbuttons0.form_name), icon_type = 'error')

    return locals()

@action('uiXgeneral', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-general.html', delimiters='[%[ ]]',))

def uiXgeneral():
    ctrl_info= { 'c':'uiXgeneral', 'v':'ui-general.html' }
    messages = ['uiXgeneral', 'ui-general.html']
    #
    ctrl_template_url = "\'" + URL('uiXgeneral' ) + "\'"

    # 
    fuiXgeneral0= Form(db.dfuiXgeneral0, dbio=False, formstyle=FormStyleBulma)
    if fuiXgeneral0.accepted:
        icon_type ='success' if insert_form_vars(fuiXgeneral0, db.dfuiXgeneral0) else 'info'
        return json2user(mess = str( fuiXgeneral0.form_name ), icon_type=icon_type )
    elif fuiXgeneral0.errors:
        print("fuiXgeneral0 has errors: %s" % (fuiXgeneral0.errors))
        return json2user(mess = str(fuiXgeneral0.form_name), icon_type = 'error')

    return locals()

@action('pagesXblank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-blank.html', delimiters='[%[ ]]',))

def pagesXblank():
    ctrl_info= { 'c':'pagesXblank', 'v':'pages-blank.html' }
    messages = ['pagesXblank', 'pages-blank.html']
    #
    ctrl_template_url = "\'" + URL('pagesXblank' ) + "\'"

    # 
    fpagesXblank0= Form(db.dfpagesXblank0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXblank0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXblank0, db.dfpagesXblank0) else 'info'
        return json2user(mess = str( fpagesXblank0.form_name ), icon_type=icon_type )
    elif fpagesXblank0.errors:
        print("fpagesXblank0 has errors: %s" % (fpagesXblank0.errors))
        return json2user(mess = str(fpagesXblank0.form_name), icon_type = 'error')

    return locals()

@action('mapsXgoogle', method=["GET", "POST"] )
@action.uses(db, session, T, Template('maps-google.html', delimiters='[%[ ]]',))

def mapsXgoogle():
    ctrl_info= { 'c':'mapsXgoogle', 'v':'maps-google.html' }
    messages = ['mapsXgoogle', 'maps-google.html']
    #
    ctrl_template_url = "\'" + URL('mapsXgoogle' ) + "\'"

    # 
    fmapsXgoogle0= Form(db.dfmapsXgoogle0, dbio=False, formstyle=FormStyleBulma)
    if fmapsXgoogle0.accepted:
        icon_type ='success' if insert_form_vars(fmapsXgoogle0, db.dfmapsXgoogle0) else 'info'
        return json2user(mess = str( fmapsXgoogle0.form_name ), icon_type=icon_type )
    elif fmapsXgoogle0.errors:
        print("fmapsXgoogle0 has errors: %s" % (fmapsXgoogle0.errors))
        return json2user(mess = str(fmapsXgoogle0.form_name), icon_type = 'error')

    return locals()

@action('uiXtypography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-typography.html', delimiters='[%[ ]]',))

def uiXtypography():
    ctrl_info= { 'c':'uiXtypography', 'v':'ui-typography.html' }
    messages = ['uiXtypography', 'ui-typography.html']
    #
    ctrl_template_url = "\'" + URL('uiXtypography' ) + "\'"

    # 
    fuiXtypography0= Form(db.dfuiXtypography0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtypography0.accepted:
        icon_type ='success' if insert_form_vars(fuiXtypography0, db.dfuiXtypography0) else 'info'
        return json2user(mess = str( fuiXtypography0.form_name ), icon_type=icon_type )
    elif fuiXtypography0.errors:
        print("fuiXtypography0 has errors: %s" % (fuiXtypography0.errors))
        return json2user(mess = str(fuiXtypography0.form_name), icon_type = 'error')

    return locals()

@action('pagesXsignXin', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-sign-in.html', delimiters='[%[ ]]',))

def pagesXsignXin():
    ctrl_info= { 'c':'pagesXsignXin', 'v':'pages-sign-in.html' }
    messages = ['pagesXsignXin', 'pages-sign-in.html']
    #
    ctrl_template_url = "\'" + URL('pagesXsignXin' ) + "\'"

    # 
    fpagesXsignXin0= Form(db.dfpagesXsignXin0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsignXin0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsignXin0, db.dfpagesXsignXin0) else 'info'
        return json2user(mess = str( fpagesXsignXin0.form_name ), icon_type=icon_type )
    elif fpagesXsignXin0.errors:
        print("fpagesXsignXin0 has errors: %s" % (fpagesXsignXin0.errors))
        return json2user(mess = str(fpagesXsignXin0.form_name), icon_type = 'error')

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

    return locals()

@action('pagesXprofile', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-profile.html', delimiters='[%[ ]]',))

def pagesXprofile():
    ctrl_info= { 'c':'pagesXprofile', 'v':'pages-profile.html' }
    messages = ['pagesXprofile', 'pages-profile.html']
    #
    ctrl_template_url = "\'" + URL('pagesXprofile' ) + "\'"

    # 
    fpagesXprofile0= Form(db.dfpagesXprofile0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXprofile0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXprofile0, db.dfpagesXprofile0) else 'info'
        return json2user(mess = str( fpagesXprofile0.form_name ), icon_type=icon_type )
    elif fpagesXprofile0.errors:
        print("fpagesXprofile0 has errors: %s" % (fpagesXprofile0.errors))
        return json2user(mess = str(fpagesXprofile0.form_name), icon_type = 'error')

    return locals()

@action('pagesXinvoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-invoice.html', delimiters='[%[ ]]',))

def pagesXinvoice():
    ctrl_info= { 'c':'pagesXinvoice', 'v':'pages-invoice.html' }
    messages = ['pagesXinvoice', 'pages-invoice.html']
    #
    ctrl_template_url = "\'" + URL('pagesXinvoice' ) + "\'"

    rows_tpagesXinvoice0= db(db.tpagesXinvoice0).select()
    # 
    fpagesXinvoice0= Form(db.dfpagesXinvoice0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXinvoice0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXinvoice0, db.dfpagesXinvoice0) else 'info'
        return json2user(mess = str( fpagesXinvoice0.form_name ), icon_type=icon_type )
    elif fpagesXinvoice0.errors:
        print("fpagesXinvoice0 has errors: %s" % (fpagesXinvoice0.errors))
        return json2user(mess = str(fpagesXinvoice0.form_name), icon_type = 'error')

    return locals()

@action('formsXlayouts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forms-layouts.html', delimiters='[%[ ]]',))

def formsXlayouts():
    ctrl_info= { 'c':'formsXlayouts', 'v':'forms-layouts.html' }
    messages = ['formsXlayouts', 'forms-layouts.html']
    #
    ctrl_template_url = "\'" + URL('formsXlayouts' ) + "\'"

    # 
    fformsXlayouts0= Form(db.dfformsXlayouts0, dbio=False, formstyle=FormStyleBulma)
    if fformsXlayouts0.accepted:
        icon_type ='success' if insert_form_vars(fformsXlayouts0, db.dfformsXlayouts0) else 'info'
        return json2user(mess = str( fformsXlayouts0.form_name ), icon_type=icon_type )
    elif fformsXlayouts0.errors:
        print("fformsXlayouts0 has errors: %s" % (fformsXlayouts0.errors))
        return json2user(mess = str(fformsXlayouts0.form_name), icon_type = 'error')

    # 
    fformsXlayouts1= Form(db.dfformsXlayouts1, dbio=False, formstyle=FormStyleBulma)
    if fformsXlayouts1.accepted:
        icon_type ='success' if insert_form_vars(fformsXlayouts1, db.dfformsXlayouts1) else 'info'
        return json2user(mess = str( fformsXlayouts1.form_name ), icon_type=icon_type )
    elif fformsXlayouts1.errors:
        print("fformsXlayouts1 has errors: %s" % (fformsXlayouts1.errors))
        return json2user(mess = str(fformsXlayouts1.form_name), icon_type = 'error')

    # 
    fformsXlayouts2= Form(db.dfformsXlayouts2, dbio=False, formstyle=FormStyleBulma)
    if fformsXlayouts2.accepted:
        icon_type ='success' if insert_form_vars(fformsXlayouts2, db.dfformsXlayouts2) else 'info'
        return json2user(mess = str( fformsXlayouts2.form_name ), icon_type=icon_type )
    elif fformsXlayouts2.errors:
        print("fformsXlayouts2 has errors: %s" % (fformsXlayouts2.errors))
        return json2user(mess = str(fformsXlayouts2.form_name), icon_type = 'error')

    # 
    fformsXlayouts3= Form(db.dfformsXlayouts3, dbio=False, formstyle=FormStyleBulma)
    if fformsXlayouts3.accepted:
        icon_type ='success' if insert_form_vars(fformsXlayouts3, db.dfformsXlayouts3) else 'info'
        return json2user(mess = str( fformsXlayouts3.form_name ), icon_type=icon_type )
    elif fformsXlayouts3.errors:
        print("fformsXlayouts3 has errors: %s" % (fformsXlayouts3.errors))
        return json2user(mess = str(fformsXlayouts3.form_name), icon_type = 'error')

    # 
    fformsXlayouts4= Form(db.dfformsXlayouts4, dbio=False, formstyle=FormStyleBulma)
    if fformsXlayouts4.accepted:
        icon_type ='success' if insert_form_vars(fformsXlayouts4, db.dfformsXlayouts4) else 'info'
        return json2user(mess = str( fformsXlayouts4.form_name ), icon_type=icon_type )
    elif fformsXlayouts4.errors:
        print("fformsXlayouts4 has errors: %s" % (fformsXlayouts4.errors))
        return json2user(mess = str(fformsXlayouts4.form_name), icon_type = 'error')

    return locals()

@action('iconsXfeather', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icons-feather.html', delimiters='[%[ ]]',))

def iconsXfeather():
    ctrl_info= { 'c':'iconsXfeather', 'v':'icons-feather.html' }
    messages = ['iconsXfeather', 'icons-feather.html']
    #
    ctrl_template_url = "\'" + URL('iconsXfeather' ) + "\'"

    # 
    ficonsXfeather0= Form(db.dficonsXfeather0, dbio=False, formstyle=FormStyleBulma)
    if ficonsXfeather0.accepted:
        icon_type ='success' if insert_form_vars(ficonsXfeather0, db.dficonsXfeather0) else 'info'
        return json2user(mess = str( ficonsXfeather0.form_name ), icon_type=icon_type )
    elif ficonsXfeather0.errors:
        print("ficonsXfeather0 has errors: %s" % (ficonsXfeather0.errors))
        return json2user(mess = str(ficonsXfeather0.form_name), icon_type = 'error')

    return locals()

@action('pagesXsettings', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-settings.html', delimiters='[%[ ]]',))

def pagesXsettings():
    ctrl_info= { 'c':'pagesXsettings', 'v':'pages-settings.html' }
    messages = ['pagesXsettings', 'pages-settings.html']
    #
    ctrl_template_url = "\'" + URL('pagesXsettings' ) + "\'"

    # 
    fpagesXsettings0= Form(db.dfpagesXsettings0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsettings0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsettings0, db.dfpagesXsettings0) else 'info'
        return json2user(mess = str( fpagesXsettings0.form_name ), icon_type=icon_type )
    elif fpagesXsettings0.errors:
        print("fpagesXsettings0 has errors: %s" % (fpagesXsettings0.errors))
        return json2user(mess = str(fpagesXsettings0.form_name), icon_type = 'error')

    # 
    fpagesXsettings1= Form(db.dfpagesXsettings1, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsettings1.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsettings1, db.dfpagesXsettings1) else 'info'
        return json2user(mess = str( fpagesXsettings1.form_name ), icon_type=icon_type )
    elif fpagesXsettings1.errors:
        print("fpagesXsettings1 has errors: %s" % (fpagesXsettings1.errors))
        return json2user(mess = str(fpagesXsettings1.form_name), icon_type = 'error')

    # 
    fpagesXsettings2= Form(db.dfpagesXsettings2, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsettings2.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsettings2, db.dfpagesXsettings2) else 'info'
        return json2user(mess = str( fpagesXsettings2.form_name ), icon_type=icon_type )
    elif fpagesXsettings2.errors:
        print("fpagesXsettings2 has errors: %s" % (fpagesXsettings2.errors))
        return json2user(mess = str(fpagesXsettings2.form_name), icon_type = 'error')

    # 
    fpagesXsettings3= Form(db.dfpagesXsettings3, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsettings3.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsettings3, db.dfpagesXsettings3) else 'info'
        return json2user(mess = str( fpagesXsettings3.form_name ), icon_type=icon_type )
    elif fpagesXsettings3.errors:
        print("fpagesXsettings3 has errors: %s" % (fpagesXsettings3.errors))
        return json2user(mess = str(fpagesXsettings3.form_name), icon_type = 'error')

    return locals()

@action('chartsXchartjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('charts-chartjs.html', delimiters='[%[ ]]',))

def chartsXchartjs():
    ctrl_info= { 'c':'chartsXchartjs', 'v':'charts-chartjs.html' }
    messages = ['chartsXchartjs', 'charts-chartjs.html']
    #
    ctrl_template_url = "\'" + URL('chartsXchartjs' ) + "\'"

    # 
    fchartsXchartjs0= Form(db.dfchartsXchartjs0, dbio=False, formstyle=FormStyleBulma)
    if fchartsXchartjs0.accepted:
        icon_type ='success' if insert_form_vars(fchartsXchartjs0, db.dfchartsXchartjs0) else 'info'
        return json2user(mess = str( fchartsXchartjs0.form_name ), icon_type=icon_type )
    elif fchartsXchartjs0.errors:
        print("fchartsXchartjs0 has errors: %s" % (fchartsXchartjs0.errors))
        return json2user(mess = str(fchartsXchartjs0.form_name), icon_type = 'error')

    return locals()

@action('tablesXbootstrap', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tables-bootstrap.html', delimiters='[%[ ]]',))

def tablesXbootstrap():
    ctrl_info= { 'c':'tablesXbootstrap', 'v':'tables-bootstrap.html' }
    messages = ['tablesXbootstrap', 'tables-bootstrap.html']
    #
    ctrl_template_url = "\'" + URL('tablesXbootstrap' ) + "\'"

    rows_ttablesXbootstrap0= db(db.ttablesXbootstrap0).select()
    rows_ttablesXbootstrap1= db(db.ttablesXbootstrap1).select()
    rows_ttablesXbootstrap2= db(db.ttablesXbootstrap2).select()
    rows_ttablesXbootstrap3= db(db.ttablesXbootstrap3).select()
    rows_ttablesXbootstrap4= db(db.ttablesXbootstrap4).select()
    rows_ttablesXbootstrap5= db(db.ttablesXbootstrap5).select()
    rows_ttablesXbootstrap6= db(db.ttablesXbootstrap6).select()
    # 
    ftablesXbootstrap0= Form(db.dftablesXbootstrap0, dbio=False, formstyle=FormStyleBulma)
    if ftablesXbootstrap0.accepted:
        icon_type ='success' if insert_form_vars(ftablesXbootstrap0, db.dftablesXbootstrap0) else 'info'
        return json2user(mess = str( ftablesXbootstrap0.form_name ), icon_type=icon_type )
    elif ftablesXbootstrap0.errors:
        print("ftablesXbootstrap0 has errors: %s" % (ftablesXbootstrap0.errors))
        return json2user(mess = str(ftablesXbootstrap0.form_name), icon_type = 'error')

    return locals()

@action('formsXbasicXinputs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forms-basic-inputs.html', delimiters='[%[ ]]',))

def formsXbasicXinputs():
    ctrl_info= { 'c':'formsXbasicXinputs', 'v':'forms-basic-inputs.html' }
    messages = ['formsXbasicXinputs', 'forms-basic-inputs.html']
    #
    ctrl_template_url = "\'" + URL('formsXbasicXinputs' ) + "\'"

    # 
    fformsXbasicXinputs0= Form(db.dfformsXbasicXinputs0, dbio=False, formstyle=FormStyleBulma)
    if fformsXbasicXinputs0.accepted:
        icon_type ='success' if insert_form_vars(fformsXbasicXinputs0, db.dfformsXbasicXinputs0) else 'info'
        return json2user(mess = str( fformsXbasicXinputs0.form_name ), icon_type=icon_type )
    elif fformsXbasicXinputs0.errors:
        print("fformsXbasicXinputs0 has errors: %s" % (fformsXbasicXinputs0.errors))
        return json2user(mess = str(fformsXbasicXinputs0.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/kit/api/test_table/
# curl -X  GET   http://localhost:8000/kit/api/test_table/9
# curl -X DELETE  http://localhost:8000/kit/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/kit/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/kit/api/test_table/
#  http         localhost:8000/kit/api/test_table/9
#  http -f POST localhost:8000/kit/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/kit/api/test_table/2
#  http -f PUT localhost:8000/kit/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

