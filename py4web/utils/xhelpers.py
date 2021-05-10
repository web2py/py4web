
import functools
import types
import itertools
import threading


def thread_safe(*ts_names, safeguard = False, store_name = '__ts_store__'):
    '''
    if not ts_names:
        turns all `self.some = ...`  assignments in __init__
        into thread safe props
    else:
        turns only ts_names

    safeguard = True:
        mimic __slots__ behaviour i.e. after __init__ was invoked
        self.new_attr = ... causes an AttributeError

    Usage:
        @thread_safe()
        def __init__(self):
            self.a = 'a'

        when the first time self.__init__ is invoked:
            self.__class__ is patched:
                self.__class__.a = property(...)  # inject thread safe property
                del self.__dict__['a']   # remove instance attr
    '''
    ts_names = list(ts_names)

    def inner(init):
        class_patched = False

        def patch(self, ts_attrs):
            if not ts_attrs:
                return
            cls = self.__class__
            fget = lambda nm: lambda s: getattr(s.__dict__[store_name], nm)
            fset = lambda nm: lambda s, v: setattr(s.__dict__[store_name], nm, v)
            fdel = lambda nm: lambda s: delattr(s.__dict__[store_name], nm)
            store = self.__dict__[store_name]
            for a in ts_attrs:
                ts_prop = property(
                    fget(a), fset(a), fdel(a)
                )
                setattr(cls, a, ts_prop)
                setattr(store, a, self.__dict__.get(a))
                try:
                    del self.__dict__[a]
                except KeyError:
                    pass

        @functools.wraps(init)
        def patcher(self, *args, **kw):
            nonlocal class_patched
            # maybe patched
            if store_name in self.__dict__:
                return init(self, *args, **kw)
            else:
                store = self.__dict__[store_name] = threading.local()

            if class_patched:
                # init store
                [setattr(store, a, None) for a in ts_names]
                return init(self, *args, **kw)

            attr_keys = list(self.__dict__.keys())
            ret = init(self, *args, **kw)
            if not ts_names:
                new_attr_keys = self.__dict__.keys()
                ts_names[:] = list(set(new_attr_keys) - set(attr_keys))
            patch(self, ts_names)
            class_patched = True
            if safeguard:
                attr_keys = list(self.__dict__.keys())
                attr_len = len(attr_keys)
                __setattr__ = getattr(self.__class__,'__setattr__', object.__setattr__)
                def __safe_setattr__(s, k, v):
                    ret = __setattr__(s, k, v)
                    if len(s.__dict__) > attr_len:
                        unsafe_key = set(s.__dict__.keys()) - set(attr_keys)
                        raise RuntimeError(f'unsafe attribute assignment detected: `{unsafe_key}`')
                self.__class__.__setattr__ = __safe_setattr__
            return ret
        return patcher
    return inner


class DictList(dict):
    '''
        Provides access by index:
            d = DictList(akey = 'a', bkey = 'b')
            d[0] == 'a'
            d[-1] == 'b'
            d.keys()[-1] == 'bkey'
    '''

    def keys(self):
        keys = super().keys()
        return list(keys)

    def __getitem__(self, v):
        if isinstance(v, int):
            if v < 0:
                v = len(self) + v
            v = next(itertools.islice(super().keys(), v, v+1))
        return super().__getitem__(v)


def parse_defs(f:types.FunctionType, map_keys = None):
    ''' Parse function args
        returns dict {fun, posonly, regular, kwonly}
        Usage:
            def foo(a = 1, *, b = 2): pass
            defs = parse_defs(foo)
            defs['regular']['a'] == 1
            defs['kwonly']['b'] == 2
            defs['fun'] is foo == True
    '''
    path_q_cnt = f.__code__.co_argcount
    path_cnt = f.__code__.co_posonlyargcount
    q_cnt =  path_q_cnt - path_cnt
    body_cnt = f.__code__.co_kwonlyargcount
    args_cnt = path_cnt + q_cnt + body_cnt
    arg_names = f.__code__.co_varnames[:args_cnt]
    adefs = f.__defaults__ or []
    defs = f.__kwdefaults__.copy() if f.__kwdefaults__ else {}
    q_delim_idx = None
    defs_start_idx = path_q_cnt - len(adefs)
    for i, name in enumerate(arg_names[defs_start_idx : path_q_cnt]):
        defs[name] = adefs[i]
        if adefs[i] == '?':
            q_delim_idx = defs_start_idx + i

    dlt_fix = 0
    if not path_cnt and q_delim_idx is not None:
        path_cnt = q_delim_idx
        dlt_fix = 1

    keys = dict(
        fun = 'fun',
        posonly = 'posonly',
        regular = 'regular',
        kwonly  = 'kwonly'
    )
    if map_keys:
        keys.update(map_keys)
    fun, posonly, regular, kwonly = keys.values()

    defs = {
        fun: f,
        posonly: DictList([ (nm, defs.get(nm, NoDef)) for nm in arg_names[:path_cnt] ]),
        regular: {nm:  defs.get(nm) for nm in arg_names[path_cnt + dlt_fix:path_q_cnt] },
        kwonly: {nm:  defs.get(nm) for nm in arg_names[path_q_cnt:] },
    }

    return defs
