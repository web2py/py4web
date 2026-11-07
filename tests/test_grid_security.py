import io
import unittest

from py4web import DAL, HTTP, Field, request, response
from py4web.utils.grid import Grid


class GridSecurityTest(unittest.TestCase):
    def setUp(self):
        self.db = DAL("sqlite:memory")
        self.db.define_table("thing", Field("name"), Field("owner", "integer"))
        self.db.thing.insert(name="mine", owner=1)
        self.db.thing.insert(name="theirs", owner=2)
        request.app_name = "app"
        request.cookies.clear()
        response._cookies = ""

    def tearDown(self):
        self.db.close()

    def make_grid(self, query, method="GET", post=None, **kwargs):
        request.environ["REQUEST_METHOD"] = method
        request.environ["PATH_INFO"] = "/app/grid"
        request.environ["QUERY_STRING"] = "&".join(
            f"{k}={v}" for k, v in query.items()
        )
        # drop what ombott cached from the previous simulated request
        for key in list(request.environ):
            if key.startswith("ombott.request.") and key not in (
                "ombott.request.cookies",
                "ombott.request.ext.app_name",
            ):
                del request.environ[key]
        body = "&".join(f"{k}={v}" for k, v in (post or {}).items()).encode()
        request.environ["wsgi.input"] = io.BytesIO(body)
        request.environ["CONTENT_LENGTH"] = str(len(body))
        request.environ["CONTENT_TYPE"] = "application/x-www-form-urlencoded"
        return Grid(self.db.thing.owner == 1, **kwargs)

    def assertRedirects(self, func):
        with self.assertRaises(HTTP) as cm:
            func()
        self.assertEqual(cm.exception.status, 303)

    def test_details_own_record(self):
        grid = self.make_grid({"mode": "details", "id": 1})
        self.assertEqual(grid.record.name, "mine")

    def test_cannot_access_record_outside_query(self):
        for mode in ("details", "edit", "delete"):
            self.assertRedirects(
                lambda: self.make_grid({"mode": mode, "id": 2})
            )

    def test_cannot_delete_record_outside_query(self):
        self.assertRedirects(
            lambda: self.make_grid({"mode": "delete", "id": 2}, method="POST", post={})
        )
        self.assertIsNotNone(self.db.thing(2))

    def test_invalid_id(self):
        self.assertRedirects(lambda: self.make_grid({"mode": "details", "id": "x"}))

    def test_delete_requires_formkey(self):
        with self.assertRaises(HTTP) as cm:
            self.make_grid({"mode": "delete", "id": 1}, method="POST", post={})
        self.assertEqual(cm.exception.status, 403)
        self.assertIsNotNone(self.db.thing(1))

    def test_delete_with_formkey(self):
        grid = self.make_grid({"mode": "delete", "id": 1})
        post = {"_formname": grid.form.form_name, "_formkey": grid.form.formkey}
        # the cookie with the signing key is sent back by the browser
        request.cookies["_formkey"] = response._cookies["_formkey"].value
        self.assertRedirects(
            lambda: self.make_grid({"mode": "delete", "id": 1}, method="POST", post=post)
        )
        self.assertIsNone(self.db.thing(1))

    def test_referrer(self):
        from py4web.utils.grid import safe_referrer

        request.environ["HTTP_HOST"] = "example.com"
        self.assertEqual(safe_referrer("/app/grid?page=2"), "/app/grid?page=2")
        self.assertEqual(
            safe_referrer("http://example.com/app/grid"), "http://example.com/app/grid"
        )
        for bad in [
            "javascript:alert(1)",
            "https://evil.com/",
            "//evil.com",
            "/\\evil.com",
            "/\t/evil.com",
            "data:text/html,x",
        ]:
            self.assertIsNone(safe_referrer(bad), bad)

    def test_bad_referrer_ignored(self):
        import base64

        ref = base64.b16encode(b"javascript:alert(1)").decode()
        grid = self.make_grid({"mode": "details", "id": 1, "referrer": ref})
        self.assertIsNone(grid.referrer)
        grid = self.make_grid({"mode": "details", "id": 1, "referrer": "zz"})
        self.assertIsNone(grid.referrer)


if __name__ == "__main__":
    unittest.main()
