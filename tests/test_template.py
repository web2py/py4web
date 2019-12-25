import os
import unittest
from py4web.core import Template, request

PATH = os.path.join(os.path.dirname(__file__), "templates")


class TemplateTest(unittest.TestCase):
    def test_template(self):
        t = Template("index.html", path=PATH)
        output = t.transform(dict(n=3))
        self.assertEqual(output, "0,1,2.\n")
