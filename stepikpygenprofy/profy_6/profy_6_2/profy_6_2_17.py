from string import ascii_lowercase

symbols = [symbol for symbol in input()]
ascii_lowercase = [symbol for symbol in ascii_lowercase]
sentence = input().lower()

letters = {ascii_lowercase[i]: symbols[i] for i in range(len(symbols))}

new_sentence = ''

for symbol in sentence:
    if symbol in letters:
        new_sentence += letters[symbol]
    else:
        new_sentence += symbol

print(new_sentence)
