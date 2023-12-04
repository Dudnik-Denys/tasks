import sys
from collections import Counter

pokemons = [line.strip() for line in sys.stdin]
counter = Counter(pokemons)
print(sum(counter.values()) - len(counter.values()))
