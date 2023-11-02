words_lst = [input().split() for _ in range(int(input()))]
words_dct = {word[0]: word[1] for word in words_lst}
data = input()

for key, value in words_dct.items():
    if key == data:
        print(value)
        break
    elif value == data:
        print(key)
        break

# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])
