import re


def normalize_jpeg(filename: str) -> str:
    return re.sub(r"jpe?g$", "jpg", filename, flags=re.I)
