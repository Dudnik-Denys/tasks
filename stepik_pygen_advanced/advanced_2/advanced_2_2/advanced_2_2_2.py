nums = list(map(int, input().split()))


def big(nums: list) -> int:
    total = 0

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            total += 1

    return total


print(big(nums))
