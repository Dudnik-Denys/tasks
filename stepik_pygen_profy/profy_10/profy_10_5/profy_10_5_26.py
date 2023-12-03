def palindromes():
    index = 1
    while True:
        if str(index) == str(index)[::-1]:
            yield index
        index += 1


generator = palindromes()
