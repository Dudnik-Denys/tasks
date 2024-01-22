class Handler:
    def __init__(self, methods=('GET', )):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method in self.methods:
                return self.__getattribute__(method.lower())(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"
