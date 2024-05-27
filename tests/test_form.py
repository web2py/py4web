import io
import unittest
import uuid

from py4web import Field, Session, request, response
from py4web.utils.form import Form

SECRET = str(uuid.uuid4())


class FormTest(unittest.TestCase):
    def setUp(self):
        request.environ["wsgi.input"] = io.BytesIO()
        request.cookies.clear()
        response._cookies = ""

    def test_form(self):
        session = Session(secret=SECRET)
        session.on_request({})
        table = [Field("name")]
        form_name = "testing_form"
        f = Form(table, form_name=form_name, csrf_session=session)
        value = f.formkey
        post_vars = dict(_formname=form_name, _formkey=value)
        self.assertTrue(f._verify_form(post_vars))
        session.on_success({})
