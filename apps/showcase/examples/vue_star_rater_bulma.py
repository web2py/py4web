from py4web import action

from ..examples.vue_star_rater import star_rater


@action("vue_star_rater_bulma", method=["GET"])
@action.uses("star_rater_vue_bulma.html", star_rater)
def vue_star_rater_bulma():
    return dict(get_posts_url=URL("star_rater_get_posts"))
