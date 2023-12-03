def linear(nested_list: list) -> list:
    result = []
    for elem in nested_list:
        if isinstance(elem, list):
            result.extend(linear(elem))
        else:
            result.append(elem)
    return result
