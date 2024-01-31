class LowerString(str):
    def __new__(cls, obj='', *args, **kwargs):
        instance = super().__new__(cls, str(obj).lower(), *args, **kwargs)
        return instance
