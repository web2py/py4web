#!/usr/bin/env python

from __future__ import print_function

# standard modules
import argparse
import cgitb
import collections
import copy
import datetime
import functools
import importlib
import inspect
import json
import linecache
import logging
import numbers
import os
import platform
import pydoc
import re
import sys
import threading
import time
import traceback
import types
import uuid

# optional web servers for speed
try: 
    import gunicorn
except:
    gunicorn = None
try:
    import gevent; gevent.monkey.patch_all()
except:
    gevent = None

# third part modules
import jwt    # pip import PyJWT
import bottle # pip import bottle
import yatl   # pip import yatl
import pydal  # pip import pydal
from pydal import _compat

import reloader
reloader.enable()

__all__ = ['render', 'DAL', 'Field', 'action', 'request', 'response', 'redirect', 'abort', 'HTTP', 'Session', 'Cache']

TEMPLATE_500 = """<html><body style="background:white"><div style="padding-top:10%;margin:auto;color:red;font-family:helvetica;text-align:center"><a style="padding:5px 10px;border:2px solid red;color:red;text-decoration:none" href="/_error/{0}">&#x2639; Internal Error: {0}</a></div></body><html>"""

HTTP = bottle.HTTPResponse
Field = pydal.Field
render = yatl.render
request = bottle.request
response = bottle.response
redirect = bottle.redirect           
abort = bottle.abort

########################################################################################
# a O(1) LRU cache and memoize with expiration and monitoring (using linked list)
#########################################################################################

class Node(object):

    def __init__(self, key=None, value=None, t=None, m=None, prev=None, next=None):
        self.key, self.value, self.t, self.m, self.prev, self.next = key, value, t, m, prev, next

