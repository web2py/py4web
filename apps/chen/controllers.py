
import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader
import yatl


from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME
from py4web.core import bottle

## exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#
# AI-biorex, 15:10:58 16.12.2020 UTC+3
# src: https://github.com/PanJiaChen/vue-element-admin.git 
#



@action('index', method=["GET", "POST"] )
@action('static/tte', method=["GET", "POST"] )
@action('static/tte/index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T, )
def index(param=None):
    ctrl_info= "ctrl: index, view: index.html"
    if not param is None:
        print (param)
    return locals()



Glb= {'debug': True, 'my_app_name': APP_NAME, 'tte_path': '/static/tte'}

def before_request():
    bad_path= '/chen/static/tte/chen/static/tte/'
    bad_root='/chen/chen/'
    if bottle.request.environ["PATH_INFO"].startswith(bad_path):
        bottle.request.environ["PATH_INFO"]= bottle.request.environ["PATH_INFO"].replace( '/chen/static/tte', '', 1)
        print ( f'before_request:    /chen: goto {bottle.request.environ["PATH_INFO"]}' )
    elif bottle.request.environ["PATH_INFO"].startswith(bad_root):
        bottle.request.environ["PATH_INFO"]= bottle.request.environ["PATH_INFO"].replace( '/chen', '', 1)
        print ( f'before_request:    /chen: goto {bottle.request.environ["PATH_INFO"]}' )

#bottle.default_app().add_hook( "before_request", before_request )


@bottle.error(404)
def error404(error):

    func_mess = []

    def check_rule(maybe_app_root):
        for e in Reloader.ROUTES:
            if ('rule' in e ) and ( e["rule"] == maybe_app_root ):
                Glb["debug"] and func_mess.append( f"     found_rule: {e['rule']}")
                return True
        return False

    location = "/" + Glb["my_app_name"]
    lx = bottle.request.path.split("/", 2)

    if ( len(lx) >= 2 ) and check_rule("/" + lx[1]):

        location = "/" + lx[1]
        files_prefix = location + Glb["tte_path"]

        location_2x = location + location + "/"
        files_prefix_2x = files_prefix + files_prefix + "/"

        def rm_bad_prefix(bad_prefix):
            new_location = bottle.request.path.replace(bad_prefix, "", 1)
            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
            return new_location

        if bottle.request.path.startswith(files_prefix_2x):
            if len(bottle.request.path) > len(files_prefix_2x):
                location = rm_bad_prefix(files_prefix)

        elif bottle.request.path.startswith(location_2x):
            if len(bottle.request.path) > len(location_2x):
                location = rm_bad_prefix(location)

    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)



from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/', method=["GET", "POST", "PUT", "DELETE"])
@action('api/<tablename>/<rec_id>', method=["GET", "POST", "PUT", "DELETE"])
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.POST
                               )
#
# curl -X  GET   http://localhost:8000/chen/api/test_table/
# curl -X  GET   http://localhost:8000/chen/api/test_table/9
# curl -X DELETE  http://localhost:8000/chen/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/chen/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/chen/api/test_table/19
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/chen/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/chen/api/test_table/
#  http -f POST localhost:8000/chen/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/chen/api/test_table/2
#  http -f PUT localhost:8000/chen/api/test_table/2 f0=111111 f1=2222222 f2=333333

