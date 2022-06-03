from py4web import URL, action, redirect


@action("page_with_parameters")
def page_with_parameters():
    return redirect(URL("page_with_parameters/a/b/c"))


@action("page_with_parameters/<x>/<y>/<z>")
def page_with_parameters(x, y, z):
    return repr({"x": x, "y": y, "z": z})
