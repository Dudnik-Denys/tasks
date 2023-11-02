def get_biggest(numbers: list) -> int:
    maximum = -1
    if numbers:
        numbers = sorted([str(num) for num in numbers])
        numbers = sorted(numbers, key=lambda x: x * len(max(numbers, key=len)), reverse=True)
        maximum = int(''.join(numbers))

    return maximum
