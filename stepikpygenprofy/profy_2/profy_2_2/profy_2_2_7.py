# w = input()
# n = int(input())
# data = [input() for _ in range(n)]
# glas = 0
#
# for char in w:
#     if char in 'ауоыиэяюёе':
#         glas += 1
#
# for word in data:
#
#     count = 0
#     for i in range(len(word)):
#         try:
#             if word[i] in 'ауоыиэяюёе' and w[i] in 'ауоыиэяюёе':
#                 count += 1
#             elif word[i] in 'ауоыиэяюёе' and w[i] not in 'ауоыиэяюёе':
#                 count -= 1
#         except IndexError:
#             pass
#
#     if count == glas:
#         print(word)


# Гениальное решение автора курса
# vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)
