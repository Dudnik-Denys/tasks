def detect_capital_use(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()
