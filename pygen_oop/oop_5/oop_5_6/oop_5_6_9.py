class Calculator:
    def __call__(self, a, b, operation):
        try:
            return eval(f'{a}{operation}{b}')
        except ZeroDivisionError:
            raise ValueError('Деление на ноль невозможно')
