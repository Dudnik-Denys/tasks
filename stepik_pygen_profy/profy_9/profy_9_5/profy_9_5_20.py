def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))
