nums = input().split()


def diff(numbers: list) -> int:
    total = 1

    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i + 1]:
            total += 1

    return total


print(diff(nums))
