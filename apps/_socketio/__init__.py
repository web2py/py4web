from py4web import action, request



# pls, run socketio server - look at utils/wsservers.py
# test example for python-socketio

@action("index")
@action.uses("index.html")
def index():
    return dict()

@action('echo/<path:path>', method=["GET", "POST"])
def echo(path=None):
    print (path)
    print ('GET from sio-server')


