def filter_anagrams(word: str, words: list) -> list:
    filtered_words = [element for element in words if sorted(element) == sorted(word)]
    return filtered_words
