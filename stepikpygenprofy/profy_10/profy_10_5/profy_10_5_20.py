def card_deck(suit):
    deck = {
        'пик': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'],
        'треф': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'],
        'бубен': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'],
        'червей': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
    }

    while True:
        for key, value in deck.items():
            if key != suit:
                for card in value:
                    yield f'{card} {key}'
