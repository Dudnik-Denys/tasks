from random import shuffle


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    _SUITS = {
        '♣': 1,
        '♢': 2,
        '♡': 3,
        '♠': 4
    }

    _RANKS = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self):
        self._deck = []

        for suit in self._SUITS:
            for rank in self._RANKS:
                self._deck.append(Card(suit, rank))

    def shuffle(self):
        if len(self._deck) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self._deck)

    def deal(self):
        if not self._deck:
            raise ValueError('Все карты разыграны')
        return self._deck.pop()

    def __str__(self):
        return f'Карт в колоде: {len(self._deck)}'
