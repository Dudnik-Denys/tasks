nums = input()

print(['YES', 'NO'][len(nums) != len(set(nums))])
