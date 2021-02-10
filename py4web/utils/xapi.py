import json
import re
import functools
from types import SimpleNamespace

from .xhelpers import parse_defs, DictList, thread_safe

# ---------------- [ Experimental API for general purposes ] ----------------------
"""
## Usage example

from py4web.utils.xapi import API
from py4web import action
import datetime

api  = API.factory()  # create api wrapper
api.add_proxy('uses') # declare decorator with deferred resolution

# create filters/validators
P = api.make_filter('path')
Q = api.make_filter('query')
B = api.make_filter('body')

@api()
class MyAPI:
    # declare/init all thread safe attrs in __init__
    @api.thread_safe(safeguard = True)
    def __init__(self, foo):
        self.now = None
        self.foo = foo
        self.method = None

    # @api.uses(T)  # `global` fixtures
    def on_request(self, route_ctx):
        self.method = route_ctx['route']['method']
        self.now = datetime.datetime.now()

    @api.get('/')
    @api.get('<id>')
    @api.uses(db)
    def todos_list(self, id = P.id.int|None):
        if id:
            return db(db.todo.id == id).select().first().as_dict()
        else:
            return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())

    @api.post('/')
    @api.uses(db)
    def create(self, info = B.info):
        return dict(id=db.todo.insert(info=info))

    @api.put('<id>')
    @api.uses(db)
    def update(self, id = P.id.int, info = B.info):
        return dict(id = db(db.todo.id == id).update(info=info))

    @api.shaper()  # like `Fixture.transform`
    def shaper(self, ret):
        ret['timestamp'] = self.now
        return ret

    @api.on_success()
    @api.on_error(P.ValueError)  # @api.on_error()  - catch all errors
    def on(self, err = None):
        if err:
            raise HTTP(f'400 something went wrong: {str(err)}')


# api context - adapter between framework and api:
# context-object must have:
#   .get(ctx_property:str) ->  ctx_property:dict
#   .__call__(**path_params)
#   .__contains__(ctx_property:str)
# ctx_properties should match filters/validators, i.e.:
#   if we have `P = api.make_filter('path')`
#   then `ctx.get('path')` must return ctx_property

class API_CTX:
    def __init__(self):
        self.ctx = dict(
            path = lambda: None,
            query = lambda: request.query,
            body = lambda: request.json,
        )
    def __call__(self, **args):
        self.ctx['path'] = lambda: args

    def get(self, k):
        return self.ctx.get(k)()

    def __contains__(self, p):
        return p in self.ctx

# set mounter and resolve deferred decorators
api.proxy(mounter = action, uses = action.uses)

# set api context
api.set_context(API_CTX())

# will be mounted at `app/xtodo`
MyAPI.premount('xtodo')

# run api
MyAPI.run(foo = 'foo')

# instead of last 2 above we can
# MyAPI.mount('xtodo', args = ['foo'])
# or MyAPI.mount('xtodo', kwargs = dict(foo = 'foo'))
"""


def _re(p):
    rex = re.compile(p)

    def inner(v):
        ret = (v := rex.match(v)) and v.group()
        if ret is None:
            raise Param.ValueError('doesn`t match')
        return ret
    return inner


class Map:
    def __init__(self):
        self.cbs = []

    def __call__(self, v):
        cbs = self.cbs
        apply = lambda it, cbs: [(it:=cb(it)) for cb in cbs][-1]
        it = None
        idx = None
        try:
            ret = [apply(it, cbs) for idx, it in enumerate(v)]
        except Exception as err:
            if idx is None:
                err = Param.ValueError(
                    f'`{str(v)}` is invalid, reason: {str(err)}',
                    type = 'invalid',
                    invalid = v,
                    reason = err
                )
            else:
                err = Param.ValueError(
                    f'`{str(it)}` at [{idx}] is invalid, reason: {str(err)}',
                    type = 'invalid',
                    invalid = it,
                )
            err.extra.update(
                name = None, filter = self, value = v,
                reason = err
            )
            raise err
        return ret

