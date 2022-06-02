import io
import unittest
import time
import memcache
import subprocess
import pytest

from py4web import request, response, Session, DAL
from py4web.core import _before_request
from py4web.utils.dbstore import DBStore

def unquote(text):
    print(repr(text))
    if text[:1] + text[-1:] == '""':
        text = text[1:-1]
    return text

class TestSession(unittest.TestCase):
    def setUp(self):
        request.environ["wsgi.input"] = io.StringIO()
        _before_request()  # mimic before_request bottle-hook
        request.cookies.clear()
        response._cookies = ""

    def test_session(self):
        request.app_name = "myapp"
        session = Session(secret="a", expiration=10)
        context = dict(status=200)
        session.on_request(context)
        session["key"] = "value"
        cookie_name = session.local.session_cookie_name
        session.on_success(context)
        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        b = unquote(b)
        request.cookies[a] = b

        _before_request()
        with pytest.raises(RuntimeError) as err:
            session.local
        self.assertTrue("py4web hint" in str(err.value))

        session = Session(secret="b", expiration=10)
        request.cookies[a] = b
        context = dict(status=200)
        session.on_request(context)
        self.assertEqual(session.get("key"), None)

        session = Session(secret="a", expiration=10)
        request.cookies[a] = b
        session.on_request(context)
        self.assertEqual(session.get("key"), "value")

    def test_session_in_db(self):
        request.app_name = "myapp"
        db = DAL("sqlite:memory")
        session = Session(secret="a", expiration=10, storage=DBStore(db))
        request.cookies.clear()
        context = dict(status=200)
        session.on_request(context)
        session["key"] = "value"
        cookie_name = session.local.session_cookie_name
        session.on_success(context)
        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        b = unquote(b)
        request.cookies[a] = b

        _before_request()
        with pytest.raises(RuntimeError) as err:
            session.local
        self.assertTrue("py4web hint" in str(err.value))

        session = Session(expiration=10, storage=DBStore(db))
        request.cookies[a] = b
        context = dict(status=200)
        session.on_request(context)
        self.assertEqual(session.get("key"), "value")

        session = Session(expiration=10, storage=DBStore(db))
        request.cookies[a] = "wrong_cookie"
        context = dict(status=200)
        session.on_request(context)
        self.assertEqual(session.get("key"), None)

    def test_session_in_memcache(self):
        memcache_process = None
        try:
            memcache_process = subprocess.Popen(["memcached", "-p", "11211"])
            time.sleep(1)
            request.app_name = "myapp"
            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(secret="a", expiration=10, storage=conn)
            request.cookies.clear()
            context = dict(status=200)
            session.on_request(context)
            session["key"] = "value"
            cookie_name = session.local.session_cookie_name
            session.on_success(context)

            a, b = (
                str(response._cookies)[len("Set-Cookie: ") :]
                .split(";")[0]
                .split("=", 1)
            )
            b = unquote(b)
            request.cookies[a] = b

            _before_request()
            with pytest.raises(RuntimeError) as err:
                session.local
            self.assertTrue("py4web hint" in str(err.value))

            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(expiration=10, storage=conn)
            request.cookies[a] = b
            context = dict(status=200)
            session.on_request(context)
            self.assertEqual(session.get("key"), "value")

            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(expiration=10, storage=conn)
            request.cookies[a] = "wrong_cookie"
            context = dict(status=200)
            session.on_request(context)
            self.assertEqual(session.get("key"), None)
        finally:
            if memcache_process is None:
                print("memcached not availabl, test skipped")
            elif memcache_process:
                memcache_process.kill()
