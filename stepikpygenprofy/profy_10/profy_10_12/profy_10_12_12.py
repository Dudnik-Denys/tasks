from itertools import combinations


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

ways_set = set()
for w in range(1, len(wallet) + 1):
    for way in combinations(wallet, w):
        if sum(way) == 100:
            ways_set.add(way)

print(len(ways_set))
