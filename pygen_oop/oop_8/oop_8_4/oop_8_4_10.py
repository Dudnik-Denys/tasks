from functools import update_wrapper


class reverse_args:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)
