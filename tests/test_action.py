import copy
import multiprocessing
import os
import time
import unittest
import uuid

import mechanize

from py4web import action, DAL, Field, Session, Cache
from py4web.core import bottle, request, error404

os.environ["PY4WEB_APPS_FOLDER"] = os.path.sep.join(
    os.path.normpath(__file__).split(os.path.sep)[:-2]
)

db = DAL("sqlite://storage_%s" % uuid.uuid4(), folder="/tmp/")
db.define_table("thing", Field("name"))
session = Session(secret="my secret")
cache = Cache()

action.app_name = "tests"


@action("index")
@cache.memoize(expiration=1)
@action.uses(db, session)
@action.requires(lambda: True)
def index():
    db.thing.insert(name="test")
    session["number"] = session.get("number", 0) + 1

    # test copying Field ThreadSafe attr
    db.thing.name.default = "test_clone"
    field_clone = copy.copy(db.thing.name)
    clone_ok = 1 if field_clone.default == db.thing.name.default == "test_clone" else 0
    return "ok %s %s %s" % (session["number"], db(db.thing).count(), clone_ok)


def run_server():
    bottle.run(host="localhost", port=8001)


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
        self.assertEqual(res.read(), b"ok 2 2 1")

    def test_local(self):
        # for test coverage
        Session.__init_request_ctx__()  # mimic before_request-hook
        index()

    def test_error_page(self):
        request.path = "hello/world"
        self.assertTrue("NOT FOUND" in error404("oops"))
