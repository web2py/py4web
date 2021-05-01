from py4web import action, request


# pls, run websockets server - look at utils/wsservers.py
# test example for websockets

@action("index")
@action.uses("index.html")
def index():
    return dict()

