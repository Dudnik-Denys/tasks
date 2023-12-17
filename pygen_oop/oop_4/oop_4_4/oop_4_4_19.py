class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not (isinstance(new_name, str) and new_name.isalpha() and new_name):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not (type(new_age) == int and (0 <= new_age <= 110)):
            raise ValueError('Некорректный возраст')
        self._age = new_age
