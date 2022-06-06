from py4web import action
from py4web.utils.form import Form, FormStyleDefault

from .common import T, db, session


@action("custom_form", method=["GET", "POST"])
@action.uses("examples/custom_form.html", db, session, T)
def custom_form(id=None):
    form = Form(db.person, id, deletable=False, formstyle=FormStyleDefault)
    rows = db(db.person).select()
    return dict(form=form, rows=rows)
