#!/usr/bin/env python
from __future__ import print_function

# standard modules
import argparse
import cgitb
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
import sys
import threading
import time
import traceback
import types
import urllib.parse
import uuid
import http.client

# optional web servers for speed
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

# third part modules
import jwt       # pip import PyJWT
import bottle    # pip import bottle
import yatl      # pip import yatl
import pydal     # pip import pydal
import pluralize # pip import pluralize
from pydal import _compat

import reloader

__all__ = ['render', 'DAL', 'Field', 'action', 'request', 'response', 'redirect', 'abort', 'HTTP', 'Session', 'Cache', 'user_in', 'Translator', 'URL']

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
        return obj.to_list()
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
    return json.dumps(obj, default=objectify, sort_keys=sort_keys, indent=indent)

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

class Translator(pluralize.Translator, Fixture):
    def on_request(self): self.select(request.headers.get('Accept-Language', 'en'))
    def on_success(self): response.headers['Content-Language'] = self.local.tag

#########################################################################################
# The template rendered fixture
#########################################################################################

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
        context.update(URL=URL)
        context.update(output)
        context['__vars__'] = output
        app_folder = os.path.join(os.environ['WEB3PY_APPLICATIONS_FOLDER'], request.app_name)
        path = os.path.join(app_folder, 'templates')
        filename = os.path.join(path, self.filename)
        template = Template.cache.get(filename, lambda: Template.read(filename), expiration=1,
                                      monitor=lambda: os.path.getmtime(filename))
        output = yatl.render(template, path=path, context=context, delimiters=self.delimiters)
        return output

#########################################################################################
# The session fixture
#########################################################################################

class Session(Fixture):

    def __init__(self, secret=None, expiration=None, algorithm='HS256', storage=None, secure=False):
        """
        secret is the shared key used to encrypt the session (using algorithm)
        expiration is in seconds
        (optional) storage must have a get(key) and set(key,value,expiration) methods
        if not provided session is stored in jwt cookie else the jwt is stored in storage and its uuid key in cookie
        """
        if not secret and not storage: raise SyntaxError("a secret or a storage must be specified")
        self.secret = secret
        self.expiration = expiration
        self.algorithm = algorithm
        self.local = threading.local()
        self.storage = storage
        self.secure = secure
        if isinstance(storage, Session):
            self.__prerequisites__ = [storage]
        if hasattr(storage, '__prerequisites__'):
            self.__prerequisites__ = storage.__prerequisites__

    def load(self):
        self.local.session_cookie_name = '%s_session' % request.app_name        
        cookie_data = _compat.to_bytes(request.get_cookie(self.local.session_cookie_name))
        self.local.changed = False
        self.local.secure = request.url.startswith('https')
        self.local.data = {}
        if cookie_data:
            try:
                if self.storage:
                    json_data = self.storage.get(cookie_data)
                    if json_data:
                        self.local.data = json.loads(json_data)
                else:
                    self.local.data = jwt.decode(cookie_data, self.secret, algorithms=[self.algorithm])
                if self.expiration is not None and self.storage is None:
                    assert self.local.data['timestamp'] > time.time() - int(self.expiration)
                assert self.local.data.get('secure') == self.local.secure
            except (jwt.exceptions.InvalidSignatureError, AssertionError, ValueError):
                pass
        if not 'uuid' in self.local.data:
            self.local.changed = True
            self.local.data['uuid'] = _compat.to_native(str(uuid.uuid4()))
            self.local.data['secure'] = self.local.secure

    def save(self):
        self.local.data['timestamp'] = time.time()        
        if self.storage:
            cookie_data = self.local.data['uuid']
            self.storage.set(cookie_data, json.dumps(self.local.data), self.expiration)
        else:
            cookie_data = jwt.encode(self.local.data, self.secret, algorithm=self.algorithm)
        response.set_cookie(self.local.session_cookie_name, 
                            _compat.to_native(cookie_data), path='/', secure=self.local.secure)


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
# the URL helper
#########################################################################################

