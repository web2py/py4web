from py4web import action


@action("page_without_template")
def page_without_template():
    return "ok"
