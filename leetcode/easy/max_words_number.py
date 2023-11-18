def most_words_found(sentences: list[str]) -> int:
    return max([len(i.split()) for i in sentences])
