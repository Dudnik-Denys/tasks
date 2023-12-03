def custom_pairwise(iterable, size):
    group = []
    for _ in range(size):
        try:
            group.append(next(iterable))
        except StopIteration:
            while len(group) < size:
                group.append(None)
    return tuple(group)


def grouper(iterable, n):
    iterator = iter(iterable)
    while True:
        result = custom_pairwise(iterator, n)
        if result.count(None) == len(result):
            break
        yield result


# А все решалось намного проще :D
# from itertools import repeat, zip_longest
#
# def grouper(iterable, n):
#     return zip_longest(*repeat(iter(iterable), n))
