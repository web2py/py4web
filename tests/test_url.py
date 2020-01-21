import random
import time
import unittest

from py4web import request, URL


class TestURL(unittest.TestCase):
    def test_url(self):
        request.app_name = "_default"
        self.assertEqual(URL("index"), "/index")
        request.app_name = "app"
        self.assertEqual(URL("index"), "/app/index")
        self.assertEqual(URL("a", "b", vars=dict(x=1), hash="y"), "/app/a/b?x=1#y")
