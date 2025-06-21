from yatl.helpers import A, I

from py4web import URL, action, redirect
from py4web.utils.form import FormStyleDefault
from py4web.utils.grid import Column, Grid, GridClassStyle, IconStyleFontawsome

from .common import T, auth, db, session


@action("example_html_grid")
def example_html_grid():
    redirect(URL("example_html_grid2"))


@action("example_html_grid2", method=["POST", "GET"])
@action.uses("examples/html_grid.html", session, db, auth, T)
def example_html_grid2():
    #  controllers and used for all grids in the app
    grid_param = dict(
        rows_per_page=5,
        include_action_button_text=True,
        search_button_text="Filter",
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
        icon_style=IconStyleFontawsome,
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
    grid = Grid(
        query,
        columns=[
            Column("Custom",
                   represent=lambda row: A("click me")
                   ),
            db.thing.name,
            Column("Color", 
                   required_fields=[db.thing.color], 
                   represent=lambda row: I(_class="fa fa-circle", _style="color:" + row.color )
                   ),
            db.thing.is_ready,
            db.thing.time_created,
            db.thing.date_created,
            db.thing.timetime_created,
        ],
        search_queries=search_queries,
        orderby=orderby,
        show_id=False,
        T=T,
        **grid_param,
    )


    return dict(grid=grid)
