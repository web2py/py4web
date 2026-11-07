import io
import os
import unittest
import uuid

from py4web.core import DAL, HTTP, Fixture, Session, bottle, request, response, safely
from py4web.utils.auth import Auth, AuthAPI, SimpleTokenPlugin
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


    def test_sso_links_existing_account_with_verified_email(self):
        self.on_request()
        uid = self.db.auth_user.insert(email="sso@example.com", password="x")
        user = self.auth.get_or_register_user(
            {"sso_id": "fake:42", "email": "sso@example.com", "email_verified": True}
        )
        self.assertEqual(user["id"], uid)
        self.assertEqual(self.db.auth_user(uid).sso_id, "fake:42")
        # next login is found by sso_id, still no duplicate
        user = self.auth.get_or_register_user(
            {"sso_id": "fake:42", "email": "sso@example.com", "email_verified": True}
        )
        self.assertEqual(user["id"], uid)
        self.assertEqual(self.db(self.db.auth_user).count(), 1)

    def test_sso_does_not_link_unverified_email(self):
        self.on_request()
        uid = self.db.auth_user.insert(email="sso@example.com", password="x")
        with self.assertRaises(HTTP) as cm:
            self.auth.get_or_register_user(
                {"sso_id": "fake:42", "email": "sso@example.com"}
            )
        self.assertEqual(cm.exception.status, 401)
        self.assertEqual(self.db(self.db.auth_user).count(), 1)
        self.assertIsNone(self.db.auth_user(uid).sso_id)

    def test_sso_without_email(self):
        self.on_request()
        user = self.auth.get_or_register_user({"sso_id": "fake:42"})
        self.assertTrue(user["id"])

class TestTwoFactorServerSide(AuthTestBase):
    def setUp(self):
        super().setUp()
        self.auth.param.two_factor_send = lambda user, code: code
        self.register()
        self.verify(1)

    def start(self):
        self.on_request()
        self.session["auth.2fa_user"] = 1
        self.session["auth.2fa_next_url"] = "/app/index"
        request.environ["REQUEST_METHOD"] = "GET"
        request.environ["wsgi.input"] = io.BytesIO()

    def two_factor(self):
        response.headers.pop("Location", None)
        with self.assertRaises(HTTP) as cm:
            self.auth.form_source.two_factor()
        return cm.exception.status, response.headers.get("Location")

    def test_counter(self):
        counter = self.auth.attempts
        self.assertEqual(counter.count("k"), 0)
        self.assertEqual(counter.hit("k", 60), 1)
        self.assertEqual(counter.hit("k", 60), 2)
        self.assertEqual(counter.count("k"), 2)
        self.assertEqual(counter.hit("other", 60), 1)
        counter.reset("k")
        self.assertEqual(counter.count("k"), 0)
        # expired entries do not count
        counter.hit("old", -1)
        self.assertEqual(counter.count("old"), 0)
        # keys are not stored in clear
        self.assertIsNone(self.db.auth_attempt(key_hash="k"))

    def test_max_tries_enforced_server_side(self):
        self.start()
        self.auth.form_source.two_factor()  # generates the code, renders form
        self.assertTrue(self.session.get("auth.2fa_code"))
        for _ in range(self.auth.param.two_factor_tries):
            self.auth.attempts.hit("2fa:1", 300)
        # even with a session claiming tries are left (replayed cookie)
        self.session["auth.2fa_tries_left"] = 3
        status, location = self.two_factor()
        self.assertEqual(status, 303)
        self.assertIn("/auth/login", location)
        self.assertIsNone(self.session.get("auth.2fa_user"))

    def test_code_expires(self):
        self.start()
        self.auth.form_source.two_factor()
        self.session["auth.2fa_expires"] = 1
        status, location = self.two_factor()
        self.assertEqual(status, 303)
        self.assertIn("/auth/login", location)
        self.assertIsNone(self.session.get("auth.2fa_code"))


class TestTokenUser(AuthTestBase):
    def test_token_user_not_stored_in_session(self):
        plugin = SimpleTokenPlugin(self.auth)
        self.auth.token_plugins.append(plugin)
        self.register()
        self.verify(1)
        token = plugin.table.insert(user_id=1, description="test")
        token = plugin.table[token].token
        request.environ["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        try:
            self.on_request()
            self.assertEqual(self.auth.user_id, 1)
            self.assertTrue(self.auth.is_logged_in)
            self.assertEqual(self.auth.get_user()["email"], USER["email"])
            self.assertIsNone(self.session.get("user"))
            self.assertFalse(self.session.local.changed)
        finally:
            request.environ.pop("HTTP_AUTHORIZATION", None)
        # without the token the next request is anonymous
        self.on_request()
        self.assertIsNone(self.auth.user_id)
        self.assertFalse(self.auth.is_logged_in)


class TestLoginHardening(AuthTestBase):
    def login(self, password, email=USER["email"]):
        self.on_request()
        return self.api("login", {"email": email, "password": password})

    def test_new_passwords_use_strong_hash(self):
        from py4web.utils.auth import PASSWORD_HASH_ALG

        self.register()
        self.assertTrue(self.db.auth_user[1].password.startswith(PASSWORD_HASH_ALG))

    def test_old_hash_is_upgraded_on_login(self):
        from pydal.validators import CRYPT

        from py4web.utils.auth import PASSWORD_HASH_ALG

        self.register()
        self.verify(1)
        old = str(CRYPT(digest_alg="pbkdf2(1000,20,sha512)")(USER["password"])[0])
        self.db(self.db.auth_user.id == 1).update(password=old)
        self.assertEqual(self.login(USER["password"])["status"], "success")
        self.assertTrue(self.db.auth_user[1].password.startswith(PASSWORD_HASH_ALG))
        self.assertEqual(self.login(USER["password"])["status"], "success")

    def test_login_throttled_per_account(self):
        self.register()
        self.verify(1)
        limit = self.auth.param.login_max_attempts
        for _ in range(limit):
            self.assertEqual(self.login("wrong")["message"], "Invalid Credentials")
        # even the right password is refused now
        res = self.login(USER["password"])
        self.assertEqual(res["message"], "Too many failed attempts, try again later")
        self.assertIsNone(self.auth.user_id)
        # other accounts are not affected
        self.assertEqual(
            self.login("x", email="other@example.com")["message"], "Invalid Credentials"
        )

    def test_success_resets_counter(self):
        self.register()
        self.verify(1)
        for _ in range(self.auth.param.login_max_attempts - 1):
            self.login("wrong")
        self.assertEqual(self.login(USER["password"])["status"], "success")
        self.assertEqual(self.login("wrong")["message"], "Invalid Credentials")
        self.assertEqual(self.login(USER["password"])["status"], "success")


if __name__ == "__main__":
    unittest.main()
