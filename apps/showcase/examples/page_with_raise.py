from py4web import HTTP, action


@action("page_with_raise")
def page_with_raise():
    raise HTTP(400, "oops")
