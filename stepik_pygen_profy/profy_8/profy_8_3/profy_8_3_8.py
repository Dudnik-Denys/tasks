number_of_frogs = lambda year: 77 if year == 1 else 3 * (number_of_frogs(year - 1) - 30)
