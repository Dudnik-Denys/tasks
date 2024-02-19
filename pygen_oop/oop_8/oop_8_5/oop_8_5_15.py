def auto_repr(args: list, kwargs: list):
    def decorator(cls):
        def wrapper(self):
            result = f'{type(self).__name__}('
            result += ', '.join(repr(self.__dict__[arg]) for arg in args)
            result += ', ' if args and kwargs else ''
            result += ', '.join(kwarg + '=' + repr(self.__dict__[kwarg]) for kwarg in kwargs)
            result += ')'
            return result
        cls.__repr__ = wrapper
        return cls
    return decorator
