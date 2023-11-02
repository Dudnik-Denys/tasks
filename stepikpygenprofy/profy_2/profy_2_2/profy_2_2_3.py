n, x, y, a, b = [int(i) for i in input().split()]
nums = list(range(1, n + 1))

nums[x - 1:y] = reversed(nums[x - 1:y])
nums[a - 1:b] = reversed(nums[a - 1:b])

print(*nums)
