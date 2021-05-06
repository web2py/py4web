import logging
from bottle import ServerAdapter

try:
    from .utils.wsservers import *
except ImportError:
    wsservers_list = []


__all__ = [
    "geventWebSocketServer",
    "wsgirefThreadingServer",
    "rocketServer",
] + wsservers_list


def geventWebSocketServer():
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.logging import create_logger

    class GeventWebSocketServer(ServerAdapter):
        def run(self, handler):
            server = pywsgi.WSGIServer(
                (self.host, self.port),
                handler,
                handler_class=WebSocketHandler,
                **self.options
            )

            if not self.quiet:
                server.logger = create_logger("geventwebsocket.logging")
                server.logger.setLevel(logging.INFO)
                server.logger.addHandler(logging.StreamHandler())

            server.serve_forever()

    return GeventWebSocketServer


def wsgirefThreadingServer():
    # https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
    from wsgiref.simple_server import make_server
    from socketserver import ThreadingMixIn
    import socket
    from concurrent.futures import ThreadPoolExecutor  # pip install futures

    class WSGIRefThreadingServer(ServerAdapter):
        def run(self, app):
            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(
                        self.process_request_thread, request, client_address
                    )

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(max_workers=40)

            class Server:
                def __init__(
                    self, server_address=("127.0.0.1", 8000), handler_cls=None
                ):
                    self.wsgi_app = None
                    self.listen, self.port = server_address
                    self.handler_cls = handler_cls

                def set_app(self, app):
                    self.wsgi_app = app

                def get_app(self):
                    return self.wsgi_app

                def serve_forever(self):
                    self.server = make_server(
                        self.listen,
                        self.port,
                        self.wsgi_app,
                        ThreadingWSGIServer,
                        self.handler_cls,
                    )
                    self.server.serve_forever()

            class FixedHandler(WSGIRequestHandler):
                def address_string(self):  # Prevent reverse DNS lookups please.
                    return self.client_address[0]

                def log_request(*args, **kw):
                    if not self.quiet:
                        return WSGIRequestHandler.log_request(*args, **kw)

            handler_cls = self.options.get("handler_class", FixedHandler)
            server_cls = Server

            if ":" in self.host:  # Fix wsgiref for IPv6 addresses.
                if getattr(server_cls, "address_family") == socket.AF_INET:

                    class server_cls(server_cls):
                        address_family = socket.AF_INET6

            srv = make_server(self.host, self.port, app, server_cls, handler_cls)
            srv.serve_forever()

    return WSGIRefThreadingServer


def rocketServer():
    try:
        from rocket3 import Rocket3 as Rocket
    except ImportError:
        from .rocket3 import Rocket3 as Rocket
    import logging.handlers

    class RocketServer(ServerAdapter):
        def run(self, app):
            if not self.quiet:
                log = logging.getLogger("Rocket")
                log.setLevel(logging.INFO)
                log.addHandler(logging.StreamHandler())
            server = Rocket((self.host, self.port), "wsgi", dict(wsgi_app=app))
            server.start()

    return RocketServer
