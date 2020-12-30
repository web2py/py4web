import os
import unittest
from py4web import response, Field
from py4web.utils.form import Form


class FormTest(unittest.TestCase):
    def test_form(self):
        table = [Field("name")]
        form_name = 'testing_form'
        f = Form(table,form_name=form_name)
        value = f.formkey
        post_vars = dict(_formname=form_name, _form_key=value)
        self.assertTrue(f._verify_form(post_vars))
