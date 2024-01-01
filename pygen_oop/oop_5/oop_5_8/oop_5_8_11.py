class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default=default
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return self.default
