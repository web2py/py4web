from py4web import action, request

from .common import auth
from .models import db, parse_post_content


@action("index")
@action.uses("index.html", auth.user)
def index():
    return dict(message="hello world")

@action("api/tags", method="GET")
@action.uses(auth.user)
def get_api_tags():
    """retrieve known tags"""
    rows = db(db.tag_item).select(
        db.tag_item.name,
        orderby=db.tag_item.name,
        groupby=db.tag_item.name)
    return {"tags": [row.name for row in rows]}

@action("api/posts", method="GET")
@action.uses(auth.user)
def get_api_posts():
    """retrieve posts and users metadata"""
    if "tags" in request.query:
        tags = request.query.get("tags").split(",")
        query = (db.post_item.id==db.tag_item.post_item_id)&(db.tag_item.name.belongs(tags))
    else:
        query = db.post_item
    # get selected posts
    rows = db(query).select(
        db.post_item.ALL,
        groupby=db.post_item.id,
        orderby=~db.post_item.created_on,
        limitby=(0,100))
    # get usernames for authors of those posts
    users = {
        user.id: user.username for user in
        db(db.auth_user.id.belongs(row.created_by for row in rows)).select()}
    return {"posts": rows.as_list(), "users": users}

@action("api/posts", method="POST")
@action.uses(auth.user)
def post_api_posts():
    """submit a new post"""
    content = request.json.get("content")
    res = db.post_item.validate_and_insert(content=content)
    if res["id"]: parse_post_content(content, res["id"])
    return res

@action("api/posts/<post_item_id:int>", method="DELETE")
@action.uses(auth.user)
def delete_api_posts(post_item_id):
    """delete a a post"""
    return {"deleted": db(db.post_item.id==post_item_id).delete()}
