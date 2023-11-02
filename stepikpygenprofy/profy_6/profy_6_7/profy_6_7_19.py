from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as txt_file:
    text = [[symbol for symbol in line.lower().strip() if symbol.isalpha()] for line in txt_file.readlines()]
    letters = ''

    for line in text:
        for char in line:
            letters += char

counter = Counter(letters)

for letter, count in sorted(counter.items()):
    print(f'{letter}: {count}')
