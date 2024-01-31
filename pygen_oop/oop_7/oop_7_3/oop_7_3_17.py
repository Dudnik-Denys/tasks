class SuperInt(int):
    def repeat(self, n=2):
        res = ''
        for i in range(1, n + 1):
            if i == 1:
                res += f'{super().real}'
            else:
                res += f'{abs(super().real)}'
        return SuperInt(int(res))

    def to_bin(self):
        return f'{super().real:b}'

    def next(self):
        return SuperInt(super().real + 1)

    def prev(self):
        return SuperInt(super().real - 1)

    def __iter__(self):
        yield from [SuperInt(num) for num in str(super().real) if num.isdigit()]
