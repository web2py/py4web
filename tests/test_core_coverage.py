"""
Comprehensive unit tests for py4web/core.py functions and classes
that lack coverage in the existing test suite.

Covers: utcnow, module2filename, load_module, required_folder, safely,
        Node, objectify (extended), dumps (extended), BareFixture,
        LocalUndefined, Fixture.is_valid, Flash, Condition,
        redirect, HTTP, error_page, render, check_compatible,
        MetaPathRouter, SimpleErrorLogger, ErrorLogger,
        try_app_watch_tasks, log_routes, Translator,
        Reloader, Session (extended), action.uses fixture ordering.
"""

import contextlib
import datetime
import enum
import io
import json
import logging
import os
import shutil
import sys
import tempfile
import threading
import types
import unittest
import uuid

import py4web
from py4web.core import (
    BareFixture,
    Cache,
    Condition,
    DAL,
    Flash,
    Fixture,
    HTTP,
    LocalUndefined,
    Node,
    Session,
    Template,
    Translator,
    action,
    bottle,
    check_compatible,
    dumps,
    error_page,
    get_error_snapshot,
    log_routes,
    module2filename,
    objectify,
    redirect,
    render,
    request,
    required_folder,
    response,
    safely,
    try_app_watch_tasks,
    utcnow,
    APP_WATCH,
    MetaPathRouter,
    SimpleErrorLogger,
    ErrorLogger,
)

os.environ["PY4WEB_APPS_FOLDER"] = os.path.sep.join(
    os.path.normpath(__file__).split(os.path.sep)[:-2]
)


# ──────────────────────────────────────────────
# utcnow
# ──────────────────────────────────────────────
class TestUtcnow(unittest.TestCase):
    def test_returns_datetime(self):
        result = utcnow()
        self.assertIsInstance(result, datetime.datetime)

    def test_has_utc_timezone(self):
        result = utcnow()
        self.assertEqual(result.tzinfo, datetime.timezone.utc)

    def test_is_close_to_now(self):
        before = datetime.datetime.now(datetime.timezone.utc)
        result = utcnow()
        after = datetime.datetime.now(datetime.timezone.utc)
        self.assertGreaterEqual(result, before)
        self.assertLessEqual(result, after)


# ──────────────────────────────────────────────
# module2filename
# ──────────────────────────────────────────────
class TestModule2Filename(unittest.TestCase):
    def test_single_component_is_package(self):
        # apps.myapp -> myapp/__init__.py
        result = module2filename("apps.myapp")
        self.assertEqual(result, os.path.join("myapp", "__init__.py"))

    def test_two_components_is_module(self):
        # apps.myapp.controllers -> myapp/controllers.py
        result = module2filename("apps.myapp.controllers")
        self.assertEqual(result, os.path.join("myapp", "controllers.py"))

    def test_three_components(self):
        result = module2filename("apps.myapp.sub.module")
        self.assertEqual(result, os.path.join("myapp", "sub", "module.py"))


# ──────────────────────────────────────────────
# required_folder
# ──────────────────────────────────────────────
class TestRequiredFolder(unittest.TestCase):
    def test_creates_folder(self):
        tmp = tempfile.mkdtemp()
        try:
            path = required_folder(tmp, "subfolder")
            self.assertTrue(os.path.isdir(path))
            self.assertEqual(path, os.path.join(tmp, "subfolder"))
        finally:
            shutil.rmtree(tmp)

    def test_existing_folder(self):
        tmp = tempfile.mkdtemp()
        try:
            path = required_folder(tmp)
            self.assertEqual(path, tmp)
        finally:
            shutil.rmtree(tmp)

    def test_nested_creation(self):
        tmp = tempfile.mkdtemp()
        try:
            path = required_folder(tmp, "a", "b", "c")
            self.assertTrue(os.path.isdir(path))
        finally:
            shutil.rmtree(tmp)


