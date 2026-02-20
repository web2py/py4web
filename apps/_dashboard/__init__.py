import base64
import copy
import datetime
import functools
import io
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import traceback
import uuid
import zipfile
import pathlib

import pathspec
import requests

from pydal.restapi import Policy, RestAPI
from pydal.validators import CRYPT

import py4web
from py4web import (
    HTTP,
    URL,
    Translator,
    __version__,
    abort,
    action,
    redirect,
    request,
    response,
)
from py4web.core import DAL, Fixture, Reloader, Session, dumps, error_logger, safely
from py4web.utils.factories import ActionFactory
from py4web.utils.grid import Grid

from .diff2kryten import diff2kryten
from .utils import *
from .settings import *


class Logged(Fixture):
    """Fixture to ensure user is logged in"""

    def __init__(self, session):
        self.__prerequisites__ = [session]
        self.session = session

    def on_request(self, context):
        user = self.session.get("user")
        if not user or not user.get("id"):
            abort(403)


def catch_errors(func):
    """Wraps APIs that return a status=success/error and includes a traceback in response"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            result = {"status": "error", "traceback": traceback.format_exc()}
        return result

    return wrapper


def change_password_handler(old_password, new_password):
    """Change the dashboard password"""
    password_file = os.environ.get("PY4WEB_PASSWORD_FILE")
    if not password_file:
        return {"status": "error", "message": "PY4WEB_PASSWORD_FILE environment variable not set"}
    if not os.path.exists(password_file):
        return {"status": "error", "message": f"Password file not found: {password_file}"}
    
    try:
        # Read current password from file
        with open(password_file, "r") as fp:
            stored_password = fp.read().strip()
        
        # Verify old password matches
        if CRYPT()(old_password)[0] != stored_password:
            return {"status": "error", "message": "Current password is incorrect"}
        
        # Encrypt new password
        encrypted_password = str(CRYPT()(new_password)[0])
        if not encrypted_password:
            return {"status": "error", "message": "Failed to encrypt password"}
        
        # Write to temporary file first, then rename to avoid data loss
        temp_fd, temp_path = tempfile.mkstemp(text=True)
        try:
            with os.fdopen(temp_fd, 'w') as fp:
                fp.write(encrypted_password)
            # Only rename if write was successful
            shutil.move(temp_path, password_file)
        except Exception as temp_error:
            # Clean up temp file if it exists
            try:
                os.unlink(temp_path)
            except:
                pass
            raise temp_error
        
        return {"status": "success", "message": "Password changed successfully"}
    except Exception as e:
        return {"status": "error", "message": f"Error: {str(e)}"}


def load_user_settings():
    """Load user settings from user_settings.toml"""
    settings_file = os.path.join(settings.APP_FOLDER, "user_settings.toml")
    default_settings = {"selected_theme": "AlienDark"}
    
    if not os.path.exists(settings_file):
        # Create default settings file
        try:
            with open(settings_file, "w") as fp:
                fp.write('selected_theme = "AlienDark"\n')
            return default_settings
        except Exception:
            return default_settings
    
    try:
        with open(settings_file, "r") as fp:
            content = fp.read()
        # Simple TOML parser for key = "value" format
        parsed_settings = {}
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                parsed_settings[key] = value
        return parsed_settings if parsed_settings else default_settings
    except Exception:
        return default_settings


def save_user_settings(settings_dict):
    """Save user settings to user_settings.toml"""
    settings_file = os.path.join(settings.APP_FOLDER, "user_settings.toml")
    try:
        with open(settings_file, "w") as fp:
            for key, value in settings_dict.items():
                fp.write(f'{key} = "{value}"\n')
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_available_themes():
    """Get list of available themes by reading static/themes/ folder"""
    themes_dir = os.path.join(settings.APP_FOLDER, "static", "themes")
    try:
        if os.path.isdir(themes_dir):
            themes = sorted(
                [
                    d
                    for d in os.listdir(themes_dir)
                    if os.path.isdir(os.path.join(themes_dir, d))
                    and not d.startswith(".")
                ]
            )
            return themes
    except (OSError, IOError):
        pass
    return []


def normalize_selected_theme(selected_theme, available_themes=None):
    """Normalize a selected theme against currently available themes."""
    themes = available_themes if available_themes is not None else get_available_themes()
    if selected_theme and selected_theme in themes:
        return selected_theme
    if "AlienDark" in themes:
        return "AlienDark"
    if themes:
        return themes[0]
    return "AlienDark"


session = Session()
T = Translator(settings.T_FOLDER)
authenticated = ActionFactory(Logged(session))
session_secured = action.uses(Logged(session))


@action("version")
def version():
    return __version__


if MODE in ("demo", "readonly", "full"):

    @action("index")
    @action.uses("index.html", session, T)
    def index():
        themes = get_available_themes()
        user_settings = load_user_settings()
        selected_theme = normalize_selected_theme(
            user_settings.get("selected_theme", "AlienDark"), themes
        )
        
        return dict(
            languages=dumps(getattr(T.local, "language", {})),
            mode=MODE,
            user_id=(session.get("user") or {}).get("id"),
            themes=themes,
            selected_theme=selected_theme,
        )


    @action("login", method="POST")
    @action.uses(session)
    def login():
        if MODE == "demo":
            valid = True
        else:
            valid = False
            password = request.json.get("password")
            password_file = os.environ.get("PY4WEB_PASSWORD_FILE")
            if password and password_file and os.path.exists(password_file):
                with open(password_file, "r") as fp:
                    encrypted_password = fp.read().strip()
                    valid = CRYPT()(password)[0] == encrypted_password
        if valid:
            session["user"] = dict(id=1)
        return dict(user=valid, mode=MODE)

    @action("logout", method="POST")
    @action.uses(session)
    def logout():
        session["user"] = None
        return dict()

    @action("change_password", method="POST")
    @action.uses(Logged(session))
    @catch_errors
    def change_password():
        old_password = request.json.get("old_password")
        password = request.json.get("password")
        if not old_password:
            return {"status": "error", "message": "Current password is required"}
        if not password:
            return {"status": "error", "message": "New password is required"}
        return change_password_handler(old_password, password)

    @action("save_theme", method="POST")
    @action.uses(Logged(session))
    @catch_errors
    def save_theme():
        theme = request.json.get("theme")
        if not theme:
            return {"status": "error", "message": "Theme name is required"}
        themes = get_available_themes()
        if theme not in themes:
            return {"status": "error", "message": "Theme is not available"}
        user_settings = load_user_settings()
        user_settings["selected_theme"] = theme
        return save_user_settings(user_settings)

    @action("tickets/search")
    @action.uses(Logged(session), "dbadmin.html")
    def dbadmin():
        db = error_logger.database_logger.db
        themes = get_available_themes()
        user_settings = load_user_settings()

        def make_grid():
            make_safe(db)
            table = db.py4web_error
            columns = [field for field in table if not field.name == "snapshot"]
            return Grid(
                table,
                columns=columns,
                details=False,
                editable=False,
                pre_action_buttons=[
                    lambda row: {
                        "text": "Show",
                        "url": URL("ticket", row.uuid),
                        "icon": "fa-eye",
                    }
                ],
            )

        grid = action.uses(db)(make_grid)()
        return dict(
            table_name="py4web_error",
            grid=grid,
            themes=themes,
            selected_theme=normalize_selected_theme(
                user_settings.get("selected_theme", "AlienDark"), themes
            ),
        )

    @action("dbadmin/<app_name>/<db_name>/<table_name>")
    @action.uses(Logged(session), "dbadmin.html")
    def dbadmin(app_name, db_name, table_name):
        themes = get_available_themes()
        user_settings = load_user_settings()
        module = Reloader.MODULES.get(app_name)
        db = getattr(module, db_name)

        def make_grid():
            make_safe(db)
            table = db[table_name]
            for field in table:
                field.readable = True
                field.writable = True
                # Make reference fields clickable
                if field.type_name in ("reference", "big-reference", "list:reference"):
                    field.represent = make_admin_reference_represent(
                        app_name, db_name, field
                    )

            columns = [
                field
                for field in table
                if field.type_name
                in (
                    "id",
                    "string",
                    "integer",
                    "double",
                    "time",
                    "date",
                    "datetime",
                    "boolean",
                    "reference",
                    "big-reference",
                )
            ]
            return Grid(table, columns=columns)

        grid = action.uses(db)(make_grid)()
        return dict(
            app_name=app_name,
            table_name=table_name,
            grid=grid,
            themes=themes,
            selected_theme=normalize_selected_theme(
                user_settings.get("selected_theme", "AlienDark"), themes
            ),
        )

    @action("info")
    @session_secured
    @catch_errors
    def info():
        # Start with OS information
        os_info = f"{platform.system()} {platform.release()}"
        vars = [
            {"name": "os", "version": os_info},
            {"name": "py4web", "version": __version__},
            {"name": "python", "version": sys.version}
        ]
        for module in sorted(sys.modules):
            if not "." in module:
                try:
                    m = __import__(module)
                    if "__version__" in dir(m):
                        vars.append({"name": module, "version": m.__version__})
                except ImportError:
                    pass
        return {"status": "success", "payload": vars}

    @action("routes")
    @session_secured
    @catch_errors
    def routes():
        """Returns current registered routes"""
        sorted_routes = {
            name: list(sorted(routes, key=lambda route: route["rule"]))
            for name, routes in Reloader.ROUTES.items()
        }
        return {"payload": sorted_routes, "status": "success"}

    @action("apps")
    @session_secured
    @catch_errors
    def apps():
        """Returns a list of installed apps"""
        apps = os.listdir(FOLDER)
        exposed_names = APP_NAMES and APP_NAMES.split(",")
        apps = [
            {
                "name": app,
                "error": Reloader.ERRORS.get(app),
                "running": app in Reloader.ROUTES and not Reloader.ERRORS.get(app),
                "edit_url": URL("app_detail", app),
            }
            for app in apps
            if os.path.isdir(os.path.join(FOLDER, app))
            and not app.startswith("__")
            and not app.startswith(".")
            and (not exposed_names or app in exposed_names)
        ]
        apps.sort(key=lambda item: item["name"])
        return {"payload": apps, "status": "success"}

    @action("app_detail/<name:re:\\w+>")
    @session_secured
    @catch_errors
    def app_detail(name):
        """Returns a focused payload for app edit layout."""
        app_path = os.path.join(FOLDER, name)
        if not os.path.isdir(app_path):
            return {"status": "error", "message": "App does not exist"}

        def normalize_path(path):
            """Convert Windows backslashes to forward slashes for consistent frontend handling"""
            return path.replace(os.sep, '/')

        def list_files_recursive(base_path, relative_path=""):
            """Recursively list all folders and their files"""
            sections = {}
            full_path = os.path.join(base_path, relative_path) if relative_path else base_path
            
            try:
                for item in os.listdir(full_path):
                    if item.startswith(".") or item == "__pycache__":
                        continue
                    
                    item_path = os.path.join(full_path, item)
                    # Normalize to forward slashes for frontend
                    item_relative = os.path.join(relative_path, item) if relative_path else item
                    item_relative = normalize_path(item_relative)
                    
                    if os.path.isdir(item_path):
                        # Add this directory as a section
                        files_in_dir = [
                            f for f in os.listdir(item_path)
                            if not f.startswith(".")
                            and os.path.isfile(os.path.join(item_path, f))
                        ]
                        sections[item_relative] = sorted(files_in_dir)
                        
                        # Recursively process subdirectories
                        subsections = list_files_recursive(base_path, os.path.join(relative_path, item) if relative_path else item)
                        sections.update(subsections)
                    elif os.path.isfile(item_path) and not relative_path:
                        # Root-level files
                        if "" not in sections:
                            sections[""] = []
                        sections[""].append(item)
            except (OSError, IOError):
                pass
            
            return sections

        all_sections = list_files_recursive(app_path)
        
        # Sort root files if they exist
        if "" in all_sections:
            all_sections[""] = sorted(all_sections[""])

        payload = {
            "name": name,
            "path": app_path,
            "error": Reloader.ERRORS.get(name),
            "running": name in Reloader.ROUTES and not Reloader.ERRORS.get(name),
            "edit_layout": True,
            "sections": all_sections,
        }
        return {"status": "success", "payload": payload}

    @action("delete_app/<name:re:\\w+>", method="POST")
    @session_secured
    @catch_errors
    def delete_app(name):
        """delete the app"""
        path = os.path.join(FOLDER, name)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        archive = os.path.join(FOLDER, "%s.%s.zip" % (name, timestamp))
        if os.path.exists(path) and os.path.isdir(path):
            # zip the folder, just in case
            shutil.make_archive(archive, "zip", path)
            # then remove the app
            shutil.rmtree(path)
            return {"status": "success", "payload": "Deleted"}
        return {"status": "success", "payload": "App does not exist"}

    @action("new_file/<name:re:\\w+>/<file_name:path>", method="POST")
    @session_secured
    def new_file(name, file_name):
        """creates a new file or folder"""
        path = os.path.join(FOLDER, name)
        
        # Check if this is a folder creation request (query parameter)
        is_folder = request.query.get("folder") == "1"
        
        if not os.path.exists(path):
            return {"status": "success", "payload": "App does not exist"}
        
        full_path = os.path.join(path, file_name)
        if not full_path.startswith(path + os.sep):
            return {"status": "success", "payload": "Invalid path"}
        
        # Create folder
        if is_folder:
            try:
                os.makedirs(full_path, exist_ok=True)
                return {"status": "success"}
            except Exception as e:
                return {"status": "error", "message": str(e)}
        
        # File creation (existing logic)
        if os.path.exists(full_path):
            return {"status": "success", "payload": "File already exists"}
        parent = os.path.dirname(full_path)
        if not os.path.exists(parent):
            os.makedirs(parent)
        with open(full_path, "w") as fp:
            if full_path.endswith(".html"):
                fp.write('[[extend "layout.html"]]\nHello World!')
            elif full_path.endswith(".py"):
                fp.write("# -*- coding: utf-8 -*-")
        return {"status": "success"}

    @action("walk/<path:path>")
    @session_secured
    @catch_errors
    def walk(path):
        """Returns a nested folder structure as a tree"""
        top = os.path.join(FOLDER, path)
        filter = None
        filter_file = os.path.join(top, PY4WEB_IGNORE)
        if os.path.exists(filter_file):
            with open(filter_file, "r") as stream:
                patterns = stream.readlines()
            try:
                filter = pathspec.PathSpec.from_lines("gitwildmatch", patterns)
            except Exception:
                print(traceback.format_exc())

        def visible(root, name, filter=filter):
            if filter:
                return not filter.match_file(os.path.join(root, name))
            return not (
                name.startswith(".")
                or name.startswith("#")
                or name.endswith("~")
                or name[-4:] in (".pyc", ".pyo")
                or name == "__pycache__"
                or os.path.basename(root) == "uploads"
            )

        if not os.path.exists(top) or not os.path.isdir(top):
            return {"status": "error", "message": "folder does not exist"}
        store = {}
        for root, dirs, files in os.walk(top, topdown=False, followlinks=True):
            if visible(*os.path.split(root)):
                store[root] = {
                    "dirs": list(
                        sorted(
                            [
                                {"name": d, "content": store[os.path.join(root, d)]}
                                for d in dirs
                                if visible(root, d) and os.path.join(root, d) in store
                            ],
                            key=lambda item: item["name"],
                        )
                    ),
                    "files": list(sorted([f for f in files if visible(root, f)])),
                }
        return {"payload": store[top], "status": "success"}

    @action("load/<path:path>")
    @session_secured
    @catch_errors
    def load(path):
        """Loads a text file"""
        path = safe_join(FOLDER, path) or abort()
        content = open(path, "rb").read().decode("utf8", errors="ignore")
        return {"payload": content, "status": "success"}

    @action("load_bytes/<path:path>")
    @session_secured
    def load_bytes(path):
        """Loads a binary file"""
        path = safe_join(FOLDER, path) or abort()
        return open(path, "rb").read()

    @action("packed/<path:path>")
    @session_secured
    def packed(path):
        """Packs an app"""
        appname = path.split(".")[-2]
        # some security
        app_dir = os.path.join(FOLDER, appname)
        if "/" in path or appname.startswith(".") or not os.path.exists(app_dir):
            raise HTTP(400)
        store = io.BytesIO()
        zip = zipfile.ZipFile(store, mode="w", compression=zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(app_dir, topdown=False):
            if not root.startswith("."):
                for name in files:
                    if not (
                        name.endswith("~") or name.endswith(".pyc") or name[:1] in "#."
                    ):
                        filename = os.path.join(root, name)
                        short = filename[len(app_dir + os.path.sep) :]
                        zip.write(filename, short)
        zip.close()
        data = store.getvalue()
        response.headers["Content-Type"] = "application/zip"
        return data

    @action("tickets")
    @session_secured
    @catch_errors
    def tickets():
        """Returns most recent tickets grouped by path+error"""
        tickets = safely(error_logger.database_logger.get) if MODE != "DEMO" else None
        return {"payload": tickets or [], "status": "success"}

    @action("clear")
    @session_secured
    def clear_tickets():
        if MODE != "demo":
            safely(error_logger.database_logger.clear)

    @action("ticket/<ticket_uuid>")
    @action.uses("ticket.html")
    @session_secured
    def error_ticket(ticket_uuid):
        themes = get_available_themes()
        user_settings = load_user_settings()
        selected_theme = normalize_selected_theme(
            user_settings.get("selected_theme", "AlienDark"), themes
        )
        if MODE != "demo":
            return dict(
                ticket=safely(
                    lambda: error_logger.database_logger.get(ticket_uuid=ticket_uuid)
                ),
                selected_theme=selected_theme
            )
        else:
            return dict(ticket=None, selected_theme=selected_theme)

    @action("rest/<path:path>", method=["GET", "POST", "PUT", "DELETE"])
    @session_secured
    @catch_errors
    def api(path):
        # this is not final, requires pydal 19.5
        args = path.split("/")
        app_name = args[0]
        if MODE != "full":
            raise HTTP(403)
        module = Reloader.MODULES.get(app_name)

        if not module:
            return {"status": "success", "databases": []}
        databases = [
            name for name in dir(module) if isinstance(getattr(module, name), DAL)
        ]

        def tables(name):
            db = getattr(module, name)
            make_safe(db)
            return [
                {
                    "name": t._tablename,
                    "fields": t.fields,
                    "link": URL("dbadmin", app_name, name, t._tablename),
                }
                for t in getattr(module, name)
            ]

        return {
            "status": "success",
            "databases": [{"name": name, "tables": tables(name)} for name in databases],
        }


def extract(source, target_dir):
    with zipfile.ZipFile(source, "r") as zfile:
        allfiles = [info.filename for info in zfile.infolist()]
        roots = None
        if not "__init__.py" in allfiles:
            # check for subfolders that contain __init__.py
            roots = list(
                set(
                    path[:-12]
                    for path in allfiles
                    if path.count("/") == 1 and path.endswith("/__init__.py")
                )
            )
            # there can be only one
            if len(roots) != 1:
                abort(500)
        # extract only the subfolder
        with tempfile.TemporaryDirectory() as tmpdir:
            zfile.extractall(tmpdir)
            zfile.close()
            source_dir = tmpdir if roots is None else os.path.join(tmpdir, roots[0])
            # make sure we do not override the databases and uploads folders:
            if os.path.exists(target_dir):
                for folder in ["databases", "uploads"]:
                    source_folder = os.path.join(source_dir, folder)
                    if os.path.exists(source_folder):
                        shutil.rmtree(source_folder)
            shutil.copytree(
                source_dir,
                target_dir,
                dirs_exist_ok=True,
            )


if MODE == "full":

    @action("reload")
    @action("reload/<name>")
    @session_secured
    @catch_errors
    def reload(name=None):
        """Reloads installed apps"""
        Reloader.import_app(name) if name else Reloader.import_apps()
        return {"status": "success"}

    @action("save/<path:path>", method="POST")
    @session_secured
    @catch_errors
    def save(path, reload_app=True):
        """Saves a file"""
        app_name = path.split("/")[0]
        path = safe_join(FOLDER, path) or abort()
        with open(path, "wb") as myfile:
            body = json.load(request.body)
            myfile.write(body.encode("utf8"))
        if reload_app:
            Reloader.import_app(app_name)
        return {"status": "success"}

    @action("delete/<path:path>", method="POST")
    @session_secured
    @catch_errors
    def delete(path):
        """Deletes a file or empty folder"""
        fullpath = safe_join(FOLDER, path) or abort()
        
        # Check if it's a directory
        if os.path.isdir(fullpath):
            # Only allow deletion if directory is empty
            if os.listdir(fullpath):
                return {"status": "error", "message": "Cannot delete non-empty folder. Delete all files first."}

        recursive_unlink(fullpath)
        return {"status": "success"}

    def install_by_unzip_or_treecopy(source, source_dir, target_dir):
        """Installs an app by either unzipping it (if py4web installed from pip)
        or by copying the directory tree (if installed from source)."""
        if os.path.exists(source):
            extract(source, target_dir)
        else:
            shutil.copytree(source_dir, target_dir)

    def prepare_target_dir(form, target_dir):
        """Prepares the target directory for the new app.
        If should_exist is False, leaves the directory blank."""
        if form["mode"] == "new":
            if os.path.exists(target_dir):
                abort(500)  # already validated client side
        elif form["mode"] == "update":
            if not os.path.exists(target_dir):
                abort(500)  # not an update

    @action("new_app", method="POST")
    @session_secured
    @catch_errors
    def new_app():
        form = request.json
        # Directory for zipped assets
        assets_dir = os.path.join(os.path.dirname(py4web.__file__), "assets")
        app_name = form["name"]
        target_dir = safe_join(FOLDER, app_name)
        if form["type"] == "minimal":
            source = os.path.join(assets_dir, "py4web.app._minimal.zip")
            source_dir = safe_join(FOLDER, "_minimal")
            prepare_target_dir(form, target_dir)
            install_by_unzip_or_treecopy(source, source_dir, target_dir)
        elif form["type"] == "scaffold":
            source = os.path.join(assets_dir, "py4web.app._scaffold.zip")
            source_dir = safe_join(FOLDER, "_scaffold")
            prepare_target_dir(form, target_dir)
            install_by_unzip_or_treecopy(source, source_dir, target_dir)
        elif form["type"] == "web":
            prepare_target_dir(form, target_dir)
            source = form["source"]
            if source.endswith(".zip"):  # install from the web (zip file)
                res = requests.get(source)
                mem_zip = io.BytesIO(res.content)
                extract(mem_zip, target_dir)
            elif source.endswith(".git"):
                # clone from a git repo
                process = subprocess.Popen(
                    ["git", "clone", source, form["name"]], cwd=FOLDER
                )
                process.communicate()
                if process.returncode != 0:
                    abort(500)
        elif form["type"] == "upload":
            prepare_target_dir(form, target_dir)
            source_stream = io.BytesIO(base64.b64decode(form["file"]))
            extract(source_stream, target_dir)
        else:
            abort(500)
        settings = os.path.join(target_dir, "settings.py")
        if os.path.exists(settings):
            with open(settings) as fp:
                data = fp.read()
            data = data.replace("<session-secret-key>", str(uuid.uuid4()))
            with open(settings, "w") as fp:
                fp.write(data)
        try:
            Reloader.import_app(app_name)
        except Exception:
            pass
        return {"status": "success"}

    #
    # Below here work in progress
    #

    @action("gitlog/<project>")
    @action.uses(Logged(session), "gitlog.html")
    @catch_errors
    def gitlog(project):
        themes = get_available_themes()
        user_settings = load_user_settings()
        if not is_git_repo(os.path.join(FOLDER, project)):
            return "Project is not a GIT repo"
        branches = get_branches(cwd=os.path.join(FOLDER, project))
        commits = get_commits(cwd=os.path.join(FOLDER, project))
        return dict(
            status="success",
            commits=commits,
            checkout=checkout,
            project=project,
            branches=branches,
            selected_theme=normalize_selected_theme(
                user_settings.get("selected_theme", "AlienDark"), themes
            ),
        )

    @authenticated.callback()
    def checkout(project, commit):
        if not is_git_repo(project):
            raise HTTP(400)
        run("git stash", cwd=os.path.join(FOLDER, project))
        run("git checkout " + commit, cwd=os.path.join(FOLDER, project))
        Reloader.import_app(project)

    @action("swapbranch/<project>", method="POST")
    @action.uses(Logged(session))
    def swapbranch(project):
        if not is_git_repo(project):
            raise HTTP(400)

        branch = (
            request.forms.get("branches") if request.forms.get("branches") else "master"
        )
        # swap branches then go back to gitlog so new commits load
        checkout(project, branch)
        redirect(URL("gitlog", project))

    @action("gitshow/<project>/<commit>")
    @action.uses(Logged(session), "gitshow.html")
    def gitshow(project, commit):
        if not is_git_repo(project):
            raise HTTP(400)
        flag = request.params.get("showfull")
        opt = ""
        if flag == "true":
            opt = " -U9999"
        patch = run("git show " + commit + opt, cwd=os.path.join(FOLDER, project))
        return diff2kryten(patch)


# handle internationalization & pluralization files
#


@action("translations/<name>", method="GET")
@action.uses(Logged(session), "translations.html")
def translations(name):
    """returns a json with all translations for all languages"""
    themes = get_available_themes()
    user_settings = load_user_settings()
    folder = os.path.join(FOLDER, name, "translations")
    if not os.path.exists(folder):
        os.makedirs(folder)
    t = Translator(folder)
    return dict(
        languages=t.languages,
        selected_theme=normalize_selected_theme(
            user_settings.get("selected_theme", "AlienDark"), themes
        ),
    )


@action("api/translations/<name>", method="GET")
@action.uses(Logged(session))
def get_translations(name):
    """returns a json with all translations for all languages"""
    t = Translator(os.path.join(FOLDER, name, "translations"))
    return t.languages


@action("api/translations/<name>", method="POST")
@action.uses(Logged(session))
def post_translations(name):
    """updates all languages"""
    folder = os.path.join(FOLDER, name, "translations")
    if not os.path.exists(folder):
        os.makedirs(folder)
    t = Translator(folder)
    t.languages = request.json
    if MODE == "full":
        t.save()


@action("api/translations/<name>/search", method="GET")
@action.uses(Logged(session))
def update_translations(name):
    """find all T(...) decorated strings in the code and returns them"""
    app_folder = os.path.join(FOLDER, name)
    strings = Translator.find_matches(app_folder)
    return {"strings": strings}
