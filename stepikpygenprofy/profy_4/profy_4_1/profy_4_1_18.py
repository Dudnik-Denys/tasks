import sys

nums = [int(num.strip()) for num in sys.stdin]


def is_arithmetic(sequence: list) -> str:
    counter = 0
    for x in range(len(sequence[:-1])):
        if sequence[x + 1] - sequence[x] == 1:
            counter += 1
        else:
            break
    if counter == len(sequence) - 1:
        return 'Арифметическая прогрессия'
    return 'Не прогрессия'


def is_geometric(sequence: list) -> str:
    counter = 0
    for x in range(len(sequence[:-1])):
        if sequence[x + 1] == sequence[x] * 2:
            counter += 1
        else:
            break
    if counter == len(sequence) - 1:
        return 'Геометрическая прогрессия'
    return 'Не прогрессия'


print([is_geometric(nums), is_arithmetic(nums)][nums[2] - nums[1] == 1])
