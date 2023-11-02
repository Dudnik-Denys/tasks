s = input()


def write_text_to_file(text: str):
    with open('output.txt', mode='w', encoding='utf-8') as file:
        file.write(text)


write_text_to_file(s)
