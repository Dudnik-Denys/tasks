class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self._length = 0

    def push_back(self, obj):
        if not self.top:
            self.top = obj
            self.tail = obj
        else:
            obj.previous = self.tail
            self.tail.next = obj
            self.tail = obj
        self._length += 1

    def pop_back(self):
        if self._length == 1:
            self.top = None
            self.tail = None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous
        self._length -= 1

    def __add__(self, other):
        if not isinstance(other, list):
            self.push_back(other)
        return self

    def __mul__(self, other):
        if isinstance(other, list):
            for elem in other:
                self.push_back(StackObj(elem))
        return self


class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__previous = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        self.__previous = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
