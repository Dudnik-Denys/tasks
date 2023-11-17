def reverse(sequence):
    yield from (x for x in sequence[::-1])