class Cache(object):
    """
    O(1) caching object that remembers the 'size' most recent values
    Example:

        cache = Cache(size=1000)
        h = cache.get(filename, lambda: hash(open(filename).read()), 60, lambda: os.path.getmtime())
    
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
        """if not key stored or expired and monitor == None or monitor() value changed, returns value = callback()"""
        node, t0 = self.mapping.get(key), time.time()
        if node:
            value, t, node.next.prev, node.prev.next = node.value, node.t, node.prev, node.next
        if not node:
            self.free -= 1
        m = monitor and monitor()
        if node and node.t + expiration < t0:
            m = monitor and monitor()
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
                key = '%s:%s:%s:%s' % (func.__module__, func.__name__, args, kwargs)
                return self.get(key, lambda args=args, kwargs=kwargs: func(*args, **kwargs), expiration=expiration)
            return memoized_func
        return decorator

#########################################################################################
# a better json serializer
#########################################################################################

def objectify(obj):
    """converts the obj(ect) into a json serializable object"""
    if isinstance(obj, numbers.Integral):
        return int(obj)
    elif isinstance(obj, (numbers.Rational, numbers.Real)):
        return float(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime, datetime.time)):
        return obj.isoformat()
    elif hasattr(obj, 'to_list') and callable(obj.to_list):
        return item.to_list()
    elif hasattr(obj, '__iter__') or isinstance(obj, types.GeneratorType):
        return list(obj)
    elif hasattr(obj, 'to_dict') and callable(obj.to_dict):
        return obj.to_dict()
    elif hasattr(obj, '__dict__') and hasattr(obj,'__class__'):
        d = copy.copy(obj.__dict__)
        d['__class__'] = obj.__class__.__name__
        return d
    else:
        return str(obj)

def dumps(obj, sort_keys=True, indent=2):
    return json.dumps(obj, default=objectify, sort_keys=sort_keys, indent=indet)

#########################################################################################
# Generic Fixture (database connctions, templates, sessions, and requirements are fixtures)
#########################################################################################

class Fixture(object):
    def on_request(self): pass   # called when request arrives
    def on_error(self): pass     # called when request errors
    def on_success(self): pass   # called when request is successfull
    def transform(self, output): # transforms the output, for example to apply template
        return output

class DAL(pydal.DAL, Fixture):
    def on_request(self): self._adapter.reconnect()
    def on_error(self): self.rollback()
    def on_success(self): self.commit()

class Template(Fixture):

    cache = Cache(100)

    def __init__(self, filename, delimiters='[[ ]]'):
        self.filename = filename
        self.delimiters = delimiters        
        
    @staticmethod
    def read(filename):
        with open(filename) as stream:
            return stream.read()

    def transform(self, output):
        if not isinstance(output, dict):
            return output
        context = dict(request=request)
        context.update(yatl.helpers.__dict__)
        context.update(output)
        context['__vars__'] = output 
        app_folder = os.path.join(os.environ['WEB3PY_APPLICATIONS'], request.app_name)
        path = os.path.join(app_folder, 'templates')
        filename = os.path.join(path, self.filename)
        template = Template.cache.get(filename, lambda: Template.read(filename), expiration=1, 
                                      monitor=lambda: os.path.getmtime(filename)) 
        output = yatl.render(template, path=path, context=context, delimiters=self.delimiters)
        return output


class Session(Fixture):

    def __init__(self, secret, expiration=None, algorithm='HS256'):
        self.secret = secret
        self.expiration = expiration
        self.algorithm = algorithm        
        self.local = threading.local()

    def load(self):
        self.local.session_cookie_name = '%s_session' % request.app_name
        enc_data = _compat.to_bytes(request.get_cookie(self.local.session_cookie_name))
        self.local.changed = False
        try:
            self.local.data = jwt.decode(enc_data, self.secret, algorithms=[self.algorithm])
            assert self.expiration is None or self.local.data['timestamp'] > time.time() - int(self.expiration)
        except Exception as e:
            self.local.data = {}
        if not 'uuid' in self.local.data:
            self.local.changed = True
            self.local.data['uuid'] = str(uuid.uuid4())

    def get(self, key, default=None):
        return self.local.data.get(key, default)

    def __getitem__(self, key):
        return self.local.data[key]

    def __setitem__(self, key, value):
        self.local.changed = True
        self.local.data[key] = value

    def save(self):
        self.local.data['timestamp'] = time.time()        
        enc_data = jwt.encode(self.local.data, self.secret, algorithm = self.algorithm)
        response.set_cookie(self.local.session_cookie_name, _compat.to_native(enc_data))

    def on_request(self):
        self.load()

    def on_error(self):
        if self.local.changed:
            self.save()
        
    def on_success(self):
        if self.local.changed:
            self.save()

#########################################################################################
# the action decorator
#########################################################################################

class action(object):
    """@action(...) is a decorator for functions to be exposed as actions"""

    current = threading.local()

    def __init__(self, path, **kwargs):
        self.path = path
        self.kwargs = kwargs

    @staticmethod
    def uses(*fixtures):
        """associated fixtures to an action"""
        fixtures = [Template(obj) if isinstance(obj, str) else obj for obj in fixtures]
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
                except Exception:
                    [obj.on_error() for obj in fixtures]
                    raise
            return wrapper
        return decorator

    @staticmethod
    def requires(*requirements):
        """enforces requiremets or abort(401)"""
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
        """catches and logs errors in an action. also sets request.app_name"""
        @functools.wraps(func)
        def wrapper(*func_args, **func_kwargs):
            try:
                request.app_name = app_name
                return func(*func_args, **func_kwargs)
            except bottle.HTTPResponse as e:
                raise e
            except:
                logging.error(traceback.format_exc())
                try:                    
                    ticket = log_error(get_error_snapshot())
                except:
                    ticket = "unknown"
                return  TEMPLATE_500.format(ticket)
        return wrapper 

    @staticmethod
    def combine(*decorators):
        def wrapper(func):
            for decorator in reversed(decorators):
                func = decorator(func)
            return func
        return wrapper

    def __call__(self, func):
        """builds the decorator"""
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        folder = os.path.dirname(os.path.abspath(module.__file__))
        app_name = folder[len(os.environ['WEB3PY_APPLICATIONS'])+1:].split(os.sep)[0]
        path = self.path if self.path[:1] == '/' else '/%s/%s' % (app_name, self.path)
        func = action.catch_errors(app_name, func)
        func = bottle.route(path, **self.kwargs)(func)
        return func

def user_in(session):
    def requirement():
        session.on_request()
        return session.get('user_id', None) is not None 
    return requirement

#########################################################################################
# monkey patch ssl bug for gevent
#########################################################################################

__ssl__ = __import__('ssl')
_ssl = getattr(__ssl__, '_ssl') or getattr(__ssl__, '_ssl2')

if not hasattr(_ssl, 'sslwrap'):
    def new_sslwrap(sock, server_side=False, keyfile=None, certfile=None, 
                    cert_reqs=__ssl__.CERT_NONE, ssl_version=__ssl__.PROTOCOL_SSLv23, 
                    ca_certs=None, ciphers=None):
        context = __ssl__.SSLContext(ssl_version)
        context.verify_mode = cert_reqs or __ssl__.CERT_NONE
        if ca_certs:
            context.load_verify_locations(ca_certs)
        if certfile:
            context.load_cert_chain(certfile, keyfile)
        if ciphers:
            context.set_ciphers(ciphers)
        caller_self = inspect.currentframe().f_back.f_locals['self']
        return context._wrap_socket(sock, server_side=server_side, ssl_sock=caller_self)
    _ssl.sslwrap = new_sslwrap

#########################################################################################
# error handling
#########################################################################################

def get_error_snapshot(depth=5):
    """Return a dict describing a given traceback (based on cgitb.text)."""

    etype, evalue, etb = sys.exc_info()
    if isinstance(etype, type):
        etype = etype.__name__

    data = {}
    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['python_version'] = sys.version
    platform_keys = [
        'machine', 'node', 'platform', 'processor', 'python_branch', 'python_build',
        'python_compiler', 'python_implementation', 'python_revision', 'python_version',
        'python_version_tuple', 'release', 'system', 'uname', 'version']
    data['platform_info'] = {key: getattr(platform, key)() for key in platform_keys}
    data['os_environ'] = {
        key: pydoc.text.repr(value) for key, value in os.environ.items()}
    data['traceback'] = traceback.format_exc()
    data['exception_type'] = str(etype)
    data['exception_value'] = str(evalue)
    # loopover the stack frames
    items = inspect.getinnerframes(etb, depth)
    del etb # Prevent circular references that would cause memory leaks
    data['stackframes'] = stackframes = []
    for frame, file, lnum, func, lines, index in items:
        file = file and os.path.abspath(file) or '?'
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        # basic frame information
        f = {'file': file, 'func': func, 'lnum': lnum}
        f['code'] = lines
        line_vars = cgitb.scanvars(lambda: linecache.getline(file, lnum), frame, locals)
        # dump local variables (referenced in current line only)
        f['vars'] = {key: pydoc.text.repr(value) for key, value in locals.items() if not key.startswith('__')}
        stackframes.append(f)

    return data


def log_error(error_snapshot):
    uri = os.environ['WEB3PY_SYSTEM_DB_URI']
    db = DAL(uri)
    db.define_table('web3py_error',
                    Field('uuid'),
                    Field('method'),
                    Field('path','string'),
                    Field('timestamp','datetime'),
                    Field('client_ip','string'),
                    Field('snapshot','json'))
    error_uuid = str(uuid.uuid4())
    db.web3py_error.insert(
            uuid=error_uuid,
            method=request.method,
            path=request.path,
            timestamp=datetime.datetime.utcnow(),
            client_ip=request.environ.get('REMOTE_ADDR'),
            snapshot=error_snapshot)
    return error_uuid

#########################################################################################
# loading/reloading logic
#########################################################################################

class Reloader(object):
    
    MODULES = {}
    ERRORS = {}

    def import_apps(self):
        """import or reimport modules and exposed static files"""
        folder = os.environ['WEB3PY_APPLICATIONS']
        app = bottle.default_app()
        app.routes = app.routes[:] 
        new_apps = []
        for app_name in os.listdir(folder):
            path = os.path.join(folder, app_name)
            if os.path.isdir(path) and not path.endswith('__'):
                try:
                    module = Reloader.MODULES.get(app_name)
                    if not module:
                        module = importlib.import_module(app_name)
                        Reloader.MODULES[app_name] = module
                        new_apps.append(path)
                    else:
                        reloader.reload(module)
                    Reloader.ERRORS[app_name] = None
                except:
                    print(traceback.format_exc())
                    Reloader.ERRORS[app_name] = traceback.format_exc()
        # expose static files
        for path in new_apps:
            @bottle.route('/%s/static/<filename:path>' % path.split(os.path.sep)[-1])
            def server_static(filename, path=path):
                return bottle.static_file(filename, root=os.path.join(path, 'static'))

#########################################################################################
# find all routes
#########################################################################################

def get_routes():
    app = bottle.default_app()
    routes = []
    for route in app.routes:
        func = route.callback
        routes.append({'rule': route.rule,
                       'method': route.method,
                       'filename': func.__module__, #.replace('.',os.sep) + '.py',
                       'action': func.__name__})
    return sorted(routes, key=lambda item: item['rule'])

#########################################################################################
# web server and reload logic
#########################################################################################

def start_server(args):
    host, port = args.address.split(':')
    if args.workers < 1:
        bottle.run(host=host, port=int(port))
    else:
        if not gunicorn:
            logging.error('gunicorn not installed')
        elif not gunicorn:
            logging.error('gevent not installed')
        else:
            bottle.run(server='gunicorn', host=host, port=int(port),
                       workers=args.workers, worker_class='gevent', reloader=True,
                       certfile=args.certfile, keyfile=args.keyfile)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='path to the applications folder')
    parser.add_argument('--address', default='127.0.0.1:8000',help='serving address')
    parser.add_argument('--workers', default=0, type=int, help='number of gunicorn workers')
    parser.add_argument('--certfile', default=None, type=int, help='ssl certificate file')
    parser.add_argument('--keyfile', default=None, type=int, help='ssl key file')
    parser.add_argument('--system_db_uri', default='sqlite:memory:', type=str, help='db uri for logging')
    action.args = args = parser.parse_args()
    args.folder = os.path.abspath(args.folder)
    os.environ['WEB3PY_APPLICATIONS'] = args.folder
    os.environ['WEB3PY_SYSTEM_DB_URI'] = args.system_db_uri
    sys.path.append(args.folder)
    reloader = Reloader()
    reloader.import_apps()
    for item in get_routes():
        print(item)
    start_server(args)


if __name__ == '__main__':
    main()
