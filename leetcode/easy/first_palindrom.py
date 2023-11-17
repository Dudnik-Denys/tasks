def first_palindrome(words: list[str]) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ''
