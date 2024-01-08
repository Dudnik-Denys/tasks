class LoopTracker:
    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._empty_accesses = self._accesses = 0
        self._is_empty = False
        try:
            self._nextvalue = self._first = next(self._iterable)
        except StopIteration:
            self._is_empty = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty:
            self._empty_accesses += 1
            raise StopIteration
        self._curvalue = self._nextvalue
        self._accesses += 1
        try:
            self._nextvalue = next(self._iterable)
        except StopIteration:
            self._is_empty = True
        return self._curvalue

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if hasattr(self, '_first'):
            return self._first
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if hasattr(self, '_curvalue'):
            return self._curvalue
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return self._is_empty
