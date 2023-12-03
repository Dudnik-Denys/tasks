nums = input().split()


def nums_sort(num: str):
    total = 0
    for x in num:
        total += int(x)
    return total


print(*sorted(nums, key=lambda num: (nums_sort(num), int(num))))