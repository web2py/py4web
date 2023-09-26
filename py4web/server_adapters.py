import logging
import os
import ssl

from ombott.server_adapters import ServerAdapter

try:
    from .utils.wsservers import *
except ImportError:
    wsservers_list = []

__all__ = [
    "gevent",
    "geventWebSocketServer",
    "wsgirefThreadingServer",
    "rocketServer",
] + wsservers_list


def check_level(level):

    # lib/python3.7/logging/__init__.py
    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0

    return (
        level
        if level
        in (
            logging.CRITICAL,
            logging.ERROR,
            logging.WARN,
            logging.INFO,
            logging.DEBUG,
            logging.NOTSET,
        )
        else logging.WARN
    )


def logging_conf(level, log_file="server-py4web.log"):

    # export PY4WEB_LOGS=/tmp # set log_file directory

    log_dir = os.environ.get("PY4WEB_LOGS", None)

    log_param = {
            "format":"%(threadName)s | %(message)s",
            "level":check_level(level),
        }

    if log_dir:
        h = logging.FileHandler( 
                  os.path.join( log_dir, log_file), 
                  mode = "w",
                  encoding = "utf-8"
                  )
        log_param.update( {"handlers": [h]} )

    logging.basicConfig(**log_param)


def get_workers(opts, default=10):
    try:
        return opts["workers"] if opts["workers"] else default
    except KeyError:
        return default


def gevent():
    # gevent version 22.10.2

    import threading

    from gevent import local, pywsgi  # pip install gevent

    if not isinstance(threading.local(), local.local):
        msg = "Ombott requires gevent.monkey.patch_all() (before import)"
        raise RuntimeError(msg)

    # ./py4web.py run apps --watch=off -s gevent -L 20
    #
    # ./py4web.py run apps -s gevent --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem -L 0
    # ./py4web.py run apps -s gevent --watch=off --host=192.168.1.161 --port=8443 --ssl_cert=server.pem -L 0

    class GeventServer(ServerAdapter):
        def run(self, handler):

            logger = "default"  # not None - from gevent doc
            if not self.quiet:

                logger = logging.getLogger("gevent")
                log_dir = os.environ.get("PY4WEB_LOGS", None)
                fh = (
                    logging.FileHandler(None)
                    if not log_dir
                    else (
                        logging.FileHandler(os.path.join(log_dir, "server-py4web.log"))
                    )
                )
                logger.setLevel(check_level(self.options["logging_level"]))
                logger.addHandler(fh)
                logger.addHandler(logging.StreamHandler())

            certfile = self.options.get("certfile", None)

            ssl_args = (
                dict(
                    certfile=certfile,
                    keyfile=self.options.get("keyfile", None),
                    ssl_version=ssl.PROTOCOL_SSLv23,
                    server_side=True,
                    do_handshake_on_connect=False,
                )
                if certfile
                else dict()
            )

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                handler,
                log=logger,
                error_log=logger,
                **ssl_args
            )

            server.serve_forever()

    return GeventServer


def geventWebSocketServer():
    from gevent import pywsgi

    # from geventwebsocket.handler import WebSocketHandler # pip install gevent-websocket
    from gevent_ws import WebSocketHandler  # pip install gevent gevent-ws

    # https://stackoverflow.com/questions/5312311/secure-websockets-with-self-signed-certificate
    # https://pypi.org/project/gevent-ws/
    # ./py4web.py run apps -s geventWebSocketServer --watch=off --ssl_cert=server.pem -H 192.168.1.161 -P 9000 -L 10
    # vi apps/_websocket/templates/index.html    set: ws, wss, host, port
    # firefox http://localhost:8000/_websocket
    # firefox https://192.168.1.161:9000/_websocket  test wss
    # curl --insecure -I -H 'Upgrade: websocket' \
    #   -H "Sec-WebSocket-Key: `openssl rand -base64 16`" \
    #   -H 'Sec-WebSocket-Version: 13' \
    #   -sSv  https://192.168.1.161:9000/

    class GeventWebSocketServer(ServerAdapter):
        def run(self, handler):
            logger = "default"  # not None !! from gevent doc
            if not self.quiet:
                logging_conf(
                    self.options["logging_level"],
                )
                logger = logging.getLogger("gevent-ws")

            certfile = self.options.get("certfile", None)

            ssl_args = (
                dict(
                    certfile=certfile,
                    keyfile=self.options.get("keyfile", None),
                )
                if certfile
                else dict()
            )

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                handler,
                handler_class=WebSocketHandler,
                log=logger,
                error_log=logger,
                **ssl_args
            )

            server.serve_forever()

    return GeventWebSocketServer


def wsgirefThreadingServer():
    # https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

    import socket
    from concurrent.futures import ThreadPoolExecutor  # pip install futures
    from socketserver import ThreadingMixIn
    from wsgiref.simple_server import WSGIRequestHandler, WSGIServer, make_server

    class WSGIRefThreadingServer(ServerAdapter):
        def run(self, app):

            if not self.quiet:

                logging_conf(
                    self.options["logging_level"],
                )
                self.log = logging.getLogger("WSGIRef")

            self_run = self  # used in internal classes to access options and logger

            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(
                        self.process_request_thread, request, client_address
                    )

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(
                    max_workers=get_workers(self.options, default=40)
                )

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

                    # openssl req -newkey rsa:4096 -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
                    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
                    # ./py4web.py run apps -s wsgirefThreadingServer --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem
                    # openssl s_client -showcerts -connect 127.0.0.1:8443

                    certfile = self_run.options.get("certfile", None)

                    if certfile:
                        self.server.socket = ssl.wrap_socket(
                            self.server.socket,
                            certfile=certfile,
                            keyfile=self_run.options.get("keyfile", None),
                            ssl_version=ssl.PROTOCOL_SSLv23,
                            server_side=True,
                            do_handshake_on_connect=False,
                        )

                    self.server.serve_forever()

            class LogHandler(WSGIRequestHandler):
                def address_string(self):  # Prevent reverse DNS lookups please.
                    return self.client_address[0]

                def log_request(self, *args, **kw):
                    if not self_run.quiet:
                        return WSGIRequestHandler.log_request(self, *args, **kw)

                def log_message(self, format, *args):
                    if not self_run.quiet:  # and ( not args[1] in ['200', '304']) :
                        msg = "%s - - [%s] %s" % (
                            self.client_address[0],
                            self.log_date_time_string(),
                            format % args,
                        )
                        self_run.log.info(msg)

            handler_cls = self.options.get("handler_class", LogHandler)
            server_cls = Server

            if ":" in self.host:  # Fix wsgiref for IPv6 addresses.
                if getattr(server_cls, "address_family") == socket.AF_INET:

                    class ServerClass(Server):
                        address_family = socket.AF_INET6

                    server_cls = ServerClass

            srv = make_server(self.host, self.port, app, server_cls, handler_cls)
            srv.serve_forever()

    return WSGIRefThreadingServer


def rocketServer():
    try:
        from rocket3 import Rocket3 as Rocket
    except ImportError:
        from .rocket3 import Rocket3 as Rocket

    class RocketServer(ServerAdapter):
        def run(self, app):

            if not self.quiet:

                logging_conf(
                    self.options["logging_level"],
                )

            interface = (
                (
                    self.host,
                    self.port,
                    self.options["keyfile"],
                    self.options["certfile"],
                )
                if (
                    self.options.get("certfile", None)
                    and self.options.get("keyfile", None)
                )
                else (self.host, self.port)
            )

            server = Rocket(interface, "wsgi", dict(wsgi_app=app))
            server.start()

    return RocketServer
