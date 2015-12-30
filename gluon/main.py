# TODO:
# - handle content type
# - sessions
# - cookies output
# - error handling

import os
import sys
import functools
import threading
import datetime

sys.path.append('site-packages')
sys.path.append('gluon/packages/dal')

from gluon import dal

from gluon.storage import Storage
from gluon.rocket import HttpServer
from gluon.contenttype import contenttype
from gluon.http import HTTP
from gluon.template import render
from gluon.streamer import stream_file_or_304_or_206
from gluon.utils import reconstruct_url, web2py_uuid, get_client, get_localhosts
from gluon.environ_parsers import parse_cookies, parse_body, parse_get_vars, parse_post_vars, parse_all_vars
from gluon.restricted_error import RestrictedError
from pydal.base import BaseAdapter

current = threading.local()

def memoize_property(func):    
    @functools.wraps(func)
    def tmp(self):
        aname = '_'+func.__name__
        try:
            value = getattr(self, aname)
        except AttributeError:
            value = func(self)
            setattr(self, aname, value)
        return value
    return property(tmp)

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self._items = filter(lambda x:x, self.environ['PATH_INFO'].split('/'))
        self.application = self._items[0] if len(self._items)>0 else 'welcome'
        self.controller = self._items[1] if len(self._items)>1 else 'default'
        self.function = self._items[2] if len(self._items)>2 else 'index'
        self.args = self._items[3:]
    @memoize_property
    def uuid(self):
        return web2py_uuid()
    @memoize_property
    def url(self): 
        return reconstruct_url(self.environ)
    @memoize_property
    def now(self):        
        return datetime.datetime.now()
    @memoize_property
    def utcnow(self):
        return datetime.datetime.utcnow()
    @memoize_property
    def body(self):
        return parse_body(self.environ)
    @memoize_property
    def cookies(self):
        return parse_cookies(self.environ)
    @memoize_property
    def get_vars(self):
        return parse_get_vars(self.environ)
    @memoize_property
    def post_vars(self):
        return parse_post_vars(self.environ, self.body.read())
    @memoize_property
    def vars(self):
        return parse_all_vars(self.get_vars, self.post_vars)
    @memoize_property
    def client(self):
        return get_client(self.environ)
    @memoize_property
    def method(self):
        return self.environ['REQUEST_METHOD']
    @memoize_property
    def folder(self):
        raise NotImplementedEror
    @memoize_property
    def is_ajax(self):
        return self.environ.get('HTTP_X_REQUESTED_WITH','').lower() == 'xmlhttprequest'
    @memoize_property
    def is_local(self):
        remote_addr = self.environ['REMOTE_ADDR']
        return (remote_addr in get_localhosts(self.environ) and self.client == remote_addr)
    @memoize_property
    def is_https(self):        
        def e(x): return self.environ.get(x,'').upper()
        return 'HTTPS' in (e('wsgi_url_scheme'), e('HTTP_X_FORWARDED_PROTO')) or e('HTTPS')=='ON'

class Response(object):
    def __init__(self):
        self.status = '200 OK' 
        self.headers = {}
    @memoize_property
    def cookies(self):
        return Cookie.SimpleCookie()
    def stream(self, filename):
        stream_file_or_304_or_206(filename, environ=current.request.environ)
        
    
class CodeRunner(object):

    def __init__(self, environment=None):
        self.environment = environment or {}    

    @staticmethod
    def cached_code(filename, cache_controllers = {}):
        new_mtime = os.path.getmtime(filename)
        try:
            mtime, code = cache_controllers[filename]
            if new_mtime != mtime:
                raise KeyError
        except KeyError:
            code = compile(open(filename).read(), filename, 'exec')
            cache_controllers[filename] = (new_mtime, code)
        return code

    def import_code(self, filename, function_name=None, *args, **kwargs):        
        code = self.cached_code(filename)
        try:
            exec code in self.environment
            if function_name:
                return self.environment[function_name](*args, **kwargs)
        except Exception, error:
            import traceback
            print traceback.format_exc()
            etype, evalue, tb = sys.exc_info()
            output = "%s %s" % (etype, evalue)
            raise RestrictedError(filename, code, output, self.environment)

def simple_app(environ, start_response):
    ext = '.html' # FIX ME
    runner = CodeRunner()
    try:
        try:
            request = Request(environ)
            if request.controller == 'static':
                filename = os.path.join('applications',request.application,'static',*request._items[2:])
                stream_file_or_304_or_206(filename, environ=environ)
            else:
                response = Response()
                runner.environment['request'] = current.request = request
                runner.environment['response'] = current.response = response
                filename = 'applications/%s/controllers/%s.py' % (request.application, request.controller)
                content = runner.import_code(filename, request.function)
                if isinstance(content, dict):
                    template_path = os.path.join('applications',request.application,'views')
                    template_filename = os.path.join(template_path,request.controller,request.function+ext)
                    content = render(filename=template_filename, path = template_path, context = content)
                response.headers["Content-type"] = contenttype(ext)
                raise HTTP(200, content, headers=response.headers)
        except HTTP, http:
            BaseAdapter.close_all_instances('commit')
            return http.to(start_response, env=environ)
        except RestrictedError, err:       
            BaseAdapter.close_all_instances('rollback')
            start_response('500 Internal Error', [("Content-type", "text/plain")])        
            content = 'some error'
            return [content]
    except:
        BaseAdapter.close_all_instances('rollback')
        import traceback
        start_response('500 Internal Error', [("Content-type", "text/plain")])        
        content = traceback.format_exc()    
        return [content]
        

def main():
    print 'starting'
    HttpServer(simple_app, port=8888).start()
