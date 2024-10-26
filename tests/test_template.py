import os
import unittest

from py4web.core import Template

PATH = os.path.join(os.path.dirname(__file__), "templates")


class TemplateTest(unittest.TestCase):
    def test_template(self):
        t = Template("index.html", path=PATH)
        context = dict(output=dict(n=3))
        t.on_success(context)
        output = context["output"]
        self.assertEqual(output, "0,1,2.\n")
