from py4web import URL, action, redirect, request


@action("page_with_query")
def page_with_query():
    if not request.query:
        redirect(URL("page_with_query", vars=dict(x=1, y=2)))
    return repr(dict(request.query))
