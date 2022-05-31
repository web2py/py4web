from py4web import action

from .vue_grid import mygrid


@action("vue_grid_bulma", method=["GET"])
@action.uses("vuegrid_bulma.html", mygrid)
def vue_grid_bulma():
    """This page generates a sample grid."""
    return dict(grid=mygrid())
