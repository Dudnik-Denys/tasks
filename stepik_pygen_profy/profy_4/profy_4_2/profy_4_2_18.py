import csv

with open('titanic.csv', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file, delimiter=';')

    survived = {}

    for line in data:
        if line['name'] not in survived and line['survived'] == '1' and float(line['age']) < 18:
            survived[line['name']] = line['sex']

    for key, value in sorted(survived.items(), key=lambda x: x[1], reverse=True):
        print(key)
