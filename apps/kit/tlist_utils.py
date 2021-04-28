from yatl.helpers import A, I, SPAN, XML, DIV, P, TABLE, THEAD, TR, TD, TBODY, H6, IMG
from py4web import action, request, response, abort, redirect, URL, Field
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.grid import Grid, GridClassStyle
from py4web.utils.form import Form, FormStyleDefault
from py4web.core import Template
from py4web import URL
import pydal

from .atab_utils import sql2table

from .common import flash

@action("tlist", method=["GET", "POST"])
@action.uses(flash, db, session, T, Template("tlist.html", delimiters="[[ ]]"),)
def tlist():
    ts=[ e for e in db.tables  ]
    headers= ['tname', 'len',  'cmd1', 'cmd2', 'cmd3']

    #flash.set("Hello World", sanitize=True)

    #cmd = ['000', '111', '222', '333']

    def show_len(tn):
        c = db(db[tn].id>0).count()
        return f'{c}' if c else ''


    cmd = [ 
            lambda tn : show_len(tn) ,
            lambda tn : A( "table",  _role="button",  _href=URL( f"p4w_sql_table/{tn}",   ), ) ,
            lambda tn : A( "form",   _role="button",  _href=URL( f"p4w_create_form/{tn}", ), ) , 
            lambda tn : A( "grid",   _role="button",  _href=URL( f"p4w_grid/{tn}",        ), ) ,
          ]

    #w, h = len(cmd), len(ts);
    #Matrix = [[0 for x in range(w)] for y in range(h)] 

    Matrix = [[0 for x in range(1+ len( cmd ))] for y in range(  len(ts) )] 
    for i in range(len( ts  )):
        tnn = ts[i]
        for j in range(1 + len( cmd ) ):
           if j == 0:
               Matrix [i] [j] = tnn #ts[i]
           else:
               Matrix [i] [j] = cmd[j-1]( tnn  )
        
    #print (Matrix) 
    xview= DIV(
             SPAN(ts, _style="color:red"),
             TABLE(
                   #THEAD(TR(*[TD(H6(h)) for h in headers])),
                   TBODY(*[TR(*[TD(Matrix[y][x]) for x in range(1+ len(cmd))]) for y in range (len(ts))]),
                   ),
           )
    return dict(message=f'{len(ts)} tables:', xview=xview) 



@action("mygrid", method=["GET", "POST"])
def mygrid():
    args = repr(dict(request.query))
    return f"mygrid: {args}"

@action("p4w_form", method=["GET", "POST"])
def p4w_form():
    args = repr(dict(request.query))
    return f"p4w_form: {args}"

@action("f1", method=["GET", "POST"])
def f1():
    args = repr(dict(request.query))
    tbl = dict( request.query ).get('t_','') 
    redirect( URL(  f"p4w_grid/{tbl}") )
    
    
    return f"f1: {args}"

@action("p4w_grid")
@action("p4w_grid/<path:path>", method=["POST", "GET"])
@action.uses(session, db, auth, "p4w_grid.html")
def p4w_grid(path=None,):
    def get_param(ppath=None):
        if not ppath is None:
            if any([e in ppath for e in ("/details/", "/edit/", "/delete/", "/new")]):
                return ppath.split("/", 1)
            elif not "/" in path:
                return ppath, None
        return None, ppath

    #user = auth.get_user()
#
    #if len(user):
    #    message = "hello {first_name}".format(**user)
    #else:
    #    redirect(URL("tabadm"))
    #print ( path )

    tbl, path = get_param(path)

    if not tbl in db.tables:
        return f"bad table: {tbl}, path: {path}"

    grid_param = dict(
        rows_per_page=5,
        include_action_button_text=False,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
    )

    # labels=[ db[tbl][f].label for f in db[tbl].fields ]
    search_queries = [
        [db[tbl][f].label + " ~ ", lambda v: db[tbl][f].contains(v)]
        for f in db[tbl].fields
        if f != "id"
    ]
    search_queries.append(
        ["id = ", lambda v: db[tbl].id == int(v) if v.isnumeric() else "error"]
    )
    query = db[tbl].id > 0
    orderby = [db[tbl].id]
    fields = [field for field in db[tbl] if field.readable]
    grid = Grid(
        path,
        query,
        fields=fields,
        search_queries=search_queries,
        orderby=orderby,
        **grid_param,
    )
  
    import datetime
 
    def re_fmt(tbl):
        xfmt= dict()
        for e in db[tbl].fields:
           if  db[tbl][e].type == 'datetime':
                #print (  f"{tbl}.{e}"  )
                xfmt[ f"{tbl}.{e}"] =  lambda e: SPAN( e.strftime("%d.%m.%Y %H:%M:%S"), _style="color:red"  ) 
           else:  
                xfmt[ f"{tbl}.{e}"] =  lambda e: SPAN(e[:15] + "...") 
           
        return xfmt

    #fmt = {f"{tbl}.{e}": lambda e: SPAN(e[:20] + "...") for e in db[tbl].fields}
    fmt = re_fmt( tbl )
    for k, v in fmt.items():
        grid.formatters[k] = v
    
    return dict(grid=grid, message=SPAN(f'{tbl}', _style="color:red"))


@action("p4w_create_form", method=["GET", "POST"])
@action("p4w_create_form/<path:path>", method=["GET", "POST"])
@action.uses(session, db, auth, "p4w_create_form.html")
def p4w_html_form(path=None, id=None):
    #print ('form path: ', path)
    if '/' in path:
        path, id = path.split('/',1)
    tbl = path
    if not tbl in db.tables:
        return f"bad table: {tbl}, path: {path}"
    form = Form(db[tbl], id, deletable=False, formstyle=FormStyleDefault)
    return dict(message=SPAN( tbl, _style="color:red"  ), form=form) 

@action("p4w_sql_table", method=["GET", "POST"])
@action("p4w_sql_table/<path:path>", method=["GET", "POST"])
@action.uses(session, db, auth, "p4w_sql_table.html")
def p4w_sql_table(path=None, id=None):
    #print ('form path: ', path)
    if '/' in path:
        path, id = path.split('/',1)
    tbl = path
    if not tbl in db.tables:
        return f"bad table: {tbl}, path: {path}"
    form = Form(db[tbl], id, deletable=False, formstyle=FormStyleDefault)
    mytab= sql2table( tbl,db , fld_skip=[] )
    return dict(message=SPAN( tbl, _style="color:red"  ), form=form, mytab=mytab,)


