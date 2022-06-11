from py4web import action, request

# pls, run socketio server - look into py4web/utils/wsservers.py.txt
# test example for python-socketio
#
# sio examples https://github.com/ali96343/lvsio 
# https://github.com/ali96343/capp


@action("socketio/index")
@action.uses("socketio/socketio_index.html")
def index():
    sio_url = "http://localhost:8000"
    return dict(sio_url=sio_url)


@action("socketio/echo/<path:path>", method=["GET", "POST"])
def echo(path=None):
    print(path)
    print("GET from sio-server")
