from py4web import URL, action, redirect

from .common import session


@action("session_clear")
@action.uses(session)
def session_clear():
    session.clear()
    redirect(URL("session_counter"))
