def capitalize_title(title: str) -> str:
    result = ''
    for word in title.split():
        result += word.capitalize() + ' ' if len(word) > 2 else word.lower() + ' '
    return result.strip()
