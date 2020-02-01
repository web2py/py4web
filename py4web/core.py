#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Standard modules
import argparse
import cgitb
import datetime
import functools
import importlib
import importlib.machinery
import inspect
import json
import linecache
import logging
import numbers
import os
import getpass
import platform
import sys
import threading
import time
import traceback
import types
import urllib.parse
import uuid
import http.client
import http.cookies
import zipfile

# Optional web servers for speed
try:
    import gunicorn
except ImportError:
    gunicorn = None
try:
    import gevent
    import gevent.monkey

    gevent.monkey.patch_all()
except ImportError:
    gevent = None

# Third party modules
import jwt  # this is PyJWT
import bottle
import yatl
import threadsafevariable
import pydal
import pluralize
from pydal._compat import to_native, to_bytes

__all__ = [
    "render",
    "DAL",
    "Field",
    "action",
    "request",
    "response",
    "redirect",
    "abort",
    "HTTP",
    "Session",
    "Cache",
    "user_in",
    "Translator",
    "URL",
    "check_compatible",
    "wsgi",
]

DEFAULTS = dict(
    PY4WEB_APPS_FOLDER="apps",
    PY4WEB_SERVICE_FOLDER=".service",
    PY4WEB_SERVICE_DB_URI="sqlite://service.storage",
)

ART = r"""
██████╗ ██╗   ██╗██╗  ██╗██╗    ██╗███████╗██████╗
██╔══██╗╚██╗ ██╔╝██║  ██║██║    ██║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ███████║██║ █╗ ██║█████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ╚════██║██║███╗██║██╔══╝  ██╔══██╗
██║        ██║        ██║╚███╔███╔╝███████╗██████╔╝
╚═╝        ╚═╝        ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝
Is still experimental...
"""

Field = pydal.Field
render = yatl.render
request = bottle.request
response = bottle.response
abort = bottle.abort

os.environ.update(
    {key: value for key, value in DEFAULTS.items() if not key in os.environ}
)

########################################################################################
# Implement a O(1) LRU cache and memoize with expiration and monitoring (using linked list)
#########################################################################################


class Node:
    def __init__(self, key=None, value=None, t=None, m=None, prev=None, next=None):
        self.key, self.value, self.t, self.m, self.prev, self.next = (
            key,
            value,
            t,
            m,
            prev,
            next,
        )


class Cache:
    """
    O(1) caching object that remembers the 'size' most recent values
    Example:

        cache = Cache(size=1000)
        h = cache.get(filename, lambda: hash(
            open(filename).read()), 60, lambda: os.path.getmtime())

    (computes and cashes the hash of file filename but only reads the file if mtime changes and
     does not check the mtime more oftern than every 60. caches the 1000 most recent hashes)
    """

    def __init__(self, size=1000):
        self.free = size
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {}

    def get(self, key, callback, expiration=3600, monitor=None):
        """If key not stored or key has expired and monitor == None or monitor() value has changed, returns value = callback()"""
        node, t0 = self.mapping.get(key), time.time()
        if node:
            value, t, node.next.prev, node.prev.next = (
                node.value,
                node.t,
                node.prev,
                node.next,
            )
        if not node:
            self.free -= 1
        m = monitor and monitor()
        if node and node.t + expiration < t0:
            if m is None or node.m != m:
                node = None
        if node is None:
            value, t = callback(), t0
        new_node = Node(key, value, t, m, prev=self.head, next=self.head.next)
        self.mapping[key] = self.head.next = new_node.next.prev = new_node
        if self.free < 0:
            last_node = self.tail.prev
            self.tail.prev, last_node.prev.next = last_node.prev, self.tail
            del self.mapping[last_node.key]
            self.free += 1
        return value

    def memoize(self, expiration=3600):
        def decorator(func):
            @functools.wraps(func)
            def memoized_func(*args, **kwargs):
                key = "%s:%s:%s:%s" % (func.__module__, func.__name__, args, kwargs)
                return self.get(
                    key,
                    lambda args=args, kwargs=kwargs: func(*args, **kwargs),
                    expiration=expiration,
                )

            return memoized_func

        return decorator


#########################################################################################
# A Better JSON Serializer
#########################################################################################


