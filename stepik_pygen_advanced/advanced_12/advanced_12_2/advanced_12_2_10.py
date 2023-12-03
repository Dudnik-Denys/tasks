import random

word = [char for char in input()]
random.shuffle(word)
print(''.join(word))
