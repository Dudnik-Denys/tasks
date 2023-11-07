def recursive_sum(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    if a > 0:
        return 1 + recursive_sum(a - 1, b)
    return 1 + recursive_sum(a, b - 1)
