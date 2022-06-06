from py4web import action
from py4web.utils.publisher import ALLOW_ALL_POLICY, Publisher

from .common import db

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)


@action("example_ajax_grid")
@action.uses("examples/ajax_grid.html")
def example_ajax_grid():
    return dict(grid=publisher.grid(db.person))