def is_bool(v):
    v = v.lower()
    if v not in ('true', 'false'):
        raise Param.ValueError(
                f'`{v}` must be true/false',
        )
    return v == 'true'

class Param:
    class ValueError(Exception):
        def __init__(self, msg, **extra):
            super().__init__(msg)
            self.msg = msg
            self.extra = extra

        def __getattr__(self, k):
            if k not in self.extra:
                raise AttributeError(f"there is no {k}-attribute")
            return self.extra[k]

        def __contains__(self, k):
            return k in self.extra

    _filters = dict(
        str = str,
        int = int,
        re = _re,
        json = json.loads,
        bool = is_bool,
        # if filter-fun is wrapped in set it should be evaluated
        # see  _init_filters
        map = {Map},
        to = lambda f: f,
        item = lambda k: (lambda obj: obj[k]),
        get = lambda k, default = None:  (lambda obj: obj.get(k, default)),
        attr = lambda k, default = None: (lambda obj: getattr(obj, k, default))
    )

    def _init_filters(self):
        for k, f in self._filters.items():
            if isinstance(f, set):
                self._filters[k] = list(f)[0]()

    def __init__(self, ctx_prop:str, allow_extra = True, **filters):
        self._ctx_prop = ctx_prop
        self._allow_extra = allow_extra
        self._filters = dict(**self._filters)

        self._filters.update(filters)
        self._init_filters()
        self._filter_chain = []  # [[name, filter:callable], ...]
        self._required = True
        self._name = None
        self._factory = None
        # optional:
        # self._default

    def _blank_copy(self):
        return self.__class__(self._ctx_prop, self._allow_extra, **self._filters)

    def __getitem__(self, k):
        if k is ...:
            if not self._name:
                ret = self._blank_copy()
                ret._name = k
            else:
                raise RuntimeError('`[...]` is no allowed here')
            return ret
        else:
            if not self._name:
                raise RuntimeError('use dot-access notation')
            self._filter_chain.append(['item', self._filters['item'](k)])
            return self
            #return super().__getitem__(k)

    def __getattr__(self, k):
        if k[0] == '_':
            raise AttributeError(f'attr `{k}` is not set')
        if not self._name:
            ret = self._blank_copy()
            ret._name = k
            return ret

        last_flt = self._filter_chain and self._filter_chain[-1][1] or None
        if last_flt and isinstance(last_flt, Map):
            last_flt.cbs.append(self._filters[k])
        else:
            self._filter_chain.append([k, self._filters[k]])
        return self

    def __call__(self, *args, **kw):
        # maybe factory call
        if not self._name:
            ret = self._blank_copy()
            ret._name, ret._factory = (args[0], args[1]) if isinstance(args[0], str) else (args[0].__name__, args[0])
            return ret

        last_flt = self._filter_chain[-1][1]
        if isinstance(last_flt, Map):
            if not last_flt.cbs:
                last_flt.cbs.extend(args)
            else:
                last_flt.cbs[-1] = (last_flt.cbs[-1](*args, **kw))
        else:
            self._filter_chain[-1][1] = last_flt(*args, **kw)
        return self

    def __or__(self, other):
        self.__dict__['_default'] = other
        self._required = False
        return self

    def apply(self, obj):
        name = self._name
        if name is ...:
            name = f'ctx.{self._ctx_prop}'
            ret = obj
        else:
            ret = obj.get(self._name)
        value = ret
        if ret is None:
            if not self._required:
                ret = self._default
            else:
                raise self.ValueError(f'missing `{name}`', type = 'missing')
        if ret is None:
            return ret
        for k, f in self._filter_chain:
            try:
                ret = f(ret)
            except Exception as err:
                if isinstance(err, Param.ValueError):
                    if (extra := getattr(err, 'extra', None)):
                        if not extra['name']:
                            extra['name'] = name
                        raise err

                raise self.ValueError(
                    f'`{name}` is invalid, reason: {str(err)}',
                    type = 'invalid',
                    name = name, filter = f, value = value, invalid = ret,
                    reason = err
                )
        return ret


