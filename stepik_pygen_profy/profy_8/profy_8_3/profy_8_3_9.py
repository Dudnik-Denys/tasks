def range_sum(numbers: list, start: int, end: int) -> int:
    if start == end:
        return numbers[end]
    return numbers[start] + range_sum(numbers, start + 1, end)
