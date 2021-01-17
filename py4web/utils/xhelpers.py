
import functools
import types
import itertools
import threading


def thread_safe(*ts_names, safeguard = False):
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
            self.__init__ is undecorated:
                self.__class__.__init__   = pure__init__

    '''

    def inner(init):
        def patch(self, ts_attrs):
            if not ts_attrs:
                return
            cls = self.__class__
            store = threading.local()
            fget = lambda nm: lambda s: getattr(store, nm)
            fset = lambda nm: lambda s, v: setattr(store, nm, v)
            fdel = lambda nm: lambda s: delattr(store, nm)
            for a in ts_attrs:
                setattr(store, a, self.__dict__.get(a))
                ts_prop = property(
                    fget(a), fset(a), fdel(a)
                )
                setattr(cls, a, ts_prop)
                try:
                    del self.__dict__[a]
                except KeyError:
                    pass

        @functools.wraps(init)
        def patcher(self, *args, **kw):
            #print(f'patch : {str(self)}')
            attr_keys = list(self.__dict__.keys())
            ret = init(self, *args, **kw)
            if not ts_names:
                new_attr_keys = self.__dict__.keys()
                _ts_names = set(new_attr_keys) - set(attr_keys)
            else:  _ts_names = ts_names
            patch(self, _ts_names)
            setattr(self.__class__, '__init__', init)
            __setattr__ = self.__class__.__setattr__
            __getattrubute__ = getattr(self.__class__,'__getattribute__', object.__getattribute__)
            __setattr__ = getattr(self.__class__,'__setattr__', object.__setattr__)

            if safeguard:
                is_safe = set()
                def __safe_getattribue__(s, k):
                    ret = __getattrubute__(s, k)
                    is_safe.add(k)
                    return ret
                def __safe_setattr__(s, k, v):
                    if k in is_safe:
                        return __setattr__(s, k, v)
                    else:
                        s.__getattribute__(k)
                        return __setattr__(s, k, v)
                self.__class__.__getattribute__ = __safe_getattribue__
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
