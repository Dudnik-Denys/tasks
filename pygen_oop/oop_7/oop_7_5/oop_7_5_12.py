from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, h, v):
        pass


class King(ChessPiece):
    def can_move(self, h, v):
        if h in 'abcdefgh' and v in range(1, 9):
            h = ord(h) - 96
            if (ord(self.horizontal) - 96) != h or self.vertical != v:
                hz = (ord(self.horizontal) - 96) - h
                vt = self.vertical - v
                return -1 <= hz <= 1 and -1 <= vt <= 1
        return False


class Knight(ChessPiece):
    def can_move(self, h, v):
        if h in 'abcdefgh' and v in range(1, 9):
            return abs(((ord(self.horizontal) - 96) - (ord(h) - 96)) * (self.vertical - v)) == 2
        return False