def URL(*parts, vars=None, hash=None, scheme=False):
    """ 
    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{app_name}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{app_name}/a/b?x=1
    """
    prefix = '/%s/' % request.app_name if request.app_name != '_default' else '/'
    url = prefix + '/'.join(map(urllib.parse.quote, parts))
    if vars:
        url += '?' + '&'.join('%s=%s' % (k, urllib.parse.quote(str(v))) for k,v in vars.items())
    if hash:
        url += '#%s' % hash
    if not scheme is False:
        orig_scheme, _, domain = request.url.split('/')[:3]
        scheme = orig_scheme if scheme is True else '' if scheme is None else scheme + ':'
        url = '%s//%s/%s' % (scheme, domain, url)
    return url

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
    def uses(*fixtures_in):
        """associated fixtures to an action"""
        fixtures = []
        for fixture in fixtures_in:
            # a template string is a fixture
            if isinstance(fixture, str):
                fixtures.append(Template(obj))
            else:
                # fixtures may have prerequisites (dependencies)
                for other_fixture in getattr(fixture, '__prerequisites__', []):
                    if not other_fixture in fixtures:
                        fixtures.append(other_fixture)
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
                ret = func(*func_args, **func_kwargs)
                if isinstance(ret, dict):
                    response.headers['Content-Type'] = 'application/json'
                    ret = dumps(ret)
                return ret
            except bottle.HTTPResponse as e:
                raise e
            except Exception:
                logging.error(traceback.format_exc())
                try:
                    ticket = ErrorStorage().log(request.app_name, get_error_snapshot())
                except Exception:
                    logging.error(traceback.format_exc())
                    ticket = "unknown"
                return  error_page(500, button_text=ticket, href='/_dashboard/ticket/'+ticket)
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
        app_name = folder[len(os.environ['WEB3PY_APPLICATIONS_FOLDER'])+1:].split(os.sep)[0]
        path = ('/' if app_name == '_default' else '/%s/' % app_name) + self.path # the _default app has no prefix
        func = action.catch_errors(app_name, func)
        func = bottle.route(path, **self.kwargs)(func)
        if path.endswith('/index'): # /index is always optional
            func = bottle.route(path[:-6] or '/', **self.kwargs)(func)
        return func

def user_in(session):
    def requirement():
        session.on_request()
        return session.get('user', None) is not None
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
    data['os_environ'] = {key: str(value) for key, value in os.environ.items()}
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
        f['vars'] = {key: str(value) for key, value in locals.items() if not key.startswith('__')}
        stackframes.append(f)

    return data


class ErrorStorage(object):
    def __init__(self):
        uri = os.environ['WEB3PY_SERVICE_DB_URI']
        folder = os.environ['WEB3PY_SERVICE_FOLDER']
        self.db = DAL(uri, folder=folder)
        self.db.define_table('web3py_error',
                             Field('uuid'),
                             Field('app_name'),
                             Field('method'),
                             Field('path','string'),
                             Field('timestamp','datetime'),
                             Field('client_ip','string'),
                             Field('error','string'),
                             Field('snapshot','json'))

    def log(self, app_name, error_snapshot):
        ticket_uuid = str(uuid.uuid4())
        try:
            id = self.db.web3py_error.insert(
                uuid=ticket_uuid,
                app_name=app_name,
                method=request.method,
                path=request.path,
                timestamp=datetime.datetime.utcnow(),
                client_ip=request.environ.get('REMOTE_ADDR'),
                error=error_snapshot['exception_value'],
                snapshot=error_snapshot)
            print('id=',id)
            self.db.commit()
            return ticket_uuid
        except Exception:
            self.db.rollback()
            return 'internal-error'

    def get(self, ticket_uuid=None, since=None, until=None, limitby=100, app_name=None):
        db = self.db
        if ticket_uuid: 
            query, orderby = db.web3py_error.uuid==ticket_uuid, None
            rows = db(query).select(orderby=orderby, limitby=(0, limitby)).as_list()
        else:
            if since:
                query, orderby = db.web3py_error.timestamp >= since, db.web3py_error.timestamp
            elif until:
                query, orderby = db.web3py_error.timestamp < until, ~db.web3py_error.timestamp
            else:
                raise NotImplementedError
            if app_name:
                query &= db.web3py_error.app_name == app_name        
            fields = [field for field in db.web3py_error if not field.type == 'json']
            rows = db(query).select(*fields, orderby=orderby, limitby=(0, limitby)).as_list()
        return rows if not ticket_uuid else rows[0] if rows else None
    

#########################################################################################
# loading/reloading logic
#########################################################################################

