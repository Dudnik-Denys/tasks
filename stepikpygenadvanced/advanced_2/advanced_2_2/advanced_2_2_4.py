nums = list(map(int, input().split()))


def change(numbers: list) -> list:
    last = numbers.pop()
    numbers.insert(0, last)
    return numbers


print(*change(nums))
