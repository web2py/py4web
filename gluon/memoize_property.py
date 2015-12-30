import functools

def memoize_property(func):
    @functools.wraps(func)
    def tmp(self):
        aname = '_'+func.__name__
        try:
            value = getattr(self, aname)
        except AttributeError:
            value = func(self)
            setattr(self, aname, value)
        return value
    return property(tmp)
