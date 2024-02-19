from functools import update_wrapper


class takes_numbers:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for elem in args + tuple(kwargs.values()):
            if type(elem) not in (int, float):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
