import uuid
from types import SimpleNamespace
import json
import jwt
import time

from omfitt import BaseFixture
from ..core.globs import current_config


class Session(BaseFixture):

    # All apps share the same default secret if not specified.
    # important for _dashboard reload
    # the actual value is loaded from a file
    @property
    def local(self):
        return self._safe_local

    def __init__(
        self,
        secret=None,
        expiration=None,
        algorithm="HS256",
        storage=None,
        same_site="Lax",
    ):
        """
        secret is the shared key used to encrypt the session (using algorithm)
        expiration is in seconds
        (optional) storage must have a get(key) and set(key,value,expiration) methods
        if not provided session is stored in jwt cookie else the jwt is stored in storage and its uuid key is stored in the cookie
        """
        self.secret = secret or current_config.session_secret
        self.expiration = expiration
        self.algorithm = algorithm
        self.storage = storage
        self.same_site = same_site
        if isinstance(storage, Session):
            self.use_fixtures(storage)
        if hasattr(storage, "__prerequisites__"):
            self.__prerequisites__ = storage.__prerequisites__

    def take_on(self, app_ctx, route_ctx):
        self.load(app_ctx, route_ctx)
        route_ctx.provide('session', self)

    def on_finalize(self, app_ctx, route_ctx):
        if self._safe_local.changed:
            self.save()

    def initialize(self, request, response, app_name="unknown", data=None, changed=False, secure=False):
        local = self._safe_local = SimpleNamespace()
        local.request = request
        local.response = response
        local.changed = changed
        local.data = data or {}
        local.session_cookie_name = f"{app_name}_session"
        local.secure = secure

    def load(self, app_ctx, route_ctx):
        request = route_ctx.request
        self.initialize(
            request=request,
            response=route_ctx.response,
            app_name=app_ctx.app_name,
            changed=False,
            secure=request.url.startswith("https"),  # FIXME
        )
        self_local = self._safe_local
        raw_token = (
            request.get_cookie(self_local.session_cookie_name)
            or request.query.get("_session_token")
        )
        if not raw_token and request.method in {"POST", "PUT", "DELETE", "PATCH"}:
            raw_token = (
                request.forms and request.forms.get("_session_token")
                or request.json and request.json.get("_session_token")
            )
        if raw_token:
            token_data = raw_token.encode()
            try:
                if self.storage:
                    json_data = self.storage.get(token_data)
                    if json_data:
                        self_local.data = json.loads(json_data)
                else:
                    self_local.data = jwt.decode(
                        token_data, self.secret, algorithms=[self.algorithm]
                    )
                if self.expiration is not None and self.storage is None:
                    assert (
                        self_local.data["timestamp"] > time.time() - int(self.expiration)
                    )
                assert self.get_data().get("secure") == self_local.secure
            except Exception:
                pass
        if "uuid" not in self.get_data():
            self.clear()

    def get_data(self):
        return getattr(self._safe_local, "data", {})

    def save(self):
        self_local = self._safe_local
        response = self_local.response
        self_local.data["timestamp"] = time.time()
        if self.storage:
            cookie_data = self_local.data["uuid"]
            self.storage.set(cookie_data, json.dumps(self_local.data), self.expiration)
        else:
            cookie_data = jwt.encode(
                self_local.data, self.secret, algorithm=self.algorithm
            )
            if isinstance(cookie_data, bytes):
                cookie_data = cookie_data.decode()

        response.set_cookie(
            self_local.session_cookie_name,
            cookie_data,
            path="/",
            secure=self_local.secure,
            same_site=self.same_site,
        )

    def get(self, key, default=None):
        return self.get_data().get(key, default)

    def __getitem__(self, key):
        return self.get_data()[key]

    def __delitem__(self, key):
        if key in self.get_data():
            self._safe_local.changed = True
            del self._safe_local.data[key]

    def __setitem__(self, key, value):
        self._safe_local.changed = True
        self._safe_local.data[key] = value

    def __contains__(self, k):
        return k in self.keys()

    def keys(self):
        return self.get_data().keys()

    def __iter__(self):
        yield from self.get_data().items()

    def clear(self):
        """Produces a brand-new session."""
        local = self._safe_local
        local.changed = True
        local.data.clear()
        local.data["uuid"] = str(uuid.uuid1())
        local.data["secure"] = local.secure
