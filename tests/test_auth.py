import io
import os
import unittest
import uuid

from py4web.core import DAL, HTTP, Field, Fixture, Session, bottle, request, safely
from py4web.utils.auth import Auth, AuthAPI

SECRET = str(uuid.uuid4())


class TestAuth(unittest.TestCase):
    def setUp(self):
        os.environ["PY4WEB_APPS_FOLDER"] = "apps"
        self.db = DAL("sqlite:memory")
        self.session = Session(secret=SECRET, expiration=10)
        self.auth = Auth(
            self.session, self.db, define_tables=True, password_complexity=None
        )
        self.auth.enable()
        self.auth.action = self.action
        request.app_name = "_scaffold"

    def tearDown(self):
        # this is normally done by @action
        safely(lambda: Fixture.local_delete(self.session))
        bottle.app.router.remove("/*")

    def action(self, name, method, query, data):
        request.environ["REQUEST_METHOD"] = method
        request.environ["ombott.request.query"] = query
        request.environ["ombott.request.json"] = data
        request.environ["wsgi.input"] = io.BytesIO()
        # we break a symmetry below. should fix in auth.py
        if name.startswith("api/"):
            return getattr(AuthAPI, name[4:])(self.auth)
        return getattr(self.auth.form_source, name)()

    def on_request(self, context=None, keep_session=False):
        # store the current session
        context = context or {}
        try:
            storage = self.session.local.__dict__
        except RuntimeError:
            storage = None
        # reinitialize everything
        safely(lambda: Fixture.local_delete(self.session))
        safely(lambda: Fixture.local_delete(self.auth.flash))
        self.session.on_request(context)
        self.auth.flash.on_request(context)
        self.auth.on_request(context)
        # restore the previous session
        if keep_session and storage:
            self.session.local.__dict__.update(storage)

    def test_extra_fields(self):
        db = DAL("sqlite:memory")
        self.auth = Auth(
            self.session, db, define_tables=True, extra_fields=[Field("favorite_color")]
        )
        self.on_request()
        self.assertEqual(type(db.auth_user.favorite_color), Field)

    def test_register_invalid(self):
        self.on_request()
        body = {"email": "pinco.pallino@example.com"}
        res = self.auth.action("api/register", "POST", {}, body)
        self.assertEqual(
            res,
            {
                "id": None,
                "errors": {
                    "username": "required",
                    "password": "required",
                    "first_name": "required",
                    "last_name": "required",
                },
                "status": "error",
                "message": "validation errors",
                "code": 401,
            },
        )

    def test_register(self):
        self.on_request()
        body = {
            "username": "ppallino",
            "email": "pinco.pallino@example.com",
            "password": "123456789",
            "first_name": "Pinco",
            "last_name": "Pallino",
        }
        self.assertEqual(
            self.auth.action("api/register", "POST", {}, body),
            {"id": 1, "status": "success", "code": 200},
        )
        user = self.db.auth_user[1]
        self.assertTrue(user.action_token.startswith("pending-registration"))
        self.assertEqual(self.auth.get_user(), {})

        self.on_request()
        body = {"email": "pinco.pallino@example.com", "password": "1234567"}
        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {"status": "error", "message": "Invalid Credentials", "code": 400},
        )

        self.on_request()
        body = {"email": "pinco.pallino@example.com", "password": "123456789"}
        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {"status": "error", "message": "Registration is pending", "code": 400},
        )

        self.on_request()
        token = user.action_token[len("pending-registration") + 1 :]
        try:
            self.auth.action("verify_email", "GET", {"token": token}, {})
            assert False, "email not verified"
        except HTTP:
            pass
        user = self.db.auth_user[1]
        self.assertTrue(user.action_token is None)

        self.on_request()
        body = {"email": "pinco.pallino@example.com", "password": "1234567"}
        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {"status": "error", "message": "Invalid Credentials", "code": 400},
        )

        self.on_request()
        body = {"email": "pinco.pallino@example.com", "password": "123456789"}
        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {
                "user": {
                    "id": 1,
                    "username": "ppallino",
                    "email": "pinco.pallino@example.com",
                    "first_name": "Pinco",
                    "last_name": "Pallino",
                },
                "status": "success",
                "code": 200,
            },
        )

        self.on_request()
        body = {
            "email": "ppallino",  # can login with both email and username
            "password": "123456789",
        }
        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {
                "user": {
                    "id": 1,
                    "username": "ppallino",
                    "email": "pinco.pallino@example.com",
                    "first_name": "Pinco",
                    "last_name": "Pallino",
                },
                "status": "success",
                "code": 200,
            },
        )

        self.on_request(keep_session=True)
        body = {"email": "pinco.pallino@example.com"}
        self.assertEqual(
            self.auth.action("api/request_reset_password", "POST", {}, body),
            {"status": "success", "code": 200},
        )

        self.on_request(keep_session=True)
        body = {"token": "junk", "new_password": "987654321"}
        self.assertEqual(
            self.auth.action("api/reset_password", "POST", {}, body),
            {
                "status": "error",
                "message": "validation errors",
                "errors": {"token": "invalid token"},
                "code": 401,
            },
        )

        self.on_request(keep_session=True)
        body = {
            "token": self.auth._link.split("?token=")[1],
            "new_password": "987654321",
            "new_password2": "987654321",
        }
        self.assertEqual(
            self.auth.action("api/reset_password", "POST", {}, body),
            {"status": "success", "code": 200},
        )

        self.assertEqual(
            self.auth.get_user(),
            {
                "id": 1,
                "username": "ppallino",
                "email": "pinco.pallino@example.com",
                "first_name": "Pinco",
                "last_name": "Pallino",
            },
        )

        self.on_request(keep_session=True)
        body = {}
        self.assertEqual(
            self.auth.action("api/change_password", "POST", {}, body),
            {
                "errors": {"old_password": "invalid current password"},
                "status": "error",
                "message": "validation errors",
                "code": 401,
            },
        )

        self.on_request(keep_session=True)
        body = {"old_password": "987654321", "new_password": "432187659"}
        self.assertEqual(
            self.auth.action("api/change_password", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )

        self.on_request(keep_session=True)
        body = {"password": "432187659", "new_email": "somebody@example.com"}
        self.assertEqual(
            self.auth.action("api/change_email", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )

        self.on_request(keep_session=True)
        body = {"first_name": "Max", "last_name": "Powers"}
        self.assertEqual(
            self.auth.action("api/profile", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )


if __name__ == "__main__":
    unittest.main()
