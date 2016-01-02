import Cookie
from gluon.streamer import stream_file_or_304_or_206
from gluon.template import render
from gluon.memoize_property import memoize_property

class Response(object):
    def __init__(self):
        self.status = 200
        self.headers = {}
        self.view = {}
        self.flash = None
        self.render = render
        self.auto_commit = True
        self.static_version = None
    @memoize_property
    def cookies(self):
        return Cookie.SimpleCookie()
    def stream(self, filename):
        stream_file_or_304_or_206(filename, environ=current.request.environ)
