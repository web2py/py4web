from py4web import URL, action, redirect


@action("index")
def index():
    redirect(URL("static/index.html"))
