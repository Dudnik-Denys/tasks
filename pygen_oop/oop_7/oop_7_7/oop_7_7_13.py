from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length: int):
        self.length = length
        self._data = ['']

    def add(self, data: str):
        data = data.split(' ')
        for word in data:
            if len(word) <= self.length:
                if len(self._data[-1]) >= 1 and len(word) + len(self._data[-1]) < self.length:
                    self._data[-1] = self._data[-1] + ' ' + word
                elif len(self._data[-1]) == 0:
                    self._data[-1] = word
                else:
                    self._data.append(word)

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for row in self._data:
            print(row)
        self._data = ['']


class RightParagraph(Paragraph):
    def end(self):
        for row in self._data:
            spaces = ' ' * (self.length - len(row))
            print(spaces + row)
        self._data = ['']
