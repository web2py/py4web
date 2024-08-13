# from geventwebsocket.handler import WebSocketHandler # pip install gevent-websocket
from gevent import pywsgi
from gevent_ws import WebSocketHandler  # pip install gevent gevent-ws
from ombott.server_adapters import ServerAdapter

from .logging_utils import logging_conf

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


class GeventWebSocketAdapter(ServerAdapter):
    "Class implementing a Gevent websocket server"

    def run(self, handler):
        "Runs the server"
        logger = None  # "default"

        if not self.quiet:
            logger = logging_conf(
                self.options["logging_level"],
                "gevent-ws",
            )

        args = dict(
            handler_class=WebSocketHandler,
            log=logger,
            error_log=logger,
        )

        certfile = self.options.get("certfile")
        keyfile = self.options.get("keyfile")
        if certfile and keyfile:
            args.update(certfile=certfile, keyfile=keyfile)

        server = pywsgi.WSGIServer((self.host, self.port), handler, **args)

        server.serve_forever()
