class Stack:
    def __init__(self):
        self.top = None
        self.__current = None
        self.__length = 0

    def push(self, elem):
        if not self.top:
            self.top = elem
            self.__current = elem
        else:
            self.__current.next = elem
            elem.previous = self.__current
            self.__current = elem
        self.__length += 1

    def pop(self):
        item = None
        if self.__length > 1:
            item = self.__current
            self.__current = self.__current.previous
            self.__current.next = None
        if self.__length == 1:
            item = self.top
            self.top = None
            self.__current = None
        self.__length -= 1 if item else 0
        return item

    def get_data(self):
        if self.__length >= 1:
            size = self.__length
            item = self.top
            result = []

            while size > 0:
                result.append(item.data)
                item = item.next
                size -= 1
            return result
        return []


class StackObj:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.previous = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, elem):
        if isinstance(elem, StackObj) or None:
            self.__next = elem
