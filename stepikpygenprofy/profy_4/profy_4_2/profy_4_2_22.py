import csv


def sorting(data: list[dict], shop: str, item_name: str) -> int:
    for dictionary in data:
        if dictionary['Магазин'] == shop:
            return int(dictionary[item_name])


with open('prices.csv', encoding='utf-8') as csv_file:
    minimal_cost = {}
    items = []
    parser = []
    reader = csv.DictReader(csv_file, delimiter=';')

    for line in reader:
        parser.append(line)
        for item in line.keys():
            if item != 'Магазин' and item not in items:
                items.append(item)

    for row in parser:
        for i in range(len(items)):
            if row['Магазин'] not in minimal_cost:
                minimal_cost[row['Магазин']] = items[i]
            elif row['Магазин'] in minimal_cost and int(row[items[i]]) < int(row[minimal_cost[row['Магазин']]]):
                minimal_cost[row['Магазин']] = items[i]
            elif row['Магазин'] in minimal_cost and int(row[items[i]]) == int(row[minimal_cost[row['Магазин']]]):
                alphabet_sort = sorted([items[i], minimal_cost[row['Магазин']]])[0]
                minimal_cost[row['Магазин']] = alphabet_sort

    sorted_minimal_costs = sorted(minimal_cost.items(), key=lambda x: (sorting(parser, x[0], x[1]), x[1], x[0]))
    print(f'{sorted_minimal_costs[0][1]}: {sorted_minimal_costs[0][0]}')
