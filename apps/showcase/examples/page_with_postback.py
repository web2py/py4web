from py4web import URL, action, request


@action("page_with_postback", method=["GET", "POST"])
def page_with_postback():
    return (
        "<html><body><pre>%s</pre>"
        + '<form method="POST" action="%s" enctype="multipart/form-data">'
        + '<input type="hidden" name="data" value="dummy"/>'
        + "<button>Click</button></form></body></html>"
    ) % (dict(request.forms), URL("page_with_postback"))
