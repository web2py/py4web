#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PY4WEB - a web framework for rapid development of efficient database driven web applications"""

# Standard modules
import asyncio
import cgitb
import code
import collections
import copy
import datetime
import enum
import functools
import http.client
import http.cookies
import importlib.machinery
import importlib.util
import inspect
import io
import json
import linecache
import logging
import numbers
import os
import pathlib
import platform
import re
import signal
import sys
import threading
import time
import traceback
import types
import urllib.parse
import uuid
import zipfile
from collections import OrderedDict
from contextlib import redirect_stdout, redirect_stderr

import portalocker
from watchgod import awatch

from . import server_adapters

# Optional web servers for speed
try:
    import gunicorn
except ImportError:
    gunicorn = None

import click

# Third party modules
import ombott as bottle
from ombott.request.helpers import FormsDict
import pluralize
import pydal
import renoir
import renoir.constants
import renoir.writers
import threadsafevariable
import yatl

from .utils.misc import secure_dumps, secure_loads

bottle.DefaultConfig.max_memfile_size = 16 * 1024 * 1024
bottle.DefaultConfig.app_name_header = "HTTP_X_PY4WEB_APPNAME"
# apply DefaultConfig changes to default_app
bottle.default_app().setup()

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
    "Flash",
    "Translator",
    "URL",
    "check_compatible",
    "required_folder",
    "wsgi",
    "Condition",
]

PY4WEB_CMD = sys.argv[0]

REGEX_APPJSON = r"(^|\s|,)application/json(,|\s|$)"

DEFAULTS = dict(
    PY4WEB_APPS_FOLDER="apps",
    PY4WEB_SERVICE_FOLDER=".service",
    PY4WEB_SERVICE_DB_URI="sqlite://service.storage",
)

HELPERS = {name: getattr(yatl.helpers, name) for name in yatl.helpers.__all__}

ART = r"""
 /#######  /##     /##/##   /## /##      /## /######## /####### 
| ##__  ##|  ##   /##/ ##  | ##| ##  /# | ##| ##_____/| ##__  ##
| ##  \ ## \  ## /##/| ##  | ##| ## /###| ##| ##      | ##  \ ##
| #######/  \  ####/ | ########| ##/## ## ##| #####   | ####### 
| ##____/    \  ##/  |_____  ##| ####_  ####| ##__/   | ##__  ##
| ##          | ##         | ##| ###/ \  ###| ##      | ##  \ ##
| ##          | ##         | ##| ##/   \  ##| ########| #######/
|__/          |__/         |__/|__/     \__/|________/|_______/
Is still experimental...
"""

Field = pydal.Field
request = bottle.request
response = bottle.response
abort = bottle.abort

# monkey patching bottle/ombott
sys.modules[FormsDict.__module__].urlunquote = urllib.parse.unquote
FormsDict.recode_unicode = False

os.environ.update(
    {key: value for key, value in DEFAULTS.items() if key not in os.environ}
)
os.environ["PY4WEB_PATH"] = str(pathlib.Path(__file__).resolve().parents[1])


# hold all framework hooks in one place
# NOTE: `after_request` hooks are not currently used
_REQUEST_HOOKS = types.SimpleNamespace(before=set())


def _before_request(*args, **kw):
    [h(*args, **kw) for h in _REQUEST_HOOKS.before]


bottle.default_app().add_hook("before_request", _before_request)


def module2filename(module):
    filename = os.path.join(*module.split(".")[1:])
    filename = (
        os.path.join(filename, "__init__.py")
        if not filename.count(os.sep)
        else filename + ".py"
    )
    return filename


def required_folder(*parts):
    """joins the args and creates the folder if not exists"""
    path = os.path.join(*parts)
    if not os.path.exists(path):
        os.makedirs(path)
    assert os.path.isdir(path), "%s is not a folder as required" % path
    return path


def safely(func, exceptions=(Exception,), log=False, default=None):
    """
    runs the funnction and returns True on success,
    False if one of the exceptions is raised
    """
    try:
        return func()
    except exceptions as err:
        if log:
            logging.warn(str(err))
        return default() if callable(default) else default


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
        self.lock = threading.Lock()

    def get(self, key, callback, expiration=3600, monitor=None):
        """If key not stored or key has expired and monitor == None or monitor() value has changed, returns value = callback()"""
        node, t0 = self.mapping.get(key), time.time()
        with self.lock:
            if node:
                # if a node was found remove it from storage
                value, t, node.next.prev, node.prev.next = (
                    node.value,
                    node.t,
                    node.prev,
                    node.next,
                )
            else:
                self.free -= 1
        # check if something may invalidate cache
        m = monitor() if monitor else None
        # check if cache expired
        if node and node.t + expiration < t0:
            # if cache should always be invalidated or m changed
            if m is None or node.m != m:
                # ignore the value found
                node = None
        if node is None:
            value, t = callback(), t0
        # add the new node back into storage
        with self.lock:
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
        return obj.isoformat().replace("T", " ")
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        return obj
    elif hasattr(obj, "as_list"):
        return obj.as_list()
    elif hasattr(obj, "as_dict"):
        return obj.as_dict()
    elif hasattr(obj, "__iter__") or isinstance(obj, types.GeneratorType):
        return list(obj)
    elif hasattr(obj, "xml"):
        return obj.xml()
    elif isinstance(
        obj, enum.Enum
    ):  # Enum class handled specially to address self reference in __dict__
        return dict(name=obj.name, value=obj.value, __class__=obj.__class__.__name__)
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

    __request_master_ctx__ = threading.local()
    __fixture_debug__ = False

    # normally on_success/on_error are only called if none of the previous
    # on_request failed, if a fixture is_hook then on_error is always called.
    is_hook = False

    @classmethod
    def __init_request_ctx__(cls):
        cls.__request_master_ctx__.request_ctx = dict()

    @classmethod
    def __mount_local__(cls, self, storage):
        cls.__request_master_ctx__.request_ctx[self] = storage

    @property
    def _safe_local(self):
        try:
            ret = self.__request_master_ctx__.request_ctx[self]
        except (KeyError, AttributeError) as err:
            msg = "py4web hint: check @action.uses() for the missing fixture {}".format(
                self
            )
            raise RuntimeError(msg) from err
        return ret

    @_safe_local.setter
    def _safe_local(self, storage):
        self.__mount_local__(self, storage)

    def is_valid(self):
        """check if the fixture is valid in context"""
        ctx = self.__request_master_ctx__.request_ctx
        if self not in ctx:
            logging.warn(
                "attempted access to fixture %s from outside a request",
                self.__class__.__name__,
            )
            return False
        return True

    def on_request(self, context):
        pass  # called when a request arrives

    def on_error(self, context):
        pass  # called when a request errors

    def on_success(self, context):
        pass  # called when a request is successful


