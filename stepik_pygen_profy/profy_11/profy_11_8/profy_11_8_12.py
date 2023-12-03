import re

data = input()


def swap_letters(word: re.Match) -> str:
    suffix = word.group(0)[2:] if len(word.group(0)) > 2 else ''
    return word.group(0)[1] + word.group(0)[0] + suffix


print(re.sub(r'\b\w{2,}\b', swap_letters, data))


# ))
# from re import sub
#
# print(sub(r'\b(\w)(\w)', r'\2\1', input()))
