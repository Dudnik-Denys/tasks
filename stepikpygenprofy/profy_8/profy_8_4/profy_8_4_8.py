def dict_travel(nested_dicts, result=''):
    for key, value in sorted(nested_dicts.items()):
        if isinstance(value, dict):
            dict_travel(value, result + f'{key}.')
        else:
            print(f'{result}{key}: {value}')
    return result


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
