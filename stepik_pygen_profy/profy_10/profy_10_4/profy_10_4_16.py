class Alphabet:
    def __init__(self, language: str):
        self.languages = {'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                          'ru': ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]}

        self.language = self.languages[language]
        self.iterable = iter(self.language)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterable)
        except StopIteration:
            self.iterable = iter(self.language)
            return next(self.iterable)
