import datetime

with open('diary.txt', 'r', encoding='utf-8') as file:
    text = []
    text_part = []

    for line in file.readlines():
        if line != '\n':
            text_part.append(line.strip())
        else:
            text_part[0] = text_part[0].split(';')
            text_part[0][0] = text_part[0][0].split('.')
            text_part[0][0][2], text_part[0][0][0] = text_part[0][0][0], text_part[0][0][2]
            text_part[0][0] = '-'.join(text_part[0][0])
            text_part[0][1] = text_part[0][1].replace(' ', '')
            text_part[0][0] = datetime.date.fromisoformat(text_part[0][0])
            text_part[0][1] = datetime.time.fromisoformat(text_part[0][1])
            text_part[0] = datetime.datetime.combine(text_part[0][0], text_part[0][1])
            text.append(text_part)
            text_part = []
    text_part[0] = text_part[0].split(';')
    text_part[0][0] = text_part[0][0].split('.')
    text_part[0][0][2], text_part[0][0][0] = text_part[0][0][0], text_part[0][0][2]
    text_part[0][0] = '-'.join(text_part[0][0])
    text_part[0][1] = text_part[0][1].replace(' ', '')
    text_part[0][0] = datetime.date.fromisoformat(text_part[0][0])
    text_part[0][1] = datetime.time.fromisoformat(text_part[0][1])
    text_part[0] = datetime.datetime.combine(text_part[0][0], text_part[0][1])
    text.append(text_part)

    text = sorted(text, key=lambda x: x[0])
    for dt in text:
        dt[0] = dt[0].strftime('%d.%m.%Y; %H:%M')

with open('new_diary.txt', 'w', encoding='utf-8') as new:
    for paragraph in text:
        for sentence in paragraph:
            new.write(sentence + '\n')
        new.write('\n')

with open('new_diary.txt', 'r', encoding='utf-8') as final:
    final_text = final.readlines()[:-1]
    final_text[-1] = final_text[-1].replace('\n', '')
    for line in final_text:
        print(line, end='')


# Normal solution
# from datetime import datetime
#
# notes = {}
# pattern = '%d.%m.%Y; %H:%M'
#
# with open('diary.txt', encoding='utf-8') as file:
#     diary = file.read().split('\n\n')
#     for note in diary:
#         dt, text = note.split('\n', 1)
#         dt = datetime.strptime(dt, pattern)
#         notes[dt] = text
#
# for dt, text in sorted(notes.items()):
#     print(dt.strftime(pattern))
#     print(text)
#     print()
