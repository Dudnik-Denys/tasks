class HistoryDict:
    def __init__(self, data=()):
        self.__data = dict(data)
        self.__history = {key: [value] for key, value in self.__data.items()}

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        yield from self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value
        if key in self.__history:
            self.__history[key].append(value)
        else:
            self.__history[key] = [value]

    def __delitem__(self, key):
        del self.__data[key]
        del self.__history[key]

    def keys(self):
        return self.__data.keys()

    def values(self):
        return self.__data.values()

    def items(self):
        return self.__data.items()

    def history(self, item):
        if item not in self.__history:
            return []
        return self.__history[item]

    def all_history(self):
        return self.__history


historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())

# {'name': ['Irenica'], 'country': ['Russia'], 'level': ['junior']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy'], 'level': ['junior', 'middle', 'senior']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy'], 'level': ['God']}
