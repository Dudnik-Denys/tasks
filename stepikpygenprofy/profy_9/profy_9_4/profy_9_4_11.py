def numbers_sum(elems: list):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""

    total = sum([elem for elem in elems if type(elem) in (int, float)])
    return total


print(numbers_sum(['beegeek', 'stepik', '100']))
