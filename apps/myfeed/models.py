from .common import *
from pydal.validators import IS_NOT_EMPTY

db.define_table(
    "feed_item", Field("body", "text", requires=IS_NOT_EMPTY()), auth.signature
)

db.define_table("item_like", Field("item_id", "reference feed_item"), auth.signature)

db.define_table(
    "friend_request",
    Field("from_user", "reference auth_user"),
    Field("to_user", "reference auth_user"),
    Field("status", options=("accepted", "rejected", "pending")),
)

db.commit()
