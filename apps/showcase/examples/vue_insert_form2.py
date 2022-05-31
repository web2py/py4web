from py4web import action

from ..common import db, session
from ..components.vueform import InsertForm

signed_url = URLSigner(session, lifespan=3600)


def not_too_expensive(fields):
    """Validation function that checks that the total price is low enough."""
    if (
        fields["product_quantity"]["validated_value"]
        * fields["product_cost"]["validated_value"]
    ) > 1000000:
        err = "Please insert only products with total value of less than a million."
        fields["product_quantity"]["error"] = err
        fields["product_cost"]["error"] = err


myform = InsertForm(
    "insert_product",
    session,
    db.product,
    validate=not_too_expensive,
    redirect_url="index",
)


@action("vue_insert_form", method=["GET"])
@action.uses("vueform_bulma.html", myform)
def vue_insert_form():
    return dict(form=myform())
