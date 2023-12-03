def non_negative_even(numbers: list) -> bool:
    return len(list(filter(lambda x: x >= 0 and x % 2 == 0, numbers))) == len(numbers)


print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
