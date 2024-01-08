class AttrDict:
    def __init__(self, data={}):
        self.__dict__.update(data)

    def __repr__(self):
        return f'AttrDict({self.__dict__})'

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        raise KeyError

    def __iter__(self):
        yield from self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __setattr__(self, key, value):
        pass
