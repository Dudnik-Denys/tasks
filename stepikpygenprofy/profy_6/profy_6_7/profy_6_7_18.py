from collections import Counter

counter = Counter(input().split(','))

for key, value in sorted(counter.items()):
    cost = sum([ord(char) for char in key if char.isalpha()])
    result = cost * value
    print(f'{key.ljust(len(max(counter.keys(), key=len)))}: {cost} UC x {value} = {result} UC')
