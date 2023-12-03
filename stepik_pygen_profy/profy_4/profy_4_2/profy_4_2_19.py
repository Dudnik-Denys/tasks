import csv
from datetime import datetime

new_log = {}

with open('name_log.csv', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file)

    for line in data:
        if line['email'] not in new_log:
            new_log[line['email']] = line
        elif line['email'] in new_log and datetime.strptime(line['dtime'], '%d/%m/%Y %H:%M') > datetime.strptime(new_log[line['email']]['dtime'], '%d/%m/%Y %H:%M'):
            new_log[line['email']]['dtime'] = line['dtime']
            new_log[line['email']]['username'] = line['username']

with open('new_name_log.csv', 'w', encoding='utf-8') as new_csv_file:
    columns = ['username', 'email', 'dtime']
    writer = csv.DictWriter(new_csv_file, fieldnames=columns)
    writer.writeheader()

    for key, value in sorted(new_log.items(), key=lambda x: x):
        writer.writerow(value)
