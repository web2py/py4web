import urllib
import calendar
import time
import uuid
import json
import random
import jwt
import string
import requests
from py4web.core import URL, abort, redirect, request


class SSO(object):

    name = "undefined"
    maps = {}

    ### methods that must be overwritten

    def __init__(self, **parameters):
        self.parameters = parameters
        self.next = URL("index")  # Destination after login succeeds

    def get_login_url(self):
        """returns the url for login"""
        return ""

    def handle_request(self, auth, path, get_vars, post_vars):
        if path == "login":
            self.next = request.query.get("next") or URL("index")
            redirect(self.get_login_url())
        elif path == "callback":
            self._handle_callback(auth, get_vars)
        else:
            abort(404)

    def callback(self, get_vars):
        return {}

    ### methods that probably do not need to be overwritten

    def _handle_callback(self, auth, get_vars):
        data = self.callback(get_vars)
        if not data:
            abort(401)
        error = data.get("error")
        if error:
            if isinstance(error, str):
                code, msg = 401, error
            else:
                code = error.get("code", 401)
                msg = error.get("message", "Unknown error")
            abort(code, msg)
        if auth.db:
            # map returned fields into auth_user fields
            user = {}
            for key, value in self.maps.items():
                value, parts = data, value.split(".")
                for part in parts:
                    value = value[int(part) if part.isdigit() else part]
                    user[key] = value
            user["sso_id"] = "%s:%s" % (self.name, user["sso_id"])
            if not "username" in user:
                user["username"] = user["sso_id"]
            # store or retrieve the user
            data = auth.get_or_register_user(user)
        else:
            # WIP Allow login without DB
            if not "id" in data:
                data["id"] = data.get("username") or data.get("email")
        user_id = data.get("id")
        auth.store_user_in_session(user_id)
        redirect(self.next)

    @staticmethod
    def _build_url(base, data):
        return (
            base
            + "?"
            + "&".join("%s=%s" % (k, urllib.parse.quote(v)) for k, v in data.items())
        )


class OAuth2(SSO):
    name = "undefined"
    login_button_content = ""
    login_button_class = ""
    login_url = ""
    token_url = ""
    userinfo_url = ""
    default_scope = ""
    algorithms = ["HS256", "RS256"]

    def __init__(
        self,
        client_id,
        client_secret,
        callback_url,
        scope=None,
        scheme=True,
        passed_state=None,
    ):
        SSO.__init__(self)
        self.parameters = dict(
            client_id=client_id,
            client_secret=client_secret,
            callback_url=callback_url,
            scope=scope or self.default_scope,
            scheme=scheme,
            passed_state=passed_state,
        )

    def state_generator(
        self,
        size=18,
        chars=string.ascii_uppercase + string.digits + string.ascii_lowercase,
    ):
        return "".join(random.choice(chars) for _ in range(size))

    def get_login_url(self, state=None, next=None):
        callback_url = self.parameters.get("callback_url")
        vars = {}
        if next:
            vars["next"] = next
        data = dict(
            access_type="offline",
            redirect_uri=URL(
                callback_url, vars=vars, scheme=self.parameters.get("scheme")
            ),
            response_type="code",
            client_id=self.parameters.get("client_id"),
        )
        scope = self.parameters.get("scope")
        state = self.state_generator()
        if scope:
            data["scope"] = scope
            data["include_granted_scopes"] = "true"
        if state:
            data["state"] = state
        return self._build_url(self.login_url, data)

    def callback(self, query):
        code = query.get("code")
        statecheck = query.get("state")
        if not code:
            return False
        passed_state = self.parameters.get("passed_state")
        if passed_state is not None and statecheck != passed_state:
            return False
        data = dict(
            code=code,
            client_id=self.parameters.get("client_id"),
            client_secret=self.parameters.get("client_secret"),
            redirect_uri=URL(
                self.parameters.get("callback_url"),
                scheme=self.parameters.get("scheme"),
            ),
            grant_type="authorization_code",
        )
        res = requests.post(self.token_url, data=data)
        output = res.json()
        token = output.get("id_token")
        if token is not None:
            # Lets not get the  user attributes via the userinfo endpoint
            # but lets take the userinfo directly extracted from the token
            # res = requests.get(self.userinfo_url, headers=headers)
            data = jwt.decode(
                token,
                algorithms=self.algorithms,
                # because of this open issue
                # https://github.com/jpadilla/pyjwt/issues/359
                options={"verify_signature": False},
            )
        else:
            # fallback to old approach if "id_token" is not in the response
            token = output.get("access_token")
            headers = {"Authorization": "Bearer %s" % token}
            res = requests.get(self.userinfo_url, headers=headers)
            data = res.json()
        return data

    def revoke(self, token):
        requests.post(self.revoke_url, data=dict(token=token))
