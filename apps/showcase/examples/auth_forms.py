from py4web import action

from .common import T, auth, db, session


@action("auth_forms", method=["GET", "POST"])
@action.uses("examples/auth_forms.html", db, session, T, auth)
def auth_forms():
    disabled = False
    # this is experimntal, we must disable forms that require a logged in user
    if not auth.is_logged_in:
        disabled = "disabled"
    return dict(
        register_form=auth.form("register"),
        login_form=auth.form("login"),
        reset_password_form=auth.form("reset_password"),
        change_password_form=disabled or auth.form("change_password"),
        profile_form=disabled or auth.form("profile"),
    )
