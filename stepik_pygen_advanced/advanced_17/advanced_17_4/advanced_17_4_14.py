with open('logfile.txt', mode='r', encoding='utf-8') as file, \
     open('output.txt', mode='w', encoding='utf-8') as output:
    data = {line.split(',')[0]: tuple(line.strip().replace(' ', '').split(',')[1:]) for line in file.readlines()}

    for key, value in data.items():
        begin = list(map(int, value[0].split(':')))
        finish = list(map(int, value[1].split(':')))
        begin = begin[0] * 60 + begin[1]
        finish = finish[0] * 60 + finish[1]
        if finish - begin >= 60:
            output.write(key + '\n')
