import os

from yatl.helpers import A, I

from py4web import URL, action, redirect
from py4web.utils.form import FormStyleDefault
from py4web.utils.grid import Column, Grid, GridClassStyle

from .common import T, auth, db, session


@action("example_html_grid")
def example_html_grid():
    redirect(URL("example_html_grid/select"))


@action("example_html_grid/<path:path>", method=["POST", "GET"])
@action.uses("examples/html_grid.html", session, db, auth, T)
def example_html_grid(path=None):
    #  controllers and used for all grids in the app
    grid_param = dict(
        rows_per_page=5,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
    )

    search_queries = [
        ["By Name", lambda value: db.thing.name.contains(value)],
        ["By Color", lambda value: db.thing.color == value],
        [
            "By Name or Color",
            lambda value: db.thing.name.contains(value) | (db.thing.color == value),
        ],
    ]

    query = db.thing.id > 0
    orderby = [db.thing.name]
    columns = [field for field in db.thing if field.readable]
    columns.insert(0, Column("Custom", lambda row: A("click me")))
    grid = Grid(
        path,
        query,
        columns=columns,
        search_queries=search_queries,
        orderby=orderby,
        show_id=False,
        T=T,
        **grid_param
    )

    grid.columns[3].represent = lambda row: I(
        _class="fa fa-circle", _style="color:" + row.color
    )

    return dict(grid=grid)