def objectify(obj):
    """converts the obj(ect) into a json serializable object"""
    if isinstance(obj, numbers.Integral):
        return int(obj)
    elif isinstance(obj, (numbers.Rational, numbers.Real)):
        return float(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime, datetime.time)):
        return obj.isoformat()
    elif isinstance(obj, str):
        return obj
    elif hasattr(obj, "__iter__") or isinstance(obj, types.GeneratorType):
        return list(obj)
    elif hasattr(obj, 'xml'):
        return obj.xml()
    elif hasattr(obj, "__dict__") and hasattr(obj, "__class__"):
        d = dict(obj.__dict__)
        d["__class__"] = obj.__class__.__name__
        return d
    return str(obj)


def dumps(obj, sort_keys=True, indent=2):
    return json.dumps(obj, default=objectify, sort_keys=sort_keys, indent=indent)


#########################################################################################
# Base Fixture (database connections, templates, sessions, and requirements are fixtures)
#########################################################################################


class Fixture:
    def on_request(self):
        pass  # called when a request arrives

    def on_error(self):
        pass  # called when a request errors

    def on_success(self):
        pass  # called when a request is successful

    def transform(self, output):  # transforms the output, for example to apply template
        return output


class Translator(pluralize.Translator, Fixture):
    def on_request(self):
        self.select(request.headers.get("Accept-Language", "en"))

    def on_success(self):
        response.headers["Content-Language"] = self.local.tag


class DAL(pydal.DAL, Fixture):
    def on_request(self):
        threadsafevariable.ThreadSafeVariable.restore(ICECUBE)

    def on_error(self):
        self.rollback()

    def on_success(self):
        self.commit()


# make sure some variables in pydal are thread safe
for _ in ["readable", "writable", "default", "update", "requires"]:
    setattr(pydal.DAL.Field, _, threadsafevariable.ThreadSafeVariable())

# this global object will be used to store their state to restore it for every http request
ICECUBE = {}

#########################################################################################
# The Template Rendered Fixture
#########################################################################################


class Template(Fixture):

    cache = Cache(100)

    def __init__(self, filename, path=None, delimiters="[[ ]]"):
        self.filename = filename
        self.path = path
        self.delimiters = delimiters

    @staticmethod
    def reader(filename):
        """Cached file reader, only reads template if it has changed"""

        def raw_read():
            with open(filename, encoding="utf8") as stream:
                return stream.read()

        return Template.cache.get(
            filename, raw_read, expiration=1, monitor=lambda: os.path.getmtime(filename)
        )

    def transform(self, output):
        if not isinstance(output, dict):
            return output
        context = dict(request=request)
        context.update(yatl.helpers.__dict__)
        context.update(URL=URL)
        context.update(output)
        context["__vars__"] = output
        app_folder = os.path.join(os.environ["PY4WEB_APPS_FOLDER"], request.app_name)
        path = self.path or os.path.join(app_folder, "templates")        
        filename = os.path.join(path, self.filename)
        if not os.path.exists(filename):
            generic_filename = os.path.join(path, 'generic.html')
            if os.path.exists(generic_filename):
                filename = generic_filename
        output = yatl.render(
            Template.reader(filename),
            path=path,
            context=context,
            delimiters=self.delimiters,
            reader=Template.reader,
        )
        return output


#########################################################################################
# The Session Fixture
#########################################################################################


