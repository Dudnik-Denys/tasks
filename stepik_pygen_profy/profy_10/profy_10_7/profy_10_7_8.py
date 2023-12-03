import csv

with open('data.csv', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file)
    result = sum(int(line['raisedAmt']) for line in data if line['round'] == 'a')
    print(result)