class Validator:
    def __init__(self, f):
        self.with_factories = []
        self.defs = defs = parse_defs(f)
        filters = self.filters = dict()
        self.raw_args = []
        defs = dict(**defs['regular'], **defs['kwonly'])
        for a, v in defs.items():
            if not isinstance(v, Param):
                self.raw_args.append(a)
                continue
            ctx_prop = v._ctx_prop
            if not ctx_prop in filters:
                filters[ctx_prop] = dict()
            filters[ctx_prop][a] = v
            if v._factory:
                self.with_factories.append(v)

    def apply(self, ftype, obj):
        ret = dict()
        extra = list(obj.keys())
        allow_extra = False
        for a, v in self.filters[ftype].items():
            ret[a] = v.apply(obj)
            if v._name in extra:
                extra.remove(v._name)
            if not allow_extra:
                allow_extra = v._allow_extra or v._name is ...


        if ret and not allow_extra and extra:
            raise Param.ValueError(f'unexpected: {extra}', type = 'unexpected')
        return ret

    def __call__(self, ctx):
        '''
        ctx = {path{}, query{}, body{}}
        '''
        ret = dict()
        for ftype, obj in self.filters.items():
            ret[ftype] = self.apply(ftype, ctx.get(ftype) or {})
        return ret

    def run_factories(self, ctx):
        [ctx.factory(flt._ctx_prop, flt._name, flt._factory) for flt in self.with_factories]


def post_proc(
    cb,
    shapers: list = None,
    on_success: list = None,
    on_error: dict = None,
    success_exceptions: list = None
):
    '''
    on_error: {cb1: (FooException, BarException), cb2: None/<Falseness means all errors> }
    '''

    @functools.wraps(cb)
    def inner(*args, **kw):
        ret = None
        shapers = inner.shapers
        on_success = inner.on_success
        on_error = inner.on_error
        success_exceptions = tuple(inner.success_exceptions or ())
        try:
            ret = cb(*args, **kw)
            [h() for h in on_success]
            for shaper in shapers:
                ret = shaper(ret)
        except Exception as exon:
            if success_exceptions and isinstance(exon, success_exceptions):
                [h(exon) for h in on_success]
            else:
                for h, errors in on_error.items():
                    #  `not errors` means on any error
                    if not errors or isinstance(exon, errors):
                        h(exon)
            raise
        return ret

    inner.on_success = on_success or []
    inner.on_error = on_error or {}
    inner.shapers = shapers or []
    inner.success_exceptions = success_exceptions or []
    return inner


def make_decorator(ctx, *, with_context_init = True):
    def decor(src = None, fun = None, fixtures = None):
        @functools.wraps(fun)
        def inner(**oargs):
            args = dict()
            raw_args = dict()
            for k, v in oargs.items():
                if k in validator.raw_args:
                    raw_args[k] = v
                else:
                    args[k] = v
            if with_context_init:
                ctx(**args)
            if fixtures:
                ctx_fixtures = ctx.get('fixtures')
                [ctx_fixtures.get(_) for _ in fixtures]
            ctx_values = validator(ctx)
            [raw_args.update(_) for _ in ctx_values.values()]
            return fun(**raw_args)

        if fun:
            validator = Validator(src or fun)
            validator.run_factories(ctx)
            return post_proc(
                inner,
                shapers= [lambda r: ctx.emit('transform', r)],
                on_success= [lambda *a, **kw : ctx.emit('on_success', *a, **kw)],
                on_error= {(lambda *a, **kw: ctx.emit('on_error', *a, **kw)): None},
            )
        else:
            return lambda f: decor(src = src, fun = f)
    return decor


def with_method_shortcuts(methods):
    def injector(cls):
        for m in methods:
            setattr(cls, m.lower(), classmethod(functools.partial(cls.route.__func__, method = m)))
        return cls
    return injector

