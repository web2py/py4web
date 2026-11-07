import io
import os
import unittest
import uuid

from py4web.core import DAL, HTTP, Fixture, Session, bottle, request, response, safely
from py4web.utils.auth import Auth, AuthAPI
from py4web.utils.auth_plugins import OAuth2

SECRET = str(uuid.uuid4())

USER = {
    "username": "ppallino",
    "email": "pinco.pallino@example.com",
    "password": "123456789",
    "first_name": "Pinco",
    "last_name": "Pallino",
}


class AuthTestBase(unittest.TestCase):
    auth_kwargs = {}

    def setUp(self):
        os.environ["PY4WEB_APPS_FOLDER"] = "apps"
        self.db = DAL("sqlite:memory")
        self.session = Session(secret=SECRET, expiration=10)
        self.auth = Auth(
            self.session,
            self.db,
            define_tables=True,
            password_complexity=None,
            **self.auth_kwargs,
        )
        self.auth.enable()
        request.app_name = "_scaffold"
        for key in ("HTTP_ORIGIN", "HTTP_HOST", "REMOTE_ADDR"):
            request.environ.pop(key, None)

    def tearDown(self):
        safely(lambda: Fixture.local_delete(self.session))
        safely(lambda: Fixture.local_delete(self.auth.flash))
        bottle.app.router.remove("/*")

    def api(self, name, data, method="POST", query=None):
        request.environ["REQUEST_METHOD"] = method
        request.environ["ombott.request.query"] = query or {}
        request.environ["ombott.request.json"] = data
        request.environ["wsgi.input"] = io.BytesIO()
        return getattr(AuthAPI, name)(self.auth)

    def on_request(self, keep_session=False):
        try:
            storage = self.session.local.__dict__
        except RuntimeError:
            storage = None
        safely(lambda: Fixture.local_delete(self.session))
        safely(lambda: Fixture.local_delete(self.auth.flash))
        self.session.on_request({})
        self.auth.flash.on_request({})
        self.auth.on_request({})
        if keep_session and storage:
            self.session.local.__dict__.update(storage)

    def register(self, **fields):
        self.on_request()
        res = self.api("register", dict(USER, **fields))
        self.assertTrue(res.get("id"), res)
        return res["id"]

    def verify(self, user_id):
        self.db(self.db.auth_user.id == user_id).update(action_token=None)


class TestEmailLinks(AuthTestBase):
    def test_link_ignores_origin_when_base_url_set(self):
        self.auth.param.base_url = "https://real.example.com/"
        self.register()
        self.verify(1)
        self.on_request()
        request.environ["HTTP_ORIGIN"] = "https://evil.example.com"
        self.api("request_reset_password", {"email": USER["email"]})
        self.assertTrue(
            self.auth._link.startswith(
                "https://real.example.com/_scaffold/auth/reset_password?token="
            ),
            self.auth._link,
        )

    def test_link_falls_back_to_origin(self):
        self.register()
        self.verify(1)
        self.on_request()
        request.environ["HTTP_ORIGIN"] = "https://origin.example.com"
        self.api("request_reset_password", {"email": USER["email"]})
        self.assertTrue(
            self.auth._link.startswith("https://origin.example.com/"),
            self.auth._link,
        )


class TestResetPasswordStates(AuthTestBase):
    def test_reset_does_not_bypass_email_verification(self):
        self.register()
        self.on_request()
        self.api("request_reset_password", {"email": USER["email"]})
        token = self.db.auth_user[1].action_token
        self.assertTrue(token.startswith("pending-registration:"), token)
        self.on_request()
        res = self.api(
            "login", {"email": USER["email"], "password": USER["password"]}
        )
        self.assertEqual(res.get("message"), "Registration is pending")

    def test_reset_does_not_bypass_approval(self):
        self.register()
        self.db(self.db.auth_user.id == 1).update(action_token="pending-approval")
        self.on_request()
        self.api("request_reset_password", {"email": USER["email"]})
        self.assertEqual(self.db.auth_user[1].action_token, "pending-approval")

    def test_reset_allowed_on_active_account(self):
        self.register()
        self.verify(1)
        self.on_request()
        self.api("request_reset_password", {"email": USER["email"]})
        token = self.db.auth_user[1].action_token
        self.assertTrue(token.startswith("reset-password-request:"), token)


class TestApiLoginTwoFactor(AuthTestBase):
    def test_api_login_requires_two_factor(self):
        self.auth.param.two_factor_send = lambda user, code: code
        self.register()
        self.verify(1)
        self.on_request()
        res = self.api(
            "login", {"email": USER["email"], "password": USER["password"]}
        )
        self.assertEqual(res["status"], "error")
        self.assertEqual(res["code"], 401)
        self.assertTrue(res["two_factor_url"].endswith("/auth/two_factor"))
        self.assertIsNone(self.auth.user_id)
        self.assertEqual(self.session.get("auth.2fa_user"), 1)

    def test_api_login_without_two_factor(self):
        self.register()
        self.verify(1)
        self.on_request()
        res = self.api(
            "login", {"email": USER["email"], "password": USER["password"]}
        )
        self.assertEqual(res["status"], "success")
        self.assertEqual(self.auth.user_id, 1)


class FakeOAuth2(OAuth2):
    name = "fake"
    login_url = "https://idp.example.com/authorize"
    maps = {"sso_id": "sub", "email": "email", "first_name": "given_name",
            "last_name": "family_name"}

    def callback(self, query):
        return {"sub": "42", "email": "sso@example.com", "given_name": "S",
                "family_name": "O"}


class TestSSO(AuthTestBase):
    def setUp(self):
        super().setUp()
        self.plugin = FakeOAuth2("id", "secret", "auth/plugin/fake/callback")

    def call(self, path, query):
        request.environ["ombott.request.query"] = query
        response.headers.pop("Location", None)
        with self.assertRaises(HTTP) as cm:
            self.plugin.handle_request(self.auth, path, query, {})
        self.location = response.headers.get("Location")
        return cm.exception

    def test_state_is_stored_and_checked(self):
        self.on_request()
        res = self.call("login", {"next": "https://evil.com"})
        self.assertEqual(res.status, 303)
        state = self.session.get("_oauth2_state")
        self.assertTrue(state and len(state) >= 32)
        self.assertIn("state=" + state, self.location)
        # next is not an open redirect
        self.assertNotIn("evil", self.session.get("_next"))
        # wrong state is rejected (login CSRF)
        res = self.call("callback", {"code": "x", "state": "wrong"})
        self.assertEqual(res.status, 401)
        self.assertIsNone(self.auth.user_id)

    def test_callback_without_login_is_rejected(self):
        self.on_request()
        res = self.call("callback", {"code": "attacker-code", "state": ""})
        self.assertEqual(res.status, 401)

    def test_valid_callback_logs_in(self):
        self.on_request()
        self.call("login", {"next": "/app/page"})
        state = self.session.get("_oauth2_state")
        res = self.call("callback", {"code": "x", "state": state})
        self.assertEqual(res.status, 303)
        self.assertEqual(self.location, "/app/page")
        self.assertTrue(self.auth.user_id)

    def test_blocked_account_cannot_sso(self):
        self.on_request()
        self.call("login", {})
        state = self.session.get("_oauth2_state")
        self.db.auth_user.insert(
            email="sso@example.com", sso_id="fake:42", action_token="account-blocked"
        )
        res = self.call("callback", {"code": "x", "state": state})
        self.assertEqual(res.status, 403)
        self.assertIsNone(self.auth.user_id)


if __name__ == "__main__":
    unittest.main()
