from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    symbols = symbols.lower()
    word = word.lower()
    symbols_counter = Counter(symbols)
    word_counter = Counter(word)
    intersection = symbols_counter & word_counter
    return intersection >= word_counter
