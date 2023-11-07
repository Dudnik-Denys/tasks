def recursive_sum(nested_lists: list) -> int:
    total = 0
    for elem in nested_lists:
        if isinstance(elem, list):
            total += recursive_sum(elem)
        else:
            total += elem
    return total


# recursive_sum = lambda lists: sum(elem if type(elem) is int else recursive_sum(elem) for elem in lists)
