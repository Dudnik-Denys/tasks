class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if ('method' in request and request['method'] == 'GET') or 'method' not in request:
            return f"GET: {self.func(request)}"
