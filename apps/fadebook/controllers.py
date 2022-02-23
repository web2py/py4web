from py4web import action, redirect, URL, Field, HTTP
from py4web.utils.form import Form
from .common import flash, session, db, auth
from .make_up_data import make

#
# Convenience functions
#

authenticated_api = action.uses(session, db, auth.user)


def check_liked(items):
    """add a liked attributed to each item"""
    query = db.item_like.created_by == auth.user_id
    query &= db.item_like.item_id.belongs(items.as_dict().keys())
    liked_ids = [row.item_id for row in db(query).select(db.item_like.item_id)]
    for item in items:
        item["liked"] = "true" if item.id in liked_ids else "false"


def friend_ids(user_id):
    """return a list of ids of friends (included user_id self)"""
    query = db.friend_request.status == "accepted"
    query &= (db.friend_request.to_user == user_id) | (
        db.friend_request.from_user == user_id
    )
    rows = db(query).select()
    return (
        set([user_id]) 
        |set(row.from_user for row in rows)
        | set(row.to_user for row in rows)
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
    # make up some random data if only one user
    make()
    # a form to post a new item to the feed
    form = Form(db.feed_item)
    # list of 100 most recent posted items by user or friends
    items = db(db.feed_item.created_by.belongs(friend_ids(auth.user_id))).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    # determine if they were liked or not
    check_liked(items)
    return locals()


@action("home/<user_id:int>", method=["GET", "POST"])
@action.uses("home.html", auth.user)
def home(user_id):
    if user_id not in friend_ids(auth.user_id):
        raise HTTP(400)
    user = db.auth_user(user_id)
    # list of recent items posted by the user
    items = db(db.feed_item.created_by == user_id).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    # determine if they were liked or not
    check_liked(items)
    return locals()


@action("friends", method=["GET", "POST"])
@action.uses("friends.html", auth.user)
def friends():
    # a search form (simply by first name)
    form = Form([Field("name", required=True)])
    users = []
    if form.accepted:
        # select users based on the tokens in the search input
        query = None
        for token in form.vars.get("name").split():
            q = db.auth_user.first_name.lower().startswith(
                token.lower()
            ) | db.auth_user.last_name.lower().startswith(token.lower())
            query = query & q if query else q
        if query:
            users = db(query).select()

    # make list of requests
    alphabetical = db.auth_user.first_name + db.auth_user.last_name
    query_received = (db.friend_request.to_user == auth.user_id) & (
        db.friend_request.from_user == db.auth_user.id
    )
    requests_received = db(query_received).select(orderby=alphabetical)
    # make list of requests sent
    query_sent = (db.friend_request.from_user == auth.user_id) & (
        db.friend_request.to_user == db.auth_user.id
    )
    requests_sent = db(query_sent).select(orderby=alphabetical)

    # return the form, lists, and button factories
    return locals()


#
# Callback actions
#


@action("like/<item_id:int>", method=["POST"])
@authenticated_api
def like(item_id):
    # try unlike
    if db(db.item_like.item_id == item_id).delete():
        return dict(liked="false")
    # else like
    db.item_like.insert(item_id=item_id)
    return dict(liked="true")


@action("friendship/request/<user_id:int>", method=["POST"])
@authenticated_api
def friendship_request(user_id):
    # if request does not exist already, create it
    query = (db.friend_request.to_user == user_id) & (
        db.friend_request.from_user == auth.user_id
    )
    query |= (db.friend_request.to_user == auth.user_id) & (
        db.friend_request.from_user == user_id
    )
    if not db(query).count():
        db.friend_request.insert(
            from_user=auth.user_id, to_user=user_id, status="pending"
        )

@action("friendship/<id:int>/accept", method=["POST"])
@authenticated_api
def friendship_accept(id):
    # the target user can accept the request
    db(
        (db.friend_request.id == id) & (db.friend_request.to_user == auth.user_id)
    ).update(status="accepted")


# make a button factory to reject frindship
@action("friendship/<id:int>/reject", method=["POST"])
@authenticated_api
def friendship_reject(id):
    # both origin and target users can delete a request
    db(db.friend_request.id == id).delete()
