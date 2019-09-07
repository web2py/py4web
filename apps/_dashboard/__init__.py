import os
import sys
import time
import shutil
import datetime
import zipfile
import subprocess
import io

import requests

import py4web
from py4web import __version__, action, abort, request, response, redirect, Translator
from py4web.core import Reloader, dumps, ErrorStorage, Session, Fixture
from pydal.validators import CRYPT
from yatl.helpers import BEAUTIFY
from . utils import *

MODE = os.environ.get('PY4WEB_DASHBOARD_MODE', 'none')
FOLDER = os.environ['PY4WEB_APPS_FOLDER']
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

session_secured = action.uses(Logged(session))

if MODE in ('demo', 'readonly', 'full'):
    @action('index')
    @action.uses('index.html', session, T)
    def index():
        return dict(languages = dumps(T.local.language), 
                    mode = MODE,
                    user_id=(session.get('user') or {}).get('id'))

    @action('login', method='POST')
    @action.uses(session)
    def login():
        if MODE == 'demo':
            valid = True
        else:
            valid = False
            password = request.json.get('password')
            password_file = os.environ.get('PY4WEB_PASSWORD_FILE')
            if password and password_file and os.path.exists(password_file):
                with open(password_file, 'r') as fp:
                    encrypted_password = fp.read().strip()
                    valid = CRYPT()(password)[0] == encrypted_password
        if valid:
            session['user'] = dict(id=1)
        return dict(user=valid, mode=MODE)
    
    @action('logout', method='POST')
    @action.uses(session)
    def logout():
        session['user'] = None
        return dict()

    @action('dbadmin')
    @action.uses(Logged(session), 'dbadmin.html')
    def dbadmin():
        return dict(languages = dumps(T.local.language))

    @action('info') 
    @session_secured
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
    @session_secured
    def routes():
        """returns current registered rounts"""
        return {'payload':Reloader.ROUTES, 'status':'success'}
    

    @action('apps')
    @session_secured
    def apps():
        """returns a list of installed apps"""
        apps = os.listdir(FOLDER)
        apps = [{'name':app, 'error':Reloader.ERRORS.get(app)} 
                for app in apps 
                if os.path.isdir(os.path.join(FOLDER, app)) and
                not app.startswith('__') and
                not app.startswith('.')]                
        apps.sort(key=lambda item: item['name'])
        return {'payload': apps, 'status':'success'}

    @action('walk/<path:path>')
    @session_secured
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
    @session_secured
    def load(path):
        """loads a text file"""
        path = safe_join(FOLDER, path) or abort()
        content = open(path,'rb').read().decode('utf8')
        return {'payload':content, 'status':'success'}
    
    @action('load_bytes/<path:path>')
    @session_secured
    def load_bytes(path):
        """loads a binary file"""
        path = safe_join(FOLDER, path) or abort()
        return open(path,'rb').read()

    @action('packed/<path:path>')
    @session_secured
    def packed(path):
        """packs an app"""
        appname = path.split('.')[-2]
        appname = sanitize(appname)
        app_dir = os.path.join(FOLDER, appname)
        store = io.BytesIO()
        zip = zipfile.ZipFile(store, mode='w')
        for root, dirs, files in os.walk(app_dir, topdown=False):
            if not root.startswith('.'):
                for name in files:
                    if not (name.endswith('~') or name.endswith('.pyc') or name[:1] in '#.'):
                        filename = os.path.join(root, name)
                        short = filename[len(app_dir+os.path.sep):]
                        print('added', filename, short)
                        zip.write(filename, short)
        zip.close()
        data = store.getvalue()
        response.headers['Content-Type'] = 'application/zip'
        return data

    @action('tickets')
    @session_secured
    def tickets():
        """returns most recent tickets groupped by path+error"""
        tickets = error_storage.get()
        return {'payload': tickets}

    @action('ticket/<ticket_uuid>')
    @action.uses('ticket.html')
    def error_ticket(ticket_uuid):
        return dict(ticket=ErrorStorage().get(ticket_uuid=ticket_uuid))

    @action('rest/<path:path>', method=['GET','POST','PUT','DELETE'])
    @session_secured
    def api(path):
        # this is not final, equires pydal 19.5
        args = path.split('/')
        app_name = args[0]
        from py4web.core import Reloader, DAL
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
    @session_secured
    def reload():
        """reloads installed apps"""
        Reloader.import_apps()
        return 'ok'

    @action('save/<path:path>', method='POST')
    @session_secured
    def save(path):
        """saves a file"""
        path = safe_join(FOLDER, path) or abort()
        with open(path, 'wb') as myfile:
            myfile.write(request.body.read())
        return {'status':'success'}

    @action('delete/<path:path>', method='POST')
    @session_secured
    def delete(path):
        """deletes a file"""
        fullpath = safe_join(FOLDER, path) or abort()
        recursive_unlink(fullpath)
        return {'status':'success'}

    @action('new_app', method='POST')
    @session_secured
    def new_app():
        form = request.json
        target_dir = safe_join(FOLDER, form['name'])
        if os.path.exists(target_dir):
            if form['mode'] == 'new':
                abort(500) # already validated client side
            elif form['mode'] == 'replace':
                shutil.rmtree(target_dir)
        elif form['type'] != 'web' and not form['source'].endswith('.git'):
            os.mkdir(target_dir)
        assets_dir = os.path.join(os.path.dirname(py4web.__file__), 'assets')
        source = None
        if form['type'] == 'minimal':            
            source = os.path.join(assets_dir,'py4web.app._minimal.zip')
        elif form['type'] == 'scaffold':
            source = os.path.join(assets_dir,'py4web.app._scaffold.zip')
        elif form['type'] == 'web':
            source = form['source']
        elif form['type'] == 'upload':
            source_stream = io.BytesIO(base64.b64decode(form['file']))
        else:
            abort(500)
        # TODO catch and report better errors below
        if form['type'] == 'upload':
            zip = zipfile.ZipFile(source_stream, 'r')
            zip.extractall(target_dir)
            zip.close()
        elif not '://' in source:  # install from a local asset (zip) file
            zip = zipfile.ZipFile(source, 'r')
            zip.extractall(target_dir)
            zip.close()
        elif source.endswith('.zip'):  # install from the web (zip file)
            res = requests.get(source)
            mem_zip = io.BytesIO(res.content)
            zipfile.ZipFile(mem_zip, 'r')
            zip.extractall(target_dir)
            zip.close()
        elif source.endswith('.git'):  # clone from a git repo
            if subprocess.call(['git', 'clone', source, form['name']]):
                abort(500)
        else:
            abort(400)
        return {'status':'success'}

    