_REQUEST_HOOKS.before.add(Fixture.__init_request_ctx__)


class Translator(pluralize.Translator, Fixture):
    def on_request(self, context):
        self.select(request.headers.get("Accept-Language", "en"))

    def on_success(self, context):
        response.headers["Content-Language"] = self.local.tag


class DAL(pydal.DAL, Fixture):
    def on_request(self, context):
        self.get_connection_from_pool_or_new()
        threadsafevariable.ThreadSafeVariable.restore(ICECUBE)

    def on_error(self, context):
        self.recycle_connection_in_pool_or_close("rollback")

    def on_success(self, context):
        self.recycle_connection_in_pool_or_close("commit")


# make sure some variables in pydal are thread safe
def thread_safe_pydal_patch():
    Field = pydal.DAL.Field
    tsafe_attrs = [
        "readable",
        "writable",
        "default",
        "filter_in",
        "filter_out",
        "label",
        "update",
        "requires",
        "widget",
        "represent",
    ]
    for a in tsafe_attrs:
        b = threadsafevariable.ThreadSafeVariable()
        setattr(Field, a, b)

    # hack 'copy.copy' behavior, since it makes a shallow copy,
    # but ThreadSafe-attributes (see above) are class-level, so:
    # no copy -> no attr in ICECUBE for the fresh one -> gevent-error on try to access to any of ThreadSafe-attributes
    def field_copy(self):
        # to prevent infinite recursion
        # temporarily set __copy__ to None
        me = self.__class__.__copy__
        self.__class__.__copy__ = None
        clone = copy.copy(self)
        self.__class__.__copy__ = me
        for a in tsafe_attrs:
            setattr(clone, a, getattr(self, a))
        return clone

    # to avoid possible future problems
    if hasattr(Field, "__copy__"):
        raise RuntimeError("code fix required!")
    setattr(Field, "__copy__", field_copy)


thread_safe_pydal_patch()

# this global object will be used to store their state to restore it for every http request
ICECUBE = {}


#########################################################################################
# Flash Fixture
#########################################################################################


class Flash(Fixture):
    """
    flash = Flash()

    @action('index')
    @action.uses(flash)
    def index():
        flash.set('hello', _class='important')
        return dict()

    Flash messages are added to the dict and, upon redirect, carry forward
    Also notice all Flash objects share the same threading local so act as singletons
    """

    # this essential makes flash a singleton
    # necessary because auth defines its own flash
    # possible because flash does not depend on the app

    @property
    def local(self):
        return self._safe_local

    def on_request(self, context):
        self._safe_local = types.SimpleNamespace()
        # when a new request arrives we look for a flash message in the cookie
        flash = request.get_cookie("py4web-flash")
        if flash:
            self.local.flash = json.loads(flash)
        else:
            self.local.flash = None

    def on_success(self, context):
        # if we redirect and have a flash message we move it to the session
        status = context["status"]
        if status == 303 and self.local.flash:
            response.set_cookie("py4web-flash", json.dumps(self.local.flash), path="/")
        else:
            response.delete_cookie("py4web-flash", path="/")
        context["output"] = self.transform(context["output"])
        self.local.__dict__.clear()

    def on_error(self, context):
        """Clears the local to prevent leakage."""
        self.local.__dict__.clear()

    def set(self, message, _class="", sanitize=True):
        # we set a flash message
        if sanitize:
            message = yatl.sanitizer.xmlescape(message)
        self.local.flash = {"message": message, "class": _class}

    def transform(self, data):
        # if we have a valid flash message, we inject it in the response dict
        if isinstance(data, dict):
            if "flash" not in data:
                data["flash"] = self.local.flash or ""
        else:
            if self.local.flash is not None:
                response.headers["component-flash"] = json.dumps(self.local.flash)
        self.local.flash = None
        return data


#########################################################################################
# The Template Rendered Fixture
#########################################################################################


class RenoirXMLEscapeMixin:
    def _escape_data(self, data):
        """Allows Renoir to convert yatl helpers to strings"""
        return safely(
            lambda: data.xml(), default=lambda: self._to_html(self._to_unicode(data))
        )


class RenoirCustomWriter(RenoirXMLEscapeMixin, renoir.writers.Writer):
    ...


class RenoirCustomEscapeAllWriter(RenoirXMLEscapeMixin, renoir.writers.EscapeAllWriter):
    ...


class Renoir(renoir.Renoir):
    """Custom Renoir Engine that understands yatl helpers"""

    _writers = {
        renoir.constants.ESCAPES.common: RenoirCustomWriter,
        renoir.constants.ESCAPES.all: RenoirCustomEscapeAllWriter,
    }


def render(
    content=None,
    filename=None,
    path=".",
    context={},
    delimiters="[[ ]]",
    cached_renoir_engines=Cache(100),
):
    """
    renders the template using renoire, same API as yatl.render, does caching of
    both Renoire engine and source files
    """
    engine = cached_renoir_engines.get(
        (path, delimiters),
        lambda: Renoir(path=path, delimiters=delimiters.split(" "), reload=True),
    )
    if content is not None:
        return engine._render(content, context=context)
    return engine.render(filename, context=context)


class Template(Fixture):

    cache = Cache(100)

    def __init__(self, filename, path=None, delimiters="[[ ]]"):
        self.filename = filename
        self.path = path
        self.delimiters = delimiters

    def on_success(self, context):
        output = context["output"]
        if not isinstance(output, dict):
            return output
        ctx = dict(request=request)
        ctx.update(HELPERS)
        ctx.update(URL=URL)
        ctx.update(context.get("template_inject", {}))
        ctx.update(output)
        ctx["__vars__"] = output
        app_folder = os.path.join(os.environ["PY4WEB_APPS_FOLDER"], request.app_name)
        path = self.path or os.path.join(app_folder, "templates")
        filename = os.path.join(path, self.filename)
        if not os.path.exists(filename):
            generic_filename = os.path.join(path, "generic.html")
            if os.path.exists(generic_filename):
                filename = generic_filename
        context["output"] = render(
            filename=filename, path=path, context=ctx, delimiters=self.delimiters
        )