@with_method_shortcuts('DELETE GET HEAD OPTIONS PATCH POST PUT'.split())
class API:
    class Use:
        def __init__(self, current):
            self.current:'API' = current

        def __getattr__(self, k):
            return self.current._use(k)


    __mounted__ = {}
    #__deps__ = None  # extarnal dependencies
    #__current__ = None,
    #__ctx__ = None
    thread_safe = staticmethod(thread_safe)
    ValueError = Param.ValueError

    @classmethod
    def factory(cls, *, mounter = None) -> 'API':
        deps = dict(
            mounter = mounter,
        )
        api = type('api',
            (cls,),
            dict(
                __deps__ = deps,
                __current__ = None,
                __ctx__ = None
            )
        )
        return api

    @classmethod
    def set_context(cls, ctx):
        cls.__ctx__ = ctx

    @property
    def context(self):
        return self.local_ctx or self.__ctx__


    @classmethod
    def proxy(cls, **name_cbs):
        for name, cb in name_cbs.items():
            cls.__deps__[name] = cb

    @classmethod
    def add_proxy(cls, *names, **names_cbs):
        proxies = dict.fromkeys(names)
        proxies.update(names_cbs)
        for name, proxy_to in proxies.items():
            cls._add_proxy(name, proxy_to)

    @classmethod
    def _add_proxy(cls, name, proxy_to = None):
        if proxy_to:
            cls.__deps__[name] = proxy_to
        @classmethod
        def proxy_meth(cls, *uargs, **ukw):
            self = cls.__current__
            def wrapper(fun):
                proxy = cls._meta(fun)['proxy']
                wrapped = fun
                @functools.wraps(fun)
                def inner(*a, **kw):
                    return wrapped(*a, **kw)

                def patcher(patched):
                    nonlocal wrapped
                    wrapped = patched
                proxy[name] = dict(
                    fun = fun,
                    args = [uargs, ukw],
                    patcher = patcher
                )
                return inner
            return wrapper
        return setattr(cls, name, proxy_meth)


    def __new__(cls):
        self = super().__new__(cls)
        cls.__current__ = self
        cls.use = cls.Use(self)
        return self

    def __init__(self):
        self.routes = {}
        self.meta_data = {}
        self.handlers = {}  # on_success, on_error ...
        self.on_mounted = {}  # perform local context extend
        self.api = None
        self.local_ctx = None

    def __call__(self, cls) -> 'API':
        self.cls = cls
        self.__class__.__current__ = None
        self.__class__.use = None
        return self

    def _use(self, name):
        def wrapper():
            def inner(f):
                self._meta(f)['fixtures'][name] = True
                return f
            return inner
        return wrapper

    @staticmethod
    def make_filter(ctx_prop, **kw):
        return Param(ctx_prop, **kw)

    def run(self, *args, **kw):
        raise RuntimeError('api is not premounted')

    def premount(self, *args, **kw):
        run = functools.partial(self.mount, *args, **kw)
        args = kw.get('args', [])
        kwargs = kw.get('kwargs', {})
        self.run = lambda *a, **kw: run(args= [*args, *a], kwargs= dict(kwargs, **kw))

    def mount(self, path, *, ctx = None, mounter = None, args = None, kwargs = None):
        if not mounter:
            mounter = self.__deps__['mounter']
        cls = self.cls
        self._patch_proxy()
        self._mount(path, cls, mounter, ctx = ctx, args = args, kwargs = kwargs)
        self.__mounted__[self.api] = self.routes

        # extend context
        for name, cb in self.on_mounted.items():
            self.context.factory('fixtures', name, getattr(self.api, cb.__name__))
        on_mounted = getattr(self.api, 'on_mounted', None)
        if on_mounted:
            on_mounted(self.context)


    def _patch_proxy(self):
        for meta_data in self.meta_data.values():
            for proxy_name, proxy_data in meta_data['proxy'].items():
                uargs, ukw = proxy_data['args']
                patched = self.__deps__[proxy_name](
                    *uargs, **ukw
                )(proxy_data['fun'])
                proxy_data['patcher'](patched)

    def _mount(self, base_path, cls, mounter, ctx, args = None, kwargs = None):
        if not ctx:
            ctx = self.__ctx__
        ctx = ctx.copy()
        self.local_ctx = ctx
        # now `self.context` is self.local_ctx
        api = self.api = cls(*(args or []), **(kwargs or {}))
        api_init = getattr(api, 'on_request', None)
        decorator = make_decorator(ctx, with_context_init = not api_init)
        def make_with_init(cb, route):
            @functools.wraps(cb)
            def with_init(*args, **kw):
                route_ctx = dict(
                    api_context = ctx,
                    api_method = cb.__name__,
                    route = route,
                    payload = dict(args = args[:], vars = dict(**kw)),
                )
                ctx(**kw)
                api_init(route_ctx)
                return cb(*args, **kw)
            return with_init

        # decorated callbacks for reuse in case of multiroutes
        decorated = {}
        for r in self.routes.values():
            raw_cb = r['cb'] = getattr(api, r['cb'].__name__)
            if raw_cb not in decorated:
                meta_data = self.meta_data[raw_cb.__name__]
                decorated[raw_cb] = decorator(meta_data['cb'], raw_cb, meta_data['fixtures'])
            cb = decorated[raw_cb]
            path = f"{base_path}/{r.get('path')}".rstrip('/')
            if api_init:
                cb = make_with_init(cb, r)
            cb = self.with_postproc(cb)
            mounter(path, method = r.get('method'))(cb)
        return cls

    def with_postproc(self, cb):
        if not self.handlers:
            return cb

        bound = lambda f: getattr(self.api, f.__name__)

        errors = errcb = None
        if (error := self.handlers.get('error')):
            errcb = bound(error['cb'])
            errors = tuple(error['args']) or Exception
            cb.on_error[errcb] = errors

        if (success := self.handlers.get('success')):
            success = bound(success['cb'])
            cb.on_success.append(success)

        if (shaper := self.handlers.get('shaper')):
            shaper = bound(shaper['cb'])
            cb.shapers.append(shaper)

        return cb

    @classmethod
    def route(cls, path = None, method = 'GET'):
        self = cls.__current__

        def inner(fun):
            f = cls._meta(fun)['cb']  # returns undecorated fun
            _path = f.__name__ if path is None else path
            _method = method
            if isinstance(_method, str):
                _method = [_method]
            for m in _method:
                if [
                    k for k, v in self.routes.items()
                    if (v['cb'] is not f) and (v['cb'].__name__ == f.__name__)
                ]:
                    raise KeyError('callbacks with matching names are not supported')
                self.routes[f"{_path}.{m}"] = dict(
                    cb = f,
                    path = _path,
                    method = m,
                )
            return fun
        return inner

    @classmethod
    def meta(cls, f = None):
        if not f:
            return cls.meta
        cls._meta(f)
        return f

    @classmethod
    def _meta(cls, f):
        self:API = cls.__current__
        return self.meta_data.setdefault(
            f.__name__,
            dict(
                cb = f,
                proxy = dict(),
                fixtures = dict()
            )
        )

    @classmethod
    def on_error(cls, *args):
        return cls._set_handler('error', args)

    @classmethod
    def on_success(cls):
        return cls._set_handler('success')

    @classmethod
    def shaper(cls):
        return cls._set_handler('shaper')

    @classmethod
    def _set_handler(cls, on, args = None):
        self:API = cls.__current__
        if on in self.handlers:
            raise KeyError(f'there should only be one `{on}` handler')
        hon = self.handlers[on] = dict(args = args)

        def inner(f):
            hon['cb'] = f
            return f
        return inner

    @classmethod
    def fixture(cls, name = None):
        self:API = cls.__current__
        def inner(f):
            self.on_mounted[name or f.__name__] = f
            return f
        return inner



