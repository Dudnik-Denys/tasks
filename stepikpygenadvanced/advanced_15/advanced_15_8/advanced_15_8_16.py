def evaluate(coefficients, x):
    total = 0
    indx = len(coefficients) - 1
    for num in coefficients:
        if indx > 0:
            total = total + (num * (x ** indx))
            indx -= 1
        elif indx <= 0:
            total += num

    return total


nums = tuple(map(int, input().split()))
manydick = int(input())

print(evaluate(nums, manydick))
