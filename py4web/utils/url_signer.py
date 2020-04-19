import hashlib, hmac
import uuid
from py4web import request, abort
from py4web.core import Fixture, Session


class URLVerifier(Fixture):
    """This class checks for the validity of URL signatures.
     Specifically, an object of this class can be passed as argument
     to action.uses() to check for the validity of signatures, and the
     sign() method can be used to sign a URL.  If an object of this class
     is passed to the URL helper, it can be used to sign a URL."""

    def __init__(self, url_signer):
        super().__init__()
        if url_signer.session is not None:
            self.__prerequisites__ = [url_signer.session]
        self.url_signer = url_signer

    def on_request(self):
        """Checks the request's signature"""
        # extra and remove the signature from the query
        signature = request.query.get("_signature")
        if signature is None:
            abort(403)
        del request.query["_signature"]
        # Verifies the query keys.
        if signature != self.url_signer.sign(request.fullpath, request.query):
            abort(403)


class URLSigner(Fixture):
    def __init__(self, session=None, key=None, salt=b"", variables_to_sign=None):
        """
        Signer for URLs.
        :param session: Session.  If a session is not specified, it will use a key
            to sign the URLs.
        :param key: key to sign, used if no session is specified.  If neither a
            session nor a key is specified, then Session.SECRET is used to sign.
        :param salt: Optional salt that can be used in signing; used to create
            signers with different behavior while sharing the same session key.
        :param variables_to_sign: List of variables to be included in the signature.

        The usage is as follows, typically.

        # We build a URL signer.
        url_signer = URLSigner(session)

        @action('/somepath')
        @action.uses(url_signer)
        def somepath():
            # This controller signs a URL.
            return dict(signed_url = URL('/anotherpath', signer=url_signer))

        @action('/anotherpath')
        @action.uses(url_signer.verify())
        def anotherpath():
            # The signature has been verified.
            return dict()
        """
        super().__init__()
        self.session = session
        if session is not None:
            # This ensures that the session will be saved with its changes
            # (including the signing key).
            self.__prerequisites__ = [session]
        self.key = key or Session.SECRET
        self.salt = salt
        self.variables_to_sign = variables_to_sign or []
        assert "_signature" not in self.variables_to_sign

    def _get_key(self):
        """Gets the signing key, creating it if necessary."""
        if self.session is None:
            key = self.key
        else:
            key = self.session.get("_signature_key")
            if key is None:
                key = str(uuid.uuid1())
                self.session["_signature_key"] = key
        return key.encode("utf8")

    def sign(self, url, variables):
        """Signs the URL"""
        h = hmac.new(self._get_key(), msg=self.salt, digestmod=hashlib.sha256)
        h.update(url.encode("utf8"))
        # Adds the variables that need to be signed.
        for key in self.variables_to_sign:
            h.update(("%s=%r" % (key, variables[key])).encode("utf8"))
        return h.hexdigest()

    def sign_vars(self, url, variables):
        """Signs a URL, adding to vars (the variables of the URL) a signature."""
        variables["_signature"] = self.sign(url, variables)

    def verify(self):
        """returns a fixture that verifies the URL and optionally the query_keys"""
        return URLVerifier(self)
