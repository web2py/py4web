from py4web import action, request


@action("index")
@action.uses("index.html")
def index():
    return dict()

@action('websocket')
def echo():
    ws  = request.environ.get("wsgi.websocket")
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: break


