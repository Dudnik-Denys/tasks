def ranges(numbers: list[int]) -> list[tuple]:
    result = []
    try:
        temp = [numbers[0]]
    except IndexError:
        return result

    for i in range(1, len(numbers) + 1):
        if i < len(numbers):
            if numbers[i] - 1 == numbers[i - 1]:
                temp.append(numbers[i])
            else:
                result.append(temp)
                temp = [numbers[i]]
        else:
            if numbers[len(numbers) - 1] - 1 == numbers[len(numbers) - 2]:
                temp.append(numbers[len(numbers) - 1])
                result.append(temp)
            else:
                result.append([numbers[len(numbers) - 1]])

    for i in range(len(result)):
        result[i] = (min(result[i]), max(result[i]))

    return result


# Все гениальное просто :)
# from itertools import groupby
#
#
# def ranges(numbers):
#     result = []
#     for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
#         group = tuple(group)
#         group = group[0], group[-1]
#         result.append(group)
#     return result
