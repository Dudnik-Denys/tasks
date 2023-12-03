with open('class_scores.txt', mode='r', encoding='utf-8') as file, \
     open('new_scores.txt', mode='w', encoding='utf-8') as new:
    text = {line.strip().split()[0]: int(line.strip().split()[1]) + 5 for line in file.readlines()}

    for key, value in text.items():
        if value > 100:
            value = 100
        new.write(key + ' ' + str(value) + '\n')
