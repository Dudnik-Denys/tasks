def flatten(nested_list: list[int] | list[list[int]]):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem
