def alternating_sequence(count=None):
    index = 0
    while index != count:
        index += 1
        yield index if index % 2 != 0 else -index