#########################################################################################
# The Session Fixture
#########################################################################################


class Session(Fixture):

    # All apps share the same default secret if not specified.
    # important for _dashboard reload
    # the actual value is loaded from a file
    SECRET = None
    __slots__ = ["_safe", "secret", "expiration", "algorithm", "storage", "same_site"]

    @property
    def local(self):
        return self._safe_local

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
        session is stored signed and encrypted in the cookie
        """
        # assert Session.SECRET, "Missing Session.SECRET"
        self.secret = secret or Session.SECRET
        self.expiration = expiration
        self.algorithm = algorithm
        self.storage = storage
        self.same_site = same_site
        if isinstance(storage, Session):
            self.__prerequisites__ = [storage]
        if hasattr(storage, "__prerequisites__"):
            self.__prerequisites__ = storage.__prerequisites__

    def initialize(self, app_name="unknown", data=None, changed=False, secure=False):
        self._safe_local = types.SimpleNamespace()
        local = self.local
        local.changed = changed
        local.data = data or {}
        local.session_cookie_name = "%s_session" % app_name
        local.secure = secure

    def load(self):
        self.initialize(
            app_name=request.app_name,
            changed=False,
            secure=request.url.startswith("https"),
        )
        self_local = self.local
        raw_token = request.get_cookie(
            self_local.session_cookie_name
        ) or request.query.get("_session_token")
        if not raw_token and request.method in {"POST", "PUT", "DELETE", "PATCH"}:
            raw_token = (
                request.forms
                and request.forms.get("_session_token")
                or request.json
                and request.json.get("_session_token")
            )
        if Fixture.__fixture_debug__:
            logging.debug("Session token found %s", raw_token)
        if raw_token:
            try:
                if self.storage:
                    token_data = raw_token.encode()
                    json_data = self.storage.get(token_data)
                    if json_data:
                        self_local.data = json.loads(json_data)
                else:
                    try:
                        self_local.data = secure_loads(raw_token, self.secret.encode())
                    except (AssertionError, json.JSONDecodeError):
                        self_local.data = {}
                if self.expiration is not None and self.storage is None:
                    assert self_local.data["timestamp"] > time.time() - int(
                        self.expiration
                    )
                assert self.get_data().get("secure") == self_local.secure
            except Exception as err:
                if Fixture.__fixture_debug__:
                    logging.debug("Session error %s", err)
        if (
            self.get_data().get("session_cookie_name") != self_local.session_cookie_name
            or "uuid" not in self.get_data()
        ):
            self.clear()

    def get_data(self):
        return getattr(self.local, "data", {})

    def save(self):
        self_local = self.local
        self_local.data["timestamp"] = time.time()
        self_local.data["session_cookie_name"] = self_local.session_cookie_name
        if self.storage:
            cookie_data = self_local.data["uuid"]
            self.storage.set(cookie_data, json.dumps(self_local.data), self.expiration)
        else:
            cookie_data = secure_dumps(self_local.data, self.secret.encode())
        if Fixture.__fixture_debug__:
            logging.debug("Session stored %s", cookie_data)
        response.set_cookie(
            self_local.session_cookie_name,
            cookie_data,
            path="/",
            secure=self_local.secure,
            same_site=self.same_site,
        )

    def get(self, key, default=None):
        return self.get_data().get(key, default)

    def __getitem__(self, key):
        return self.get_data()[key]

    def __delitem__(self, key):
        if key in self.get_data():
            self.local.changed = True
            del self.local.data[key]

    def __setitem__(self, key, value):
        self.local.changed = True
        self.local.data[key] = value

    def keys(self):
        return self.get_data().keys()

    def __iter__(self):
        yield from self.get_data().items()

    def clear(self):
        """Produces a brand-new session."""
        self_local = self.local
        self_local.changed = True
        self_local.data.clear()
        self_local.data["uuid"] = str(uuid.uuid1())
        self_local.data["secure"] = self_local.secure

    def on_request(self, context):
        self.load()

    def on_error(self, context):
        if self.local.changed:
            self.save()

    def on_success(self, context):
        if self.local.changed:
            self.save()


#########################################################################################
# The URL Helper
#########################################################################################


def URL(
    *parts,
    vars=None,
    hash=None,
    scheme=False,
    signer=None,
    use_appname=None,
    static_version=None,
):
    """
    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{script_name?}/{app_name?}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),use_appname=False) -> /{script_name?}/a/b?x=1
    """
    if use_appname is None:
        # force use_appname on domain-unmapped apps
        use_appname = not request.environ.get("HTTP_X_PY4WEB_APPNAME")
    if use_appname:
        # app_name is not set by py4web shell
        app_name = getattr(request, "app_name", None)
    has_appname = use_appname and app_name
    script_name = (
        request.environ.get("SCRIPT_NAME", "")
        or request.environ.get("HTTP_X_SCRIPT_NAME", "")
    ).rstrip("/")
    if parts and parts[0].startswith("/"):
        prefix = ""
    elif has_appname and app_name != "_default":
        prefix = "%s/%s/" % (script_name, app_name)
    else:
        prefix = "%s/" % script_name
    broken_parts = []
    for part in parts:
        broken_parts += str(part).rstrip("/").split("/")
    if static_version != "" and broken_parts and broken_parts[0] == "static":
        if not static_version:
            # try to retrieve from __init__.py
            app_module = "apps.%s" % app_name if has_appname else "apps"
            try:
                static_version = getattr(
                    sys.modules[app_module], "__static_version__", None
                )
            except KeyError:
                static_version = None
        if static_version:
            broken_parts.insert(1, "_" + static_version)

    url = prefix + "/".join(map(urllib.parse.quote, broken_parts))
    # Signs the URL if required.  Copy vars into urlvars not to modify it.
    urlvars = dict(vars) if vars else {}
    if signer:
        # Note that we need to sign the non-urlencoded URL, since
        # at verification time, it will be already URLdecoded.
        signer.sign(prefix + "/".join(broken_parts), urlvars)
    if urlvars:
        url += "?" + "&".join(
            "%s=%s" % (k, urllib.parse.quote(str(v))) for k, v in urlvars.items()
        )
    if hash:
        url += "#%s" % hash
    if scheme is not False:
        original_url = request.environ.get("HTTP_ORIGIN") or request.url
        orig_scheme, _, domain = original_url.split("/", 3)[:3]
        if scheme is True:
            scheme = orig_scheme
        elif scheme is None:
            scheme = ""
        else:
            scheme += ":"
        url = "%s//%s%s" % (scheme, domain, url)
    return url


#########################################################################################
# The Action Decorator
#########################################################################################


class HTTP(BaseException):

    """An exception that is considered success"""

    def __init__(self, status, body="", headers={}):
        self.status = status
        self.body = body
        self.headers = headers


def redirect(location):
    """raises HTTP(303) to the specified location"""
    response.headers["Location"] = location
    raise HTTP(303)


class action:
    """@action(...) is a decorator for functions to be exposed as actions"""

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
            stack.extend(getattr(fixture, "__prerequisites__", ()))
        for fixture in reversed(reversed_fixtures):
            if isinstance(fixture, str):
                fixture = Template(fixture)
            if fixture not in fixtures:
                fixtures.append(fixture)

        def decorator(func):

            if Fixture.__fixture_debug__:
                # in debug mode log all calls to fixtures
                def call(f, context):
                    logging.debug(
                        f"Calling {f.__self__.__class__.__name__}.{f.__name__}"
                    )
                    return f(context)

            else:

                def call(f, context):
                    return f(context)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # data shared by all fixtures in the pipeline for each request
                processed = []
                context = {
                    "fixtures": fixtures,
                    "status": 200,
                    "output": None,
                    "exception": None,
                    "processed": processed,
                }
                try:
                    for fixture in fixtures:
                        call(fixture.on_request, context)
                        processed.append(fixture)
                    context["output"] = func(*args, **kwargs)
                except HTTP as http:
                    context["status"] = http.status
                    raise http
                except bottle.HTTPError as error:
                    context["exception"] = error
                except bottle.HTTPResponse:
                    raise
                except Exception as error:
                    context["exception"] = error
                finally:
                    for fixture in reversed(fixtures):
                        if fixture in processed or getattr(fixture, "is_hook", False):
                            try:
                                if context.get("exception"):
                                    call(fixture.on_error, context)
                                else:
                                    call(fixture.on_success, context)
                            except Exception as error:
                                context["exception"] = context.get("exception") or error
                    if context.get("exception"):
                        raise context["exception"]
                return context.get("output", "")

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
                response.headers.update(http.headers)
                return http.body
            except bottle.HTTPResponse:
                raise
            except Exception:
                snapshot = get_error_snapshot()
                logging.error(snapshot["traceback"])
                ticket_uuid = error_logger.log(request.app_name, snapshot) or "unknown"
                response.status = 500
                return error_page(
                    500,
                    button_text=ticket_uuid,
                    href="/_dashboard/ticket/" + ticket_uuid,
                )

        return wrapper

    def __call__(self, func):
        """Building the decorator"""
        app_name = action.app_name
        if self.path[0] == "/":
            path = self.path.rstrip("/") or "/"
        else:

            base_path = "" if app_name == "_default" else f"/{app_name}"
            path = (f"{base_path}/{self.path}").rstrip("/")
        Reloader.register_route(app_name, path, self.kwargs, func)
        if path.endswith("/index"):  # /index is always optional
            short_path = path[:-6] or "/"
            Reloader.register_route(app_name, short_path, self.kwargs, func)
        return func


class Condition(Fixture):
    def __init__(self, condition, on_false=None, exception=HTTP(400)):
        self.condition = condition
        self.on_false = on_false
        self.exception = exception

    def on_request(self, context):
        if not self.condition():
            if self.on_false is not None:
                self.on_false()
            raise self.exception


#########################################################################################
# Monkey Patch: Cookies
#########################################################################################

http.cookies.Morsel._reserved["same-site"] = "SameSite"

#########################################################################################
# Monkey Patch: ssl bug for gevent
#########################################################################################

__ssl__ = __import__("ssl")
_ssl = getattr(__ssl__, "_ssl") or getattr(__ssl__, "_ssl2")


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


#########################################################################################
# Error Handling
#########################################################################################


def get_error_snapshot(depth=5):
    """Return a dict describing a given traceback (based on cgitb.text)."""

    tb = traceback.format_exc()
    errorlog = os.environ.get("PY4WEB_ERRORLOG")
    if errorlog:
        msg = f"[{datetime.datetime.now().isoformat()}]: {tb}\n"
        if errorlog == ":stderr":
            sys.stderr.write(msg)
        elif errorlog == ":stdout":
            sys.stdout.write(msg)
        elif errorlog == "tickets_only":
            pass
        else:
            with portalocker.Lock(errorlog, "a", timeout=2) as fp:
                fp.write(msg)

    etype, evalue, etb = sys.exc_info()
    if isinstance(etype, type):
        etype = etype.__name__

    data = {}
    data["timestamp"] = datetime.datetime.utcnow().isoformat().replace("T", " ")
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
    data["traceback"] = tb
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
            line_vars = cgitb.scanvars(
                lambda: linecache.getline(file, lnum), frame, locals
            )
            # Dump local variables (referenced in current line only)
            f["vars"] = {
                key: repr(value)
                for key, value in locals.items()
                if not key.startswith("__")
            }
        stackframes.append(f)

    return data


class SimpleErrorLogger:
    def log(self, app_name, snapshot):
        """logs the error"""
        logging.error("%s error:\n%s" % (app_name, snapshot["traceback"]))
        return None


class DatabaseErrorLogger:
    def __init__(self):
        """creates the py4web_error table in the service database"""
        uri = os.environ["PY4WEB_SERVICE_DB_URI"]
        folder = os.environ["PY4WEB_SERVICE_FOLDER"]
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
        """store error snapshot (ticket) in the database"""
        ticket_uuid = str(uuid.uuid4())
        try:
            self.db.py4web_error.insert(
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
        except Exception as err:
            logging.error(str(err))
            self.db.rollback()
            return None

    def get(self, ticket_uuid=None):
        """retrieve a ticket from error database"""
        db = self.db
        if ticket_uuid:
            query, orderby = db.py4web_error.uuid == ticket_uuid, None
            rows = db(query).select(orderby=orderby, limitby=(0, 1)).as_list()
        else:
            orderby = ~db.py4web_error.timestamp
            groupby = db.py4web_error.path | db.py4web_error.error
            query = (
                db.py4web_error.timestamp
                > datetime.datetime.now() - datetime.timedelta(days=7)
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

    def clear(self):
        """erase all tickets from database"""
        db = self.db
        db(db.py4web_error).delete()
        self.db.commit()


class ErrorLogger:

    """
    To create your own custom logger for an app:

    class MyLogger:
        def log(app_name, error_snap_shop):
            ...
            return ticket_uuid

    error_logger.plugins['app_name'] = MyLogger()
    """

    def __init__(self):
        self.fallback_logger = SimpleErrorLogger()
        self.database_logger = None
        self.plugins = {}

    def initialize(self):
        """try inizalize database if we have service folder"""
        self.database_logger = safely(DatabaseErrorLogger, log=True)

    def _get_logger(self, app_name):
        """get the appropriate logger for the app"""
        return (
            self.plugins.get(app_name) or self.database_logger or self.fallback_logger
        )

    def log(self, app_name, error_snapshot):
        """log the error snapshot"""
        logger = self._get_logger(app_name)
        ticket_uuid = safely(lambda: logger.log(app_name, error_snapshot))
        if not ticket_uuid:
            self.fallback_logger.log(app_name, error_snapshot)
        return ticket_uuid


error_logger = ErrorLogger()

#########################################################################################
# Loading &  Reloading Logic
#########################################################################################


class StreamProxy:
    def __init__(self, stream):
        self._stream = stream

    def write(self, *args, **kwargs):
        return self._stream.write(*args, **kwargs)


class Reloader:

    ROUTES = collections.defaultdict(list)
    MODULES = {}
    ERRORS = {}

    @staticmethod
    def install_reloader_hook():
        # used by watcher
        def hook(*a, **k):
            app_name = request.path.split("/")[1]
            if not app_name in Reloader.ROUTES:
                app_name = "_default"
            if DIRTY_APPS.get(app_name):
                Reloader.import_app(app_name)
                DIRTY_APPS[app_name] = False
            ## APP_WATCH tasks, if used by any app
            try_app_watch_tasks()

        _REQUEST_HOOKS.before.add(hook)

    @staticmethod
    def clear_routes(app_names=None):
        remove_route = bottle.default_app().router.remove
        if app_names is None:
            app_names = Reloader.ROUTES.keys()
        for app_name in app_names:
            for route in Reloader.ROUTES[app_name]:
                remove_route(route["rule"])
            Reloader.ROUTES[app_name] = []

    @staticmethod
    def import_apps():
        """Import or reimport modules and exposed static files"""
        Reloader.clear_routes()
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        # if first time reload dummy top module
        if not Reloader.MODULES:
            path = os.path.join(folder, "__init__.py")
            loader = importlib.machinery.SourceFileLoader("apps", path)
            loader.load_module()
        # Then load all the apps as submodules
        for app_name in os.listdir(folder):
            Reloader.import_app(app_name, clear_before_import=False)

    @staticmethod
    def import_app(app_name, clear_before_import=True):
        if clear_before_import:
            Reloader.clear_routes([app_name])
        Reloader.ROUTES[app_name] = []
        folder = os.environ["PY4WEB_APPS_FOLDER"]
        path = os.path.join(folder, app_name)
        init = os.path.join(path, "__init__.py")

        if os.path.isdir(path) and not path.endswith("__") and os.path.exists(init):

            action.app_name = app_name
            module_name = "apps.%s" % app_name

            def clear_modules():
                # all files/submodules
                names = [
                    name
                    for name in sys.modules
                    if (name + ".").startswith(module_name + ".")
                ]
                for name in names:
                    del sys.modules[name]

            try:
                module = Reloader.MODULES.get(app_name)
                if not module:
                    click.echo("[ ] loading %s ..." % app_name)
                else:
                    click.echo("[ ] reloading %s ..." % app_name)
                    # forget the module
                    del Reloader.MODULES[app_name]
                    clear_modules()

                load_module_message = None
                buf_out = StreamProxy(io.StringIO())
                buf_err = StreamProxy(buf_out._stream)
                with redirect_stdout(buf_out), redirect_stderr(buf_err):
                    module = importlib.machinery.SourceFileLoader(
                        module_name, init
                    ).load_module()
                    load_module_message = buf_out._stream.getvalue()
                buf_out._stream.close()
                buf_out._stream = sys.stdout
                buf_err._stream = sys.stderr

                if load_module_message:
                    click.secho("\x1b[A    output %s       " % app_name, fg="yellow")
                    click.echo(load_module_message)

                click.secho("\x1b[A[X] loaded %s       " % app_name, fg="green")
                Reloader.MODULES[app_name] = module
                Reloader.ERRORS[app_name] = None
            except Exception as err:
                Reloader.ERRORS[app_name] = traceback.format_exc()
                error_logger.log(app_name, get_error_snapshot())
                click.secho(
                    "\x1b[A[FAILED] loading %s (%s)" % (app_name, err),
                    fg="red",
                )
                # clear all files/submodules if the loading fails
                clear_modules()
                return None

        # Expose static files with support for static asset management
        static_folder = os.path.join(path, "static")

        if os.path.exists(static_folder):
            app_name = path.split(os.path.sep)[-1]
            prefix = "" if app_name == "_default" else f"/{app_name}"
            path = prefix + r"/static/<re((_\d+(\.\d+){2}/)?)><fp.path()>"

            def server_static(fp, static_folder=static_folder):
                filename = fp
                response.headers.setdefault("Pragma", "cache")
                response.headers.setdefault("Cache-Control", "private")
                return bottle.static_file(filename, root=static_folder)

            Reloader.register_route(app_name, path, {"method": "GET"}, server_static)

        ICECUBE.update(threadsafevariable.ThreadSafeVariable.freeze())

    @staticmethod
    def register_route(app_name, rule, kwargs, func):
        dec_func = action.catch_errors(app_name, func)
        bottle.route(rule, **kwargs)(dec_func)
        filename = module2filename(func.__module__)
        methods = kwargs.get("method", ["GET"])
        if isinstance(methods, str):
            methods = [methods]
        for method in methods:
            Reloader.ROUTES[app_name].append(
                {
                    "rule": rule,
                    "method": method,
                    "filename": filename,
                    "action": func.__name__,
                }
            )


#########################################################################################
# Web Server and Reload Logic: Error Handling
#########################################################################################

ERROR_PAGES = {
    "*": (
        "<html><head><style>body{color:white;text-align: center;background-color:[[=color]];font-family:serif} "
        "h1{font-size:6em;margin:16vh 0 8vh 0} h2{font-size:2em;margin:8vh 0} "
        "a{color:white;text-decoration:none;font-weight:bold;padding:10px 10px;border-radius:10px;border:2px solid #fff;transition: all .5s ease} "
        "a:hover{background:rgba(0,0,0,0.1);padding:10px 30px}</style></head>"
        '<body><h1>[[=code]]</h1><h2>[[=message]]</h2>[[if button_text:]]<a href="[[=href]]">[[=button_text]]</a>[[pass]]</body></html>'
    ),
}


def error_page(code, button_text=None, href="#", color=None, message=None):
    message = http.client.responses[code].upper() if message is None else message
    color = (
        {"4": "#F44336", "5": "#607D8B"}.get(str(code)[0], "#2196F3")
        if not color
        else color
    )
    context = dict(
        code=code, message=message, button_text=button_text, href=href, color=color
    )
    # if client accepts 'application/json' - return json
    if re.search(REGEX_APPJSON, request.headers.get("accept", "")):
        response.status = code
        return json.dumps(context)
    # else - return html error-page
    content = ERROR_PAGES.get(code) or ERROR_PAGES["*"]
    return render(content=content, context=context, delimiters="[[ ]]")


@bottle.error(404)
def error404(error):
    guess_app_name = (
        "index"
        if request.environ.get("HTTP_X_PY4WEB_APPNAME")
        else request.path.split("/")[1]
    )
    if guess_app_name == "index":
        href = "/"
    else:
        href = "/" + guess_app_name
    script_name = (
        request.environ.get("SCRIPT_NAME", "")
        or request.environ.get("HTTP_X_SCRIPT_NAME", "")
    ).rstrip("/")
    if script_name:
        href = script_name + href
    return error_page(404, button_text=guess_app_name, href=href)


#########################################################################################
# Web Server and Reload Logic: Operations
#########################################################################################

DIRTY_APPS = dict()  # apps that need to be reloaded (lazy watching)

APP_WATCH = {"files": dict(), "handlers": OrderedDict(), "tasks": dict()}

""" Decorator that binds a func as an watchdog handler of non-'.py' files.
Paths to files must be relative to app, w/o app name(folder).

