class Param:
    """
    An interface to expore predefined parameters
    which can be overwritten but not deleted or added
    Example:

    p = Param(a=1, b=2)
    p.a = 3
    p.b = 4
    print(p.a, p.b)
    p.c = 5 # Error
    """

    def __init__(self, **attr):
        self.__dict__.update(attr)

    def __setattr__(self, key, value):
        getattr(self, key)
        self.__dict__[key] = value

    def __getitem__(self, key):
        return getattr(self, key)

    __setitem__ = __setattr__
