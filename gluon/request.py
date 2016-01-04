import os
import datetime
import logging
from gluon.storage import List
from gluon.current import current
from gluon.utils import reconstruct_url, web2py_uuid, get_client, get_localhosts
from gluon.environ_parsers import parse_cookies, parse_body, parse_get_vars, parse_post_vars, parse_all_vars, parse_user_agent
from gluon.memoize_property import memoize_property

def session_cached(func):
    if hasattr(current,'session') and current.session:
        name = '_'+func.__name__
        def tmp(self):
            value = current.session.get(name)
            if not value:
                current.session[name] = value = func(self)
            return value
        tmp.__name__ = func.__name__
        return tmp
    else:
        return func

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.items = filter(lambda x:x, self.environ['PATH_INFO'].split('/'))
        self.application = self.items[0] if len(self.items)>0 else 'welcome'
        self.controller = self.items[1] if len(self.items)>1 else 'default'
        function = self.items[2] if len(self.items)>2 else 'index'
        self.function, self.extension = (function+'.html').split('.')[:2]
        self.folder = os.path.join('applications',self.application)
        self.logger = logging.getLogger('Web2py.app.%s' % self.application)
    @memoize_property
    def uuid(self):
        return '%s.%s.%s.%s' % (self.application,self.client.replace(':', '_'),self.utcnow.strftime('%Y-%m-%d.%H-%M-%S'),web2py_uuid())
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
    def args(self):
        return List(self.items[3:])
    @memoize_property
    def get_vars(self):
        return parse_get_vars(self.environ)
    @memoize_property
    def post_vars(self):
        return parse_post_vars(self.environ, self.body)
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
    @memoize_property
    @session_cached
    def user_agent(self):
        return parse_user_agent(self.environ)
