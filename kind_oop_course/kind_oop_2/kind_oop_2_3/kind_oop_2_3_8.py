class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]


class RegisterForm:
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')
