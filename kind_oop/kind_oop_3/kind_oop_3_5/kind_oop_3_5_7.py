class Morph:
    def __init__(self, *words):
        self.words = words

    def add_word(self, word):
        if word not in self.words:
            self.words += (word, )

    def get_words(self):
        return self.words

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self.words

    def __ne__(self, other):
        if isinstance(other, str):
            return other.lower() not in self.words


dict_words = [
    Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
    Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов',
          'векторам', 'векторами', 'векторах'),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты',
          'эффектов', 'эффектам', 'эффектами', 'эффектах'),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
    ]

text = input()

result = 0

for word in text.strip('?,.!-').lower().split():
    for morph in dict_words:
        if word in morph.get_words():
            result += 1
            break

print(result)
