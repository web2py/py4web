import unittest

from py4web import URL, request


class TestURL(unittest.TestCase):
    def test_url(self):
        request.app_name = "_default"
        self.assertEqual(URL("index"), "/index")
        request.app_name = "app"
        self.assertEqual(URL("index"), "/app/index")
        self.assertEqual(URL("a", "b", vars=dict(x=1), hash="y"), "/app/a/b?x=1#y")


if __name__ == "__main__":
    unittest.main()
