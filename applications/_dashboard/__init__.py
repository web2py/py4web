import os
import sys
import time
from web3py import __version__, action, request, response, redirect
from web3py.core import Reloader, dumps, ErrorStorage
from yatl.helpers import BEAUTIFY

@action('/dashboard')
def home():
    redirect('/%s/static/index.html' % request.app_name)

@action('info')
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
def routes():
    return {'payload':Reloader.ROUTES, 'status':'success'}

@action('reload')
def reload():
    Reloader.import_apps()
    return 'ok'

@action('apps')
def apps():
    apps = os.listdir(os.environ['WEB3PY_APPLICATIONS'])
    apps = [{'name':app, 'error':Reloader.ERRORS.get(app)} 
            for app in apps 
            if os.path.isdir(os.path.join(os.environ['WEB3PY_APPLICATIONS'], app)) and
            not app.startswith('__')]
    return {'payload': apps, 'status':'success'}

@action('walk/<path:path>')
def walk(path):
    top = os.path.join(os.environ['WEB3PY_APPLICATIONS'], path)
    if not os.path.exists(top) or not os.path.isdir(top):
        return {'status':'error', 'message':'Folder does not exist'}
    store = {}
    for root, dirs, files in os.walk(top, topdown=False):
        store[root] = {
            'dirs':[{'name':dir, 'content':store[os.path.join(root,dir)]} for dir in dirs if dir[0]!='.' and dir[:2]!='__'],
            'files':[f for f in files if f[0]!='.' and f[-1]!='~' and f[-4:]!='.pyc']
                     
            }
    return {'payload':store[top], 'status':'success'}

@action('load/<path:path>')
def load(path):
    path = os.path.join(os.environ['WEB3PY_APPLICATIONS'], path) # ADD SECURITY
    content = open(path,'rb').read().decode('utf8')
    return {'payload':content, 'status':'success'}

@action('load_bytes/<path:path>')
def load_bytes(path):
    path = os.path.join(os.environ['WEB3PY_APPLICATIONS'], path) # ADD SECURITY 
    return open(path,'rb').read()

@action('save/<path:path>', method='POST')
def save(path):
    path = os.path.join(os.environ['WEB3PY_APPLICATIONS'], path) # ADD SECURITY 
    with open(path, 'wb') as myfile:
        myfile.write(request.body.read())
    return {'status':'success'}

@action('packed/<appname>')
def packed(appname):
    deposit = os.path.join(os.environ['WEB3PY_APPLICATIONS'], appname, '.deposit') # ADD SECURITY 
    if not os.path.exists(deposit):
        os.mkdir(deposit)
    name = 'app.'+appname+'.w3p'
    dest = os.path.join(deposit, name)
    app_pack(dest, os.path.join('applications',appname))
    return static(os.path.abspath(dest))

@action('delete/<path:path>', method='post')
def delete(path):
    fullpath = os.path.join(os.environ['WEB3PY_APPLICATIONS'], path) # ADD SECURITY 
    recursive_unlink(fullpath)
    return {'status':'success'}

@action('ticket/<ticket_uuid>')
@action.uses('ticket.html')
def error_ticket(ticket_uuid):
    return dict(ticket_record=BEAUTIFY(ErrorStorage().get(ticket_uuid=ticket_uuid)))

