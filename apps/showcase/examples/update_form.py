import os

from py4web import action
from py4web.utils.form import Form, FormStyleDefault

from .common import T, db, session


# exposed as /examples/create_form or /examples/update_form/<id>
@action("update_form/<id>", method=["GET", "POST"])
@action.uses("examples/form.html", db, session, T)
def update_form(id):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleDefault)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)
