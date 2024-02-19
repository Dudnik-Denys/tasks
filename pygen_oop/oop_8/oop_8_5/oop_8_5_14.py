from typing import Callable
from re import compile, findall


def snake_case(attrs=False):
    pattern = compile(r'_{,2}([a-z]+)*([A-Z][a-z]*)')

    def decorator(cls):
        methods = [method for method, value in cls.__dict__.items() if isinstance(value, Callable)]
        attributes = [attr for attr, value in cls.__dict__.items() if attr[-2:] != '__' and not isinstance(value, Callable)]

        for method in methods:
            prefix = '__' if method.startswith('__') else '_' if method.startswith('_') else ''
            regexp = findall(pattern, method)
            if regexp:
                temp = prefix + regexp[0][0] + '_' if regexp[0][0] else prefix + regexp[0][0]
                value = cls.__dict__[method]
                for group in regexp:
                    temp = temp + group[1].lower() + '_'
                temp = temp.rstrip('_')
                delattr(cls, method)
                setattr(cls, temp, value)
        if attrs:
            for attr in attributes:
                prefix = '__' if attr.startswith('__') else '_' if attr.startswith('_') else ''
                regexp = findall(pattern, attr)
                if regexp:
                    temp = prefix + regexp[0][0] + '_' if regexp[0][0] else prefix + regexp[0][0]
                    value = getattr(cls, attr)
                    for group in regexp:
                        temp = temp + group[1].lower() + '_'
                    temp = temp.rstrip('_')
                    delattr(cls, attr)
                    setattr(cls, temp, value)
        return cls
    return decorator
