def first_largest(iterable, number):
    for index, elem in enumerate(iterable):
        if elem > number:
            return index
    return -1
