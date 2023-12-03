import csv


def condense_csv(filename: str, id_name: str):
    condense_dict = {}

    with open(filename, encoding='utf-8') as non_condensed_file:
        reader = csv.reader(non_condensed_file)

        for line in reader:
            if line[0] not in condense_dict:
                condense_dict[line[0]] = {line[1]: line[2]}
            else:
                condense_dict[line[0]].update({line[1]: line[2]})

    columns = [id_name]

    for x in condense_dict:
        for key in condense_dict[x].keys():
            columns.append(key)
        break

    with open('condensed.csv', 'w', encoding='utf-8') as condensed_file:
        writer = csv.DictWriter(condensed_file, fieldnames=columns)
        writer.writeheader()

        for x in condense_dict:
            column = 1
            line = {columns[0]: x}
            for value in condense_dict[x].values():
                line.update({columns[column]: value})
                column += 1
            writer.writerow(line)


condense_csv('simply_than_look.csv', 'ID')
