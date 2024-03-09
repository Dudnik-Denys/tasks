class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)

    def remove_module(self, index):
        self.modules.pop(index)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, index):
        self.lessons.pop(index)


class LessonItem:
    _MAIN_ATTRS = ('title', 'practices', 'duration')

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if key == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in self._MAIN_ATTRS[1:] and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in self._MAIN_ATTRS[1:] and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item in self._MAIN_ATTRS:
            raise TypeError('Руки прочь, гнида')
        del item
