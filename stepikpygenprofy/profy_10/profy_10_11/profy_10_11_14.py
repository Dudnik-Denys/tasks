from itertools import groupby


def group_anagrams(words):
    group_iter = groupby(sorted(words, key=lambda x: sorted(x)), key=lambda x: ''.join(sorted(x)))
    return (tuple(tpl[1]) for tpl in group_iter)
