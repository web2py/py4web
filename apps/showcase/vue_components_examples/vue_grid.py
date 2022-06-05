from py4web import action

from .common import session
from .components.grid import Grid

mygrid = Grid("grid_api", session)


@action("vue_grid", method=["GET"])
@action.uses("vue/vuegrid_bulma.html", mygrid)
def vue_grid():
    """This page generates a sample grid."""
    return dict(grid=mygrid())
