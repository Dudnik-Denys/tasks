def get_method_owner(cls, method):
    result = None
    for c in cls.mro():
        if method in c.__dict__:
            result = c
            break

    return result
