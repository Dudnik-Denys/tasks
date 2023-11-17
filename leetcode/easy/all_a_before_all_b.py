def check_string(s: str) -> bool:
    return s.find('b') > s.rfind('a') if len(set(s)) > 1 else True
