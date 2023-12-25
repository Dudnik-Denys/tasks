import re


class Strip:
    def __init__(self, chars):
        chars = re.escape(chars)
        chars = f"[{chars}]*"
        self._pattern = re.compile(f"^{chars}(.*?){chars}$")

    def __call__(self, string):
        return self._pattern.search(string).group(1)
