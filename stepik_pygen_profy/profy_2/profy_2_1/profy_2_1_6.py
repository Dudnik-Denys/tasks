def same_parity(numbers: list) -> list:
    numbers = [num for num in numbers if num % 2 == numbers[0] % 2]
    return numbers
