import json
import csv

with open('students.json', encoding='utf-8') as json_file, open('data.csv', 'w', encoding='utf-8') as csv_file:
    students = json.load(json_file)
    data = {student['name']: student['phone'] for student in students if student['progress'] >= 75 and student['age'] >= 18}
    data = sorted(data.items(), key=lambda x: x[0])
    writer = csv.DictWriter(csv_file, fieldnames=['name', 'phone'])
    writer.writeheader()

    for student in data:
        writer.writerow({'name': student[0], 'phone': student[1]})
