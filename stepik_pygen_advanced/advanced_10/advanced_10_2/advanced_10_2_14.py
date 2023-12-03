data = {
    'CS101': {'class': 3004,
              'teacher': 'Хайнс',
              'time': '8:00'},
    'CS102': {'class': 4501,
              'teacher': 'Альварадо',
              'time': '9:00'},
    'CS103': {'class': 6755,
              'teacher': 'Рич',
              'time': '10:00'},
    'NT110': {'class': 1244,
              'teacher': 'Берк',
              'time': '11:00'},
    'CM241': {'class': 1411,
              'teacher': 'Ли',
              'time': '13:00'}
    }

choice = input()

print(f'{choice}: {data[choice]["class"]}, {data[choice]["teacher"]}, {data[choice]["time"]}')


# alternative solve variant:

# courses = {
#     "CS101": (3004, 'Хайнс', '8:00'),
#     "CS102": (4501, 'Альварадо', '9:00'),
#     "CS103": (6755, 'Рич', '10:00'),
#     "NT110": (1244, 'Берк', '11:00'),
#     "CM241": (1411, 'Ли', '13:00')
# }
#
# s = input()
# print('{}: {}, {}, {}'.format(s, *courses[s]))
