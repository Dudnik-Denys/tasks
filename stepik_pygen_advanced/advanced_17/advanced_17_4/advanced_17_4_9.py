import random


def write_text_to_file():
    with open('random.txt', mode='w', encoding='utf-8') as file:
        for _ in range(25):
            sequance = random.randrange(111, 777)
            file.write(str(sequance) + '\n')


write_text_to_file()
