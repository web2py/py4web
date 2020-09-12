class Param:

    def __init__(self, **attr):
        self.__dict__.update(attr)

    def __setattr__(self, key, value):
        getattr(self, key)
        self.__dict__[key] = value

    __getitem__ = getattr
    __setitem__ = setattr
