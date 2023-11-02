from collections import Counter


def count_occurences(word: str, words: str) -> int:
    counter = Counter(words.lower().split())
    return counter[word.lower()]
