from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values=False):
    for key, value in sorted(ordered_dict.items(), key=lambda x: x[int(by_values)]):
        ordered_dict.move_to_end(key)
