import base64
import copy
import datetime
import io
import os
import shutil
import subprocess
import sys
import uuid
import zipfile

import requests
from pydal.validators import CRYPT
from yatl.helpers import BEAUTIFY

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
from py4web.core import ErrorStorage, Fixture, Reloader, Session, dumps
from py4web.utils.factories import ActionFactory

from .diff2kryten import diff2kryten
from .utils import *

MODE = os.environ.get("PY4WEB_DASHBOARD_MODE", "none")
FOLDER = os.environ["PY4WEB_APPS_FOLDER"]
APP_FOLDER = os.path.dirname(__file__)
T_FOLDER = os.path.join(APP_FOLDER, "translations")
T = Translator(T_FOLDER)
error_storage = ErrorStorage()
db = error_storage.db
session = Session()


def run(command, project):
    """for runing git commands inside an app (project)"""
    return subprocess.check_output(
        command.split(), cwd=os.path.join(FOLDER, project)
    ).decode()


def get_commits(project):
    """list of git commits for the project"""
    output = run("git log", project)
    commits = []
    for line in output.split("\n"):
        if line.startswith("commit "):
            commit = {"code": line[7:], "message": "", "author": "", "date": ""}
            commits.append(commit)
        elif line.startswith("Author: "):
            commit["author"] = line[8:]
        elif line.startswith("Date: "):
            commit["date"] = datetime.datetime.strptime(
                line[6:].strip(), "%a %b %d %H:%M:%S %Y %z"
            )
        else:
            commit["message"] += line.strip() + "\n"
    return commits


def get_branches(project):
    """dictionary of git local branches for the project"""
    output = run("git branch", project)
    branches = {"current": "", "other": []}
    for line in output.split("\n"):
        if line.startswith("* "):
            branches["current"] = line[2:]
        elif not line == "":
            branches["other"].append(line[2:])
    return branches


def is_git_repo(project):
    return os.path.exists(os.path.join(FOLDER, project, ".git/config"))


class Logged(Fixture):
    def __init__(self, session):
        self.__prerequisites__ = [session]
        self.session = session

    def on_request(self):
        user = self.session.get("user")
        if not user or not user.get("id"):
            abort(403)


authenticated = ActionFactory(Logged(session))
session_secured = action.uses(Logged(session))


@action("version")
def version():
    return __version__


