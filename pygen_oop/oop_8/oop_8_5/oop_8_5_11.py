def add_attr_to_class(**attrs):
    def decorator(cls):
        for key, value in attrs.items():
            setattr(cls, key, value)
        return cls
    return decorator
