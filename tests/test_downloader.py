import io
import os
import shutil
import tempfile
import unittest

from py4web import DAL, Field, request, response
from py4web.utils.downloader import downloader


class DownloaderTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp()
        self.db = DAL("sqlite:memory")
        self.db.define_table(
            "thing", Field("file", "upload", uploadfolder=self.folder)
        )
        request.environ["QUERY_STRING"] = ""
        request.environ.pop("ombott.request.query", None)
        request.environ["REQUEST_METHOD"] = "GET"
        response.headers.clear()

    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.folder)

    def store(self, name, content=b"<script>alert(1)</script>"):
        return self.db.thing.file.store(io.BytesIO(content), name)

    def get(self, filename):
        return downloader(self.db, self.folder, filename)

    def test_html_is_attachment(self):
        res = self.get(self.store("x.html"))
        self.assertTrue(res.headers["Content-Disposition"].startswith("attachment"))
        self.assertEqual(res.headers["X-Content-Type-Options"], "nosniff")
        self.assertIn("sandbox", res.headers["Content-Security-Policy"])

    def test_svg_is_attachment(self):
        res = self.get(self.store("x.svg"))
        self.assertTrue(res.headers["Content-Disposition"].startswith("attachment"))

    def test_image_is_inline(self):
        res = self.get(self.store("x.png", b"\x89PNG"))
        self.assertNotIn("Content-Disposition", res.headers)
        self.assertEqual(res.headers["X-Content-Type-Options"], "nosniff")


if __name__ == "__main__":
    unittest.main()
