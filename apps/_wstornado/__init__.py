from py4web import action, request


@action("index")
@action.uses("index.html")
def index():
    return dict()

