import io
import unittest
import uuid

from py4web import Field, Session, request, response
from py4web.utils.form import Form

SECRET = str(uuid.uuid4())


class FormTest(unittest.TestCase):
    def setUp(self):
        request.environ["wsgi.input"] = io.BytesIO()
        request.app_name = "app"
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


class FormProcessTest(unittest.TestCase):
    def setUp(self):
        from py4web import DAL

        self.db = DAL("sqlite:memory")
        self.db.define_table("cars", Field("car_make"), format="%(car_make)s")
        self.db.define_table(
            "owner",
            Field("name"),
            Field("cars", "list:reference cars"),
            Field("secret", writable=False, default="s"),
        )
        self.db.cars.insert(car_make="Fiat")
        self.db.cars.insert(car_make="BMW")
        request.app_name = "app"
        request.cookies.clear()
        response._cookies = ""

    def tearDown(self):
        self.db.close()

    def post(self, body, **kwargs):
        from urllib.parse import urlencode

        for key in list(request.environ):
            if key.startswith("ombott.request.") and key not in (
                "ombott.request.cookies",
                "ombott.request.ext.app_name",
            ):
                del request.environ[key]
        session = Session(secret=SECRET)
        session.on_request({})
        form = Form(self.db.owner, csrf_session=session, form_name="f", **kwargs)
        data = urlencode(
            list(body) + [("_formname", "f"), ("_formkey", form.formkey)]
        ).encode()
        request.environ.update(
            {
                "REQUEST_METHOD": "POST",
                "wsgi.input": io.BytesIO(data),
                "CONTENT_LENGTH": str(len(data)),
                "CONTENT_TYPE": "application/x-www-form-urlencoded",
            }
        )
        for key in list(request.environ):
            if key.startswith("ombott.request.") and key not in (
                "ombott.request.cookies",
                "ombott.request.ext.app_name",
            ):
                del request.environ[key]
        return Form(self.db.owner, csrf_session=session, form_name="f", **kwargs)

    def test_hidden_fields_are_in_form_vars(self):
        form = self.post([("name", "Max"), ("extra", "42")], hidden=dict(extra=42))
        self.assertTrue(form.accepted)
        self.assertEqual(form.vars["extra"], "42")
        self.assertEqual(form.vars["name"], "Max")

    def test_posted_vars_do_not_write_readonly_fields(self):
        form = self.post([("name", "Max"), ("secret", "hacked")])
        self.assertTrue(form.accepted)
        self.assertEqual(self.db.owner(form.vars["id"]).secret, "s")

    def test_validation_callback_can_set_fields(self):
        def validation(form):
            form.vars["name"] = form.vars["name"].upper()
            form.vars["secret"] = "set by server"

        form = self.post([("name", "max")], validation=validation)
        row = self.db.owner(form.vars["id"])
        self.assertEqual((row.name, row.secret), ("MAX", "set by server"))

    def test_list_reference_is_a_multiple_select(self):
        html = str(Form(self.db.owner, csrf_protection=False))
        self.assertIn('multiple="multiple"', html)
        self.assertIn(">BMW</option>", html)
        form = self.post([("name", "Max"), ("cars", "1"), ("cars", "2")])
        self.assertTrue(form.accepted)
        self.assertEqual(self.db.owner(form.vars["id"]).cars, [1, 2])
        form = self.post([("name", "Max"), ("cars", "2")])
        self.assertTrue(form.accepted, form.errors)
        self.assertEqual(self.db.owner(form.vars["id"]).cars, [2])
