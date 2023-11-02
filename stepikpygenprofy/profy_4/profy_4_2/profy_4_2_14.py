import csv

filter_param = int(input())

with open('deniro.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    data = [[row[0], int(row[1]), int(row[2])] for row in reader]

    [print(f'{row[0]},{row[1]},{row[2]}') for row in sorted(data, key=lambda x: x[filter_param - 1])]
