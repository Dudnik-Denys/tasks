import csv


def first_half_sort(class_number: str) -> int:
    if len(class_number) == 3:
        return int(class_number[0])
    return int(class_number[:2])


def second_half_sort(class_number: str) -> int:
    return ord(class_number[-1])


with open('student_counts.csv', encoding='utf-8') as students, open('sorted_student_counts.csv', 'w', encoding='utf-8') as sorted_students:
    classes = []
    students_data = []
    reader = csv.DictReader(students)

    for line in reader:
        students_data.append(line)
        for item in line.keys():
            if item not in classes and item != 'year':
                classes.append(item)

    classes = sorted(classes, key=lambda x: (first_half_sort(x), second_half_sort(x)))
    columns = ['year'] + classes
    writer = csv.DictWriter(sorted_students, fieldnames=columns)
    writer.writeheader()

    for line in students_data:
        data = {'year': line['year']}
        for i in range(len(classes)):
            data.update({classes[i]: line[classes[i]]})
        writer.writerow(data)
