class CardDeck:
    def __init__(self):

        self.suits = ['пик', 'треф', 'бубен', 'червей']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']

        self.cards = [[f'{rank} {suit}' for rank in self.ranks] for suit in self.suits]
        self.deck = []

        for i in range(4):
            self.deck.extend(self.cards[i])

        self.iterable = iter(self.deck)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)
