alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = input() + ' запретил букву'

for char in alphabet:
    if len(word) > 0 and char in word:
        print(word, char)
        word = word.replace(char, '').replace('  ', ' ').strip()
