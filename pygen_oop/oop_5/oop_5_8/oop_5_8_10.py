class Ord:
    def __getattr__(self, name):
        return ord(name)
