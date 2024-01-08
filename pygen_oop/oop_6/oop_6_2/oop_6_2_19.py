from typing import Callable, Iterable


class Grouper:
    def __init__(self, iterable: Iterable, key: Callable):
        self.__iterable = iterable
        self.__key = key
        self.__groups = {}
        self.__create_groups(iterable)

    def __create_groups(self, iterable):
        for elem in iterable:
            self.add(elem)

    def group_for(self, obj):
        return self.__key(obj)

    def add(self, item):
        self.__groups.setdefault(self.__key(item), []).append(item)

    def __len__(self):
        return len(self.__groups)

    def __iter__(self):
        return iter(self.__groups.items())

    def __contains__(self, item):
        return item in self.__groups

    def __getitem__(self, item):
        return self.__groups[item]
