import urllib
import sys
import os
import logging
import importlib
import threading
import functools
import time

from .globs import request, response
from .exceptions import HTTP

url_quote = urllib.parse.quote


def redirect(location):
    """our redirect does not delete cookies and headers like bottle.HTTPResponse does;
    it is considered a success, not failure"""
    response.headers["Location"] = location
    raise HTTP(303)


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

    env = request.environ

    if use_appname is None:
        # force use_appname on domain-unmapped apps
        use_appname = not env.get("HTTP_X_PY4WEB_APPNAME")
    if use_appname:
        # app_name is not set by py4web shell
        app_name = getattr(request, "app_name", None)
    has_appname = use_appname and app_name
    script_name = (
        env.get("SCRIPT_NAME", "")
        or env.get("HTTP_X_SCRIPT_NAME", "")
    ).rstrip("/")
    if parts and parts[0].startswith("/"):
        prefix = ""
    elif has_appname and app_name != "_default":
        prefix = f"{script_name}/{app_name}/"
    else:
        prefix = f"{script_name}/"
    broken_parts = []
    [broken_parts.extend(str(part).rstrip("/").split("/")) for part in parts]
    if static_version != "" and broken_parts and broken_parts[0] == "static":
        if not static_version:
            # try to retrieve from __init__.py
            app_module = f"apps.{app_name}" if has_appname else "apps"
            try:
                static_version = getattr(
                    sys.modules[app_module], "__static_version__", None
                )
            except KeyError:
                static_version = None
        if static_version:
            broken_parts.insert(1, f"_{static_version}")

    url = prefix + "/".join(url_quote(p) for p in broken_parts)
    # Signs the URL if required.  Copy vars into urlvars not to modify it.
    urlvars = dict(vars) if vars else {}
    if signer:
        # Note that we need to sign the non-urlencoded URL, since
        # at verification time, it will be already URLdecoded.
        signer.sign(prefix + "/".join(broken_parts), urlvars)
    if urlvars:
        url += "?" + "&".join(
            f"{k}={url_quote(str(v))}" for k, v in urlvars.items()
        )
    if hash:
        url += f"#{hash}"
    if scheme is not False:
        original_url = env.get("HTTP_ORIGIN") or request.url
        orig_scheme, _, domain = original_url.split("/", 3)[:3]
        if scheme is True:
            scheme = orig_scheme
        elif scheme is None:
            scheme = ""
        else:
            scheme += ':'
        url = f'{scheme}//{domain}{url}'
    return url


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


def module2filename(module):
    filename = os.path.join(*module.split(".")[1:])
    filename = (
        os.path.join(filename, "__init__.py")
        if not filename.count(os.sep)
        else filename + ".py"
    )
    return filename


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
