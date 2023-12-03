text = input().lower().split()
edited_text = []

for word in text:
    for char in word:
        if char in '.,;:-?!':
            word = word.replace(char, '')
    edited_text.append(word)

print(len(set(edited_text)))


# words = [word.lower().strip('.,;:-?!') for word in input().split()]
#
# print(len(set(words)))
