import csv

with open('salary_data.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    data = {}

    for row in reader:
        if row['company_name'] not in data:
            data[row['company_name']] = [int(row['salary'])]
        else:
            data[row['company_name']].append(int(row['salary']))

    for key, value in data.items():
        data[key] = sum(value) / len(value)

    for key, value in sorted(data.items(), key=lambda x: (x[1], x[0])):
        print(key)