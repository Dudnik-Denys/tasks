def get_fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 != 0:
        return a * (get_fast_pow(a, n - 1))
    return get_fast_pow(a, n // 2) * get_fast_pow(a, n // 2)
