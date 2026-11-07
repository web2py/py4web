import io
import os
import unittest
import uuid

from py4web.core import DAL, Fixture, Session, bottle, request, safely
from py4web.utils.auth import Auth, AuthAPI

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


if __name__ == "__main__":
    unittest.main()
