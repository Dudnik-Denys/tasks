class Versioned:
    def __init__(self):
        self._history = {}

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if obj not in self._history:
            raise AttributeError('Атрибут не найден')
        version = self._history[obj][0]
        values = self._history[obj][1]
        return values[version]

    def __set__(self, obj, value):
        values = self._history.setdefault(obj, [-1, []])[1]
        values.append(value)

    def get_version(self, obj, n):
        values = self._history[obj][1]
        return values[n - 1]

    def set_version(self, obj, n):
        self._history[obj][0] = n - 1
