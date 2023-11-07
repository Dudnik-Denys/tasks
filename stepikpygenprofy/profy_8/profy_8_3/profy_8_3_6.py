nums_count = lambda num: 1 if num < 10 else 1 + nums_count(num // 10)

print(nums_count(int(input())))
