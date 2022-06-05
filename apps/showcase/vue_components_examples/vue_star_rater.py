from py4web import URL, action, request

from .common import session
from .components.starrater import StarRater


class MyStarRater(StarRater):
    def get_stars(self, id=None):
        """Gets the number of stars for a given id."""
        # This is a test implementation; it should be over-ridden.
        # 0 means no stars set.
        return dict(num_stars=int(id) % 6)

    def set_stars(self, id=None):
        """Sets the number of stars."""
        print("Number of stars of item", id, "set to:", int(request.json["num_stars"]))
        return "ok"


star_rater = MyStarRater("star_rater", session)


@action("star_rater_get_posts", method=["GET"])
@action.uses(star_rater)
def star_rater_get_posts():
    posts = [
        {"id": 1, "content": "Hello there"},
        {"id": 2, "content": "I love you"},
        {"id": 3, "content": "Do you love me too?"},
    ]
    for p in posts:
        # Creates the callback URL for each rater.
        p["stars_callback_url"] = star_rater.url(p["id"])
    return dict(posts=posts)


@action("vue_star_rater", method=["GET"])
@action.uses("vue/star_rater_vue_bulma.html", star_rater)
def vue_star_rater():
    return dict(get_posts_url=URL("star_rater_get_posts"))
