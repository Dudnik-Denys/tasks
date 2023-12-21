class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]
