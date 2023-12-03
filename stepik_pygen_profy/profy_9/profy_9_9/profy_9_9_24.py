from functools import lru_cache
import sys

text = [line.strip() for line in sys.stdin]


@lru_cache
def sorting(elem):
    result = ''.join(sorted([char for char in elem]))
    return result


for row in text:
    print(sorting(row))
