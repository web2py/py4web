import os, json, uuid, datetime
from py4web import action, request, response, abort, redirect, URL, Field
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from py4web.utils.form import Form, FormStyleBulma, FormStyleDefault
from .settings import APP_NAME, UPLOAD_FOLDER
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import A, I, SPAN, XML, DIV, P, TABLE, THEAD, TR, TD, TBODY, H6, IMG

from .atab_utils import sql2table


def get_unique_name(orig_name='', default_len=10):
    if orig_name:
       orig_name =  orig_name[:default_len] + '_'
    suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_")
    return "_".join(['at', suffix]) +orig_name + str(uuid.uuid4())

def data2file( data, fnm, mode = 'wb' ):
    with open(fnm, mode) as f:
        f.write( data )
    return fnm

@action("p4wdownload_file", method=["GET", "POST"])
@action.uses(session, db, auth, "p4wdownload_file.html")
def p4wdownload_file():
    tbl = dict(request.query).get('t_', '') 
    if not tbl in db.tables:
        return f"bad table: {tbl}"
    id_ = dict(request.query).get('id_', 1)
    try:
        id = int(id_)
    except ( ValueError, TypeError) :
        id = 1


    r = db[tbl](id)
    if r is None:
        return f"bad id: {id}"

    orig_fnm = r.orig_file_name

    fpath = os.path.join( UPLOAD_FOLDER , r.uniq_file_name )

    return file2browser (  fpath , orig_fnm )


def file2browser( file_path , orig_fnm = 'orig_fnm'  ):    
    import mimetypes
    mimetypes.init()

    file_content = '';

    try:
         with open(file_path, 'rb') as f:
           file_content= f.read()
    except IOError:
           file_content = f"Error: File {orig_fnm} {file_path} does not appear to exist"

    ext = os.path.splitext( orig_fnm  )
    tru_ext = ext[1].lower() if len(ext) and len(ext[1]) else ''

    file_type = mimetypes.types_map.get(tru_ext, None)
    view_in_browser =('.pdf','.jpeg','.txt','.jpg','.jpe','.png','.gif','.tif','.tiff','.bmp','.svg','.ico')

    response.headers['Content-Type'] = 'application/octet-stream' if file_type is None else file_type

    response.headers['Content-disposition'] = 'inline; filename=\"%s"' % ( orig_fnm)  \
                           if not file_type is None and tru_ext.endswith( view_in_browser  ) \
                           else 'attachment; filename=\"%s"' % ( orig_fnm)
    return file_content


@action("p4wdelete_file", method=["GET", "POST"])
@action.uses(session, db, auth, )
#@action.uses(session, db, auth, "p4wdelete_file.html")
def p4wdelete_file():
    tbl = dict(request.query).get('t_', '')
    if not tbl in db.tables:
        return f"bad table: {tbl}"
    id_ = dict(request.query).get('id_', 0)
    try:
        id = int(id_)
    except ( ValueError, TypeError) :
        return f"bad id: {id_}"
    #return f"{tbl} {id}"

    r = db[tbl](id)
    if r is None:
        return f"bad id: {id}"

    file_path = os.path.join( UPLOAD_FOLDER , r.uniq_file_name )

    if os.path.isfile( file_path  ):
         os.remove( file_path  )

    db(db[tbl].id == id  ).delete()
    db.commit()
    redirect(URL('p4wupload_file', vars=dict(t_=tbl, id_=id)  ))
   

#---------------------------------------------------------------------------------------------------------

from py4web.utils.form import Form, FormStyleBulma, FormStyleDefault
from .settings import APP_NAME, UPLOAD_FOLDER
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB

from .common import flash

@action("p4wupload_file", method=["GET", "POST"])
@action.uses(flash,  session, db, T, "p4wupload_file.html")
def p4wupload_file():

    t_id = dict(request.query).get('id_', '0')
    #if t_id != '0': 
    #    flash.set(f"deleted id={t_id}", sanitize=True)

    if not os.path.isdir(UPLOAD_FOLDER):
         return f"bad upload path: {UPLOAD_FOLDER}"

    messages= []
    tbl = 'uploaded_files'
    upload_field = 'image'
    upload_form = Form(
        [
            Field( upload_field, 'upload', requires=IS_NOT_EMPTY(),),
            Field("remark", default='mycomment' ),
        ],
        formstyle=FormStyleDefault,
    )

    if upload_form.accepted and hasattr(request, 'files')  :
        bottle_class=request.files.get( upload_field, None)
        if bottle_class:
             image_file = bottle_class.raw_filename
             image_content = bottle_class.file.read()
             uniq_file_name = get_unique_name( )
             fnm2 = os.path.join( UPLOAD_FOLDER , uniq_file_name )
             with open(fnm2, 'wb') as f:
                  f.write( image_content )
             row = dict( orig_file_name = image_file, uniq_file_name=uniq_file_name, remark=upload_form.vars['remark']  )
             if db[tbl].insert(**db[tbl]._filter_fields(row)):
                   db.commit()

    elif upload_form.errors:
        messages.append( f"upload_form has errors: {upload_form.errors}")


    hlinks = ["save", "del"]

    links = [
        lambda tx, r_id: A(
            f"save:[{r_id}]",
            _title='save file to disk',
            _href=URL(f"p4wdownload_file", vars=dict(t_=tx, id_=r_id)),
        ),

        lambda tx, r_id: A(
            f"del:[{r_id}]",
            _title="run p4wdelete_file",
            _href=URL(f"p4wdelete_file", vars=dict(t_=tx, id_=r_id)),
        ),

    ]

    fld_links = {
      #  'id': lambda tx, xx, r_id: A(
      #      f'save[{r_id}]',
      #      _title='save file to disk',
      #      _href=URL(f"p4wdownload_file", vars=dict(t_=tx, x_=xx, id_=r_id)),
      #  ),
        'time': lambda tx, xx, r_id: SPAN( xx.strftime("%d.%m.%Y %H:%M:%S"), _style="color:red" ), 
    }

    mygrid = sql2table( tbl, db, links=links, hlinks=hlinks, fld_links=fld_links, items_on_page = 2, caller="p4wupload_file", page_d=dict(request.query))
    return dict( messages=messages,  upload_form=upload_form, mygrid=mygrid   ) 

#---------------------------------------------------------------------------------------------------------
