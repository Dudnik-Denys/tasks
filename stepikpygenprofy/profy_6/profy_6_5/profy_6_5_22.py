from collections import defaultdict


def wins(pairs) -> defaultdict:
    statistic = defaultdict(set)

    for pair in pairs:
        winner, loser = pair
        statistic[winner].add(loser)

    return statistic


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
