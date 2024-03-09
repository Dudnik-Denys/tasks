import re
from functools import total_ordering


@total_ordering
class StringText:
    def __init__(self, words):
        self.lst_words = words[:]

    def __len__(self):
        return len(self.lst_words)

    def __gt__(self, other):
        if isinstance(other, StringText):
            return len(self) > len(other)

    def __eq__(self, other):
        if isinstance(other, StringText):
            return len(self) == len(other)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

res = [re.compile(r'[а-яА-Я-]+').findall(line) for line in stich]
lst_text = [StringText(line) for line in res]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(elem.lst_words) for elem in lst_text_sorted]
