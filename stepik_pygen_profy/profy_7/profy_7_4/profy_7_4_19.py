def get_id(names: list, name: str) -> int:
    try:
        if not isinstance(name, str):
            raise TypeError

        if name.isalpha() and name.istitle():
            return len(names) + 1
        else:
            raise ValueError
    except ValueError:
        return ValueError('Имя не является корректным')
    except TypeError:
        return TypeError('Имя не является строкой')
