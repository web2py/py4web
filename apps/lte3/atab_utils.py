from yatl.helpers import A, I, SPAN, XML, DIV, P, TABLE, THEAD, TR, TD, TBODY, H6, IMG
from py4web import action, request, response, abort, redirect, URL, Field
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.core import Template
from py4web import URL
import pydal


def sql2table(
    tbl,
    db,
    tbl_query = None,
    order_by = None,
    items_on_page=13,
    caller="index",
    csv=False,
    pagi=False,
    links=[],
    hlinks=[],
    fld_links={},
    fld_skip=[0,],
    fld_length = None,
    page_d={},
    show_thead= True,
):
    def stop_button():
         return A( '!', _title='stop',  _role = 'button', _style="background-color:lightgray;color:black;" )


    if not tbl in db.tables:
        return f"unknown tbl: {tbl}"

    if tbl_query is None:
       tbl_query = db[tbl].id > 0

    if tbl_query  and not isinstance( tbl_query, pydal.objects.Query  ):
        return f"bad tbl_query! tbl: {tbl}"

    if order_by is None:
       order_by = ~db[tbl].id

    try:
        pg = int(page_d.get("page", 1))
    except ValueError:
        pg = 1


    table_items = len(db( tbl_query ).select())
    if items_on_page > table_items:
        items_on_page = table_items

    if table_items == 0:
        show_thead = False

    max_pages, rem = divmod( table_items, items_on_page  ) if table_items else (0,0)
    if rem: 
        max_pages += 1

    limitby= ( (pg - 1) * items_on_page, pg * items_on_page ) 
    if not pagi:
       items_on_page = table_items
       limitby = ( 0, table_items )

    rows = db( tbl_query  ).select(orderby= order_by, limitby= limitby   )

    ij_start = -len(links)
    ff = [f for f in db[tbl].fields]
    hh = [db[tbl][f].label for f in ff]


    if fld_length is None : 
            fld_length = 80 // (len(ff) -1 ) if len(ff) > 1 else 80


    def h_func(x, jj):
        if jj < 0:
            if len(hlinks) >= -jj:
                return hlinks[len(hlinks) + jj]
            return "act"
        if jj in fld_skip:
            return ''

        if not x is None and isinstance(x, str) and len(x) > fld_length :
             x=x[:fld_length] + '...'

        return f"{x}"

    def r_func(x, ii, r, t, f_nm):
        if ii < 0:
            if len(links) >= -ii:
                return links[len(links) + ii](t, r.id)
            return "act"
        if ii in fld_skip:
            return ''
        if ii in fld_links:
            return fld_links[ii](t, x, r.id)
        if f_nm in fld_links:
            return fld_links[f_nm](t, x, r.id)

        if not x is None and isinstance(x, str) and len(x) > fld_length :
             x=x[:fld_length] + '...'
            
        return f"{x}"

    return DIV(
        SPAN(f"{tbl}", _style="color:red"),
        SPAN(f"; {items_on_page}/{table_items},"), SPAN(f" {pg}/{max_pages}", _style="color:red"),
        DIV(
            SPAN(
                A(
                    "prev",
                    _role="button",
                    _href=URL(caller, vars=dict(page=pg - 1 if pg > 1 else pg),  ),
                ) if pg > 1 else stop_button() ,
                A(
                    "next",
                    _role="button",
                    _href=URL(caller, vars=dict(page=pg + 1 if pg < max_pages else pg), ),
                ) if pg < max_pages else stop_button(),

            )
            if pagi
            else "",

            SPAN(
                A(
                    "csv",
                    _role="button",
                    _title="table to csv file",
                    _href=URL("some_func", vars=dict(t_=tbl, c="a"),),
                ),
                A(
                    "xls",
                    _role="button",
                    _title="table to xls file",
                    _href=URL("some_func", vars=dict(t_=tbl, c="b"), ),
                ),
            )
            if csv
            else "",

        ) # </div>
        if csv
        else "",
        DIV(
            A(
                "prev",
                _role="button",
                _href=URL(caller, vars=dict(page=pg - 1 if pg > 1 else pg)),
            ) if pg > 1 else stop_button() ,
            A(
                "next",
                _role="button",
                _href=URL(caller, vars=dict(page=pg + 1 if pg < max_pages else pg)),
            ) if pg < max_pages else stop_button(),
        )
        if pagi
        else "",
        TABLE(
            THEAD(TR(*[TD(H6(h_func(hh[j], j))) for j in range(ij_start, len(hh))])) if show_thead else "",
            TBODY( *[ TR( *[ TD(r_func(row[ff[i]], i, row, tbl, ff[i])) for i in range(ij_start, len(ff)) ])
                    for row in rows ]
            ),
        ),
    )

@action("mytab_grid", method=["GET", "POST"])
@action.uses(Template("mytab_grid.html", delimiters="[[ ]]"), db, session, T)
def mytab_grid():
    def xfunc(tt, rr_id):
        return f"{tt}:id={rr_id}"

    hlinks = ["+img", "+r_id", "+xfunc"]
    links = [
        lambda tx, r_id: A(
            IMG(_width="30px", _height="30px", _src=URL("static/favicon.ico")),
            _title="run some_func",
            _href=URL(f"some_func", vars=dict(t_=tx, id_=r_id)),
        ),
        lambda tx, r_id: A(
            f"myf2-id:[{r_id}]",
            _title="run some3_func",
            _href=URL(f"some3_func", vars=dict(t_=tx, id_=r_id)),
        ),
        lambda tx, r_id: A(
            xfunc(tx, r_id),
            _title="run some3_func",
            _href=URL(f"some3_func", vars=dict(t_=tx, id_=r_id)),
        ),
    ]

    def yfunc(xx, rr_id):
        xx = xx[:10]
        if rr_id % 2 == 0:
            return SPAN(xx, _style="color:red")
        else:
            return SPAN(xx, _style="color:green")

    def zfunc(xx, rr_id):
        xx = xx[:10]
        if rr_id % 2 == 0:
            return SPAN(xx, _style="color:blue")
        else:
            return SPAN(xx, _style="color:brown")

    def title_func( xx, rr_id  ):
        return xx

    fld_links = {
        # by field num
        1: lambda tx, xx, r_id: A(
            yfunc(xx, r_id),
            _title= title_func( xx, r_id ), 
            _href=URL(f"some4_func", vars=dict(t_=tx, x_=xx, id_=r_id)),
        ),
        # by field name 
        'f2': lambda tx, xx, r_id: A(
            zfunc(xx, r_id),
            _title= title_func( xx, r_id ), 
            _href=URL(f"some4_func", vars=dict(t_=tx, x_=xx, id_=r_id)),
        ),
    }

    mytab = sql2table(
        "test_table",
        db,
        page_d=dict(request.query),
        caller="mytab_grid",
        links=links,
        hlinks=hlinks,
        fld_links=fld_links,
        csv = False,
        pagi = True,
    )

    return dict(message="test_table", mytab=mytab)


@action("some_func", method=["GET", "POST"])
def some_func():
    args = repr(dict(request.query))
    return f"some_func: {args}"


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


