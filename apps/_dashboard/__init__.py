import os
import sys
import time
import datetime
from web3py import __version__, action, request, response, redirect, Translator
from web3py.core import Reloader, dumps, ErrorStorage, Session, Fixture
from pydal.validators import CRYPT
from yatl.helpers import BEAUTIFY
from . utils import *

MODE = os.environ['WEB3PY_DASHBOARD_MODE']
FOLDER = os.environ['WEB3PY_APPS_FOLDER']
APP_FOLDER = os.path.dirname(__file__)
T_FOLDER = os.path.join(APP_FOLDER, 'translations')
T = Translator(T_FOLDER)
error_storage = ErrorStorage()
db = error_storage.db
session = Session()

class Logged(Fixture):

    def __init__(self, session):
        self.__prerequisites__ = [session]
        self.session = session
        
    def on_request(self):
        user = self.session.get('user')
        if not user or not user.get('id'):
            abort(403)

protected = action.uses(Logged(session))

if MODE in ('demo', 'full'):
    @action('index')
    @action.uses('index.html', session, T)
    def index():
        return dict(languages = dumps(T.local.language), user_id=(session.get('user') or {}).get('id'))

    @action('login', method='POST')
    @action.uses(session)
    def login():
        ### TODO PREVENT CSRF
        password = request.json.get('password')
        valid = password and CRYPT()(password)[0] == os.environ['WEB3PY_PASSWORD']
        if valid: session['user'] = dict(id=1)
        return dict(user=valid)
    
    @action('logout', method='POST')
    @action.uses(session)
    def logout():
        session['user'] = None
        return dict()

    @action('dbadmin')
    @protected
    def dbadmin():
        return dict(languages = dumps(T.local.language))

    @action('info') 
    @protected
    def info():
        vars = [{'name':'python', 'version':sys.version}]
        for module in sorted(sys.modules):
            if not '.' in module:
                try:
                    m = __import__(module)
                    if '__version__' in dir(m):
                        vars.append({'name':module, 'version':m.__version__})
                except ImportError: pass
        return {'status':'success', 'payload':vars}

    @action('routes')
    @protected
    def routes():
        """returns current registered rounts"""
        return {'payload':Reloader.ROUTES, 'status':'success'}
    

    @action('apps')
    @protected
    def apps():
        """returns a list of installed apps"""
        apps = os.listdir(FOLDER)
        apps = [{'name':app, 'error':Reloader.ERRORS.get(app)} 
                for app in apps 
                if os.path.isdir(os.path.join(FOLDER, app)) and
                not app.startswith('__')]
        apps.sort(key=lambda item: item['name'])
        return {'payload': apps, 'status':'success'}

    @action('walk/<path:path>')
    @protected
    def walk(path):
        """returns a nested folder structure as a tree"""
        top = os.path.join(FOLDER, path)
        if not os.path.exists(top) or not os.path.isdir(top):
            return {'status':'error', 'message':'folder does not exist'}
        store = {}
        for root, dirs, files in os.walk(top, topdown=False):
            store[root] = {
                'dirs':list(sorted([{'name':dir, 'content':store[os.path.join(root,dir)]} 
                                    for dir in dirs if dir[0]!='.' and dir[:2]!='__'], 
                                   key=lambda item: item['name'])),
                'files':list(sorted([f for f in files if f[0]!='.' and f[-1]!='~' and f[-4:]!='.pyc']))
                }
        return {'payload':store[top], 'status':'success'}

    @action('load/<path:path>')
    @protected
    def load(path):
        """loads a text file"""
        path = safe_join(FOLDER, path) or abort()
        content = open(path,'rb').read().decode('utf8')
        return {'payload':content, 'status':'success'}
    
    @action('load_bytes/<path:path>')
    @protected
    def load_bytes(path):
        """loads a binary file"""
        path = safe_join(FOLDER, path) or abort()
        return open(path,'rb').read()

    @action('packed/<appname>')
    @protected
    def packed(appname):
        """packs an app"""
        appname = sanitize(appname)
        deposit = os.path.join(FOLDER, appname, '.deposit')
        if not os.path.exists(deposit):
            os.mkdir(deposit)
        name = 'app.'+appname+'.w3p'
        dest = os.path.join(deposit, name)
        app_pack(dest, os.path.join(FOLDER, appname))
        return static(os.path.abspath(dest))
    
    @action('tickets')
    @protected
    def tickets():
        """returns most recent tickets groupped by path+error"""
        tickets = error_storage.get()
        return {'payload': tickets}

    @action('ticket/<ticket_uuid>')
    @action.uses('ticket.html')
    def error_ticket(ticket_uuid):
        return dict(ticket_record=BEAUTIFY(ErrorStorage().get(ticket_uuid=ticket_uuid)))

    @action('rest/<path:path>', method=['GET','POST','PUT','DELETE'])
    @protected
    def api(path):
        # this is not final, equires pydal 19.5
        args = path.split('/')
        app_name = args[0]
        from web3py.core import Reloader, DAL
        from pydal.restapi import RestAPI, ALLOW_ALL_POLICY, DENY_ALL_POLICY        
        policy = ALLOW_ALL_POLICY if MODE == 'full' else DENY_ALL_POLICY
        module = Reloader.MODULES[app_name]
        def url(*args): return request.url + '/' + '/'.join(args)
        databases = [name for name in dir(module) if isinstance(getattr(module, name), DAL)]
        if len(args) == 1:
            def tables(name):
                db = getattr(module, name)
                return [{'name': t._tablename, 
                         'fields': t.fields, 
                         'link': url(name, t._tablename)+'?model=true'} 
                        for t in getattr(module, name)]
            return {'databases': [{'name':name, 'tables': tables(name)} for name in databases]}
        elif len(args) > 2 and args[1] in databases:
            db = getattr(module, args[1])
            id = args[3] if len(args) == 4 else None            
            data = RestAPI(db, policy)(request.method, args[2], id, request.query, request.json)
        else:
            data = {}
        if 'code' in data:
            response.status = data['code']
        return data
    
if MODE == 'full':
    @action('reload')
    @protected
    def reload():
        """reloads installed apps"""
        Reloader.import_apps()
        return 'ok'

    @action('save/<path:path>', method='POST')
    @protected
    def save(path):
        """saves a file"""
        path = safe_join(FOLDER, path) or abort()
        with open(path, 'wb') as myfile:
            myfile.write(request.body.read())
        return {'status':'success'}


    @action('delete/<path:path>', method='post')
    @protected
    def delete(path):
        """deletes a file"""
        fullpath = safe_join(FOLDER, path) or abort()
        recursive_unlink(fullpath)
        return {'status':'success'}



