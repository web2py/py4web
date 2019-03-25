from __future__ import print_function
import re
import os
import sys
import json
import copy
import time
import uuid
import types
import numbers
import datetime
import argparse
import inspect
import importlib
import functools
import traceback
import collections

try: 
    import gunicorn
except:
    gunicorn = None
try:
    import gevent; gevent.monkey.patch_all()
except:
    gevent = None

import jwt # PyJWT
import bottle
import yatl
from pydal import DAL, Field

__all__ = ['render', 'DAL', 'Field', 'action', 'request', 'response', 'redirect', 'HTTP', 'Session']

render = yatl.render
request = bottle.request
response = bottle.response
redirect = bottle.redirect           

class HTTP(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body

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

def dumps(obj):
    return json.dumps(obj, default=objectify, sort_keys=True, indent=2)

#########################################################################################
# Session logic (uses encrypted jwt token in cookies)
#########################################################################################

class Session(object):
    def __init__(self, secret, expiration=None, algorithm='HS256'):
        self.secret = secret
        self.expiration = expiration
        self.algorithm = algorithm        

    def load(self):
        self.session_cookie_name = '%s_session' % request.app_name
        self.changed = False
        enc_data = request.get_cookie(self.session_cookie_name)
        try:
            self.data = jwt.decode(enc_data, self.secret, algorithms=[self.algorithm])
            assert self.expiration is None or self.data['timestamp'] > time.time() - int(self.expiration)
        except:
            print(traceback.format_exc())
            self.data = {}
        if not 'uuid' in self.data:
            self['uuid'] = str(uuid.uuid4())
    def get(self, key, default=None):
        return self.data.get(key, default)
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.changed = True
        self.data[key] = value
    def save(self):
        self.data['timestamp'] = time.time()
        enc_data = jwt.encode(self.data, self.secret, algorithm = self.algorithm)
        response.set_cookie(self.session_cookie_name, enc_data.decode('utf8'))

#########################################################################################
# the action decorator
#########################################################################################

class action(object):
    """@action(...) is a decorator for functions to be exposed as actions"""

    def __init__(self, path, **kwargs):
        self.path = path
        self.kwargs = kwargs
        self.view = kwargs.pop('view', None)

    def __call__(self, function):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        folder = os.path.dirname(os.path.normpath(module.__file__))
        app_name = os.path.split(folder)[-1]  ### FIX ME
        path = self.path.replace('/$app_name/', '/%s/' % app_name)
        defaults = [item.default for item in inspect.signature(function).parameters.values()]
        self.dbs = [db for db in defaults if hasattr(db, '_adapter')]
        self.sessions = [session for session in defaults if isinstance(session, Session)]        
        @bottle.route(path, **self.kwargs)
        @functools.wraps(function)
        def wrapper(*func_args, **func_kwargs):
            request.app_name = app_name
            try:
                for db in self.dbs: db._adapter.reconnect()
                for session in self.sessions: session.load()
                output = function(*func_args, **func_kwargs)
                if isinstance(output, dict):
                    if self.view:
                        path = os.path.join(folder, 'templates')
                        with open(os.path.join(path, self.view)) as stream:
                            context = dict(request=request)
                            context.update(yatl.helpers.__dict__)
                            context.update(output)
                            output = yatl.render(stream.read(), path=path, context=context, delimiters='[[ ]]')
                    else:
                        output = dumps(output)
                for db in self.dbs: db._adapter.commit()
            except bottle.HTTPResponse as e:
                raise e
            except HTTP as http:
                for db in self.dbs: db._adapter.commit()
                output = bottle.HTTPResponse(status=http.status, body=http.body)
            except:
                request.session = None
                for db in self.dbs: db._adapter.rollback()
                tb = traceback.format_exc()
                output = '<html><body><pre>%s</pre></body></html>' % yatl.xmlescape(tb)
            [session.save() for session in self.sessions if session.changed]
            return output        
        return wrapper    


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
# loading/reloading logic
#########################################################################################

class Reloader(object):
    
    ERRORS = {}

    def __init__(self, folder):
        self.folder = folder

    def import_apps(self):
        for app_name in os.listdir(self.folder):
            path = os.path.join(self.folder, app_name)
            if os.path.isdir(path) and not path.endswith('__'):
                try:
                    importlib.import_module(path.replace(os.sep, '.'), self.folder)
                    Reloader.ERRORS[app_name] = None
                except:
                    print(traceback.format_exc())
                    Reloader.ERRORS[app_name] =  traceback.format_exc()
                @bottle.route('/%s/static/<filename:path>' % app_name)
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
                       'filename': func.__module__.replace('.',os.sep) + '.py',
                       'action': func.__name__})
    return sorted(routes, key=lambda item: item['rule'])

#########################################################################################
# web server and reload logic
#########################################################################################

def start_server(args):
    host, port = args.address.split(':')
    if args.workers < 1:
        bottle.run(host=host, port=int(port), reloader=True)
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
    action.args = args = parser.parse_args()
    args.folder = os.path.normpath(args.folder)
    os.environ['WEB3PY_APPLICATIONS'] = args.folder
    sys.path.append(args.folder)
    reloader = Reloader(args.folder)
    reloader.import_apps()

    for item in get_routes():
        print(item)
    start_server(args)

if __name__ == '__main__':
    main()
