from collections import defaultdict


def flip_dict(data: dict) -> defaultdict:
    result = defaultdict(list)

    for key, value in data.items():
        for item in value:
            result[item].append(key)

    return result


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
