def cubes_of_odds(iterable):
    return (i ** 3 for i in iterable if i % 2 != 0)
