filename = input()

with open('forbidden_words.txt', mode='r', encoding='utf-8') as f_words,\
     open(filename, mode='r', encoding='utf-8') as file:
    forbidden = f_words.read().split()
    text = [line for line in file.readlines()]
    old_text = text[:]
    new_text = ''
    for word in forbidden:
        censure = '*' * len(word)

        for i in range(len(text)):
            if word in text[i].lower():
                text[i] = text[i].lower().replace(word, censure)

    for x in range(len(text)):
        for y in range(len(text[x])):
            if text[x][y] == '*':
                new_text += '*'
            else:
                new_text += old_text[x][y]

    print(new_text)
