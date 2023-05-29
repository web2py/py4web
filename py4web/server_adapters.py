import logging

from ombott.server_adapters import ServerAdapter

try:
    from .utils.wsservers import *
except ImportError:
    wsservers_list = []

__all__ = [
    "geventWebSocketServer",
    "wsgirefThreadingServer",
    "rocketServer",
    "gevent",
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

     return level if level in ( logging.CRITICAL, logging.ERROR, logging.WARN, 
                  logging.INFO, logging.DEBUG, logging.NOTSET ) else logging.WARN

def logging_conf( level, log_file="server-py4web.log"):

     logging.basicConfig(
         filename=log_file,
         format="%(threadName)s | %(message)s",
         filemode="w",
         encoding="utf-8",
         level=check_level( level ) ,
     )

def gevent():
    # gevent version 22.10.2

    from gevent import pywsgi, local # pip install gevent
    import threading, ssl

    if not isinstance(threading.local(), local.local):
        msg = "Ombott requires gevent.monkey.patch_all() (before import)"
        raise RuntimeError(msg)


    # ./py4web.py run apps --watch=off -s gevent -L 20  # look into gevent.log
    #
    # ./py4web.py run apps -s gevent --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem -L 0
    # ./py4web.py run apps -s gevent --watch=off --host=192.168.1.161 --port=8443 --ssl_cert=server.pem -L 0

    class GeventServer(ServerAdapter):
        def run(self, handler):

            logger ='default' # not None - from gevent doc
            if not self.quiet:
          
                logger = logging.getLogger('gevent')
                fh = logging.FileHandler('gevent.log')
                logger.setLevel( check_level( self.options["logging_level"] ) )
                logger.addHandler( fh )
                logger.addHandler(logging.StreamHandler())

            certfile = self.options.get("certfile", None)

            ssl_args = dict (
                     certfile = certfile,
                     keyfile = self.options.get("keyfile", None),
                     ssl_version=ssl.PROTOCOL_SSLv23,
                     server_side= True,
                     do_handshake_on_connect=False,
                ) if certfile else dict()

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                handler,
                log=logger, error_log=logger,
                **ssl_args
            )

            server.serve_forever()

    return GeventServer


def geventWebSocketServer():
    from gevent import pywsgi  # pip install gevent gevent-websocket
    from geventwebsocket.handler import WebSocketHandler 
    # from geventwebsocket.logging import create_logger # it does not work for me
  
    # ./py4web.py run apps -s geventWebSocketServer --watch=off --host=127.0.0.1 --port=8000 -L 10
    # vi apps/_websocket/templates/index.html    ws host port
    # firefox http://localhost:8000/_websocket

    # >>> geventwebsocket.get_version()
    # '0.10.1'
    # >>> gevent.__version__
    # '22.10.2'

    class GeventWebSocketServer(ServerAdapter):
        def run(self, handler):

            #ssl_args = self.options.copy()
            # keep only ssl options
            #for e in ( 'reloader', 'logging_level', 'number_workers', 'workers' ):
            #    try:
            #        del ssl_args[ e]
            #    except KeyError:
            #        pass

            ssl_args = dict()

            logger='default' # not None !! from gevent doc
            if not self.quiet:
                logging_conf(self.options["logging_level"], 'gevent-ws.log' )
                logger = logging.getLogger("geventwebsocket.logging")
                logger.addHandler(logging.StreamHandler())

            server = pywsgi.WSGIServer(
                (self.host, self.port),
                handler,
                handler_class=WebSocketHandler,
                log=logger, error_log=logger,
                **ssl_args
            )

            server.serve_forever()

    return GeventWebSocketServer


def wsgirefThreadingServer():
    # https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

    import socket, ssl
    from concurrent.futures import ThreadPoolExecutor  # pip install futures
    from socketserver import ThreadingMixIn
    from wsgiref.simple_server import (WSGIRequestHandler, WSGIServer, make_server)

    class WSGIRefThreadingServer(ServerAdapter):
        def run(self, app):
            
            if not self.quiet:

                logging_conf(self.options["logging_level"], )
                self.log = logging.getLogger("WSGIRef")
                self.log.addHandler(logging.StreamHandler())

            try:
                workers = self.options['workers'] if self.options['workers'] else 40
            except KeyError:
                workers = 40

            self_run = self # used in internal classes to access options and logger

            class PoolMixIn(ThreadingMixIn):
                def process_request(self, request, client_address):
                    self.pool.submit(
                        self.process_request_thread, request, client_address
                    )

            class ThreadingWSGIServer(PoolMixIn, WSGIServer):
                daemon_threads = True
                pool = ThreadPoolExecutor(max_workers=workers)

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
                            self.server.socket = ssl.wrap_socket (
                                self.server.socket,
                                certfile = certfile,
                                keyfile = self_run.options.get("keyfile", None),
                                ssl_version=ssl.PROTOCOL_SSLv23,
                                server_side= True,
                                do_handshake_on_connect=False,
                            )

                    self.server.serve_forever()

            class LogHandler(WSGIRequestHandler):
                def address_string(self):  # Prevent reverse DNS lookups please.
                    return self.client_address[0]

                def log_request(*args, **kw):
                    if not self_run.quiet:
                        return WSGIRequestHandler.log_request(*args, **kw)

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

    class RocketServer(ServerAdapter):
        def run(self, app):

            if not self.quiet:
             
                logging_conf( self.options["logging_level"], )
                log = logging.getLogger("Rocket")
                log.addHandler(logging.StreamHandler())

            interface = (self.host, self.port, self.options["keyfile"], self.options["certfile"]
                ) if ( self.options.get("certfile", None) and self.options.get("keyfile", None) 
                ) else ( self.host, self.port)

            server = Rocket(interface, "wsgi", dict(wsgi_app=app))
            server.start()

    return RocketServer
