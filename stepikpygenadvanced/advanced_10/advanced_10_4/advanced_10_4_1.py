words = [input().split(':') for _ in range(int(input()))]
words_dict = {word[0].lower(): word[1].strip() for word in words}

for _ in range(int(input())):
    word = input().lower()
    if word in words_dict:
        print(words_dict[word])
    else:
        print('Не найдено')
