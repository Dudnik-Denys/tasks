from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=lambda x: x, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        temp = list(self.data)
        temp[key] = value
        self.data = ''.join(temp)

    def __delitem__(self, key):
        temp = list(self.data)
        del temp[key]
        self.data = ''.join(temp)
