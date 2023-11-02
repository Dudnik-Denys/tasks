with open('goats.txt', mode='r', encoding='utf-8') as file, \
     open('answer.txt', mode='w', encoding='utf-8') as answer:
    text = [line.strip() for line in file.readlines()]
    colors = text[1: text.index('GOATS')]
    goats = text[text.index('GOATS') + 1:]
    total = {color: 0 for color in colors}
    minimal_quantity = len(text[text.index('GOATS') + 1:]) / 100 * 7

    for goat in goats:
        total[goat] += 1

    for key, value in sorted(total.items()):
        if value > minimal_quantity:
            answer.write(key + '\n')

    print(total, minimal_quantity, sep='\n')
