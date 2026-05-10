from py4web import HTTP, URL, Field, action, redirect
from py4web.utils.form import Form
from py4web.utils.url_signer import URLSigner

from .common import auth, db, flash, session
from .make_up_data import make

# All POST/DELETE callbacks below must be invoked through a URL we
# generated server-side; ``URLSigner`` adds an HMAC over the path that
# is verified before the handler runs.  This blocks third-party sites
# from forging requests against a logged-in user's session.
url_signer = URLSigner(session)


#
# Convenience functions
#


def check_liked(items):
    """Annotate each item with a ``liked`` flag for the current user."""
    if not items:
        return
    query = db.item_like.created_by == auth.user_id
    query &= db.item_like.item_id.belongs([item.id for item in items])
    liked_ids = set(row.item_id for row in db(query).select(db.item_like.item_id))
    for item in items:
        item["liked"] = "true" if item.id in liked_ids else "false"


def friend_ids(user_id):
    """Return a set of ids of friends of ``user_id`` (including ``user_id``)."""
    query = db.friend_request.status == "accepted"
    query &= (db.friend_request.to_user == user_id) | (
        db.friend_request.from_user == user_id
    )
    rows = db(query).select()
    return (
        {user_id}
        | {row.from_user for row in rows}
        | {row.to_user for row in rows}
    )


#
# Pages
#


@action("index")
@action.uses("index.html", auth)
def index():
    if auth.user_id:
        redirect(URL("feed"))
    return {}


@action("feed", method=["GET", "POST"])
@action.uses("feed.html", auth.user)
def feed():
    # Make up some random data on first run if there's only one user.
    # Demo seeding only — remove for a real deployment.
    make()
    # A form to post a new item to the feed.
    form = Form(db.feed_item)
    # Most recent posts by the user or their friends.
    items = db(db.feed_item.created_by.belongs(friend_ids(auth.user_id))).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    check_liked(items)
    return dict(form=form, items=items, url_signer=url_signer)


@action("home/<user_id:int>", method=["GET", "POST"])
@action.uses("home.html", auth.user)
def home(user_id):
    if user_id not in friend_ids(auth.user_id):
        raise HTTP(400)
    user = db.auth_user(user_id)
    items = db(db.feed_item.created_by == user_id).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    check_liked(items)
    return dict(user=user, items=items, url_signer=url_signer)


@action("friends", method=["GET", "POST"])
@action.uses("friends.html", auth.user)
def friends():
    # A search form (matched by first name).
    form = Form([Field("name", required=True)])
    users = []
    if form.accepted and form.vars.get("name"):
        # Build an OR query across the submitted tokens.
        query = None
        for token in form.vars.get("name").split():
            q = db.auth_user.first_name.lower().startswith(
                token.lower()
            ) | db.auth_user.last_name.lower().startswith(token.lower())
            query = query & q if query else q
        if query is not None:
            users = db(query).select()

    alphabetical = db.auth_user.first_name + db.auth_user.last_name
    query_received = (db.friend_request.to_user == auth.user_id) & (
        db.friend_request.from_user == db.auth_user.id
    )
    requests_received = db(query_received).select(orderby=alphabetical)
    query_sent = (db.friend_request.from_user == auth.user_id) & (
        db.friend_request.to_user == db.auth_user.id
    )
    requests_sent = db(query_sent).select(orderby=alphabetical)

    return dict(
        form=form,
        users=users,
        requests_received=requests_received,
        requests_sent=requests_sent,
        url_signer=url_signer,
    )


#
# Callback actions (state-changing; require URL signer)
#


@action("like/<item_id:int>", method=["POST"])
@action.uses(auth.user, url_signer.verify())
def like(item_id):
    """Toggle the current user's like on ``item_id``."""
    deleted = db(
        (db.item_like.item_id == item_id)
        & (db.item_like.created_by == auth.user_id)
    ).delete()
    if deleted:
        return dict(liked=False)
    db.item_like.insert(item_id=item_id)
    return dict(liked=True)


@action("friendship/request/<user_id:int>", method=["POST"])
@action.uses(auth.user, url_signer.verify())
def friendship_request(user_id):
    if user_id == auth.user_id:
        raise HTTP(400)
    # Only insert when no request exists in either direction.
    existing = (db.friend_request.to_user == user_id) & (
        db.friend_request.from_user == auth.user_id
    )
    existing |= (db.friend_request.to_user == auth.user_id) & (
        db.friend_request.from_user == user_id
    )
    if not db(existing).count():
        db.friend_request.insert(
            from_user=auth.user_id, to_user=user_id, status="pending"
        )
    return dict(ok=True)


@action("friendship/<id:int>/accept", method=["POST"])
@action.uses(auth.user, url_signer.verify())
def friendship_accept(id):
    """Only the recipient can accept a pending request."""
    db(
        (db.friend_request.id == id) & (db.friend_request.to_user == auth.user_id)
    ).update(status="accepted")
    return dict(ok=True)


@action("friendship/<id:int>/reject", method=["POST"])
@action.uses(auth.user, url_signer.verify())
def friendship_reject(id):
    """Either party can delete a request they're involved in."""
    db(
        (db.friend_request.id == id)
        & (
            (db.friend_request.from_user == auth.user_id)
            | (db.friend_request.to_user == auth.user_id)
        )
    ).delete()
    return dict(ok=True)
