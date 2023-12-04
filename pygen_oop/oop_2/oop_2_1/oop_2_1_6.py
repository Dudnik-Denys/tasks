from itertools import combinations


def inversions(sequence):
    result = sum([1 for pair in combinations(sequence, 2) if pair[0] > pair[1]])
    return result
