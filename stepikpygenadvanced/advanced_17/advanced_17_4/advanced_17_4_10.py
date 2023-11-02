with open('input.txt', mode='r', encoding='utf-8') as input_file, \
     open('output.txt', mode='w', encoding='utf-8') as output_file:

    inp = [line for line in input_file.readlines()]

    for index, row in enumerate(inp, 1):
        output_file.write(str(index) + ') ' + row)