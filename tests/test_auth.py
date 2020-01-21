import os
import unittest
import bottle
from py4web.core import Session, DAL, request, HTTP
from py4web.utils.auth import Auth


class TestAuth(unittest.TestCase):
    def setUp(self):
        os.environ["PY4WEB_APPS_FOLDER"] = "apps"
        self.db = DAL("sqlite:memory")
        self.session = Session(secret="a", expiration=10)
        self.session.local.data = {}
        self.auth = Auth(self.session, self.db, define_tables=True)
        self.auth.enable()
        request.app_name = "_scaffold"

    def test_register_invalid(self):
        body = {"email": "pinco.pallino@example.com"}
        self.assertEqual(
            self.auth.action("api/register", "POST", {}, body),
            {
                "id": None,
                "errors": {
                    "username": "Enter a value",
                    "password": "Too short",
                    "first_name": "Enter a value",
                    "last_name": "Enter a value",
                },
                "status": "error",
                "message": "validation errors",
                "code": 401,
            },
        )

    def test_register(self):
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

        body = {"email": "pinco.pallino@example.com", "password": "1234567"}
        self.assertTrue(
            self.auth.action("api/login", "POST", {}, body),
            {"status": "error", "message": "Registration is pending", "code": 400},
        )

        token = user.action_token[len("pending-registration") + 1 :]
        try:
            self.auth.action("verify_email", "GET", {"token": token}, {})
            assert False, "email not verified"
        except HTTP:
            pass
        user = self.db.auth_user[1]
        self.assertTrue(user.action_token == None)

        self.assertEqual(
            self.auth.action("api/login", "POST", {}, body),
            {"status": "error", "message": "Invalid Credentials", "code": 400},
        )

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

        body = {"email": "pinco.pallino@example.com"}
        self.assertEqual(
            self.auth.action("api/request_reset_password", "POST", {}, body),
            {"status": "success", "code": 200},
        )

        body = {"token": "junk", "new_password": "987654321"}
        self.assertTrue(
            self.auth.action("api/reset_password", "POST", {}, body),
            {
                "status": "error",
                "message": "invalid token, request expired",
                "code": 400,
            },
        )

        body = {
            "token": self.auth._link.split("?token=")[1],
            "new_password": "987654321",
        }
        self.assertTrue(
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

        body = {}
        self.assertEqual(
            self.auth.action("api/change_password", "POST", {}, body),
            {
                "errors": {"password": "invalid"},
                "status": "error",
                "message": "validation errors",
                "code": 401,
            },
        )
        body = {"password": "987654321", "new_password": "432187659"}
        self.assertEqual(
            self.auth.action("api/change_password", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )
        body = {"password": "432187659", "new_email": "somebody@example.com"}
        self.assertEqual(
            self.auth.action("api/change_email", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )
        body = {"first_name": "Max", "last_name": "Powers", "password": "xyz"}
        self.assertEqual(
            self.auth.action("api/profile", "POST", {}, body),
            {
                "errors": {"password": "invalid"},
                "status": "error",
                "message": "validation errors",
                "code": 401,
            },
        )

        body = {"first_name": "Max", "last_name": "Powers"}
        self.assertEqual(
            self.auth.action("api/profile", "POST", {}, body),
            {"updated": 1, "status": "success", "code": 200},
        )


if __name__ == "__main__":
    unittest.main()
