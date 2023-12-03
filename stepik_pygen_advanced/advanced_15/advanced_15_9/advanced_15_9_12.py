nums = [num for num in range(int(input()), int(input()) + 1)]


def func(num):
    x = str(num)

    for digit in x:
        if int(digit) != 0 and num % int(digit) == 0:
            continue
        else:
            return 0
    return num


print(*list(filter(lambda x: x > 0, list(map(func, nums)))))