class APIContext:

    def __call__(self, **args):
        raise NotImplementedError

    def get(self, k):
        raise NotImplementedError

    def __contains__(self, p):
        pass

    def emit(self, on_type, *args, **kw):
        raise NotImplementedError

    def provide(self, **fixtures):
        raise NotImplementedError

    def factory(self, ctx_prop, name, factory_cb):
        '''
        self.ctx[ctx_prop][name] = factory_cb(self.ctx[ctx_prop])
        '''
        raise NotImplementedError

    def copy(self):
        '''
        api can extend context, so we need a copy
        (of course we can make a derived context but that will be slower)
        '''
        raise NotImplementedError


#########################################################################################
# py4web adaptation
#########################################################################################


class FixturesSupplier:

    @thread_safe('issued', safeguard = True)
    def __init__(self, *, HTTPException, **fixtures):
        self.HTTPException = HTTPException
        self.fixtures = fixtures
        self.issued = None
        self.fixture_deps = dict()  # may be shared at class level
        [self._make_deps(f) for f in fixtures.values()]

    def add_fixture(self, **fixtures):
        self.fixtures.update(fixtures)
        [self._make_deps(f) for f in fixtures.values()]

    def _make_deps(self, fix):
        if fix in self.fixture_deps:
            return
        deps = getattr(fix, "__prerequisites__", ())
        if not deps:
            self.fixture_deps[fix] = []
            return
        out = []
        for dep in deps:
            self._make_deps(dep)
            out.extend(self.fixture_deps[dep])
            out.append(dep)
        out_uniq = []
        [out_uniq.append(f) for f in out if f not in out_uniq]
        self.fixture_deps[fix] = out_uniq

    def on_request(self):
        self.issued = []

    def get(self, k, default = None):
        if k in self.fixtures:
            return self[k]
        return default

    def __getitem__(self, k):
        f = self.fixtures[k]
        if f in self.issued:
            return f
        for req_f in self.fixture_deps[f]:
            if req_f in self.issued:
                continue
            req_f.on_request()
            self.issued.append(req_f)
        f.on_request()
        self.issued.append(f)
        return f

    def emit(self, on_type, *args, **kw):
        if on_type == 'transform':
            ret = args[0]
            shared_data = {}
            for f in self.issued:
                ret = getattr(f, on_type)(ret, shared_data)
            return ret
        elif on_type == 'on_error':
            on_handler = on_type
            err = args[0]
            hargs = []
            if isinstance(err, self.HTTPException):
                on_handler = f"on_{getattr(err, 'type', 'error')}"  #  'success' | 'error'
                hargs = [getattr(err, 'status', 500)] if on_handler == 'on_success' else []
            [getattr(f, on_handler)(*hargs) for f in self.issued]
        elif on_type == 'on_success':
            status = 200 if not args else getattr(args[0], 'status', 200)
            [getattr(f, on_type)(status) for f in self.issued]

    def keys(self):
        return self.fixtures.keys()