class Reloader(object):

    ROUTES = []
    MODULES = {}
    ERRORS = {}

    @staticmethod
    def import_apps():
        """import or reimport modules and exposed static files"""
        reloader.enable()
        folder = os.environ['WEB3PY_APPLICATIONS_FOLDER']
        app = bottle.default_app()
        app.routes.clear()
        # app.routes = app.routes[:]
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
        reloader.disable()
        # expose static files
        for path in new_apps:
            @bottle.route('/%s/static/<filename:path>' % path.split(os.path.sep)[-1])
            def server_static(filename, path=path):
                return bottle.static_file(filename, root=os.path.join(path, 'static'))
        # register routes
        routes = []
        def to_filename(module):
            filename = module.replace('.', os.path.sep)
            filename = os.path.join(filename, '__init__.py') if not module.count('.') else filename + '.py'
            return filename
        for route in app.routes:
            func = route.callback
            routes.append({'rule': route.rule,
                           'method': route.method,
                           'filename': to_filename(func.__module__),
                           'action': func.__name__})
        Reloader.ROUTES = sorted(routes, key=lambda item: item['rule'])


#########################################################################################
# web server and reload logic
#########################################################################################

def error_page(code, button_text=None, href='#', color=None,  message=None):
    message = http.client.responses[code].upper() if message is None else message
    color = {'4':'#F44336', '5': '#607D8B'}.get(str(code)[0], '#2196F3') if not color else color
    return yatl.render('<html><head><style>body{color:white;text-align: center;background-color:{{=color}};font-family:serif} h1{font-size:6em;margin:16vh 0 8vh 0} h2{font-size:2em;margin:8vh 0} a{color:white;text-decoration:none;font-weight:bold;padding:10px 10px;border-radius:10px;border:2px solid #fff;transition: all .5s ease} a:hover{background:rgba(0,0,0,0.1);padding:10px 30px}</style></head><body><h1>{{=code}}</h1><h2>{{=message}}</h2>{{if button_text:}}<a href="{{=href}}">{{=button_text}}</a>{{pass}}</body></html>', context=dict(code=code, message=message, button_text=button_text, href=href, color=color))

@bottle.error(404)
def error404(error):
    guess_app_name = request.path.split('/')[1]
    return error_page(404, button_text=guess_app_name, href='/'+guess_app_name)

#########################################################################################
# web server and reload logic
#########################################################################################

def start_server(args):
    host, port = args.address.split(':')
    if args.number_workers < 1:
        bottle.run(host=host, port=int(port))
    else:
        if not gunicorn:
            logging.error('gunicorn not installed')
        elif not gevent:
            logging.error('gevent not installed')
        else:
            bottle.run(server='gevent', host=host, port=int(port),
                       workers=args.number_workers, worker_class='gevent', reloader=False,
                       certfile=args.ssl_cert_filename, keyfile=args.ssl_key_filename)

ART = r"""
 _______  ____________  ____  ______  __
|  ____/ / / ____/ __ |/___ \/ __ \ \/ /
| |     / / /_  / /_/ /___/ / /_/ /\  /
| | /| / / __/ / __  //__  / ____/ / /
| |/ |/ / /___/ /_/ /___/ / / ____/ /
|___/|_/_____/_____/_____/_/ /_____/
It is still experimental...
"""

def main():
    print(ART)
    parser = argparse.ArgumentParser()
    parser.add_argument('applications_folder', help='path to the applications folder')
    parser.add_argument('--address', default='127.0.0.1:8000',help='serving address')
    parser.add_argument('--number_workers', default=0, type=int, help='number of gunicorn workers')
    parser.add_argument('--ssl_cert_filename', default=None, type=int, help='ssl certificate file')
    parser.add_argument('--ssl_key_filename', default=None, type=int, help='ssl key file')
    parser.add_argument('--service_db_uri', default='sqlite://service.storage', type=str, help='db uri for logging')
    parser.add_argument('--service_folder', default='/tmp/web3py', type=str, help='db uri for logging')
    action.args = args = parser.parse_args()
    args.applications_folder = os.path.abspath(args.applications_folder)
    for key in args.__dict__:
        os.environ['WEB3PY_'+key.upper()] = str(args.__dict__[key])
    if not os.path.exists(args.service_folder): os.makedirs(args.service_folder)
    sys.path.append(args.applications_folder)
    Reloader.import_apps()
    start_server(args)