@app_watch_handler(['static/sass/all.sass', 'static/sass/main.sass'])
def sass_compile(changed_files):
    print(changed_files); # paths of files that changed, for info
    sass.compile()
"""


def app_watch_handler(watched_app_subpaths):
    stack = inspect.stack
    invoker = pathlib.Path(stack()[1].filename)
    apps_path = pathlib.Path(os.environ["PY4WEB_APPS_FOLDER"])
    app = invoker.relative_to(os.environ["PY4WEB_APPS_FOLDER"]).parts[0]

    def decorator(func):
        handler = "{}.{}".format(func.__module__, func.__name__)
        APP_WATCH["handlers"][handler] = func
        for subpath in watched_app_subpaths:
            app_path = apps_path.joinpath(app, subpath).as_posix()
            if app_path not in APP_WATCH["files"]:
                APP_WATCH["files"][app_path] = []
            APP_WATCH["files"][app_path].append(handler)
        return func

    return decorator


def try_app_watch_tasks():
    if APP_WATCH["tasks"]:
        tried_tasks = []
        for handler in APP_WATCH["tasks"]:
            changed_files_dict = APP_WATCH["tasks"][handler]
            try:
                APP_WATCH["handlers"][handler](changed_files_dict.keys())
                tried_tasks.append(handler)
            except Exception:
                logging.error(traceback.format_exc())
        ## remove executed tasks from register
        for handler in tried_tasks:
            del APP_WATCH["tasks"][handler]


def watch(apps_folder, server_config, mode="sync"):
    def watch_folder_event_loop(apps_folder):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(watch_folder(apps_folder))

    async def watch_folder(apps_folder):
        click.echo(
            "watching (%s-mode) python file changes in: %s" % (mode, apps_folder)
        )
        async for changes in awatch(os.path.join(apps_folder)):
            apps = []
            for subpath in [pathlib.Path(pair[1]) for pair in changes]:
                name = subpath.relative_to(apps_folder).parts[0]
                if subpath.suffix == ".py":
                    apps.append(name)
                ## manage `app_watch_handler` decorators
                elif subpath.as_posix() in APP_WATCH["files"]:
                    handlers = APP_WATCH["files"][subpath.as_posix()]
                    for handler in handlers:
                        if handler not in APP_WATCH["tasks"]:
                            APP_WATCH["tasks"][handler] = {}
                        APP_WATCH["tasks"][handler][subpath.as_posix()] = True

            for name in apps:
                if mode == "lazy":
                    DIRTY_APPS[name] = True
                else:
                    Reloader.import_app(name)
            ## in 'lazy' mode it's done in bottle's 'before_request' hook
            if mode != "lazy":
                try_app_watch_tasks()

    if server_config["number_workers"] > 1:
        click.echo("--watch option has no effect in multi-process environment \n")
        return
    elif server_config["server"].startswith(("wsgiref", "waitress", "rocket")):
        # these servers block the main thread so we open a new thread for the file watcher
        threading.Thread(
            target=watch_folder_event_loop, args=(apps_folder,), daemon=True
        ).start()
    elif server_config["server"] == "tornado":
        if server_config["platform"] == "windows" and sys.version_info >= (3, 8):
            # see  https://bugs.python.org/issue37373 FIX: tornado/py3.8 on window
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        # tornado delegate to asyncio so we add a future into the event loop
        asyncio.ensure_future(watch_folder(apps_folder))
    elif server_config["server"].startswith("gevent"):
        watch_folder_event_loop(apps_folder)
    else:
        # should never happen
        return

    if mode == "lazy":
        Reloader.install_reloader_hook()


def start_server(kwargs):
    host = kwargs["host"]
    port = int(kwargs["port"])
    apps_folder = kwargs["apps_folder"]
    number_workers = kwargs["number_workers"]
    quiet = kwargs["quiet"]
    params = dict(host=host, port=port, reloader=False, quiet=quiet)
    server_config = dict(
        platform=platform.system().lower(),
        server=None if kwargs["server"] == "default" else kwargs["server"],
        number_workers=number_workers,
    )

    if not server_config["server"]:
        if server_config["platform"] == "windows" or number_workers < 2:
            server_config["server"] = "rocketServer"
        else:
            if not gunicorn:
                logging.error("gunicorn not installed")
                return
            server_config["server"] = "gunicorn"

    # Catch interrupts like Ctrl-C if needed
    if server_config["server"] not in {"rocketServer", "wsgirefWsTwistedServer"}:
        signal.signal(
            signal.SIGINT,
            lambda signal, frame: click.echo(
                "KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(
                    signal
                )
                and sys.exit(0),
            ),
        )

    params["server"] = server_config["server"]
    if params["server"] in server_adapters.__all__:
        params["server"] = getattr(server_adapters, params["server"])()
    if number_workers > 1:
        params["workers"] = number_workers
    if server_config["server"] == "gunicorn":
        sys.argv[:] = sys.argv[:1]  # else break gunicorn
    if kwargs["ssl_cert"] is not None:
        params["certfile"] = kwargs["ssl_cert"]
        params["keyfile"] = kwargs["ssl_key"]

    if server_config["server"] == "gevent":
        if kwargs["watch"] != "off":
            print("Error: watch doesn't work with gevent. ")
            print("invoke py4web with `--watch off` or choose another server. ")
            exit(255)

        if not hasattr(_ssl, "sslwrap"):
            _ssl.sslwrap = new_sslwrap

    if kwargs["watch"] != "off":
        watch(apps_folder, server_config, kwargs["watch"])
    bottle.run(**params)


def check_compatible(version):
    """To be called by apps to check if module version is compatible with py4web requirements"""
    from . import __version__

    return tuple(map(int, __version__.split("."))) >= tuple(
        map(int, version.split("."))
    )


#########################################################################################
# WSGI Adapter
#########################################################################################


class MetaPathRouter:
    """
    Instances of this class makes alias for a package name,
    in other words instruct the import system to route request
    for a package alias, i.e.:

        MetaPathRouter("pkg", "pkg_alias")
        import pkg_alias.sub

    works as

        import pkg.sub

    author: Paolo Pastori
    """

    def __init__(self, pkg, pkg_alias="apps"):
        assert pkg_alias
        assert pkg
        if pkg != pkg_alias:
            self.pkg_alias = pkg_alias
            self.pkg = pkg
            # register as path finder
            sys.meta_path.append(self)

    def find_spec(self, fullname, path=None, target=None):
        if fullname == self.pkg_alias and path is None:
            spec = importlib.util.find_spec(self.pkg)
            if spec:
                spec.name = fullname
                spec.loader = importlib.machinery.SourceFileLoader(
                    fullname, spec.origin
                )
                return spec


def install_args(kwargs, reinstall_apps=False):
    # always convert apps_folder to an absolute path
    apps_folder = kwargs["apps_folder"] = os.path.abspath(kwargs["apps_folder"])
    kwargs["service_folder"] = os.path.join(
        kwargs["apps_folder"], DEFAULTS["PY4WEB_SERVICE_FOLDER"]
    )
    kwargs["service_db_uri"] = DEFAULTS["PY4WEB_SERVICE_DB_URI"]
    for key, val in kwargs.items():
        os.environ["PY4WEB_" + key.upper()] = str(val)
    Fixture.__fixture_debug__ = kwargs.get("debug", False)
    logging.getLogger().setLevel(
        0 if Fixture.__fixture_debug__ else kwargs.get("logging_level", logging.WARNING)
    )
    yes2 = yes = kwargs.get("yes", False)
    # If the apps folder does not exist create it and populate it
    if not os.path.exists(apps_folder):
        if yes or click.confirm("Create missing folder %s?" % apps_folder):
            os.makedirs(apps_folder)
            yes2 = True
        else:
            click.echo("Command aborted")
            sys.exit(0)
    init_py = os.path.join(apps_folder, "__init__.py")
    if not os.path.exists(init_py):
        if yes2 or click.confirm("Create missing init file %s?" % init_py):
            with open(init_py, "wb"):
                pass
        else:
            click.echo("Command aborted")
            sys.exit(0)
    # ensure that "import apps.someapp" works
    apps_folder_parent, apps_folder_name = os.path.split(apps_folder)
    if apps_folder_parent not in sys.path:
        sys.path.insert(0, apps_folder_parent)
    if apps_folder_name != "apps":
        MetaPathRouter(apps_folder_name)

    if not os.path.exists(kwargs["service_folder"]):
        os.mkdir(kwargs["service_folder"])
    session_secret_filename = os.path.join(kwargs["service_folder"], "session.secret")
    if not os.path.exists(session_secret_filename):
        with open(session_secret_filename, "w") as fp:
            fp.write(str(uuid.uuid4()))

    with open(session_secret_filename) as fp:
        Session.SECRET = fp.read()

    # after everything is etup but before installing apps, init
    error_logger.initialize()

    # Reinstall apps from zipped ones in assets
    if reinstall_apps:
        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        if os.path.exists(assets_dir):
            apps = os.listdir(assets_dir)
            for filename in apps:
                zip_filename = os.path.join(assets_dir, filename)
                # These filenames do not necessarily exist if one has
                # downloaded from source and deleted them.
                app_name = filename.split(".")[-2]
                target_dir = os.path.join(apps_folder, app_name)
                if not os.path.exists(target_dir):
                    if yes or click.confirm("Create app %s?" % app_name):
                        click.echo("[ ] Unzipping app %s" % filename)
                        with zipfile.ZipFile(zip_filename, "r") as zip_file:
                            os.makedirs(target_dir)
                            zip_file.extractall(target_dir)
                            click.echo("\x1b[A[X]")


def wsgi(**kwargs):
    """Initializes everything, loads apps, returns the wsgi app"""
    install_args(kwargs)
    Reloader.import_apps()
    return bottle.default_app()


#########################################################################################
# CLI
#########################################################################################


@click.group(
    context_settings=dict(help_option_names=["-h", "-help", "--help"]),
    help='%s\n\nType "%s COMMAND -h" for available options on commands'
    % (__doc__, PY4WEB_CMD),
)
def cli():
    pass


@cli.command()
@click.option(
    "-a", "--all", is_flag=True, default=False, help="List version of all modules"
)
def version(all):
    """Show versions and exit"""
    from . import __version__

    click.echo("py4web: %s" % __version__)
    if all:
        click.echo("system: %s" % platform.platform())
        click.echo("python: %s" % sys.version.replace("\n", " "))
        for name in sorted(sys.modules):
            if hasattr(sys.modules[name], "__version__"):
                click.echo("%s: %s" % (name, sys.modules[name].__version__))


@cli.command()
@click.argument("apps_folder")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
def setup(**kwargs):
    """Setup new apps folder or reinstall it"""
    install_args(kwargs, reinstall_apps=True)


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
def shell(**kwargs):
    """Open a python shell with apps_folder's parent added to the path"""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # running in the PyInstaller binary bundle
        import site
    install_args(kwargs)
    code.interact(local=dict(globals(), **locals()))


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.argument("func")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option(
    "--args",
    default="{}",
    help="Arguments passed to the program/function",
    show_default=True,
)
def call(apps_folder, func, yes, args):
    """Call a function inside apps_folder"""
    kwargs = json.loads(args)
    install_args(dict(apps_folder=apps_folder, yes=yes))
    apps_folder_name = os.path.basename(os.environ["PY4WEB_APPS_FOLDER"])
    app_name = func.split(".")[0]
    module, name = ("%s.%s" % (apps_folder_name, func)).rsplit(".", 1)
    env = {}
    exec("from %s import %s" % (module, name), {}, env)
    request.app_name = app_name
    env[name](**kwargs)