class DefaultAPIContext(APIContext):
    def __init__(self, request, HTTP):
        self.fsupplier = FixturesSupplier(HTTPException = HTTP)
        self.request = request
        props = dict(
            path = lambda: None,
            query = lambda: request.query,
            json = lambda: request.json,
            form_data = lambda: request.POST,
            form = lambda: request.forms,
            files = lambda: request.files,
            requset = lambda: request,
            wsgi_env = lambda: request.environ,
            headers = lambda: request.headers,

            fixtures = lambda: self.fsupplier,
        )
        self.props = SimpleNamespace(**props)
        self.__props_dict__ = self.props.__dict__
        self._get = self.props.__dict__.get

    def __call__(self, **args):
        self.fsupplier.on_request()
        self.props.path = lambda: args

    def get(self, k):
        return self._get(k)()

    def __contains__(self, p):
        return p in self.__props_dict__

    def emit(self, on_type, *args, **kw):
        return self.fsupplier.emit(on_type, *args, **kw)

    def provide(self, **fixtures):
        self.fsupplier.add_fixture(**fixtures)

    def factory(self, ctx_prop, name, factory_cb):
        if ctx_prop != 'fixtures':
            raise NotImplementedError('`factory` is only supported for `fixtures`')
        self.provide(**{name: factory_cb(self.fsupplier.fixtures)})

    def copy(self):
        ret = self.__class__(self.request, self.fsupplier.HTTPException)
        ret.__props_dict__.update(self.__props_dict__)
        ret.props.fixtures = lambda: ret.fsupplier
        ret.fsupplier.add_fixture(**self.fsupplier.fixtures)
        return ret



