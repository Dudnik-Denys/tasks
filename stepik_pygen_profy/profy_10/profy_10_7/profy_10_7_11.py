def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as txt_file:
        lines = (line.strip() for line in txt_file.readlines() if len(line) > 1)
        result = []

        for planet in range(9):
            temp = {}
            for data in range(4):
                obj = next(lines)
                temp[obj[:obj.replace(' ', '').find('=')]] = obj[obj.find('=') + 2:]
            result.append(temp)

    return iter(result)
