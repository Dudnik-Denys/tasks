class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])

        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng)

    def translate(self, eng):
        return self.tr.get(eng)

tr = Translator()
words = (('tree', 'дерево'), ('car', 'машина'), ('car', 'автомобиль'), ('leaf', 'лист'), ('river', 'река'),
         ('go', 'идти'), ('go', 'ехать'), ('go', 'ходить'), ('milk', 'молоко'))

for pair in words:
    en, ru = pair
    tr.add(en, ru)

tr.remove('car')
print(*tr.translate('go'))
