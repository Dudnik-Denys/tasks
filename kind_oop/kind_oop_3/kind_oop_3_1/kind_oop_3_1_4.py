class Book:
    ATTRS = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setitem__(self, key, value):
        if key in self.ATTRS and self.ATTRS[key] == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
