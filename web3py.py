import os
import sys
import json
import argparse
import inspect
import functools
import traceback
from yatl import render
from pydal import DAL, Field
from bottle import route, request, run, static_file

__all__ = ['render', 'DAL', 'Field', 'action']

class action(object):
    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.args = args
        self.kwargs = kwargs
        self.view = kwargs.pop('view', None)        
    def __call__(self, function):
        functools.wraps(function)
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        ### TODO: fix this
        folder = os.path.dirname(module.__file__)
        app = os.path.split(folder)[-1]
        ###
        path = self.path.replace('$APP', app)
        @route(path, *self.args, **self.kwargs)
        def wrapper(*func_args, **func_kwargs):
            try:
                output = function(*func_args, **func_kwargs)
                if isinstance(output, dict):
                    if self.view:
                        path = os.path.join(folder, 'templates')
                        with open(os.path.join(path, self.view)) as stream:
                            context = dict(APP=app)
                            context.update(output)
                            output = render(stream.read(), path=path, context=context, delimiters='[[ ]]')
                    else:
                        output = json.dumps(output)
            except:
                output = traceback.format_exc()
                output = '<html><body><pre>%s</pre></body></html>' % output
            return output
        return wrapper    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='path to the applications folder')
    action.args = args = parser.parse_args()
    sys.path.append(args.folder)
    for app in os.listdir(args.folder):
        path = os.path.join(args.folder, app)
        if os.path.isdir(path):
            __import__(path.replace(os.sep, '.'))
            @route('/%s/static/<filename:path>' % app)
            def server_static(filename, path=path):
                print(filename, path)
                return static_file(filename, root=os.path.join(path, 'static'))
    run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    main()