@cli.command(name="set_password")
@click.option(
    "--password",
    prompt=True,
    confirmation_prompt=True,
    hide_input=True,
    help="Password value (asked if missing)",
)
@click.option(
    "-p",
    "--password_file",
    default="password.txt",
    help="File for the encrypted password",
    show_default=True,
)
def set_password(password, password_file):
    """Set administrator's password for the Dashboard"""
    click.echo('Storing the hashed password in file "%s"\n' % password_file)
    with open(password_file, "w") as fp:
        fp.write(str(pydal.validators.CRYPT()(password)[0]))


@cli.command(name="new_app")
@click.argument("apps_folder")
@click.argument("app_name")
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option(
    "-s",
    "--scaffold_zip",
    default=None,
    help="Path to the zip with the scaffolding app",
    show_default=False,
)
def new_app(apps_folder, app_name, yes, scaffold_zip):
    """Create a new app copying the scaffolding one"""
    install_args(dict(apps_folder=apps_folder, yes=yes))
    source = scaffold_zip or os.path.join(
        os.path.dirname(__file__), "assets", "py4web.app._scaffold.zip"
    )
    target_dir = os.path.join(os.environ["PY4WEB_APPS_FOLDER"], app_name)
    if not os.path.exists(source):
        click.echo("Source app %s does not exists" % source)
        sys.exit(1)
    elif os.path.exists(target_dir):
        click.echo("Target folder %s already exists" % target_dir)
        sys.exit(1)
    else:
        zfile = zipfile.ZipFile(source, "r")
        zfile.extractall(target_dir)
        zfile.close()