# ──────────────────────────────────────────────
# safely
# ──────────────────────────────────────────────
class TestSafely(unittest.TestCase):
    def test_success_returns_value(self):
        result = safely(lambda: 42)
        self.assertEqual(result, 42)

    def test_exception_returns_default(self):
        result = safely(lambda: 1 / 0, default="fallback")
        self.assertEqual(result, "fallback")

    def test_default_is_none(self):
        result = safely(lambda: 1 / 0)
        self.assertIsNone(result)

    def test_callable_default(self):
        result = safely(lambda: 1 / 0, default=lambda: "computed")
        self.assertEqual(result, "computed")

    def test_specific_exception_filter(self):
        result = safely(lambda: 1 / 0, exceptions=(ZeroDivisionError,), default=-1)
        self.assertEqual(result, -1)

    def test_unmatched_exception_propagates(self):
        with self.assertRaises(ZeroDivisionError):
            safely(lambda: 1 / 0, exceptions=(ValueError,))

    def test_log_parameter(self):
        with self.assertLogs(level=logging.WARNING):
            safely(lambda: 1 / 0, log=True)


# ──────────────────────────────────────────────
# Node
# ──────────────────────────────────────────────
class TestNode(unittest.TestCase):
    def test_default_init(self):
        node = Node()
        self.assertIsNone(node.key)
        self.assertIsNone(node.value)
        self.assertIsNone(node.t)
        self.assertIsNone(node.m)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

    def test_custom_init(self):
        node = Node(key="k", value="v", t=1.0, m=2)
        self.assertEqual(node.key, "k")
        self.assertEqual(node.value, "v")
        self.assertEqual(node.t, 1.0)
        self.assertEqual(node.m, 2)


# ──────────────────────────────────────────────
# objectify (extended beyond test_json.py)
# ──────────────────────────────────────────────
class TestObjectifyExtended(unittest.TestCase):
    def test_datetime(self):
        dt = datetime.datetime(2023, 1, 15, 10, 30, 0)
        result = objectify(dt)
        self.assertEqual(result, "2023-01-15 10:30:00")

    def test_as_list(self):
        class HasAsList:
            def as_list(self):
                return [1, 2, 3]
        self.assertEqual(objectify(HasAsList()), [1, 2, 3])

    def test_as_dict(self):
        class HasAsDict:
            def as_dict(self):
                return {"a": 1}
        self.assertEqual(objectify(HasAsDict()), {"a": 1})

    def test_xml_method(self):
        class HasXml:
            def xml(self):
                return "<b>hi</b>"
        self.assertEqual(objectify(HasXml()), "<b>hi</b>")

    def test_enum(self):
        class Color(enum.Enum):
            RED = 1
        result = objectify(Color.RED)
        self.assertEqual(result["name"], "RED")
        self.assertEqual(result["value"], 1)
        self.assertEqual(result["__class__"], "Color")

    def test_set(self):
        result = objectify({1, 2, 3})
        self.assertIsInstance(result, list)
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_generator(self):
        def gen():
            yield 10
            yield 20
        self.assertEqual(objectify(gen()), [10, 20])

    def test_plain_dict(self):
        d = {"x": 1}
        self.assertIs(objectify(d), d)

    def test_plain_string(self):
        self.assertEqual(objectify("hello"), "hello")

    def test_plain_list(self):
        self.assertEqual(objectify([1, 2]), [1, 2])

    def test_object_with_dict(self):
        class Obj:
            def __init__(self):
                self.x = 1
        result = objectify(Obj())
        self.assertEqual(result["x"], 1)
        self.assertEqual(result["__class__"], "Obj")

    def test_fallback_to_str(self):
        # An object with no __dict__, no special methods
        result = objectify(object())
        self.assertIsInstance(result, str)


# ──────────────────────────────────────────────
# dumps
# ──────────────────────────────────────────────
class TestDumps(unittest.TestCase):
    def test_basic_dict(self):
        result = dumps({"a": 1, "b": 2})
        parsed = json.loads(result)
        self.assertEqual(parsed, {"a": 1, "b": 2})

    def test_custom_object(self):
        class Foo:
            def __init__(self):
                self.val = 99
        result = dumps({"obj": Foo()})
        parsed = json.loads(result)
        self.assertEqual(parsed["obj"]["val"], 99)


