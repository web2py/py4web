# TODO:
# - handle content type
# - sessions
# - cookies output
# - error handling

import os
import sys
import traceback
import Cookie

from gluon import dal

from gluon.current import current
from gluon.storage import Storage
from gluon.rocket import HttpServer
from gluon.contenttype import contenttype
from gluon.http import HTTP
from gluon.template import render
from gluon.streamer import stream_file_or_304_or_206
from gluon.restricted_error import RestrictedError
from gluon.languages import translator
from gluon.request import Request
from gluon.response import Response
from gluon.session import Session
from pydal.base import BaseAdapter

os_path_join = os.path.join

def failsafe(func):
    try:
        return func()
    except:
        return None

class CodeRunner(object):

    def __init__(self, context=None):
        self.context = context or {}    

    @staticmethod
    def cached_code(filename, cache_controllers = {}):
        new_mtime = os.path.getmtime(filename)
        try:
            mtime, code = cache_controllers[filename]
            if new_mtime != mtime:
                raise KeyError
        except KeyError:
            with open(filename) as myfile:
                code = compile(myfile.read(), filename, 'exec')
            cache_controllers[filename] = (new_mtime, code)
        return code

    def import_code(self, filename, function_name=None, *args, **kwargs):        
        code = self.cached_code(filename)
        try:
            exec code in self.context
            if function_name:
                return self.context[function_name](*args, **kwargs)
        except Exception, error:
            etype, evalue, tb = sys.exc_info()
            output = "%s %s" % (etype, evalue)
            raise RestrictedError(filename, code, output, self.context)

def simple_app(environ, start_response):
    import gluon
    common_context = {key:getattr(gluon,key) for key in dir(gluon)}
    have_databases = False
    try:
        try:
            request = Request(environ)
            request_folder = request.folder            
            if request.controller == 'static':
                # serve static file 
                static_folder =  os_path_join(request_folder,'static')
                filename = os_path_join(static_folder,*request._items[2:])
                if not filename.startswith(static_folder+'/'): raise HTTP(404)
                if not os.path.exists(filename): raise HTTP(404)
                stream_file_or_304_or_206(filename, environ=environ)                
            else:
                # serve dynamic pages
                response = Response()
                session = Session()
                # build context and inject variables into context (~20% slow down)
                runner = CodeRunner(common_context.copy())
                database_folder =  os_path_join(request_folder,'databases')
                have_databases = os.path.exists(database_folder)
                if have_databases:
                    BaseAdapter.set_folder(os_path_join(request.folder, 'databases'))
                runner.context['T'] = translator(os_path_join(request.folder,'languages'),
                                                 request.environ.get('HTTP_ACCEPT_LANGUAGE'))
                runner.context['request'] = current.request = request
                runner.context['response'] = current.response = response
                runner.context['session'] = current.session = session

                controllers_folder = os_path_join(request.folder,'controllers') 
                controller_filename = os_path_join(controllers_folder,request.controller+'.py')
                if not controller_filename.startswith(controllers_folder+'/'): raise HTTP(404)
                if not os.path.exists(controller_filename): raise HTTP(404)
                # import models, ugly but faster than glob, stull 5-10% of tota;
                models_folder = os_path_join(request.folder,'models')
                if os.path.exists(models_folder):
                    for filename in sorted(filter(lambda x: x[-3:]=='.py',os.listdir(models_folder))): 
                        runner.import_code(models_folder+os.sep+filename)
                # run controller action
                view_context = runner.context.copy()
                content = runner.import_code(controller_filename, request.function)
                # optionally run view
                func_ext = request.function+'.'+request.extension
                if isinstance(content, dict):
                    view_context.update(content)
                    template_folder = os_path_join(request.folder,'views')
                    template_filename = os_path_join(template_folder,request.controller,func_ext) # FIX THIS: response.view
                    if os.path.exists(template_filename):
                        content = render(filename=template_filename, path = template_folder, context = view_context)
                    else:
                        content = repr(view_context)
                        
                response.headers["Content-type"] = contenttype(func_ext)                
                http = HTTP(response.status, content, headers=response.headers)
                if hasattr(response,'_cookies'):
                    http.cookies2headers(response.cookies)

                have_databases = have_databases and response.auto_commit
                if have_databases:
                    session._try_store_in_db(request, response)
                    BaseAdapter.close_all_instances('commit')
                    have_databases = False
                session._try_store_in_cookie_or_file(request, response)

                raise http   
        except HTTP, http:
            return http.to(start_response, env=environ)
        except Exception, err: 
            if isinstance(err, RestrictedError):
                ticket = err.log()
            else:
                print traceback.format_exc()
                #request.logger.error(traceback.format_exc())
                ticket = 'unknown'
            return  HTTP(500, ticket).to(start_response, env=environ)
    except:
        request.logger.error(traceback.format_exc())
        return HTTP(500, 'unknown').to(start_response, env=environ)
    finally:
        if have_databases:
            failsafe(lambda: BaseAdapter.close_all_instances('rollback'))

def main():
    print 'starting'
    HttpServer(simple_app, port=8888).start()
