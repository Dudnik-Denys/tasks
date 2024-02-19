class Testpaper:
    def __init__(self, subject: str, grades: list[str], minimal_rate: str):
        self.subject = subject
        self.grades = grades
        self.minimal_rate = minimal_rate


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test: Testpaper, grades: list[str]):
        if isinstance(self.tests_taken, str):
            self.tests_taken = {}
        correct_answers = sum([test.grades[i] == grades[i] for i in range(len(grades))])
        percent = round(correct_answers / (len(grades) / 100))
        result = f'Passed! ({percent}%)' if percent >= int(test.minimal_rate[:-1]) else f'Failed! ({percent}%)'
        self.tests_taken.update({test.subject: result})
