def my_pow(number, index=1):
    total = 0
    for index, num in enumerate(str(number), index):
        total = total + (int(num)) ** index
    return total
