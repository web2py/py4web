"""Tests for the root app (py4web run --root_app / PY4WEB_ROOT_APP):
the app that is served at / instead of /{app_name}/."""

import os
import shutil
import tempfile
import unittest
from unittest import mock

from click.testing import CliRunner

from py4web import URL, action, request
from py4web import core
from py4web.core import Reloader, cli, get_root_app_name, is_root_app


def rules(app_name):
    return {route["rule"] for route in Reloader.ROUTES[app_name]}


class TestRootAppName(unittest.TestCase):
    def test_defaults_to_default_app(self):
        with mock.patch.dict(os.environ):
            os.environ.pop("PY4WEB_ROOT_APP", None)
            self.assertEqual(get_root_app_name(), "_default")
            self.assertTrue(is_root_app("_default"))
            self.assertFalse(is_root_app("todo"))

    def test_empty_env_falls_back_to_default_app(self):
        with mock.patch.dict(os.environ, {"PY4WEB_ROOT_APP": ""}):
            self.assertEqual(get_root_app_name(), "_default")

    def test_env_overrides_root_app(self):
        with mock.patch.dict(os.environ, {"PY4WEB_ROOT_APP": "todo"}):
            self.assertEqual(get_root_app_name(), "todo")
            self.assertTrue(is_root_app("todo"))
            self.assertFalse(is_root_app("_default"))


class TestRootAppURL(unittest.TestCase):
    def setUp(self):
        self.saved_app_name = getattr(request, "app_name", None)

    def tearDown(self):
        request.app_name = self.saved_app_name

    def test_root_app_urls_have_no_prefix(self):
        with mock.patch.dict(os.environ, {"PY4WEB_ROOT_APP": "todo"}):
            request.app_name = "todo"
            self.assertEqual(URL("index"), "/index")
            self.assertEqual(URL("a", "b", vars=dict(x=1)), "/a/b?x=1")

    def test_default_app_is_prefixed_when_not_root(self):
        with mock.patch.dict(os.environ, {"PY4WEB_ROOT_APP": "todo"}):
            request.app_name = "_default"
            self.assertEqual(URL("index"), "/_default/index")
            request.app_name = "other"
            self.assertEqual(URL("index"), "/other/index")


class TestRootAppRoutes(unittest.TestCase):
    APPS = ("rootapp_main", "rootapp_other")

    def setUp(self):
        self.saved_app_name = action.app_name
        self.env = mock.patch.dict(os.environ, {"PY4WEB_ROOT_APP": "rootapp_main"})
        self.env.start()
        os.environ.pop("PY4WEB_URL_PREFIX", None)

    def tearDown(self):
        Reloader.clear_routes(list(self.APPS))
        for app_name in self.APPS:
            Reloader.ROUTES.pop(app_name, None)
        action.app_name = self.saved_app_name
        self.env.stop()

    def test_actions_of_root_app_have_no_prefix(self):
        action.app_name = "rootapp_main"

        @action("rootapp_page")
        def rootapp_page():
            return "ok"

        @action("index")
        def rootapp_index():
            return "ok"

        self.assertEqual(rules("rootapp_main"), {"/rootapp_page", "/index", "/"})

    def test_actions_of_other_apps_keep_prefix(self):
        action.app_name = "rootapp_other"

        @action("rootapp_page")
        def rootapp_page():
            return "ok"

        self.assertEqual(rules("rootapp_other"), {"/rootapp_other/rootapp_page"})

    def test_static_routes(self):
        folder = tempfile.mkdtemp()
        try:
            for app_name in self.APPS:
                # no __init__.py: only the static folder gets exposed
                os.makedirs(os.path.join(folder, app_name, "static"))
            with mock.patch.dict(os.environ, {"PY4WEB_APPS_FOLDER": folder}):
                for app_name in self.APPS:
                    Reloader.import_app(app_name)
        finally:
            shutil.rmtree(folder)
        static = r"/static/<re((_\d+(\.\d+){2}/)?)><fp.path()>"
        self.assertEqual(rules("rootapp_main"), {static})
        self.assertEqual(rules("rootapp_other"), {"/rootapp_other" + static})


class TestRootAppReloaderHook(unittest.TestCase):
    def test_unknown_path_reloads_root_app(self):
        hooks = core._REQUEST_HOOKS.before
        Reloader.install_reloader_hook()
        hook = hooks.pop()
        env = {"PY4WEB_ROOT_APP": "rootapp_main"}
        with (
            mock.patch.dict(os.environ, env),
            mock.patch.dict(core.DIRTY_APPS, {"rootapp_main": True, "_default": True}),
            mock.patch.object(Reloader, "import_app") as import_app,
            mock.patch.object(core, "try_app_watch_tasks"),
            mock.patch.object(core, "request", mock.Mock(path="/not_an_app/page")),
        ):
            hook()
        import_app.assert_called_once_with("rootapp_main")


class TestRootAppCLI(unittest.TestCase):
    def test_run_has_root_app_option(self):
        res = CliRunner().invoke(cli, ["run", "--help"])
        self.assertEqual(res.exit_code, 0)
        self.assertIn("--root_app", res.output)

    def test_root_app_option_is_exported_to_env(self):
        folder = tempfile.mkdtemp()
        try:
            with (
                mock.patch.dict(os.environ),
                mock.patch.object(Reloader, "import_apps"),
                mock.patch.object(core, "start_server") as start_server,
            ):
                res = CliRunner().invoke(
                    cli, ["run", "-Y", "-d", "none", "--root_app", "todo", folder]
                )
                self.assertEqual(res.exit_code, 0, res.output)
                self.assertEqual(os.environ["PY4WEB_ROOT_APP"], "todo")
                self.assertEqual(get_root_app_name(), "todo")
                self.assertIn('Root app "todo" is not loaded', res.output)
                start_server.assert_called_once()
        finally:
            shutil.rmtree(folder)

    def test_wsgi_root_app_argument(self):
        folder = tempfile.mkdtemp()
        try:
            with (
                mock.patch.dict(os.environ),
                mock.patch.object(Reloader, "import_apps"),
            ):
                core.wsgi(apps_folder=folder, yes=True, root_app="todo")
                self.assertEqual(get_root_app_name(), "todo")
        finally:
            shutil.rmtree(folder)


if __name__ == "__main__":
    unittest.main()
