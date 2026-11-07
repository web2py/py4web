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
        for key in ("ombott.request.query", "ombott.request.forms",
                    "ombott.request.post", "ombott.request.params"):
            request.environ.pop(key, None)
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


if __name__ == "__main__":
    unittest.main()
