from string import ascii_uppercase
from itertools import cycle


def alnum_sequence():
    return cycle(elem for tpl in zip(range(1, 27), ascii_uppercase) for elem in tpl)
