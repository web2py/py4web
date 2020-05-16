import random
from .common import db, action
from py4web.utils.populate import populate


def make():
    if db(db.auth_user).count() == 1:
        populate(db.auth_user, 10, contents={"is_active": True})
        populate(db.feed_item, 100, contents={"is_active": True, "parent_id": 0})
        # populate(db.item_like, 1000, contents={"is_active": True})
        ids = [r.id for r in db(db.auth_user).select() if r.id > 1]
        for k in ids[:3]:
            db.friend_request.insert(to_user=1, from_user=k, status="accepted")
            db.friend_request.insert(to_user=k, from_user=1, status="accepted")
        for k in ids[3:6]:
            db.friend_request.insert(to_user=1, from_user=k, status="pending")
        for k in ids[6:9]:
            db.friend_request.insert(to_user=1, from_user=k, status="rejected")