@cli.command()
@click.argument("apps_folder", type=click.Path(exists=True))
@click.option(
    "-Y",
    "--yes",
    is_flag=True,
    default=False,
    help="No prompt, assume yes to questions",
    show_default=True,
)
@click.option("-H", "--host", default="127.0.0.1", help="Host name", show_default=True)
@click.option(
    "-P", "--port", default=8000, type=int, help="Port number", show_default=True
)
@click.option(
    "-p",
    "--password_file",
    default="password.txt",
    help="File for the encrypted password",
    show_default=True,
)
@click.option(
    "-Q",
    "--quiet",
    is_flag=True,
    default=False,
    help="Suppress server output",
    show_default=True,
)
@click.option(
    "-s",
    "--server",
    default="default",
    type=click.Choice(
        ["default", "wsgiref", "tornado", "gunicorn", "gevent", "waitress"]
        + server_adapters.__all__
    ),
    help="server to use",
    show_default=True,
)
@click.option(
    "-w",
    "--number_workers",
    default=0,
    type=int,
    help="Number of workers",
    show_default=True,
)
@click.option(
    "-d",
    "--dashboard_mode",
    default="full",
    help="Dashboard mode: demo, readonly, full, none",
    show_default=True,
)
@click.option(
    "--watch",
    default="lazy",
    type=click.Choice(["off", "sync", "lazy"]),
    help="Watch python changes and reload apps automatically, modes: off, sync, lazy",
    show_default=True,
)
@click.option(
    "--ssl_cert", type=click.Path(exists=True), help="SSL certificate file for HTTPS"
)
@click.option("--ssl_key", type=click.Path(exists=True), help="SSL key file for HTTPS")
@click.option(
    "--errorlog",
    default=":stderr",
    help="Where to send error logs (:stdout|:stderr|tickets_only|{filename})",
    show_default=True,
)
@click.option(
    "-L",
    "--logging_level",
    type=int,
    default=logging.WARNING,
    help="The log level (0 - 50) [default: 30 (=WARNING)]",
)
@click.option(
    "-D",
    "--debug",
    is_flag=True,
    default=False,
    help="Debug switch",
    show_default=True,
)
def run(**kwargs):
    """Run all the applications on apps_folder"""
    install_args(kwargs)

    from py4web import __version__

    click.secho(ART, fg="blue")
    click.echo("Py4web: %s on Python %s\n\n" % (__version__, sys.version))

    # If we know where the password is stored, read it, otherwise ask for one
    if os.path.exists(os.path.join(os.environ["PY4WEB_APPS_FOLDER"], "_dashboard")):
        if kwargs["dashboard_mode"] not in ("demo", "none") and not os.path.exists(
            kwargs["password_file"]
        ):
            click.echo(
                'You have not set a dashboard password. Run "%s set_password" to do so.'
                % PY4WEB_CMD
            )
        else:
            click.echo(
                f"Dashboard is at: http{'s' if kwargs.get('ssl_cert', None) else ''}://{kwargs['host']}:{kwargs['port']}/_dashboard"
            )

    # Start
    Reloader.import_apps()
    start_server(kwargs)


if __name__ == "__main__":
    cli()
