from collections import Counter
import csv
import json

statistic = Counter()


def parse_csv(filename):
    with open(filename, encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        total = {}

        for line in data:
            for key, value in line.items():
                if key == 'продукт':
                    item = value
                    total[value] = 0
                else:
                    total[item] += int(value)
    return total


for quarter in range(1, 5):
    statistic.update(parse_csv(f'quarter{quarter}.csv'))

with open('prices.json', encoding='utf-8') as json_file:
    prices = json.load(json_file)

for name, cost in statistic.items():
    statistic[name] *= prices[name]

print(statistic.total())
