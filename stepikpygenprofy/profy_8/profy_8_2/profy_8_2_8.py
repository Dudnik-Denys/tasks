def while_not_zero(num):
    if num != 0:
        while_not_zero(int(input()))
    print(num)


while_not_zero(int(input()))
