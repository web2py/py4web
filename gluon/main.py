# TODO:
# - handle content type
# - sessions
# - cookies output
# - error handling

import os
import sys
import traceback
import Cookie

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

# some shortcuts
os_path_join = os.path.join
os_path_exists = os.path.exists
 
def failsafe(func, ret=None):
    try: return func()
    except Exception, err: print 'failsafe: %s' % err

# class that caches and executes code in python files
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
                func = self.context.get(function_name)
                if func and callable(func):
                    return self.context[function_name](*args, **kwargs)
                else:
                    raise HTTP(404)
        except HTTP, http:
            raise http
        except Exception, error:
            etype, evalue, tb = sys.exc_info()
            output = "%s %s" % (etype, evalue)
            raise RestrictedError(filename, code, output, self.context)

# the main wsgi app
def main_wsgi_app(environ, start_response):
    import gluon
    common_context = {key:getattr(gluon,key) for key in dir(gluon)}
    have_databases = False
    try:
        try:
            request = Request(environ)
            session = response = None
            request_folder = request.folder            
            # if client requested a static page
            if request.controller == 'static':
                
                static_folder =  os_path_join(request_folder,'static')
                filename = os_path_join(static_folder,*request._items[2:])
                if not filename.startswith(static_folder+'/'): raise HTTP(404)
                if not os_path_exists(filename): raise HTTP(404)
                stream_file_or_304_or_206(filename, environ=environ) # raise HTTP 200
            # if instead client requested a dynamic page
            else:
                # create response and session object (session is disabled here)
                response = Response()
                session = Session()
                # build context and inject variables into context
                runner = CodeRunner(common_context.copy())
                # check if there is a database folder and set the folder
                database_folder =  os_path_join(request_folder,'databases')
                have_databases = os_path_exists(database_folder)
                if have_databases:
                    BaseAdapter.set_folder(os_path_join(request_folder, 'databases'))
                # inject request specific variables into context
                runner.context['request'] = current.request = request
                runner.context['response'] = current.response = response
                runner.context['session'] = current.session = session
                runner.context['T'] = current.T = translator(os_path_join(request_folder,'languages'),
                                                             request.environ.get('HTTP_ACCEPT_LANGUAGE'))
                # raise an error if the controller file is missing
                controllers_folder = os_path_join(request_folder,'controllers') 
                controller_filename = os_path_join(controllers_folder,request.controller+'.py')
                if not controller_filename.startswith(controllers_folder+'/'): raise HTTP(404)
                if not os_path_exists(controller_filename): raise HTTP(404)
                # import models, ugly but faster than glob
                models_folder = os_path_join(request_folder,'models')
                if os_path_exists(models_folder):
                    for filename in sorted(filter(lambda x: x[-3:]=='.py',os.listdir(models_folder))): 
                        runner.import_code(models_folder+os.sep+filename)
                # run controller action
                view_context = runner.context.copy()
                content = runner.import_code(controller_filename, request.function)
                # optionally run view
                func_ext = request.function+'.'+request.extension
                if isinstance(content, dict):
                    view_context.update(content)
                    template_folder = os_path_join(request_folder,'views')
                    # maybe a response.view is specified
                    if response.view:
                        template_filename = os_path_join(template_folder,response.view)
                    # or maybe not
                    else:
                        template_filename = os_path_join(template_folder,request.controller,func_ext)
                    # if the view exists use it
                    if os_path_exists(template_filename):
                        content = render(filename=template_filename, path = template_folder, context = view_context)
                    # else but represent the context as a dict (generic views?)
                    else:
                        content = repr(view_context)
                # set the content type
                response.headers["Content-type"] = contenttype(func_ext)                
                raise HTTP(response.status, content, headers=response.headers)
        # if a HTTP is raised, everything is ok, return
        except HTTP, http:       
            if response:
                # commit databases, if any
                have_databases = have_databases and response.auto_commit
                if have_databases:
                    session._try_store_in_db(request, response)
                    BaseAdapter.close_all_instances('commit')
                    have_databases = False
                # save session, if changed
                session._try_store_in_cookie_or_file(request, response)
                # deal with cookies
                if hasattr(response,'_cookies'):
                    http.cookies2headers(response.cookies)
            return http.to(start_response, env=environ)
        # there was an error
        except Exception, err: 
            # maybe log the ticket
            if isinstance(err, RestrictedError):
                ticket = err.log()
            # or maybe not
            else:
                print traceback.format_exc()
                #request.logger.error(traceback.format_exc())
                ticket = 'unknown'
            # return HTTP 500
            return  HTTP(500, ticket).to(start_response, env=environ)
    # there was an error in handling the above error (like IOError)
    except:
        print traceback.format_exc()
        #request.logger.error(traceback.format_exc())
        # return HTTP 500
        return HTTP(500, 'unknown').to(start_response, env=environ)
    # but no matter what happens if the database was not committed, rollback
    # and close any file that may be open
    finally:
        failsafe(lambda: session and session._unlock())
        failsafe(lambda: BaseAdapter.close_all_instances('rollback'))

def main():
    print 'starting...'
    HttpServer(main_wsgi_app, port=8888).start()
