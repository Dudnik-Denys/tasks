import csv

parser = {}

with open('wifi.csv', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file, delimiter=';')

    for line in data:
        if line['district'] not in parser:
            parser[line['district']] = int(line['number_of_access_points'])
        else:
            parser[line['district']] += int(line['number_of_access_points'])

    for key, value in sorted(parser.items(), key=lambda x: (-x[1], x[0])):
        print(f'{key}: {value}')
