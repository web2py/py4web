from .common import *
from . import make_up_data


def get_requests(status=None, received=True):
    """returns a join between all friend_requests (sent or received)
    optionally filtered by status and auth_users"""
    to_user, from_user = (
        ("to_user", "from_user") if received else ("from_user", "to_user")
    )
    query = db.friend_request[to_user] == auth.user_id
    query &= db.friend_request[from_user] == db.auth_user.id
    if status:
        query &= db.friend_request.status == status
    return db(query).select(
        db.auth_user.ALL,
        db.friend_request.ALL,
        orderby=db.auth_user.first_name + db.auth_user.last_name,
    )

def check_liked(items):
    query = db.item_like.created_by==auth.user_id
    query &= db.item_like.item_id.belongs(items.as_dict().keys())
    liked_ids = [row.item_id for row in db(query).select()]
    for item in items:
        item['liked'] = item.id in liked_ids

# make a "like" button factory
@authenticated.callback()
def like(id):
    db.item_like.insert(item_id=id)


# the "/index" page
@authenticated()
def index():
    # make up some random data if only one user
    make_up_data.make()
    # my id
    me = auth.user_id
    # ids of all users following (including myself)
    ids = [r.auth_user.id for r in get_requests("accepted")] + [me]
    # a form to post a new item to the feed
    form = Form(db.feed_item)
    # list of receted posted items
    items = db(db.feed_item.created_by.belongs(ids)).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    check_liked(items)
    return dict(form=form, items=items, like=like)


# the "/home/{user_id}" page
@authenticated()
def home(id):
    # list of recent items posted by the user
    items = db(db.feed_item.created_by == id).select(
        orderby=~db.feed_item.created_on, limitby=(0, 100)
    )
    check_liked(items)
    return dict(items=items, like=like, user=db.auth_user[id])


# make a button factory to request friendship
@authenticated.callback()
def request_friendship(id):
    db.friend_request.insert(from_user=auth.user_id, to_user=id, status="pending")


# make a button factory to accept friendship
@authenticated.callback()
def accept_friendship(id):
    friend_request = db.friend_request[id]
    friend_request.update_record(status="accepted")
    # after accepting also create the reciprocal relation
    db.friend_request.insert(
        from_user=friend_request.to_user,
        to_user=friend_request.from_user,
        status="accepted",
    )


# make a button factory to reject frindship
@authenticated.callback()
def reject_friendship(id):
    db(db.friend_request.id == id).update(status="rejected")


# page "/friends" to search for new friends, see requests, accept/reject
@authenticated()
def friends():
    # list of requests received and sent
    requests_received = get_requests(received=True)
    requests_sent = get_requests(received=False)
    # a search form (simply by first name)
    form = Form([Field("name", requred=True)])
    users = []
    if form.accepted:
        query = db.auth_user.first_name.startswith(form.vars.get("name"))
        users = db(query).select()

    # return the form, lists, and button factories
    return dict(
        requests_received=requests_received,
        requests_sent=requests_sent,
        form=form,
        users=users,
        request_friendship=request_friendship,
        accept_friendship=accept_friendship,
        reject_friendship=reject_friendship,
    )
