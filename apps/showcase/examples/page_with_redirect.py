from py4web import URL, action, redirect


@action("page_with_redirect")
def page_with_redirect():
    redirect(URL("target"))


@action("target")
def target():
    return "target"
