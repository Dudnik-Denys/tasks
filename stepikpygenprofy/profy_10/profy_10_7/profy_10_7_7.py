def filter_names(names: list[str], ignore_char: str, max_names: int):
    ignore_lower_char = filter(lambda x: x[0].lower() != ignore_char.lower(), names)
    ignore_upper_char = filter(lambda x: x[0].upper() != ignore_char.upper(), ignore_lower_char)
    ignore_digits = filter(lambda x: x.isalpha(), ignore_upper_char)
    for _ in range(max_names):
        try:
            yield next(ignore_digits)
        except StopIteration:
            return
