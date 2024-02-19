from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        return self.data.get(key) or self.data.get(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data or key not in self._aliases:
            self.data[key] = value
        else:
            self.data[self._aliases[key]] = value

    def __delitem__(self, del_key):
        for alias_key, key in self._aliases.items():
            if key == del_key:
                self.data[alias_key] = self.data[del_key]
        del self.data[del_key]
