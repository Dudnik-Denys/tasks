from itertools import groupby

words = input().split()

group_iter = groupby(sorted(words, key=lambda x: len(x)), key=lambda x: len(x))

for group in group_iter:
    number, words = group
    print(f'{number} -> {", ".join(sorted(words))}')
