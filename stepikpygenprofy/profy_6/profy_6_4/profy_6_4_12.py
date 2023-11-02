from datetime import datetime
from collections import namedtuple
import csv

meeting = namedtuple('Meeting', ['surname', 'name', 'date_time'])
date_pattern = '%d.%m.%Y%H:%M'

with open('meetings.csv', encoding='utf-8') as csv_file:
    data = list(csv.DictReader(csv_file))
    meetings = []

    for meet in data:
        tpl = meeting._make([meet['surname'], meet['name'], datetime.strptime(meet['meeting_date'] + meet['meeting_time'], date_pattern)])
        meetings.append(tpl)

meetings = sorted(meetings, key=lambda m: m.date_time)

for friend in meetings:
    print(friend.surname, friend.name)
