class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper():
            result = [self.render(elem) for elem in func().split()]
            return result
        return wrapper


class RenderDigit:
    def __call__(self, num, *args, **kwargs):
        try:
            return int(num)
        except ValueError:
            return None


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
