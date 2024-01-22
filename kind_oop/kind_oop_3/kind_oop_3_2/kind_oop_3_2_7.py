class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        self._type_list = value if value in ['ul', 'ol'] else 'ul'

    def __call__(self, lst):
        result = f'<{self._type_list}>\n'

        for elem in lst:
            result += f'<li>{elem}</li>\n'

        result += f'</{self._type_list}>'
        return result
