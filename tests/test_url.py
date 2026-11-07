import unittest

from py4web import URL, request


class TestURL(unittest.TestCase):
    def test_url(self):
        request.app_name = "_default"
        self.assertEqual(URL("index"), "/index")
        request.app_name = "app"
        self.assertEqual(URL("index"), "/app/index")
        self.assertEqual(URL("a", "b", vars=dict(x=1), hash="y"), "/app/a/b?x=1#y")

    def test_x_script_name(self):
        request.app_name = "app"
        env = request.environ
        old = {k: env.get(k) for k in ("SCRIPT_NAME", "HTTP_X_SCRIPT_NAME")}
        try:
            env["SCRIPT_NAME"] = ""
            env["HTTP_X_SCRIPT_NAME"] = "/prefix"
            self.assertEqual(URL("index"), "/prefix/app/index")
            # a header that would change the host of absolute urls is ignored
            env["HTTP_X_SCRIPT_NAME"] = "@evil.com"
            self.assertEqual(URL("index"), "/app/index")
            env["HTTP_X_SCRIPT_NAME"] = "//evil.com"
            self.assertEqual(URL("index"), "/app/index")
        finally:
            for k, v in old.items():
                if v is None:
                    env.pop(k, None)
                else:
                    env[k] = v


if __name__ == "__main__":
    unittest.main()
