from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

ways_set = set()
for w in range(1, 21):
    for way in combinations_with_replacement(wallet, w):
        if sum(way) == 100:
            ways_set.add(way)

print(len(ways_set))
