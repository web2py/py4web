import os
from py4web import action, request, DAL, Field, Session, Cache, user_in, HTTP, response
from py4web.core import bottle
import functools


# define session and cache objects
session = Session(secret="some secret")
cache = Cache(size=1000)

# define database and tables
db = DAL(
    "sqlite://storage.db", folder=os.path.join(os.path.dirname(__file__), "databases")
)
db.define_table("todo", Field("info"))
db.commit()

# example index page using session, template and vue.js
@action("index")  # the function below is exposed as a GET action
@action.uses("index.html")  # we use the template index.html to render it
@action.uses(session)  # action needs a session object (read/write cookies)
def index():
    session["counter"] = session.get("counter", 0) + 1
    session["user"] = {"id": 1}  # store a user in session
    return dict(session=session)


# example of GET/POST/DELETE RESTful APIs


@action("api")  # a GET API function
@action.uses(session)  # we load the session
@action.requires(user_in(session))  # then check we have a valid user in session
@action.uses(db)  # all before starting a db connection
def todo():
    return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())


@action("api", method="POST")
@action.uses(session)
@action.requires(user_in(session))
@action.uses(db)
def todo():
    return dict(id=db.todo.insert(info=request.json.get("info")))


@action("api/<id:int>", method="DELETE")
@action.uses(session)
@action.requires(user_in(session))
@action.uses(db)
def todo(id):
    db(db.todo.id == id).delete()
    return dict()


# example of caching
@action("uuid")
@cache.memoize(expiration=5)  # here we cache the result for 5 seconds
def uuid():
    import uuid

    return str(uuid.uuid4())


from py4web.utils.xapi import API, Param, make_decorator
from py4web import action
import datetime

class API_CTX(dict):

    class Props:
        query = 'whatever'

    def __init__(self):
        self[self.Props.query] = lambda: request.query

    def __call__(self, **args):
        pass

api= make_decorator(API_CTX())

Q = Param(API_CTX.Props.query)

# without this we will get 500 error
def catch_param_error(f):
    @functools.wraps(f)
    def catcher(*args, **kw):
        try:
            ret = f(*args, **kw)
        except Param.ValueError as err:
            raise bottle.HTTPError(400, body = f'{str(err)}')
        return ret
    return catcher

@action('echo_query')
@catch_param_error
@api()
def echo_query(offset = Q.skip.int|0, limit = Q.limit.int):
    return dict(offset = offset,limit = limit)



api  = API.factory()
api.add_proxy('uses')

P = api.make_filter('path')
Q = api.make_filter('query')
B = api.make_filter('body')
F = api.make_filter('fixtures')





@api()
class MyAPI:
    @api.thread_safe(safeguard = True)
    def __init__(self, foo):
        self.now = None
        self.foo = foo
        self.method = None

    #@api.uses(db)
    def on_request(self, route_ctx):
        self.method = route_ctx['route']['method']
        self.now = datetime.datetime.now()

    @api.get('/')
    @api.get('<id>')
    def todos_list(self, id = P.id.int|None, db = F.db):
        if id:
            return db(db.todo.id == id).select().first().as_dict()
        else:
            return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())

    @api.post('/')
    @api.uses(db)
    def create(self, info = B.info):
        return dict(id=db.todo.insert(info=info))

    @api.put('<id>')
    #@api.uses(db)
    def update(self, id = P.id.int, info = B.info, db = F.db):
        return dict(id = db(db.todo.id == id).update(info=info))

    @api.shaper()
    def shaper(self, ret):
        ret['timestamp'] = self.now
        return ret

    @api.on_success()
    @api.on_error(P.ValueError)  # @api.on_error()  - catch all errors
    def on(self, err = None):
        if err:
            raise HTTP(f'400 something wrong, reason: {str(err)}')

class FixturesSupplier:
    @api.thread_safe('issued')
    def __init__(self, **fixtures):
        self.fixtures = fixtures
        self.issued = []

    def on_request(self):
        self.issued.clear()

    def get(self, k, default = None):
        if k in self.fixtures:
            return self[k]
        return default

    def __getitem__(self, k):
        f = self.fixtures[k]
        if k not in self.issued:
            self.issued.append(k)
            f.on_request()
        return f

    def on(self, on_type, *args, **kw):
        [getattr(self.fixtures[k], on_type)(*args, **kw) for k in self.issued]

    def keys(self):
        return self.fixtures.keys()

class API_CTX:
    def __init__(self):
        self.FixS = FixturesSupplier(db = db)
        self.ctx = dict(
            path = lambda: None,
            query = lambda: request.query,
            body = lambda: request.json,
            fixtures = lambda: self.FixS
        )
    def __call__(self, **args):
        self.FixS.on_request()
        self.ctx['path'] = lambda: args

    def get(self, k):
        return self.ctx.get(k)()

    def __contains__(self, p):
        return p in self.ctx

    def on(self, on_type, *args, **kw):
        self.FixS.on(on_type, *args, **kw)


api.proxy(mounter = action, uses = action.uses)
api.set_ctx(API_CTX())

MyAPI.premount('xtodo')
MyAPI.run(foo = 'foo')

