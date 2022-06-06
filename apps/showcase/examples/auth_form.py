from py4web import action

from .common import T, auth, db, session


@action("auth_form/<name>", method=["GET", "POST"])
@action.uses("examples/auth_form.html", db, session, T, auth)
def auth_form(name):
    form = auth.form(name)
    if form.submitted:
        pass
    elif form.accepted:
        pass
    elif form.errors:
        pass
    return dict(form=auth.form(name))
