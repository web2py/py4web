import json
import hashlib
import time
import traceback
import uuid
import base64
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
        try:
            h = hashlib.sha256(self.url_signer.get_key())
            h.update(self.url_signer.get_info_to_sign(request.fullpath, request.query))
            print("Given:", base64.b85encode(h.digest()).decode("utf-8"))
            print("Recvd:", request.query["_signature"])
            if base64.b85encode(h.digest()).decode("utf-8") != request.query["_signature"]:
                abort(403)
            # We remove the signature, not to pollute the request.
            del request.query["_signature"]
            # Checks the expiration time.
            if self.url_signer.lifespan is not None:
                ts = self._decode_ts(request.query["_ts"])
                print("ts:", ts)
                if ts + self.url_signer.lifespan < time.time():
                    abort(403)
            del request.query["_ts"]
        except:
            print(traceback.format_exc())
            abort(403)

    def _decode_ts(self, ts_string):
        """Decodes the timestamp, removing the salt."""
        s = base64.b85encode(ts_string.encode("utf-8")).decode("utf-8")
        return float(s.split(";")[1])


class URLSigner(Fixture):

    RESERVED_VARIABLES = ["_ts", "_signature"]

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
        assert "_ts" not in self.variables_to_sign
        assert "_signature" not in self.variables_to_sign
        self.variables_to_sign.append("_ts")

    def get_key(self):
        """Gets the signing key, creating it if necessary."""
        if self.session is None:
            key = self.key
        else:
            key = self.session.get("_signature_key")
            if key is None:
                key = str(uuid.uuid1())
                self.session["_signature_key"] = key
        return key.encode("utf8")

    def encode_ts(self):
        s = str(uuid.uuid1()) + ";" + "%.3f" % time.time()
        return base64.b85encode(s.encode("utf-8")).decode("utf-8")

    def get_info_to_sign(self, url, variables):
        """Gathers the information to be signed."""
        # The key consists of the url, and of the URL parameters.
        print("info:",  {
            "url": url,
            "info": self.signing_info() if self.signing_info is not None else "",
            "vars": {v: str(variables.get(v)) for v in self.variables_to_sign},
        })
        return json.dumps({
            "url": url,
            "info": self.signing_info() if self.signing_info is not None else "",
            "vars": {v: str(variables.get(v)) for v in self.variables_to_sign},
        }).encode("utf-8")

    def sign(self, url, variables):
        """Signs the URL"""
        for v in self.RESERVED_VARIABLES:
            assert v not in variables
        h = hashlib.sha256(self.get_key())
        variables["_ts"] = self.encode_ts()
        h.update(self.get_info_to_sign(url, variables))
        variables["_signature"] = base64.b85encode(h.digest()).decode("utf-8")

    def verify(self):
        """returns a fixture that verifies the URL and optionally the query_keys"""
        return URLVerifier(self)
