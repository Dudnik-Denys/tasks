from functools import wraps


def singleton(cls):
    old_new = cls.__new__
    cls.instance = None

    @wraps(old_new)
    def new_new(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    cls.__new__ = new_new
    return cls
