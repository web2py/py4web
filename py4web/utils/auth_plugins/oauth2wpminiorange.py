# -*- coding: utf-8 -*-

"""
This plugin has been developed for login through a third party application that
uses 'WordPress OAuth Server' plugin:
https://wordpress.org/plugins/miniorange-oauth-20-server
"""

from ...core import URL, abort, redirect
from . import OAuth2

from urllib.parse import urljoin
import jwt
import requests


class OAuth2WPMiniorange(OAuth2):
    """
    Authorized Redirect URI template to be configured in your OAuth2 server
    configuration panel:
    http(s)://<your host>/<your app name>/auth/plugin/oauth2wpminiorange/callback

    Usage example for registering plugin in your py4web application:

    auth.register_plugin(
        OAuth2WPMiniorange(
            client_id = '<your client id>',
            client_secret = '<your client secret>',
            server_host = '<your server http(s) url>'
        )
    )

    """

    # name = "oauth2wpminiorange"
    # label = "Wordpress"

    # login_url = "https://.../wp-json/moserver/authorize"
    # token_url = "https://.../wp-json/moserver/token"
    # userinfo_url = "https://.../wp-json/moserver/resource"

    default_scope = "profile openid"
    default_maps = {
        # "email": "email",
        "sso_id": "ID",
        "username": "username"
        # "first_name": "firstname",
        # "last_name": "lastname",
    }

    def __init__(
        self,
        client_id,
        client_secret,
        server_host,
        name=None,
        label="Wordpress",
        maps=None,
        login_path="/wp-json/moserver/authorize",
        token_path="/wp-json/moserver/token",
        userinfo_path="/wp-json/moserver/resource",
        **kwargs,
    ):
        name = name or self.__class__.__name__.lower()
        super(OAuth2WPMiniorange, self).__init__(
            client_id, client_secret, f"auth/plugin/{name}/callback", **kwargs
        )
        self.name = name
        self.label = label
        self.login_url = urljoin(server_host, login_path)
        self.token_url = urljoin(server_host, token_path)
        self.userinfo_url = urljoin(server_host, userinfo_path)
        self.maps = maps or self.default_maps

    ### methods that needed to be overwritten

    def _handle_callback(self, auth, get_vars):
        try:
            data = self.callback(get_vars)
        except jwt.exceptions.InvalidSignatureError as err:
            # -# In case of invalid signature jwt library raises InvalidSignatureError
            # This maybe should be common to all OAuth2 derived classes.
            abort(401, err)
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
            for key, value__ in self.maps.items():
                value_, parts = data, value__.split(".")
                for part in parts:
                    # Thi is specific of the OAuth2 server implementation
                    value = value_["userinfo"][int(part) if part.isdigit() else part]

                    user[key] = value

            # -# In case of different servers username other than id sould result
            # not unique

            sso_id = user["sso_id"]
            user["sso_id"] = "%s:%s" % (
                self.name,
                sso_id,
            )
            if not "username" in user:
                user["username"] = "%s:%s" % (
                    self.name,
                    sso_id,
                )
            else:
                user["username"] = "%s:%s" % (
                    self.name,
                    user["username"],
                )
            # store or retrieve the user
            data = auth.get_or_register_user(user)

        else:
            # WIP Allow login without DB
            if not "id" in data:
                data["id"] = data.get("username") or data.get("email")
        user_id = data.get("id")
        auth.store_user_in_session(user_id)
        redirect(URL("index"))

    # -# This method is an exact copy of the one from original class
    # without this subsequent error is raised from the jwt library (don't know why)
    # jwt.exceptions.InvalidSignatureError: Signature verification failed

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
