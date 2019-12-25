from py4web import action


@action("index")
def index():
    return "Hello World"
