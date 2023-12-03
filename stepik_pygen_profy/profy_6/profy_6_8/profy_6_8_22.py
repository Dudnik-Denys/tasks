from collections import Counter

store = Counter(list(map(int, input().split())))
buyers = Counter()

for _ in range(int(input())):
    buyer, cost = map(int, input().split())
    if store[buyer] > 0:
        buyers.update({buyer: cost})
        store[buyer] -= 1

print(buyers.total())
