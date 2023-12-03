with open('words.txt', mode='r', encoding='utf-8') as file:
    text = {word: len(word) for word in file.read().split()}
    [print(key) for key, value in text.items() if value == max(text.values())]