class Session(Fixture):

    # All apps share the same default secret if not specified. important for _dashboard reload
    SECRET = None

    def __init__(
        self,
        secret=None,
        expiration=None,
        algorithm="HS256",
        storage=None,
        same_site="Lax",
    ):
        """
        secret is the shared key used to encrypt the session (using algorithm)
        expiration is in seconds
        (optional) storage must have a get(key) and set(key,value,expiration) methods
        if not provided session is stored in jwt cookie else the jwt is stored in storage and its uuid key is stored in the cookie
        """
        if not secret and not storage:
            # when no secret is specified: one time sessions
            secret = Session.SECRET = Session.SECRET or str(uuid.uuid4())
        self.secret = secret
        self.expiration = expiration
        self.algorithm = algorithm
        self.local = threading.local()
        self.local.changed = False
        self.local.secure = None
        self.local.data = {}
        self.storage = storage
        self.same_site = same_site
        if isinstance(storage, Session):
            self.__prerequisites__ = [storage]
        if hasattr(storage, "__prerequisites__"):
            self.__prerequisites__ = storage.__prerequisites__

    def load(self):
        self.local.session_cookie_name = "%s_session" % request.app_name
        self.local.changed = False
        self.local.secure = request.url.startswith("https")
        self.local.data = {}
        raw_token = request.get_cookie(
            self.local.session_cookie_name
        ) or request.query.get("_session_token")
        if not raw_token and request.method in ("POST", "PUT", "DELETE"):
            raw_token = (request.forms and request.forms.get("_session_token")) or (
                request.json and request.json and request.json.get("_session_token")
            )
        if raw_token:
            token_data = to_bytes(raw_token)
            try:
                if self.storage:
                    json_data = self.storage.get(token_data)
                    if json_data:
                        self.local.data = json.loads(json_data)
                else:
                    self.local.data = jwt.decode(
                        token_data, self.secret, algorithms=[self.algorithm]
                    )
                if self.expiration is not None and self.storage is None:
                    assert self.local.data["timestamp"] > time.time() - int(
                        self.expiration
                    )
                assert self.local.data.get("secure") == self.local.secure
            except Exception:
                pass
        if not "uuid" in self.local.data:
            self.local.changed = True
            self.local.data["uuid"] = str(uuid.uuid4())
            self.local.data["secure"] = self.local.secure

    def save(self):
        self.local.data["timestamp"] = time.time()
        if self.storage:
            cookie_data = self.local.data["uuid"]
            self.storage.set(cookie_data, json.dumps(self.local.data), self.expiration)
        else:
            cookie_data = jwt.encode(
                self.local.data, self.secret, algorithm=self.algorithm
            )

        response.set_cookie(
            self.local.session_cookie_name,
            to_native(cookie_data),
            path="/",
            secure=self.local.secure,
            same_site=self.same_site,
        )

    def get(self, key, default=None):
        return self.local.data.get(key, default)

    def __getitem__(self, key):
        return self.local.data[key]

    def __setitem__(self, key, value):
        self.local.changed = True
        self.local.data[key] = value

    def on_request(self):
        self.load()

    def on_error(self):
        if self.local.changed:
            self.save()

    def on_success(self):
        if self.local.changed:
            self.save()


#########################################################################################
# The URL Helper
#########################################################################################


def URL(*parts, vars=None, hash=None, scheme=False):
    """
    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{app_name}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{app_name}/a/b?x=1
    """
    prefix = "/%s/" % request.app_name if request.app_name != "_default" else "/"
    broken_parts = []
    for part in parts:
        broken_parts += str(part).rstrip('/').split("/")
    url = prefix + "/".join(map(lambda x: urllib.parse.quote(x), broken_parts))
    if vars:
        url += "?" + "&".join(
            "%s=%s" % (k, urllib.parse.quote(str(v))) for k, v in vars.items()
        )
    if hash:
        url += "#%s" % hash
    if not scheme is False:
        orig_scheme, _, domain = request.url.split("/")[:3]
        scheme = (
            orig_scheme if scheme is True else "" if scheme is None else scheme + ":"
        )
        url = "%s//%s%s" % (scheme, domain, url)
    return url


#########################################################################################
# The Action Decorator
#########################################################################################


class HTTP(BaseException):
    """Our HTTP exception does not delete cookies and headers like the bottle.HTTPResponse does;
    since it is considered a success, not a failure"""

    def __init__(self, status):
        self.status = status


def redirect(location):
    """our redirect does not delete cookies and headers like bottle.HTTPResponse does;
    it is considered a success, not failure"""
    response.set_header("Location", location)
    raise HTTP(303)


