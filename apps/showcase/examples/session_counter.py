from py4web import action

from .common import session


@action("session_counter")
@action.uses("examples/session_counter.html", session)
def session_counter():
    session["counter"] = session.get("counter", 0) + 1
    return {"counter": session.get("counter")}