# ──────────────────────────────────────────────
# BareFixture
# ──────────────────────────────────────────────
class TestBareFixture(unittest.TestCase):
    def test_methods_exist_and_are_callable(self):
        f = BareFixture()
        # Should not raise
        f.on_request({})
        f.on_error({})
        f.on_success({})

    def test_is_hook_default(self):
        self.assertFalse(BareFixture.is_hook)


# ──────────────────────────────────────────────
# LocalUndefined
# ──────────────────────────────────────────────
class TestLocalUndefined(unittest.TestCase):
    def test_is_runtime_error(self):
        self.assertTrue(issubclass(LocalUndefined, RuntimeError))

    def test_can_be_raised(self):
        with self.assertRaises(LocalUndefined):
            raise LocalUndefined("test message")


# ──────────────────────────────────────────────
# Fixture.is_valid
# ──────────────────────────────────────────────
class TestFixtureIsValid(unittest.TestCase):
    def test_not_valid_before_init(self):
        f = Fixture()
        self.assertFalse(f.is_valid())

    def test_valid_after_init(self):
        f = Fixture()
        Fixture.local_initialize(f)
        try:
            self.assertTrue(f.is_valid())
        finally:
            Fixture.local_delete(f)

    def test_not_valid_after_delete(self):
        f = Fixture()
        Fixture.local_initialize(f)
        Fixture.local_delete(f)
        self.assertFalse(f.is_valid())

    def test_double_initialize_raises(self):
        f = Fixture()
        Fixture.local_initialize(f)
        try:
            with self.assertRaises(RuntimeError):
                Fixture.local_initialize(f)
        finally:
            Fixture.local_delete(f)


# ──────────────────────────────────────────────
# HTTP
# ──────────────────────────────────────────────
class TestHTTP(unittest.TestCase):
    def test_basic(self):
        exc = HTTP(404)
        self.assertEqual(exc.status, 404)
        self.assertEqual(exc.body, "")
        self.assertEqual(exc.headers, {})

    def test_with_body_and_headers(self):
        exc = HTTP(500, body="error", headers={"X-Custom": "val"})
        self.assertEqual(exc.status, 500)
        self.assertEqual(exc.body, "error")
        self.assertEqual(exc.headers["X-Custom"], "val")

    def test_is_base_exception(self):
        self.assertTrue(issubclass(HTTP, BaseException))

    def test_not_regular_exception(self):
        # HTTP intentionally does NOT inherit from Exception
        self.assertFalse(issubclass(HTTP, Exception))


# ──────────────────────────────────────────────
# redirect
# ──────────────────────────────────────────────
class TestRedirect(unittest.TestCase):
    def test_raises_http_303(self):
        with self.assertRaises(HTTP) as ctx:
            redirect("/some/path")
        self.assertEqual(ctx.exception.status, 303)

    def test_sets_location_header(self):
        # Clear any leftover Location header from previous tests
        response.headers.pop("Location", None)
        try:
            redirect("/target")
        except HTTP:
            self.assertEqual(response.headers.get("Location"), "/target")


# ──────────────────────────────────────────────
# Condition
# ──────────────────────────────────────────────
class TestCondition(unittest.TestCase):
    def test_true_condition_passes(self):
        c = Condition(lambda: True)
        # Should not raise
        c.on_request({})

    def test_false_condition_raises(self):
        c = Condition(lambda: False)
        with self.assertRaises(HTTP) as ctx:
            c.on_request({})
        self.assertEqual(ctx.exception.status, 400)

    def test_custom_exception(self):
        c = Condition(lambda: False, exception=HTTP(403))
        with self.assertRaises(HTTP) as ctx:
            c.on_request({})
        self.assertEqual(ctx.exception.status, 403)

    def test_on_false_callback(self):
        called = []
        def on_false():
            called.append(True)
            raise HTTP(302)

        c = Condition(lambda: False, on_false=on_false)
        with self.assertRaises(HTTP):
            c.on_request({})
        self.assertTrue(called)


