from yatl.helpers import A, I, SPAN, XML, DIV, P, TABLE, THEAD, TR, TD, TBODY, H6, IMG
from py4web import action, request, response, abort, redirect, URL, Field
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.core import Template
from py4web import URL
import pydal

from .atab_utils import sql2table

@action("ima_grid", method=["GET", "POST"])
@action.uses(Template("ima_grid.html", delimiters="[[ ]]"), db, session, T)
def ima_grid():

    hlinks = ["save", "replace"]

    links = [
        lambda tx, r_id: A(
            f"save:[{r_id}]",
            _title='save file to disk',
            _href=URL(f"some_func", vars=dict(t_=tx, id_=r_id)),
        ),

        lambda tx, r_id: A(
            f"replace:[{r_id}]",
            _title='replace file in app',
            _href=URL(f"some2_func", vars=dict(t_=tx, id_=r_id)),
        ),

    ]

    mytab = sql2table(
        "app_images",
        db,
        page_d=dict(request.query),
        links=links,
        hlinks=hlinks,
        caller="ima_grid",
        csv = False,
        pagi = True,
    )

    return dict(message="test sql2table", mytab=mytab)


@action("some_func", method=["GET", "POST"])
def some_func():
    from .upload_utils import file2browser 
    from .settings import APP_NAME
    from .settings import UPLOAD_FOLDER 
    import os

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

    fnm = r.f0
    fpath = os.path.join( UPLOAD_FOLDER.replace('uploads', 'static/tte')  , fnm )
    orig_fnm = fnm.split('/')[-1]

    return file2browser (  fpath , orig_fnm )

@action("some2_func", method=["GET", "POST"])
def some_func():
    args = repr(dict(request.query))
    return f"some2_func: {args}"


@action("some3_func", method=["GET", "POST"])
def some_func():
    args = repr(dict(request.query))
    return f"some3_func: {args}"


@action("some4_func", method=["GET", "POST"])
def some_func():
    args = repr(dict(request.query))
    return f"some4_func: {args}"


