sum_nums = lambda num: num if num < 10 else (num % 10) + sum_nums(num // 10)

print(sum_nums(int(input())))
