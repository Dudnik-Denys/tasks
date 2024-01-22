class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def add_obj(self, obj):
        """Метод для добавления элемента в связный список"""

        if self.head:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        else:
            self.head = obj
            self.tail = obj
        self._length += 1

    def remove_obj(self, index):
        """Метод для удаления элемента из связного списка по индексу, работает только с положительными числами"""

        if index < 0:
            raise IndexError('Индекс не должен быть отрицательным')

        sequence = self.get_list()
        length = len(sequence)
        elem = sequence[index]

        if index == 0 and length > 1:
            elem.next.prev = None
            self.head = elem.next
        elif index == 0 and length == 1:
            self.head = None
            self.tail = None
        elif index == length - 1:
            elem.prev.next = None
            self.tail = elem.prev
        else:
            elem.prev.next, elem.next.prev = elem.next, elem.prev
        self._length -= 1

    def get_list(self):
        current = self.head
        result = []

        while current is not None:
            result.append(current)
            current = current.next

        return result

    def __len__(self):
        return self._length

    def __call__(self, index):
        return self.get_list()[index].data


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
