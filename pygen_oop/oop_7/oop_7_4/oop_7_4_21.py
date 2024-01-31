class ValueDict(dict):
    def key_of(self, value):
        for key in self:
            if value == self[key]:
                return key

    def keys_of(self, value):
        result = ()
        for key in self:
            if value == self[key]:
                result += (key, )
        return result
