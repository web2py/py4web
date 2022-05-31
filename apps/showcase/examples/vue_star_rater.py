from py4web import action

from ..common import session
from ..components.starrater import StarRater

star_rater = StarRater("star_rater", session)


@action("star_rater", method=["GET"])
@action.uses("starrating.html", star_rater)
def starrater():
    # This performs a star rating of item 1.
    return dict(stars=star_rater(id=1))


@action("vue_star_rater", method=["GET"])
@action.uses("star_rater_vue.html", star_rater)
def vue_star_rater():
    return dict(get_posts_url=URL("star_rater_get_posts"))


@action("star_rater_get_posts", method=["GET"])
def star_rater_get_posts():
    posts = [
        {"id": 1, "content": "Hello there"},
        {"id": 2, "content": "I love you"},
        {"id": 3, "content": "Do you love me too?"},
    ]
    for p in posts:
        # Creates the callback URL for each rater.
        p["url"] = star_rater.url(p["id"])
    return dict(posts=posts)
