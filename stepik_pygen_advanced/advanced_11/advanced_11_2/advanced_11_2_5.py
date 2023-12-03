data = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]


def merge(values: list) -> dict:
    result = {}

    for elem in values:
        for key, value in elem.items():
            if key not in result:
                result[key] = {value, }
            elif key in result:
                result[key].add(value)

    return result


# def merge(values):
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res.setdefault(k, set()).add(v)
#     return res
