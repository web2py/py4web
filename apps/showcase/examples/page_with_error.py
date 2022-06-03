from py4web import action


@action("page_with_error")
def page_with_error():
    1 / 0
