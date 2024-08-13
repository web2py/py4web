import ssl
import threading

from gevent import local, pywsgi  # pip install gevent
from ombott.server_adapters import ServerAdapter

from .logging_utils import logging_conf

# ./py4web.py run apps --watch=off -s gevent -L 20
#
# ./py4web.py run apps -s gevent --watch=off --port=8443 --ssl_cert=cert.pem --ssl_key=key.pem -L 0
# ./py4web.py run apps -s gevent --watch=off --host=192.168.1.161 --port=8443 --ssl_cert=server.pem -L 0


class GeventAdapter(ServerAdapter):
    "Defines a gevent server"

    def run(self, handler):
        "runs the server"

        if not isinstance(threading.local(), local.local):
            msg = "Ombott requires gevent.monkey.patch_all() (before import)"
            raise RuntimeError(msg)

        logger = None  # "default"

        if not self.quiet:
            logger = logging_conf(
                self.options["logging_level"],
                "gevent",
            )
            # logger.addHandler(logging.StreamHandler())

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
            else {}
        )

        server = pywsgi.WSGIServer(
            (self.host, self.port),
            handler,
            log=logger,
            error_log=logger,
            **ssl_args,
        )

        server.serve_forever()
