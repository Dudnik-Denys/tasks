def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]
