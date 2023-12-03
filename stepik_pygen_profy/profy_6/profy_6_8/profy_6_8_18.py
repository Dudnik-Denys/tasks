from collections import Counter
import csv

with open('name_log.csv', encoding='utf-8') as csv_file:
    data = list(csv.DictReader(csv_file))

[print(key, value, sep=': ') for key, value in sorted(Counter([line['email'] for line in data]).items())]