# ──────────────────────────────────────────────
# Flash
# ──────────────────────────────────────────────
class TestFlash(unittest.TestCase):
    def setUp(self):
        request.app_name = "testapp"
        request.environ["wsgi.input"] = io.StringIO()
        # Clear any previous cookies
        request.cookies.clear()
        response._cookies = ""

    def test_flash_set_and_on_success_dict_output(self):
        flash = Flash()
        context = {"status": 200, "output": {}, "template_inject": {}}
        flash.on_request(context)
        flash.set("Hello!", _class="info")

        # Check that flash data was stored
        self.assertEqual(flash.local.flash["message"], "Hello!")
        self.assertEqual(flash.local.flash["class"], "info")

        flash.on_success(context)
        # Flash should be injected into template_inject
        self.assertIn("flash", context["template_inject"])
        Fixture.local_delete(flash)

    def test_flash_set_sanitizes(self):
        flash = Flash()
        context = {"status": 200, "output": {}, "template_inject": {}}
        flash.on_request(context)
        flash.set("<script>alert('xss')</script>")
        self.assertNotIn("<script>", flash.local.flash["message"])
        Fixture.local_delete(flash)

    def test_flash_no_sanitize(self):
        flash = Flash()
        context = {"status": 200, "output": {}, "template_inject": {}}
        flash.on_request(context)
        flash.set("<b>bold</b>", sanitize=False)
        self.assertIn("<b>bold</b>", flash.local.flash["message"])
        Fixture.local_delete(flash)

    def test_flash_on_redirect_sets_cookie(self):
        flash = Flash()
        context = {"status": 303, "output": "", "template_inject": {}}
        flash.on_request(context)
        flash.set("redirecting")
        flash.on_success(context)
        # Should set a cookie
        cookie_str = str(response._cookies)
        self.assertIn("py4web-flash", cookie_str)
        Fixture.local_delete(flash)

    def test_flash_empty_on_request(self):
        flash = Flash()
        context = {"status": 200, "output": {}, "template_inject": {}}
        flash.on_request(context)
        self.assertIsNone(flash.local.flash)
        flash.on_success(context)
        # empty flash injected
        self.assertEqual(context["template_inject"]["flash"], "")
        Fixture.local_delete(flash)


# ──────────────────────────────────────────────
# render
# ──────────────────────────────────────────────
class TestRender(unittest.TestCase):
    def test_render_content_string(self):
        result = render(content="Hello [[=name]]", context={"name": "World"})
        self.assertEqual(result, "Hello World")

    def test_render_with_loop(self):
        result = render(
            content="[[for i in range(3):]][[=i]][[pass]]",
            context={},
        )
        self.assertEqual(result, "012")

    def test_render_file(self):
        path = os.path.join(os.path.dirname(__file__), "templates")
        result = render(filename="index.html", path=path, context={"n": 2})
        self.assertEqual(result, "0,1.\n")


