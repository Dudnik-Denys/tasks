from itertools import zip_longest


def roundrobin(*args):
    if args:
        for data in zip_longest(*args, fillvalue=''):
            for elem in data:
                if elem != '':
                    yield elem
    return args
