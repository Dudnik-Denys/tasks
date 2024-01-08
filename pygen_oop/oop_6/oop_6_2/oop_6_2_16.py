class PermaDict:
    def __init__(self, data=()):
        self.__data = dict(data)

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        yield from self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        if key in self.__data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

    def keys(self):
        return self.__data.keys()

    def values(self):
        return self.__data.values()

    def items(self):
        return self.__data.items()
