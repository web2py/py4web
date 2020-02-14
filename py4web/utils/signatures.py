import hashlib
import uuid
from py4web import request, abort
from py4web.core import Fixture

class URLSigner(Fixture):
    """This class checks for the validity of URL signatures.
     Specifically, an object of this class can be passed as argument
     to action.uses() to check for the validity of signatures, and the
     sign() method can be used to sign a URL.  If an object of this class
     is passed to the URL helper, it can be used to sign a URL."""

    def __init__(self, session, salt=b""):
        """salt is some salt that can be used in signing if desired."""
        super().__init__() # Yes, I know that this currently doesn't do anything.
        self.session = session
        self.salt = salt
        self.__prerequisites__ = [session]

    def _get_key(self):
        """Gets the signing key, creating it if necessary."""
        k = self.session.get("_signature_key")
        if k is None:
            k = str(uuid.uuid4())
            self.session["_signature_key"] = k
        return k

    def _sign(self, url):
        """Signs the URL"""
        h = hashlib.sha256(self.salt)
        h.update(url.encode('utf8')) # Is utf8 the right encoding?
        h.update(self._get_key().encode('utf8'))
        return h.hexdigest()

    def sign_vars(self, url, vars):
        vars["_signature"] = self._sign(url)

    def on_request(self):
        """Checks the request's signature"""
        if request.query.get("_signature") != self._sign(request.fullpath):
            abort(403)
        del request.query["_signature"]