if MODE in ("demo", "readonly", "full"):

    @action("index")
    @action.uses("index.html", session, T)
    def index():
        return dict(
            languages=dumps(getattr(T.local, 'language', {})),
            mode=MODE,
            user_id=(session.get("user") or {}).get("id"),
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

    @action("dbadmin")
    @action.uses(Logged(session), "dbadmin.html")
    def dbadmin():
        return dict(languages=dumps(getattr(T.local, 'language', {})))

    @action("info")
    @session_secured
    def info():
        vars = [{"name": "python", "version": sys.version}]
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
    def routes():
        """Returns current registered routes"""
        return {"payload": Reloader.ROUTES, "status": "success"}

    @action("apps")
    @session_secured
    def apps():
        """Returns a list of installed apps"""
        apps = os.listdir(FOLDER)
        apps = [
            {"name": app, "error": Reloader.ERRORS.get(app)}
            for app in apps
            if os.path.isdir(os.path.join(FOLDER, app))
            and not app.startswith("__")
            and not app.startswith(".")
        ]
        apps.sort(key=lambda item: item["name"])
        return {"payload": apps, "status": "success"}

    @action("delete_app/<name:re:\w+>", method="POST")
    @session_secured
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

    @action("new_file/<name:re:\w+>/<file_name:path>", method="POST")
    @session_secured
    def new_file(name, file_name):
        """asign an sanitize inputs"""
        path = os.path.join(FOLDER, name)
        form = request.json
        if not os.path.exists(path):
            return {"status": "success", "payload": "App does not exist"}
        full_path = os.path.join(path, file_name)
        if not full_path.startswith(path + os.sep):
            return {"status": "success", "payload": "Invalid path"}
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
    def walk(path):
        """Returns a nested folder structure as a tree"""
        top = os.path.join(FOLDER, path)
        if not os.path.exists(top) or not os.path.isdir(top):
            return {"status": "error", "message": "folder does not exist"}
        store = {}
        for root, dirs, files in os.walk(top, topdown=False):
            store[root] = {
                "dirs": list(
                    sorted(
                        [
                            {"name": dir, "content": store[os.path.join(root, dir)]}
                            for dir in dirs
                            if dir[0] != "." and dir[:2] != "__"
                        ],
                        key=lambda item: item["name"],
                    )
                ),
                "files": list(
                    sorted(
                        [
                            f
                            for f in files
                            if f[0] != "." and f[-1] != "~" and f[-4:] != ".pyc"
                        ]
                    )
                ),
            }
        return {"payload": store[top], "status": "success"}

    @action("load/<path:path>")
    @session_secured
    def load(path):
        """Loads a text file"""
        path = safe_join(FOLDER, path) or abort()
        content = open(path, "rb").read().decode("utf8")
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
        appname = sanitize(appname)
        app_dir = os.path.join(FOLDER, appname)
        store = io.BytesIO()
        zip = zipfile.ZipFile(store, mode="w")
        for root, dirs, files in os.walk(app_dir, topdown=False):
            if not root.startswith("."):
                for name in files:
                    if not (
                        name.endswith("~") or name.endswith(".pyc") or name[:1] in "#."
                    ):
                        filename = os.path.join(root, name)
                        short = filename[len(app_dir + os.path.sep) :]
                        print("added", filename, short)
                        zip.write(filename, short)
        zip.close()
        data = store.getvalue()
        response.headers["Content-Type"] = "application/zip"
        return data

    @action("tickets")
    @session_secured
    def tickets():
        """Returns most recent tickets grouped by path+error"""
        tickets = error_storage.get()
        return {"payload": tickets}

    @action("clear")
    @session_secured
    def clear_tickets():
        error_storage.clear()

    @action("ticket/<ticket_uuid>")
    @action.uses("ticket.html")
    @session_secured
    def error_ticket(ticket_uuid):
        return dict(ticket=ErrorStorage().get(ticket_uuid=ticket_uuid))

    @action("rest/<path:path>", method=["GET", "POST", "PUT", "DELETE"])
    @session_secured
    def api(path):
        # this is not final, requires pydal 19.5
        args = path.split("/")
        app_name = args[0]
        from py4web.core import Reloader, DAL
        from pydal.restapi import RestAPI, Policy

        if MODE != "full":
            raise HTTP(403)
        module = Reloader.MODULES[app_name]

        def url(*args):
            return request.url + "/" + "/".join(args)

        databases = [
            name for name in dir(module) if isinstance(getattr(module, name), DAL)
        ]
        if len(args) == 1:

            def tables(name):
                db = getattr(module, name)
                return [
                    {
                        "name": t._tablename,
                        "fields": t.fields,
                        "link": url(name, t._tablename) + "?model=true",
                    }
                    for t in getattr(module, name)
                ]

            return {
                "databases": [
                    {"name": name, "tables": tables(name)} for name in databases
                ]
            }
        elif len(args) > 2 and args[1] in databases:
            db = getattr(module, args[1])
            id = args[3] if len(args) == 4 else None
            policy = Policy()
            for table in db:
                policy.set(
                    table._tablename,
                    "GET",
                    authorize=True,
                    allowed_patterns=["**"],
                    allow_lookup=True,
                    fields=table.fields,
                )
                policy.set(table._tablename, "PUT", authorize=True, fields=table.fields)
                policy.set(
                    table._tablename, "POST", authorize=True, fields=table.fields
                )
                policy.set(table._tablename, "DELETE", authorize=True)
            data = action.uses(db, T)(
                lambda: RestAPI(db, policy)(
                    request.method, args[2], id, request.query, request.json
                )
            )()
        else:
            data = {}
        if "code" in data:
            response.status = data["code"]
        return data


if MODE == "full":

    @action("reload")
    @action("reload/<name>")
    @session_secured
    def reload(name=None):
        """Reloads installed apps"""
        Reloader.import_app(name) if name else Reloader.import_apps()
        return "ok"

    @action("save/<path:path>", method="POST")
    @session_secured
    def save(path, reload_app=True):
        """Saves a file"""
        app_name = path.split("/")[0]
        path = safe_join(FOLDER, path) or abort()
        with open(path, "wb") as myfile:
            myfile.write(request.body.read())
        if reload_app:
            Reloader.import_app(app_name)
        return {"status": "success"}

    @action("delete/<path:path>", method="POST")
    @session_secured
    def delete(path):
        """Deletes a file"""
        fullpath = safe_join(FOLDER, path) or abort()
        recursive_unlink(fullpath)
        return {"status": "success"}

    def install_by_unzip_or_treecopy(source, source_dir, target_dir):
        """Installs an app by either unzipping it (if py4web installed from pip)
        or by copying the directory tree (if installed from source)."""
        if os.path.exists(source):
            zfile = zipfile.ZipFile(source, "r")
            zfile.extractall(target_dir)
            zfile.close()
        else:
            shutil.copytree(source_dir, target_dir)

    def prepare_target_dir(form, target_dir):
        """Prepares the target directory for the new app.
        If should_exist is False, leaves the directory blank."""
        if form["mode"] == "new":
            if os.path.exists(target_dir):
                abort(500)  # already validated client side
        elif form["mode"] == "replace":
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            else:
                abort(500)  # not a replacement

    @action("new_app", method="POST")
    @session_secured
    def new_app():
        form = request.json
        # Directory for zipped assets
        assets_dir = os.path.join(os.path.dirname(py4web.__file__), "assets")
        target_dir = safe_join(FOLDER, form["name"])
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
                zfile = zipfile.ZipFile(mem_zip, "r")
                zfile.extractall(target_dir)
                zfile.close()
            elif source.endswith(".git"):  # clone from a git repo
                process = subprocess.Popen(
                    ["git", "clone", source, form["name"]], cwd=FOLDER
                )
                process.communicate()
                if process.returncode != 0:
                    abort(500)
        elif form["type"] == "upload":
            prepare_target_dir(form, target_dir)
            source_stream = io.BytesIO(base64.b64decode(form["file"]))
            zfile = zipfile.ZipFile(source_stream, "r")
            zfile.extractall(target_dir)
            zfile.close()
        else:
            abort(500)
        settings = os.path.join(target_dir, "settings.py")
        if os.path.exists(settings):
            with open(settings) as fp:
                data = fp.read()
            data = data.replace("<session-secret-key>", str(uuid.uuid4()))
            with open(settings, "w") as fp:
                fp.write(data)
        return {"status": "success"}

    #
    # Below here work in progress
    #

    @action("gitlog/<project>")
    @action.uses(Logged(session), "gitlog.html")
    def gitlog(project):
        if not is_git_repo(project):
            return "Project is not a GIT repo"
        branches = get_branches(project)
        commits = get_commits(project)
        return dict(
            commits=commits, checkout=checkout, project=project, branches=branches
        )

    @authenticated.callback()
    def checkout(project, commit):
        if not is_git_repo(project):
            raise HTTP(400)
        run("git stash", project)
        run("git checkout " + commit, project)
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
        return diff2kryten(patch)

    @action("gitshow/<project>/<commit>")
    @action.uses(Logged(session), "gitshow.html")
    def gitshow(project, commit):
        if not is_git_repo(project):
            raise HTTP(400)
        flag = request.params.get("showfull")
        opt = ""
        if flag == "true":
            opt = " -U9999"
        patch = run("git show " + commit + opt, project)
        return diff2kryten(patch)
