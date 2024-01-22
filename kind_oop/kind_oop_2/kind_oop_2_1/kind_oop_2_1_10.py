class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            if not self.head:
                self.head = obj
                self.tail = obj
            else:
                self.tail.set_next(obj)
                obj.set_prev(self.tail)
                self.tail = obj
            self._length += 1

    def remove_obj(self):
        if self._length > 1:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            self._length -= 1
        elif self._length == 1:
            self.head = None
            self.tail = None
            self._length -= 1

    def get_data(self):
        result = []
        size = self._length
        obj = self.head

        while size > 0:
            result.append(obj.get_data())
            obj = obj.get_next()
            size -= 1

        return result


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, obj):
        self.__next = obj

    def get_prev(self):
        return self.__prev

    def set_prev(self, obj):
        self.__prev = obj
