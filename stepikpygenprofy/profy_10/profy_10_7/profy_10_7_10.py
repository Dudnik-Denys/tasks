def nonempty_lines(file: str):
    with open(file, encoding='utf-8') as txt_file:
        data = (line.strip() for line in txt_file.readlines())
        yield from (row if len(row) <= 25 else '...' for row in data if row)
