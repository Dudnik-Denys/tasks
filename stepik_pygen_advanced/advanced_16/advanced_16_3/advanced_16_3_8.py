from operator import sub, truediv, mul, add


def arithmetic_operation(operation):
    operations = {'+': add, '-': sub, '/': truediv, '*': mul}

    def inner(x, y):
        return operations[operation](x, y)

    return inner


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
