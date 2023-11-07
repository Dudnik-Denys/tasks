def tribonacci(n: int) -> int:
    cache = {1: 1, 2: 1, 3: 1}
    def wrapper(n: int):
        result = cache.get(n)
        if result is None:
            result = wrapper(n - 3) + wrapper(n - 2) + wrapper(n - 1)
            cache[n] = result
        return result
    return wrapper(n)
