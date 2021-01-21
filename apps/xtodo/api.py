
# example of GET/POST/PUT/DELETE RESTful APIs
from py4web import action, HTTP, request
from py4web.utils.xapi import API, DefaultAPIContext
import datetime

api = API.factory(mounter=action)
api.set_context(DefaultAPIContext(request))

P = api.make_filter('path', allow_extra = False)
# Q = api.make_filter('query', allow_extra = False)
J = api.make_filter('json', allow_extra = False)
F = api.make_filter('fixtures')

@api()
class todo_api:
    @api.thread_safe(safeguard = True)
    def __init__(self):
        self.now = None
        self.method = None
        self.user = None

    def on_request(self, route_ctx):
        self.method = route_ctx['route']['method']
        self.now = datetime.datetime.now()
        '''
        # instaed of `user = F.session['user']` in each api-method we can:
        if self.method != 'GET':
            ctx = route_ctx['api_context']
            user = ctx.get('fixtures')['session'].get('user')
            if not user:
                raise api.ValueError('user not in session', code = '401')
            self.user = user
        '''

    @api.get('/')
    @api.get('<id>')
    def todos_list(self,
        id = P.id.int|None,
        db = F.db
    ):
        if id:
            return db(db.todo.id == id).select().first().as_dict()
        else:
            return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())

    @api.post('/')
    def create(self,
        info = J.info,
        user = F.session['user'],
        db = F.db
    ):
        return dict(id=db.todo.insert(info=info))

    @api.put('<id>')
    def update(self,
        id = P.id.int,
        info = J.info,
        user = F.session['user'],
        db = F.db
    ):
        return dict(updated = db(db.todo.id == id).update(info=info))

    @api.delete('<id>')
    def delete(self,
        id = P.id.int,
        user = F.session['user'],
        db = F.db
    ):
        return dict(deleted = db(db.todo.id == id).delete())

    @api.shaper()
    def shaper(self, ret):
        ret['timestamp'] = self.now
        return ret

    @api.on_success()
    @api.on_error(api.ValueError)  # @api.on_error()  - catch all errors
    def on(self, status = None, error = None):
        if error:
            raise HTTP(f"{getattr(error, 'code', 400)} something went wrong: {str(error)}")

