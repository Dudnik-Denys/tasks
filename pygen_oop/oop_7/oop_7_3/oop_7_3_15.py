class FuzzyString(str):
    def __eq__(self, other):
        if issubclass(type(other), str):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if issubclass(type(other), str):
            return self.lower() != other.lower()
        return NotImplemented

    def __ge__(self, other):
        if issubclass(type(other), str):
            return self.lower() >= other.lower()
        return NotImplemented

    def __le__(self, other):
        if issubclass(type(other), str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __lt__(self, other):
        if issubclass(type(other), str):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):
        if issubclass(type(other), str):
            return self.lower() > other.lower()
        return NotImplemented

    def __contains__(self, item):
        return item.lower() in super().__str__().lower()
