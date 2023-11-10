def remove_marks(text: str, marks: str = ''):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.__dict__['count'] += 1

    for symbol in text:
        text = text.replace(symbol, '') if symbol in marks else text

    return text
