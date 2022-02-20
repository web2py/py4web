import io
import os
import unittest
from py4web import request, response, Field, Session
from py4web.utils.form import Form


class FormTest(unittest.TestCase):
    def setUp(self):
        request.environ["wsgi.input"] = io.BytesIO()
        request.cookies.clear()
        response._cookies = ""

    def test_form(self):
        session = Session()
        session.initialize()
        table = [Field("name")]
        form_name = "testing_form"
        f = Form(table, form_name=form_name, csrf_session=session)
        value = f.formkey
        post_vars = dict(_formname=form_name, _formkey=value)
        self.assertTrue(f._verify_form(post_vars))
