from ombott.server_adapters import ServerAdapter
from rocket3 import Rocket3

from .logging_utils import logging_conf


class Rocket3Adapter(ServerAdapter):
    "Class implementing a rocket3 server"

    def run(self, handler):
        "runs the server"

        if not self.quiet:
            logging_conf(
                self.options["logging_level"],
            )

        keyfile = self.options.get("keyfile")
        certfile = self.options.get("certfile")

        if keyfile and certfile:
            interface = (self.host, self.port, keyfile, certfile)
        else:
            interface = (self.host, self.port)

        server = Rocket3(interface, "wsgi", dict(wsgi_app=handler))
        server.start()
