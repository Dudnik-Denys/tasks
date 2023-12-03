import csv

with open('sales.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    # data = [row['name'] for row in reader if row['old_price'] > row['new_price']]
    data = [row['name'] for row in reader if int(row['old_price']) >= int(row['new_price'])]
    print(len(data))
