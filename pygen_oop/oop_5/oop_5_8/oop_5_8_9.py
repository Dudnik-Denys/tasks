class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)
