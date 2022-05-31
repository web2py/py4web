from py4web import action


@action("page_with_template")
@action.uses("page_with_template.html")
def page_with_template():
    return {"message": "Hello World"}
