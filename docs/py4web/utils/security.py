import fnmatch
import ipaddress
from py4web.core import Fixture, request, response, HTTP


def listify(item):
    """if item is not None and Not a list returns [item] else returns item"""
    if item is not None and not isinstance(item, (list, tuple)):
        item = [item]
    return item


def match_ip(ip, networks):
    """checks s an ip ('127.0.0.1') is a list of networks (['127.0.0.1/16'])"""
    ip = ipaddress.ip_address(ip)
    print("networks", networks)
    return any(ip in ipaddress.ip_network(network) for network in networks)


class CheckHeaders(Fixture):

    """
    This fixture can block an action from being excuted if:
    - it does not match the specificated protocol (http, https)
    - referer field does not match the same protocol as the current url
    - referer field does not match the same domain as the current url
    - referer field does not match the same app_name as the current url
    - ip address is not in the allowed_networks
    - ip address is in the blocked_networks (example ['127.0.0.1/16'])
    """

    def __init__(
        self,
        protocol=None,
        same_protocol=True,
        same_domain=True,
        same_app=True,
        allowed_networks=None,
        blocked_networks=None,
    ):
        self.protocol = protocol
        self.same_protocol = same_protocol
        self.same_domain = same_domain or same_app
        self.same_app = same_app
        self.allowed_networks = listify(allowed_networks)
        self.blocked_networks = listify(blocked_networks)

    def split(self, url):
        parts = url.split("/")
        checked_parts = []
        if self.same_protocol:
            checked_parts.append(parts[0])
        if self.same_domain:
            checked_parts.append(parts[2])
        if self.same_app:
            checked_parts.append(parts[3])
        return checked_parts

    def on_request(self):
        print(request.environ["REMOTE_ADDR"])
        if self.protocol and not request.url.startswith(self.protocol + "://"):
            raise HTTP(400)

        if self.blocked_networks is not None:
            if match_ip(request.environ["REMOTE_ADDR"], self.blocked_networks):
                raise HTTP(400)

        if self.allowed_networks is not None:
            if not match_ip(request.environ["REMOTE_ADDR"], self.allowed_networks):
                raise HTTP(400)

        referer = request.environ.get("HTTP_REFERER")
        if referer and not self.split(referer) == self.split(request.url):
            raise HTTP(400)


class AllowCors(Fixture):
    """
    Sets the CORS headers:
    Access-Control-Allow-Origin
    Access-Control-Allow-Headers
    Access-Control-Allow-Methods
    Access-Control-Expose-Headers
    Access-Control-Request-Headers
    """

    def __init__(
        self,
        origin="*",
        headers=["*"],
        methods=["*"],
        exposed_headers=[],
        request_headers=[],
    ):
        self.origin = origin
        self.headers = ", ".join(headers)
        self.methods = ", ".join(methods)
        self.exposed_headers = ", ".join(exposed_headers)
        self.request_headers = ", ".join(request_headers)

    def on_request(self):
        if self.origin:
            response.headers["Access-Control-Allow-Origin"] = self.origin
        if self.headers:
            response.headers["Access-Control-Allow-Headers"] = self.headers
        if self.methods:
            response.headers["Access-Control-Allow-Methods"] = self.methods
        if self.exposed_headers:
            response.headers["Access-Control-Expose-Headers"] = self.exposed_headers
        if self.request_headers:
            response.headers["Access-Control-Request-Headers"] = self.request_headers
