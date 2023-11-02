import json
import csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as csv_file, open('best_scores.json', 'w', encoding='utf-8') as json_file:
    reader = csv.DictReader(csv_file)
    data = {}
    date_pattern = '%Y-%m-%d %H:%M:%S'

    for student in reader:
        if student['email'] not in data:
            data[student['email']] = {'name': student['name'], 'surname': student['surname'], 'best_score': int(student['score']), 'date_and_time': student['date_and_time']}
        elif student['email'] in data and int(student['score']) > int(data[student['email']]['best_score']):
            data[student['email']]['best_score'] = int(student['score'])
            data[student['email']]['date_and_time'] = student['date_and_time']
        elif student['email'] in data and int(student['score']) == int(data[student['email']]['best_score']):
            latest_date = max(datetime.strptime(student['date_and_time'], date_pattern), datetime.strptime(data[student['email']]['date_and_time'], date_pattern))
            latest_date = datetime.strftime(latest_date, date_pattern)
            data[student['email']]['date_and_time'] = latest_date

    sorted_emails = sorted(data)
    parser = []

    for email in sorted_emails:
        temp = data[email] | {'email': email}
        parser.append(temp)

    json.dump(parser, json_file, indent=3)
