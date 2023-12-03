nums = list(map(int, input().split()))


def change(nums: list) -> list:
    new = []

    if len(nums) % 2 == 0:
        for i in range(0, len(nums) - 1, 2):
            new.append(nums[i + 1])
            new.append(nums[i])
    else:
        for i in range(0, len(nums) - 2, 2):
            new.append(nums[i + 1])
            new.append(nums[i])
        new.append(nums[-1])
    return new


print(*change(nums))

# numbers = input().split()
#
# for i in range(0, len(numbers) - 1, 2):
#     numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#
# print(*numbers)
