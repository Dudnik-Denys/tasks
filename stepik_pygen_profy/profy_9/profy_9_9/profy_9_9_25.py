from functools import lru_cache


@lru_cache
def ways(n: int) -> int:
    if n == 2 or n == 1:
        return 1
    if n <= 0:
        return 0
    return ways(n - 1) + ways(n - 3) + ways(n - 4)
