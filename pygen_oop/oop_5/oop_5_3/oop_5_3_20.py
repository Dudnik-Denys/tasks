from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version

    def __repr__(self):
        return f"{type(self).__name__}('{self._version}')"

    def __str__(self):
        return self._version

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, new_version: str):
        if '.' not in new_version:
            self._version = f'{new_version}.0.0'
        if new_version.count('.') == 1:
            self._version = f'{new_version}.0'
        if new_version.count('.') == 2:
            self._version = new_version

    def __eq__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self._version.split('.'))) == tuple(map(int, other._version.split('.')))
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self._version.split('.'))) > tuple(map(int, other._version.split('.')))
        return NotImplemented
