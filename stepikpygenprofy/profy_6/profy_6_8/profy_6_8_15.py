from collections import Counter

counter = Counter([len(word) for word in input().split()])
[print(f'Слово длины {length}: {count}') for length, count in sorted(counter.items(), key=lambda x: x[1])]