class action:
    """@action(...) is a decorator for functions to be exposed as actions"""

    current = threading.local()
    registered = set()
    app_name = "_default"

    def __init__(self, path, **kwargs):
        self.path = path
        self.kwargs = kwargs

    @staticmethod
    def uses(*fixtures_in):
        """Find all fixtures, including dependencies, topologically sorted"""
        fixtures = []
        reversed_fixtures = []
        stack = list(fixtures_in)
        while stack:
            fixture = stack.pop()
            reversed_fixtures.append(fixture)
            for other in getattr(fixture, "__prerequisites__", []):
                stack.append(other)
        for fixture in reversed(reversed_fixtures):
            if isinstance(fixture, str):
                fixture = Template(fixture)
            if not fixture in fixtures:
                fixtures.append(fixture)

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    [obj.on_request() for obj in fixtures]
                    ret = func(*args, **kwargs)
                    for obj in fixtures:
                        ret = obj.transform(ret)
                    [obj.on_success() for obj in fixtures]
                    return ret
                except HTTP:
                    [obj.on_success() for obj in fixtures]
                    raise
                except Exception:
                    [obj.on_error() for obj in fixtures]
                    raise
            return wrapper

        return decorator

    @staticmethod
    def requires(*requirements):
        """Enforces requirements or calls bottle.abort(401)"""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for requirement in requirements:
                    if not requirement():
                        bottle.abort(401)
                return func(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def catch_errors(app_name, func):
        """Catches and logs errors in an action; also sets request.app_name"""

        @functools.wraps(func)
        def wrapper(*func_args, **func_kwargs):
            try:
                request.app_name = app_name
                ret = func(*func_args, **func_kwargs)
                if isinstance(ret, dict):
                    response.headers["Content-Type"] = "application/json"
                    ret = dumps(ret)
                return ret
            except HTTP as http:
                response.status = http.status
                return ""
            except bottle.HTTPResponse:
                raise
            except Exception:
                logging.error(traceback.format_exc())
                try:
                    ticket = ErrorStorage().log(request.app_name, get_error_snapshot())
                except Exception:
                    logging.error(traceback.format_exc())
                    ticket = "unknown"
                return error_page(
                    500, button_text=ticket, href="/_dashboard/ticket/" + ticket
                )
        return wrapper

    def __call__(self, func):
        """Building the decorator"""
        app_name = action.app_name
        path = (
            "/" if app_name == "_default" else "/%s/" % app_name
        ) + self.path  # the _default app has no prefix
        if not func in self.registered:
            func = action.catch_errors(app_name, func)
        func = bottle.route(path, **self.kwargs)(func)
        if path.endswith("/index"):  # /index is always optional
            func = bottle.route(path[:-6] or "/", **self.kwargs)(func)
        self.registered.add(func)
        return func


def user_in(session):
    def requirement():
        session.on_request()
        return session.get("user", None) is not None

    return requirement


#########################################################################################
# Monkey Patch: Cookies
#########################################################################################

http.cookies.Morsel._reserved["same-site"] = "SameSite"

#########################################################################################
# Monkey Patch: ssl bug for gevent
#########################################################################################

__ssl__ = __import__("ssl")
_ssl = getattr(__ssl__, "_ssl") or getattr(__ssl__, "_ssl2")

if not hasattr(_ssl, "sslwrap"):

    def new_sslwrap(
        sock,
        server_side=False,
        keyfile=None,
        certfile=None,
        cert_reqs=__ssl__.CERT_NONE,
        ssl_version=__ssl__.PROTOCOL_SSLv23,
        ca_certs=None,
        ciphers=None,
    ):
        context = __ssl__.SSLContext(ssl_version)
        context.verify_mode = cert_reqs or __ssl__.CERT_NONE
        if ca_certs:
            context.load_verify_locations(ca_certs)
        if certfile:
            context.load_cert_chain(certfile, keyfile)
        if ciphers:
            context.set_ciphers(ciphers)
        caller_self = inspect.currentframe().f_back.f_locals["self"]
        return context._wrap_socket(sock, server_side=server_side, ssl_sock=caller_self)

    _ssl.sslwrap = new_sslwrap

#########################################################################################
# Error Handling
#########################################################################################


def get_error_snapshot(depth=5):
    """Return a dict describing a given traceback (based on cgitb.text)."""

    etype, evalue, etb = sys.exc_info()
    if isinstance(etype, type):
        etype = etype.__name__

    data = {}
    data["timestamp"] = datetime.datetime.utcnow().isoformat()
    data["python_version"] = sys.version
    platform_keys = [
        "machine",
        "node",
        "platform",
        "processor",
        "python_branch",
        "python_build",
        "python_compiler",
        "python_implementation",
        "python_revision",
        "python_version",
        "python_version_tuple",
        "release",
        "system",
        "uname",
        "version",
    ]

    data["platform_info"] = {key: getattr(platform, key)() for key in platform_keys}
    data["os_environ"] = {key: str(value) for key, value in os.environ.items()}
    data["traceback"] = traceback.format_exc()
    data["exception_type"] = str(etype)
    data["exception_value"] = str(evalue)

    # Loopover the stack frames
    items = inspect.getinnerframes(etb, depth)
    del etb  # Prevent circular references that would cause memory leaks
    data["stackframes"] = stackframes = []

    for frame, file, lnum, func, lines, idx in items:
        file = file and os.path.abspath(file) or "?"
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        # Basic frame information
        f = {"file": file, "func": func, "lnum": lnum}
        f["code"] = lines
        # FIXME: disable this for now until we understand why this goes into infinite loop
        if False:
            line_vars = cgitb.scanvars(lambda: linecache.getline(file, lnum), frame, locals)
            # Dump local variables (referenced in current line only)
            f["vars"] = {
                key: repr(value)
                for key, value in locals.items()
                if not key.startswith("__")
                }
        stackframes.append(f)

    return data


class ErrorStorage:
    def __init__(self):
        apps_folder = os.environ["PY4WEB_APPS_FOLDER"]
        uri = os.environ["PY4WEB_SERVICE_DB_URI"]
        folder = os.path.join(apps_folder, os.environ["PY4WEB_SERVICE_FOLDER"])
        self.db = DAL(uri, folder=folder)
        self.db.define_table(
            "py4web_error",
            Field("uuid"),
            Field("app_name"),
            Field("method"),
            Field("path", "string"),
            Field("timestamp", "datetime"),
            Field("client_ip", "string"),
            Field("error", "string"),
            Field("snapshot", "json"),
        )
        self.db.commit()

    def log(self, app_name, error_snapshot):
        ticket_uuid = str(uuid.uuid4())
        try:
            id = self.db.py4web_error.insert(
                uuid=ticket_uuid,
                app_name=app_name,
                method=request.method,
                path=request.path,
                timestamp=datetime.datetime.utcnow(),
                client_ip=request.environ.get("REMOTE_ADDR"),
                error=error_snapshot["exception_value"],
                snapshot=error_snapshot,
            )
            self.db.commit()
            return ticket_uuid
        except Exception:
            self.db.rollback()
            return "internal-error"

    def get(self, ticket_uuid=None):
        db = self.db
        if ticket_uuid:
            query, orderby = db.py4web_error.uuid == ticket_uuid, None
            rows = db(query).select(orderby=orderby, limitby=(0, 1)).as_list()
        else:
            orderby = ~db.py4web_error.timestamp
            groupby = db.py4web_error.path | db.py4web_error.error
            query = db.py4web_error.timestamp > datetime.datetime.now() - datetime.timedelta(
                days=7
            )
            fields = [field for field in db.py4web_error if not field.type == "json"]
            fields.append(db.py4web_error.id.count())
            list_rows = (
                db(query).select(*fields, orderby=orderby, groupby=groupby).as_list()
            )
            rows = []
            for item in list_rows:
                row = item["py4web_error"]
                row["count"] = item["_extra"][str(db.py4web_error.id.count())]
                rows.append(row)
        return rows if not ticket_uuid else rows[0] if rows else None


#########################################################################################
# Loading &  Reloading Logic
#########################################################################################


class Reloader:

    ROUTES = []
    MODULES = {}
    ERRORS = {}

    @staticmethod
    def import_apps():
        """Import or reimport modules and exposed static files"""
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        app = bottle.default_app()
        app.routes.clear()
        new_apps = []
        # if first time reload dummy top module
        if not Reloader.MODULES:
            path = os.path.join(folder, "__init__.py")
            module = importlib.machinery.SourceFileLoader("apps", path).load_module()
        # Then load all the apps as submodules
        for app_name in os.listdir(folder):
            action.app_name = app_name
            new_apps += Reloader.import_app(app_name)
        # Expose static files with support for static asset management
        for path in new_apps:
            static_folder = os.path.join(path, "static")
            if os.path.exists(static_folder):
                app_name = path.split(os.path.sep)[-1]
                prefix = "" if app_name == "_default" else ("/%s" % app_name)

                @bottle.route(prefix + "/static/<filename:path>")
                @bottle.route(
                    prefix + "/static/_<version:re:\\d+\\.\\d+\\.\\d+>/<filename:path>"
                )
                def server_static(filename, static_folder=static_folder, version=None):
                    return bottle.static_file(filename, root=static_folder)

        # Register routes list
        routes = []

        def to_filename(module):
            filename = os.path.join(*module.split(".")[1:])
            filename = (
                os.path.join(filename, "__init__.py")
                if not filename.count(os.sep)
                else filename + ".py"
            )
            return filename

        for route in app.routes:
            func = route.callback
            routes.append(
                {
                    "rule": route.rule,
                    "method": route.method,
                    "filename": to_filename(func.__module__),
                    "action": func.__name__,
                }
            )
        Reloader.ROUTES = sorted(routes, key=lambda item: item["rule"])
        ICECUBE.update(threadsafevariable.ThreadSafeVariable.freeze())

    @staticmethod
    def import_app(app_name):
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        path = os.path.join(folder, app_name)
        init = os.path.join(path, "__init__.py")
        new_apps = []
        if os.path.isdir(path) and not path.endswith("__") and os.path.exists(init):
            module_name = "apps.%s" % app_name
            try:
                module = Reloader.MODULES.get(app_name)
                if not module:
                    print("[ ] loading %s ..." % app_name)
                    module = importlib.machinery.SourceFileLoader(
                        module_name, init
                    ).load_module()
                    new_apps.append(path)
                    print("\x1b[A[X] loaded %s     " % app_name)
                else:
                    print("[ ] reloading %s ..." % app_name)
                    names = [
                        name
                        for name in sys.modules
                        if (name + ".").startswith(module_name + ".")
                    ]
                    for name in names:
                        try:
                            importlib.reload(sys.modules[name])
                        except ModuleNotFoundError:
                            pass
                    print("\x1b[A[X] reloaded %s     " % app_name)
                Reloader.MODULES[app_name] = module
                Reloader.ERRORS[app_name] = None
            except:
                tb = traceback.format_exc()
                print("\x1b[A[FAILED] loading %s     \n%s\n" % (app_name, tb))
                Reloader.ERRORS[app_name] = tb
        return new_apps


#########################################################################################
# Web Server and Reload Logic: Error Handling
#########################################################################################


def error_page(code, button_text=None, href="#", color=None, message=None):
    message = http.client.responses[code].upper() if message is None else message
    color = (
        {"4": "#F44336", "5": "#607D8B"}.get(str(code)[0], "#2196F3")
        if not color
        else color
    )
    return yatl.render(
        '<html><head><style>body{color:white;text-align: center;background-color:{{=color}};font-family:serif} h1{font-size:6em;margin:16vh 0 8vh 0} h2{font-size:2em;margin:8vh 0} a{color:white;text-decoration:none;font-weight:bold;padding:10px 10px;border-radius:10px;border:2px solid #fff;transition: all .5s ease} a:hover{background:rgba(0,0,0,0.1);padding:10px 30px}</style></head><body><h1>{{=code}}</h1><h2>{{=message}}</h2>{{if button_text:}}<a href="{{=href}}">{{=button_text}}</a>{{pass}}</body></html>',
        context=dict(
            code=code, message=message, button_text=button_text, href=href, color=color
        ),
    )


@bottle.error(404)
def error404(error):
    guess_app_name = request.path.split("/")[1]
    return error_page(404, button_text=guess_app_name, href="/" + guess_app_name)


#########################################################################################
# Web Server and Reload Logic: Operations
#########################################################################################


def start_server(args):
    host, port = args.host, int(args.port)
    if platform.system().lower() == "windows":
        # Tornado fail on windows
        bottle.run(host=host, port=int(port), reloader=False)
    elif args.number_workers < 1:
        bottle.run(server="tornado", host=host, port=port, reloader=False)
    else:
        if not gunicorn:
            logging.error("gunicorn not installed")
        elif not gevent:
            logging.error("gevent not installed")
        else:
            sys.argv[:] = sys.argv[:1]  # else break gunicorn
            bottle.run(
                server="gunicorn",
                host=host,
                port=port,
                workers=args.number_workers,
                worker_class="gevent",
                reloader=False,
                certfile=args.ssl_cert_filename,
                keyfile=args.ssl_key_filename,
            )


def check_compatible(version):
    """To be called by apps to check if module version is compatible with py4web requirements"""
    from . import __version__

    return tuple(map(int, __version__.split("."))) >= tuple(
        map(int, version.split("."))
    )


def wsgi(**args):
    """Initializes everything, loads apps, returns the wsgi app"""
    initialize(**args)
    Reloader.import_apps()
    return bottle.default_app()


def get_args():
    """Handle command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("apps_folder", help="Path to the applications folder")
    parser.add_argument(
        "--host", default="127.0.0.1", help="Server address (IP or hostname)"
    )
    parser.add_argument("--port", default="8000", help="Port number (e.g., 8000)")
    parser.add_argument(
        "--headless",
        default=False,
        action="store_true",
        help="Hide artwork for console access",
    )
    parser.add_argument(
        "-n",
        "--number_workers",
        default=0,
        type=int,
        help="Number of gunicorn workers to utilize",
    )
    parser.add_argument(
        "--ssl_cert_filename",
        default=None,
        type=int,
        help="Custom ssl certificate file",
    )
    parser.add_argument(
        "--ssl_key_filename", default=None, type=int, help="Custom ssl key file"
    )
    parser.add_argument(
        "--service_folder",
        default=".service",
        type=str,
        help="Service Information Storage Location",
    )
    parser.add_argument(
        "--service_db_uri",
        default="sqlite://service.storage",
        type=str,
        help="Alternative db uri for service logs",
    )
    parser.add_argument(
        "-d",
        "--dashboard_mode",
        default="full",
        help="Dashboard mode: demo, readonly, full (default), none",
    )
    parser.add_argument(
        "-p",
        "--password_file",
        default="password.txt",
        help="File containing the encrypted (CRYPT) password",
    )
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        default=False,
        help="Create missing system apps",
    )
    # Parse command line arguments
    args = parser.parse_args()
    return args


def initialize(**args):
    """Initialize from args"""
    for key in args:
        os.environ["PY4WEB_" + key.upper()] = str(args[key])
    apps_folder = os.environ["PY4WEB_APPS_FOLDER"]
    service_folder = os.path.join(apps_folder, os.environ["PY4WEB_SERVICE_FOLDER"])
    # If the apps folder does not exist create it and populate it
    if not os.path.exists(apps_folder):
        os.makedirs(apps_folder)
        init_py = os.path.join(apps_folder, "__init__.py")
        if not os.path.exists(init_py):
            with open(init_py, "w") as fp:
                fp.write("")
        args["create"] = True
    if not os.path.exists(service_folder):
        os.mkdir(service_folder)
    # Upzip the _dashboard app if it is old or does not exist
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    if os.path.exists(assets_dir):
        apps = os.listdir(assets_dir)
        for filename in apps:
            zip_filename = os.path.join(assets_dir, filename)
            # These filenames do not necessarily exist if one has
            # downloaded from source and deleted them.
            target_dir = os.path.join(apps_folder, filename.split(".")[-2])
            if not os.path.exists(target_dir):
                if args.get("create"):
                    print("[ ] Unzipping app", filename)
                    zip_file = zipfile.ZipFile(zip_filename, "r")
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    zip_file.extractall(target_dir)
                    zip_file.close()
                    print("\x1b[A[X]")


def main(args=None):
    """The main entry point: Start the server and create folders"""
    # Store args in the action to make them visible
    action.args = args = args or get_args()
    if args.headless:
        headless = True
    else:
        headless = False
    if not headless:
        print(ART)
    else:
        print("")  # Insert a blank line to improve readability
    # If we know where the password is stored, read it, otherwise ask for one
    if args.dashboard_mode not in ("demo", "none") and not os.path.exists(
        args.password_file
    ):
        password = getpass.getpass("Choose a one-time dashboard password: ")
        print('Storing the hashed password in file "%s"' % args.password_file)
        with open(args.password_file, "w") as fp:
            fp.write(str(pydal.validators.CRYPT()(password)[0]))
    # Store all args in environment variables to make them available to the following processes
    # and create any missing folders
    initialize(**args.__dict__)
    if os.path.exists(os.path.join(args.apps_folder, "_dashboard")):
        print("Dashboard is at: http://%s:%s/_dashboard" % (args.host, args.port))
    # start
    Reloader.import_apps()
    start_server(args)
