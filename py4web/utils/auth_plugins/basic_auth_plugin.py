from pydal._compat import urlopen
from pydal._compat import urllib2
import base64


class BasicAuthPlugin:

    name = "basic"
    label = "Basic"

    def __init__(self, server="127.0.0.1", table=None):
        self.server = server

    def validate_credentials(self, username, password):

        """
        to use basic login with a different server
        from gluon.contrib.login_methods.basic_auth import basic_auth
        auth.settings.login_methods.append(basic_auth('http://server'))
        """
        key = base64.b64encode(username + ":" + password)
        headers = {"Authorization": "Basic " + key}
        request = urllib2.Request(self.server, None, headers)
        try:
            urlopen(request)
            return True
        except (urllib2.URLError, urllib2.HTTPError):
            return False
