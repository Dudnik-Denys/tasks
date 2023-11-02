languages = [input().replace(' ', '').split(',') for _ in range(int(input()))]
langs = {}
result = []

for lst in languages:
    for language in lst:
        langs[language] = langs.get(language, 0) + 1
        if langs[language] == len(languages):
            result.append(language)

if result:
    print(*sorted(result), sep=', ')
else:
    print('Сериал снять не удастся')


# Решения через множества
# n = int(input())
# langs = set(input().split(', '))
#
# for _ in range(n - 1):
#     langs &= set(input().split(', '))
#
# if langs:
#     print(*sorted(langs), sep=', ')
# else:
#     print('Фильм снять не удастся')
