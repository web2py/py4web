# pylint: disable=assignment-from-none
import copy
import multiprocessing
import os
import threading
import time
import unittest
import uuid

import mechanize
import requests

from py4web import DAL, HTTP, Cache, Condition, Field, Session, abort, action
from py4web.core import Fixture, bottle, error404, request

os.environ["PY4WEB_APPS_FOLDER"] = os.path.sep.join(
    os.path.normpath(__file__).split(os.path.sep)[:-2]
)

SECRET = str(uuid.uuid4())
db = DAL("sqlite://storage_%s" % uuid.uuid4(), folder="/tmp/")
db.define_table("thing", Field("name"))
session = Session(secret=SECRET)
cache = Cache()

action.app_name = "tests"


@action("index")
@cache.memoize(expiration=1)
@action.uses(db, session)
@action.uses(Condition(lambda: True))
def index():
    new_id = db.thing.insert(name="test")
    session["number"] = session.get("number", 0) + 1

    # test copying Field ThreadSafe attr
    db.thing.name.default = "test_clone"
    return "ok %s %s %s" % (session["number"], db(db.thing).count(), new_id)


def fail():
    raise HTTP(404)


@action("conditional")
@action.uses(Condition(lambda: False, on_false=fail))
def conditional():
    return "OK"


@action("raise300")
def raise300():
    raise HTTP(300)


@action("bottle_httpresponse")
def bottle_httpresponse():
    return bottle.HTTPResponse(status=200, body="ok")


@action("abort")
def abort_response():
    abort(400)


class Corrector(Fixture):
    def on_error(self, context):
        print(context)
        context["exception"] = None
        context["output"] = "caught"


corrector = Corrector()


@action("abort_caught")
@action.uses(corrector)
def abort_response_corrected():
    abort(400)


def run_server():
    bottle.run(host="localhost", port=8001)


class FieldTest(unittest.TestCase):
    """Check that we chat we can safely clone Field(s)"""

    def test_fiel_clone(self):
        def test():
            db.thing.name.default = "test"
            field_clone = copy.copy(db.thing.name)
            assert field_clone.default == db.thing.name.default == "test"

        thread = threading.Thread(target=test)
        thread.start()
        thread.join()


class CacheAction(unittest.TestCase):
    def setUp(self):
        self.server = multiprocessing.Process(target=run_server)
        self.server.start()
        self.browser = mechanize.Browser()
        time.sleep(3)

    def tearDown(self):
        self.server.terminate()

    def test_action(self):
        res = self.browser.open("http://127.0.0.1:8001/tests/index")
        self.assertEqual(res.read(), b"ok 1 1 1")

        res = self.browser.open("http://127.0.0.1:8001/tests/index")
        self.assertEqual(res.read(), b"ok 1 1 1")

        time.sleep(2)

        res = self.browser.open("http://127.0.0.1:8001/tests/index")
        self.assertEqual(res.read(), b"ok 2 2 2")

    def test_error(self):
        res = requests.get("http://127.0.0.1:8001/tests/conditional", timeout=5)
        self.assertEqual(res.status_code, 404)

        res = requests.get("http://127.0.0.1:8001/tests/raise300", timeout=5)
        self.assertEqual(res.status_code, 300)

        res = requests.get("http://127.0.0.1:8001/tests/abort", timeout=5)
        self.assertEqual(res.status_code, 400)

        res = requests.get("http://127.0.0.1:8001/tests/abort_caught", timeout=5)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content, b"caught")

        res = requests.get("http://127.0.0.1:8001/tests/bottle_httpresponse", timeout=5)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content, b"ok")

    def test_local(self):
        # for test coverage
        request.app_name = "example"
        index()

    def test_error_page(self):
        request.path = "hello/world"
        self.assertTrue("NOT FOUND" in error404("oops"))
