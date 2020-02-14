import hashlib
import uuid
from py4web import request, abort
from py4web.core import Fixture, Session


class URLVerifier(Fixture):
    """This class checks for the validity of URL signatures.
     Specifically, an object of this class can be passed as argument
     to action.uses() to check for the validity of signatures, and the
     sign() method can be used to sign a URL.  If an object of this class
     is passed to the URL helper, it can be used to sign a URL."""
    def __init__(self, url_signer, query_keys):
        if url_signer.session:
            self.__prerequisites__ = [url_signer.session]
        self.url_signer = url_signer
        self.query_keys = query_keys

    def on_request(self):
        """Checks the request's signature"""
        vars = dict(request.query)
        # extra and remove the signature from the query
        signature = request.query.get("_signature")
        if signature is None:
            abort(403)
        del request.query["_signature"]
        # verify all query_keys or only those specified
        query = {key: value for key, value in request.query.items()
                 if self.query_keys is None or key in self.query_keys}
        if signature != self.url_signer._sign(request.fullpath, query):
            abort(403)


class URLSigner:
    def __init__(self, session=None, key=None, salt=b"", sign_query=False):
        """
        you can provde a key or a session to sign the URL
        if none provided will use the global Session.SECRET
        salt is some salt that can be used in signing if desired.
        if sign_query is set to false, the query string will also be signed
        """
        super().__init__(
        )  # Yes, I know that this currently doesn't do anything.
        self.session = session
        self.key = key or Session.SECRET
        self.salt = salt
        self.sign_query = sign_query

    def _get_key(self):
        """Gets the signing key, creating it if necessary."""
        if not self.session:
            key = self.key
        else:
            self.session.get("_signature_key")
            if key is None:
                key = str(uuid.uuid4())
                self.session["_signature_key"] = key
        return key

    def _sign(self, url, query):
        """Signs the URL"""
        h = hashlib.sha256(self.salt)
        h.update(url.encode('utf8'))  # Is utf8 the right encoding?
        if self.sign_query:
            for key in sorted(query):
                h.update(('%s=%r' % (key, query[key])).encode('utf8'))
        h.update(self._get_key().encode('utf8'))
        return h.hexdigest()

    def sign_vars(self, url, vars):
        vars["_signature"] = self._sign(url, vars)

    def verify(self, query_keys=None):
        """returns a fixture that verifies the URL and optionally the query_keys"""
        return URLVerifier(self, query_keys)
