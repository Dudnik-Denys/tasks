from functools import wraps


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls
