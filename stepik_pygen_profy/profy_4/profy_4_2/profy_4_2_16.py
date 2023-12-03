import csv

domain_usage = {}

with open('data.csv', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file)

    for line in data:
        dog = line['email'].find('@') + 1
        domain = line['email'][dog:]
        if domain not in domain_usage:
            domain_usage[domain] = 1
        else:
            domain_usage[domain] += 1

with open('domain_usage.csv', 'w', encoding='utf-8') as parser:
    columns = ['domain', 'count']
    parse_data = []

    for key, value in sorted(domain_usage.items(), key=lambda x: (x[1], x[0])):
        parse_data.append([key, value])

    writer = csv.writer(parser)
    writer.writerow(columns)
    writer.writerows(parse_data)
