import copy


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False):
        self.data = data
        self.deep = deep
        self.data_copy = copy.deepcopy(self.data) if self.deep else copy.copy(self.data)

    def __enter__(self):
        return self.data_copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return True
        if isinstance(self.data, list):
            self.data[:] = self.data_copy
        if isinstance(self.data, set | dict):
            self.data.clear()
            if type(self.data) == set:
                for elem in self.data_copy:
                    self.data.add(elem)
            if type(self.data) == dict:
                for key, value in self.data_copy.items():
                    self.data[key] = value
        return False


# Более сексуальный вариант решения
# import copy
#
#
# class Atomic:
#     def __init__(self, data, deep=False):
#         self.original = data
#         self.copy = copy.deepcopy if deep else copy.copy
#
#         if isinstance(data, list):
#             self.original_update = self.original.extend
#         elif isinstance(data, (set, dict)):
#             self.original_update = self.original.update
#
#     def __enter__(self):
#         self.data = self.copy(self.original)
#         return self.data
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.original.clear()
#             self.original_update(self.data)
#         return True
