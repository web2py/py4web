import contextlib
import io
import subprocess
import time
import unittest
import uuid

import memcache
import pytest

from py4web import DAL, Session, request, response
from py4web.core import Fixture
from py4web.utils.dbstore import DBStore


def unquote(text):
    print(repr(text))
    if text[:1] + text[-1:] == '""':
        text = text[1:-1]
    return text


secret1 = str(uuid.uuid4())
secret2 = str(uuid.uuid4())


@contextlib.contextmanager
def request_context(session, context={}):
    try:
        request.environ["wsgi.input"] = io.StringIO()
        response._cookies = ""
        yield session.on_request(context)
        session.on_success(context)
    finally:
        session.on_error(context)
        Fixture.local_delete(session)


class TestSession(unittest.TestCase):
    def test_session(self):
        request.app_name = "myapp"
        session = Session(secret=secret1, expiration=10)

        with request_context(session):
            session["key"] = "value"
            assert "key" in session.local.data

        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        b = unquote(b)
        request.cookies[a] = b

        session = Session(secret=secret2, expiration=10)
        request.cookies[a] = b
        with request_context(session):
            self.assertEqual(session.get("key"), None)

        session = Session(secret=secret1, expiration=10)
        request.cookies[a] = b
        with request_context(session):
            self.assertEqual(session.get("key"), "value")

    def test_session_token_sources(self):
        request.app_name = "myapp"
        session = Session(secret=secret1, expiration=10)
        with request_context(session):
            session["key"] = "value"
        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        token = unquote(b)
        request.cookies.clear()
        try:
            # a token in the request body is ignored (login CSRF)
            request.environ["REQUEST_METHOD"] = "POST"
            request.environ["ombott.request.json"] = {"_session_token": token}
            session = Session(secret=secret1, expiration=10)
            with request_context(session):
                self.assertEqual(session.get("key"), None)
            # a token in the X-Session-Token header is accepted
            request.environ["HTTP_X_SESSION_TOKEN"] = token
            session = Session(secret=secret1, expiration=10)
            with request_context(session):
                self.assertEqual(session.get("key"), "value")
        finally:
            request.environ["REQUEST_METHOD"] = "GET"
            request.environ.pop("ombott.request.json", None)
            request.environ.pop("HTTP_X_SESSION_TOKEN", None)

    def test_session_as_attributes(self):
        request.app_name = "myapp"
        session = Session(secret=secret1, expiration=10)

        with request_context(session):
            session.key = "value"
            assert "key" in session.local.data

        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        b = unquote(b)
        request.cookies[a] = b

        session = Session(secret=secret2, expiration=10)
        request.cookies[a] = b
        with request_context(session):
            self.assertEqual(session.key, None)

        session = Session(secret=secret1, expiration=10)
        request.cookies[a] = b
        with request_context(session):
            self.assertEqual(session.key, "value")

    def test_session_not_initialized(self):
        request.app_name = "myapp"
        session = Session(secret=secret1, expiration=10)

        with pytest.raises(RuntimeError) as err:
            session.local
        self.assertTrue("not initialized" in str(err.value))

    def test_session_in_db(self):
        request.app_name = "myapp"
        db = DAL("sqlite:memory")
        session = Session(secret=secret1, expiration=10, storage=DBStore(db))
        with request_context(session):
            session["key"] = "value"
        a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split("=", 1)
        b = unquote(b)
        request.cookies[a] = b

        with pytest.raises(RuntimeError) as err:
            session.local
        self.assertTrue("not initialized" in str(err.value))

        session = Session(expiration=10, storage=DBStore(db))
        request.cookies[a] = b
        with request_context(session):
            self.assertEqual(session.get("key"), "value")

        session = Session(expiration=10, storage=DBStore(db))
        request.cookies[a] = "wrong_cookie"
        with request_context(session):
            self.assertEqual(session.get("key"), None)

    def test_session_rotation_invalidates_old_id(self):
        request.app_name = "myapp"
        db = DAL("sqlite:memory")

        def cookie():
            a, b = str(response._cookies)[len("Set-Cookie: ") :].split(";")[0].split(
                "=", 1
            )
            return a, unquote(b)

        session = Session(secret=secret1, expiration=10, storage=DBStore(db))
        with request_context(session):
            session["key"] = "value"
        name, old_id = cookie()
        # e.g. login: the session id is rotated
        request.cookies[name] = old_id
        with request_context(session):
            self.assertEqual(session.get("key"), "value")
            session["uuid"] = "new-session-id"
        self.assertEqual(cookie()[1], "new-session-id")
        # the old id no longer loads the session
        request.cookies[name] = old_id
        with request_context(session):
            self.assertEqual(session.get("key"), None)
        # the new one does
        request.cookies[name] = "new-session-id"
        with request_context(session):
            self.assertEqual(session.get("key"), "value")
        request.cookies.clear()

    def test_session_in_memcache(self):
        memcache_process = None
        try:
            memcache_process = subprocess.Popen(["memcached", "-p", "11211"])
        except:
            print("No memcached")
            return
        try:
            time.sleep(1)
            request.app_name = "myapp"
            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(secret=secret1, expiration=10, storage=conn)
            request.cookies.clear()
            with request_context(session):
                session["key"] = "value"

            a, b = (
                str(response._cookies)[len("Set-Cookie: ") :]
                .split(";")[0]
                .split("=", 1)
            )
            b = unquote(b)
            request.cookies[a] = b

            with pytest.raises(RuntimeError) as err:
                session.local
            self.assertTrue("not initialized" in str(err.value))

            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(expiration=10, storage=conn)
            request.cookies[a] = b
            with request_context(session):
                self.assertEqual(session.get("key"), "value")

            conn = memcache.Client(["127.0.0.1:11211"], debug=0)
            session = Session(expiration=10, storage=conn)
            request.cookies[a] = "wrong_cookie"

            with request_context(session):
                self.assertEqual(session.get("key"), None)
        finally:
            if memcache_process is None:
                print("memcached not availabl, test skipped")
            elif memcache_process:
                memcache_process.kill()
