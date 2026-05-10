from pydal.validators import IS_IN_SET, IS_NOT_EMPTY

from .common import *

FRIEND_STATUSES = ("accepted", "pending", "rejected")

db.define_table(
    "feed_item",
    Field("body", "text", requires=IS_NOT_EMPTY()),
    auth.signature,
)

db.define_table(
    "item_like",
    Field("item_id", "reference feed_item"),
    auth.signature,
)

db.define_table(
    "friend_request",
    Field("from_user", "reference auth_user"),
    Field("to_user", "reference auth_user"),
    # ``options=`` is not a valid Field kwarg; use IS_IN_SET so writes
    # are actually validated.
    Field("status", requires=IS_IN_SET(FRIEND_STATUSES), default="pending"),
    auth.signature,
)

db.commit()
