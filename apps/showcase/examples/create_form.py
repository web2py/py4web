import os

from py4web import action
from py4web.utils.form import Form, FormStyleDefault

from .common import T, session
from .models import db


# exposed as /examples/create_form or /examples/update_form/<id>
@action("create_form", method=["GET", "POST"])
@action.uses("examples/form.html", db, session, T)
def create_form():
    form = Form(db.person, formstyle=FormStyleDefault)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)
