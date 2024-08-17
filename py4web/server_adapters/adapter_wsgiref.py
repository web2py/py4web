"builds and returns a wsgiref threading server"
# https://www.electricmonk.nl/log/2016/02/15/multithreaded-dev-web-server-for-the-python-bottle-web-framework/

import socket
import ssl
from concurrent.futures import ThreadPoolExecutor  # pip install futures
from socketserver import ThreadingMixIn
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer, make_server

from ombott.server_adapters import ServerAdapter

from .logging_utils import logging_conf


class WSGIRefAdapter(ServerAdapter):
    "Class implementing a WSGIRef server"

    def run(self, handler):
        "runs the server"

        self.log = None

        if not self.quiet:
            self.log = logging_conf(
                self.options["logging_level"],
                "wsgiref",
            )

        self_run = self  # used in internal classes to access options and logger

        class LogHandler(WSGIRequestHandler):
            def address_string(self):  # Prevent reverse DNS lookups please.
                return self.client_address[0]

            def log_request(self, *args, **kw):
                if not self_run.quiet:
                    WSGIRequestHandler.log_request(self, *args, **kw)

            def log_message(self, formatstr, *args):
                if not self_run.quiet:  # and ( not args[1] in ['200', '304']) :
                    msg = "%s - - [%s] %s" % (
                        self.client_address[0],
                        self.log_date_time_string(),
                        formatstr % args,
                    )
                    self_run.log.info(msg)

        class PoolMixIn(ThreadingMixIn):
            def process_request(self, request, client_address):
                self.pool.submit(self.process_request_thread, request, client_address)

        class ThreadingWSGIServer(PoolMixIn, WSGIServer):
            daemon_threads = True
            pool = ThreadPoolExecutor(max_workers=self.options.get("workers", 40))

        class Server:
            def __init__(self, server_address=("127.0.0.1", 8000), handler_cls=None):
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

        server_cls = Server

        if ":" in self.host:  # Fix wsgiref for IPv6 addresses.
            if getattr(server_cls, "address_family") == socket.AF_INET:

                class ServerClass(Server):
                    address_family = socket.AF_INET6

                server_cls = ServerClass

        srv = make_server(
            self.host, self.port, handler, server_cls, LogHandler
        )  # handler_cls)
        srv.serve_forever()
