from py4web import action

from ..common import db, session
from ..components.vueform import TableForm
from .vue_insert_form import not_too_expensive

update_form = TableForm(
    "update_product",
    session,
    db.product,
    validate=not_too_expensive,
    redirect_url="index",
)


@action("vue_update_form", method=["GET"])
@action.uses("vueform.html", update_form)
def vue_update_form():
    # For simplicity, we update the record 1.
    return dict(form=update_form(id=1))
