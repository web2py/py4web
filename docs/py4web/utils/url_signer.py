import json
import jwt
import time
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
        token = request.query.get("_signature")
        if token is None:
            abort(403)
        try:
            key = self.url_signer.get_url_key(request.fullpath, request.query)
            jwt.decode(token, key, algorithms=["HS256"])
            # We remove the signature, not to pollute the request.
            del request.query["_signature"]
        except:
            abort(403)


class URLSigner(Fixture):
    def __init__(
        self,
        session=None,
        key=None,
        variables_to_sign=None,
        signing_info=None,
        lifespan=None,
    ):
        """
        Signer for URLs.
        :param session: Session.  If a session is not specified, it will use a key
            to sign the URLs.
        :param key: key to sign, used if no session is specified.  If neither a
            session nor a key is specified, then Session.SECRET is used to sign.
        :param variables_to_sign: List of variables to be included in the signature.
        :param signing_info: A function that, when called, returns an additional
            string that is passed into the signing algorithm.  One can e.g. include
            the user id among the things that should not change by doing:
            signing_info = lambda : str(self.session.get("user", {}).get("id", ""))
        :param lifespan: Lifespan of the signature, in seconds.

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
        self.variables_to_sign = variables_to_sign or []
        self.signing_info = signing_info
        self.lifespan = lifespan
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
        return key

    def get_url_key(self, url, variables):
        # The key consists of the key, and of the URL parameters.
        additional_key = {
            "url": url,
            "info": self.signing_info() if self.signing_info is not None else "",
            "vars": {v: repr(variables.get(v)) for v in self.variables_to_sign},
        }
        key = self._get_key() + "." + json.dumps(additional_key)
        return key

    def sign(self, url, variables):
        """Signs the URL"""
        # The payload consists of a timestamp, and of additonal parameters.
        payload = {"ts": str(time.time())}
        if self.lifespan is not None:
            payload["exp"] = time.time() + self.lifespan
        key = self.get_url_key(url, variables)
        return jwt.encode(payload, key, algorithm="HS256").decode("utf-8")

    def sign_vars(self, url, variables):
        """Signs a URL, adding to vars (the variables of the URL) a signature."""
        variables["_signature"] = self.sign(url, variables)

    def verify(self):
        """returns a fixture that verifies the URL and optionally the query_keys"""
        return URLVerifier(self)
