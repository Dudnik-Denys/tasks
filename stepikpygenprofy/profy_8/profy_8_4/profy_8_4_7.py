def get_all_values(nested_dicts: dict, key: str):
    items = set()

    def wrapper(nested_dicts, key):
        if key in nested_dicts:
            items.add(nested_dicts[key])

        for value in nested_dicts.values():
            if isinstance(value, dict):
                value = wrapper(value, key)
                if value is not None:
                    items.update(value)
        return items
    return wrapper(nested_dicts, key)

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))