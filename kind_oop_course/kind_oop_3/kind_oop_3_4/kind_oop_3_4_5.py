class NewList:
    def __init__(self, data=None):
        self.data = data[:] if data is not None else []

    def __sub__(self, other):
        new = other if isinstance(other, list) else other.get_list()

        return NewList(self._diff_list(self.data, new))

    def __rsub__(self, other):
        return NewList(self._diff_list(other, self.data))

    @staticmethod
    def _diff_list(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1

        sub = lst_2[:]
        return [x for x in lst_1 if not NewList._is_elem(x, sub)]

    @staticmethod
    def _is_elem(x, sub):
        res = any(map(lambda y: type(x) == type(y) and y == x, sub))
        if res:
            sub.remove(x)
        return res

    def get_list(self):
        return self.data
