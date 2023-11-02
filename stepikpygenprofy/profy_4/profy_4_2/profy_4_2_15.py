import csv


def csv_columns(filename: str) -> dict:
    data = {}
    with open(filename, encoding='utf-8') as csv_file:
        reader = list(csv.reader(csv_file, delimiter=','))
        columns = reader[0]

        for column in range(len(columns)):
            for elem in range(len(reader[1:])):
                if columns[column] not in data:
                    data[columns[column]] = [reader[elem + 1][column]]
                else:
                    data[columns[column]].append(reader[elem + 1][column])

    return data


# Cool solution
# import csv
#
# def csv_columns(filename):
#     with open(filename, encoding='utf-8') as file:
#         rows = csv.DictReader(file)
#         my_dict = {}
#         for row in rows:
#             for key, value in row.items():
#                 my_dict.setdefault(key, []).append(value)
#         return my_dict
