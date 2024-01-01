class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        if name == 'attrs_num':
            return len(self.__dict__) + 1