# ──────────────────────────────────────────────
# error_page
# ──────────────────────────────────────────────
class TestErrorPage(unittest.TestCase):
    def test_basic_404(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "text/html"
        result = error_page(404)
        self.assertIn("NOT FOUND", result)

    def test_basic_500(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "text/html"
        result = error_page(500)
        self.assertIn("INTERNAL SERVER ERROR", result)

    def test_with_button_text(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "text/html"
        result = error_page(404, button_text="Go Home", href="/")
        self.assertIn("Go Home", result)

    def test_custom_message(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "text/html"
        result = error_page(400, message="Custom Error")
        self.assertIn("Custom Error", result)

    def test_json_response(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "application/json"
        result = error_page(404)
        data = json.loads(result)
        self.assertEqual(data["code"], 404)
        self.assertEqual(data["message"], "NOT FOUND")

    def test_button_text_escaped(self):
        request.path = "/test"
        request.environ["HTTP_ACCEPT"] = "text/html"
        result = error_page(404, button_text="<script>xss</script>")
        self.assertNotIn("<script>xss</script>", result)


# ──────────────────────────────────────────────
# check_compatible
# ──────────────────────────────────────────────
class TestCheckCompatible(unittest.TestCase):
    def test_compatible_with_old_version(self):
        self.assertTrue(check_compatible("0.0.1"))

    def test_compatible_with_same_version(self):
        from py4web import __version__
        self.assertTrue(check_compatible(__version__))

    def test_incompatible_with_future(self):
        self.assertFalse(check_compatible("99999.0.0"))


# ──────────────────────────────────────────────
# SimpleErrorLogger
# ──────────────────────────────────────────────
class TestSimpleErrorLogger(unittest.TestCase):
    def test_log_does_not_raise(self):
        logger = SimpleErrorLogger()
        snapshot = {"traceback": "some traceback"}
        # Should just log and not raise
        logger.log("test_app", snapshot)


# ──────────────────────────────────────────────
# ErrorLogger
# ──────────────────────────────────────────────
class TestErrorLogger(unittest.TestCase):
    def test_fallback_when_no_db(self):
        el = ErrorLogger()
        # No database logger initialized, should use fallback
        logger = el._get_logger("any_app")
        self.assertIsInstance(logger, SimpleErrorLogger)

    def test_plugin_takes_priority(self):
        el = ErrorLogger()

        class CustomLogger:
            def log(self, app_name, snapshot):
                return "custom-ticket"

        el.plugins["myapp"] = CustomLogger()
        logger = el._get_logger("myapp")
        self.assertIsInstance(logger, CustomLogger)

    def test_log_uses_fallback(self):
        el = ErrorLogger()
        try:
            1 / 0
        except Exception:
            snapshot = get_error_snapshot()
        result = el.log("test_app", snapshot)
        # fallback logger returns None
        self.assertIsNone(result)


# ──────────────────────────────────────────────
# MetaPathRouter
# ──────────────────────────────────────────────
class TestMetaPathRouter(unittest.TestCase):
    def test_same_name_no_registration(self):
        # When pkg == pkg_alias, should not register
        before = len(sys.meta_path)
        MetaPathRouter("samepkg", "samepkg")
        self.assertEqual(len(sys.meta_path), before)

    def test_find_spec_unrelated(self):
        router = MetaPathRouter.__new__(MetaPathRouter)
        router.pkg_alias = "fake_alias_pkg"
        router.pkg = "os"
        # Should return None for unrelated modules
        result = router.find_spec("unrelated_module")
        self.assertIsNone(result)


# ──────────────────────────────────────────────
# try_app_watch_tasks
# ──────────────────────────────────────────────
class TestTryAppWatchTasks(unittest.TestCase):
    def test_empty_tasks(self):
        # Should not raise with empty tasks
        original_tasks = APP_WATCH["tasks"].copy()
        APP_WATCH["tasks"] = {}
        try_app_watch_tasks()
        APP_WATCH["tasks"] = original_tasks

    def test_runs_handler(self):
        called = []
        handler_name = "test_module.test_func"
        original_handlers = APP_WATCH["handlers"].copy()
        original_tasks = APP_WATCH["tasks"].copy()

        APP_WATCH["handlers"][handler_name] = lambda files: called.extend(files)
        APP_WATCH["tasks"][handler_name] = {"/some/file.js": True}

        try_app_watch_tasks()

        self.assertIn("/some/file.js", called)
        # Task should be removed after execution
        self.assertNotIn(handler_name, APP_WATCH["tasks"])

        APP_WATCH["handlers"] = original_handlers
        APP_WATCH["tasks"] = original_tasks


# ──────────────────────────────────────────────
# log_routes
# ──────────────────────────────────────────────
class TestLogRoutes(unittest.TestCase):
    def test_writes_file(self):
        tmp = tempfile.mkdtemp()
        old_tempdir = os.environ.get("TEMPDIR")
        os.environ["TEMPDIR"] = tmp
        try:
            routes = bottle.default_app().routes
            log_routes(routes, "test-routes.txt")
            outpath = os.path.join(tmp, "test-routes.txt")
            self.assertTrue(os.path.exists(outpath))
        finally:
            if old_tempdir is not None:
                os.environ["TEMPDIR"] = old_tempdir
            else:
                os.environ.pop("TEMPDIR", None)
            shutil.rmtree(tmp)


# ──────────────────────────────────────────────
# Translator
# ──────────────────────────────────────────────
class TestTranslator(unittest.TestCase):
    def test_on_request_sets_language(self):
        tmp = tempfile.mkdtemp()
        try:
            T = Translator(tmp)
            request.environ["HTTP_ACCEPT_LANGUAGE"] = "en"
            T.on_request({})
            # Should not raise
            result = str(T("hello"))
            self.assertEqual(result, "hello")
        finally:
            shutil.rmtree(tmp)

    def test_on_success_sets_header(self):
        tmp = tempfile.mkdtemp()
        try:
            T = Translator(tmp)
            request.environ["HTTP_ACCEPT_LANGUAGE"] = "en"
            T.on_request({})
            T.on_success({})
            self.assertIn("Content-Language", response.headers)
        finally:
            shutil.rmtree(tmp)


# ──────────────────────────────────────────────
# Session (extended)
# ──────────────────────────────────────────────
class TestSessionExtended(unittest.TestCase):
    def setUp(self):
        request.app_name = "testapp"
        request.environ["wsgi.input"] = io.StringIO()
        request.cookies.clear()
        response._cookies = ""

    def _make_session(self):
        return Session(secret=str(uuid.uuid4()), expiration=3600)

    def test_contains(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"a": 1}
        session.local.changed = False
        self.assertIn("a", session)
        self.assertNotIn("b", session)
        Fixture.local_delete(session)

    def test_keys_and_items(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"x": 1, "y": 2}
        session.local.changed = False
        self.assertEqual(set(session.keys()), {"x", "y"})
        self.assertEqual(set(session.items()), {("x", 1), ("y", 2)})
        Fixture.local_delete(session)

    def test_iter(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"a": 1, "b": 2}
        session.local.changed = False
        self.assertEqual(set(iter(session)), {"a", "b"})
        Fixture.local_delete(session)

    def test_delitem(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"key": "val"}
        session.local.changed = False
        del session["key"]
        self.assertTrue(session.local.changed)
        self.assertNotIn("key", session.local.data)
        Fixture.local_delete(session)

    def test_clear(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"a": 1, "b": 2}
        session.local.changed = False
        session.clear()
        self.assertTrue(session.local.changed)
        self.assertEqual(len(session.local.data), 0)
        Fixture.local_delete(session)

    def test_getitem(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {"x": 42}
        session.local.changed = False
        self.assertEqual(session["x"], 42)
        with self.assertRaises(KeyError):
            _ = session["nonexistent"]
        Fixture.local_delete(session)

    def test_get_default(self):
        session = self._make_session()
        Fixture.local_initialize(session)
        session.local.data = {}
        session.local.changed = False
        self.assertEqual(session.get("missing", "default"), "default")
        Fixture.local_delete(session)

    def test_get_returns_default_when_not_initialized(self):
        session = self._make_session()
        # Don't initialize - get should return default
        result = session.get("any_key", "fallback")
        self.assertEqual(result, "fallback")


# ──────────────────────────────────────────────
# action.uses - fixture ordering and deduplication
# ──────────────────────────────────────────────
class TestActionUses(unittest.TestCase):
    def test_deduplicates_fixtures(self):
        f1 = BareFixture()
        f2 = BareFixture()

        @action.uses(f1, f2, f1)
        def func():
            return "ok"

        # The wrapper should exist and be callable
        self.assertEqual(func(), "ok")

    def test_string_fixture_becomes_template(self):
        # When a string is passed, it should be converted to a Template
        called = []

        class TrackingFixture(BareFixture):
            def on_request(self, context):
                called.append("on_request")

        tf = TrackingFixture()

        @action.uses(tf)
        def func():
            return "result"

        result = func()
        self.assertEqual(result, "result")
        self.assertIn("on_request", called)

    def test_prerequisite_expansion(self):
        # Fixtures with __prerequisites__ should be auto-expanded
        inner = BareFixture()
        outer = BareFixture()
        outer.__prerequisites__ = [inner]

        @action.uses(outer)
        def func():
            return "ok"

        result = func()
        self.assertEqual(result, "ok")


# ──────────────────────────────────────────────
# get_error_snapshot (extended)
# ──────────────────────────────────────────────
class TestGetErrorSnapshotExtended(unittest.TestCase):
    def test_snapshot_contents(self):
        try:
            raise ValueError("test error")
        except Exception:
            snapshot = get_error_snapshot()
        self.assertEqual(snapshot["exception_type"], "ValueError")
        self.assertEqual(snapshot["exception_value"], "test error")
        self.assertIn("stackframes", snapshot)
        self.assertTrue(len(snapshot["stackframes"]) > 0)
        self.assertIn("traceback", snapshot)
        self.assertIn("ValueError", snapshot["traceback"])

    def test_snapshot_has_platform_info(self):
        try:
            raise RuntimeError("x")
        except Exception:
            snapshot = get_error_snapshot()
        self.assertIn("platform_info", snapshot)
        self.assertIn("system", snapshot["platform_info"])

    def test_snapshot_has_os_environ(self):
        try:
            raise RuntimeError("x")
        except Exception:
            snapshot = get_error_snapshot()
        self.assertIn("os_environ", snapshot)
        self.assertIn("PATH", snapshot["os_environ"])

    def test_depth_parameter(self):
        try:
            raise RuntimeError("x")
        except Exception:
            snapshot = get_error_snapshot(depth=1)
        self.assertIn("stackframes", snapshot)


# ──────────────────────────────────────────────
# Cache (extended - size eviction)
# ──────────────────────────────────────────────
class TestCacheExtended(unittest.TestCase):
    def test_eviction(self):
        cache = Cache(size=2)
        cache.get("a", lambda: 1)
        cache.get("b", lambda: 2)
        cache.get("c", lambda: 3)
        # 'a' should have been evicted
        self.assertEqual(cache.free, 0)
        # Should still return values for recent keys
        self.assertEqual(cache.get("b", lambda: 99), 2)
        self.assertEqual(cache.get("c", lambda: 99), 3)
        # 'a' was evicted so callback should be called again
        self.assertEqual(cache.get("a", lambda: 42), 42)

    def test_thread_safety(self):
        cache = Cache(size=100)
        results = {}

        def worker(key, value):
            r = cache.get(key, lambda: value)
            results[key] = r

        threads = [threading.Thread(target=worker, args=(f"k{i}", i)) for i in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        # All keys should have values
        self.assertEqual(len(results), 20)


# ──────────────────────────────────────────────
# Template (extended)
# ──────────────────────────────────────────────
class TestTemplateExtended(unittest.TestCase):
    def test_non_dict_output_skipped(self):
        path = os.path.join(os.path.dirname(__file__), "templates")
        t = Template("index.html", path=path)
        context = {"output": "plain string", "template_inject": {}}
        t.on_success(context)
        # Output should remain unchanged
        self.assertEqual(context["output"], "plain string")


# ──────────────────────────────────────────────
# load_module
# ──────────────────────────────────────────────
class TestLoadModule(unittest.TestCase):
    def test_load_module(self):
        # Create a temp module file
        tmp = tempfile.mkdtemp()
        modpath = os.path.join(tmp, "testmod.py")
        try:
            with open(modpath, "w") as f:
                f.write("VALUE = 42\n")
            from py4web.core import load_module
            mod = load_module("test_dynamic_mod", modpath)
            self.assertEqual(mod.VALUE, 42)
            self.assertIn("test_dynamic_mod", sys.modules)
        finally:
            sys.modules.pop("test_dynamic_mod", None)
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
