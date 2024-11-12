import os

from py4web import Cache, action

cache = Cache(size=1000)

@action("index")
@cache.memoize(expiration=1)
def index():
    filename = os.path.join(os.path.dirname(__file__), "static", "index.html")
    with open(filename) as stream:
        return stream.read()
