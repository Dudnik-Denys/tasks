class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str):
        self.topic = topic
        self.start_time = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
        self.duration = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
        self.end_time = self.start_time + self.duration


class Conference:
    def __init__(self):
        self._conference = []

    def add(self, lecture: Lecture):
        validator = all([lecture.start_time >= elem.end_time or lecture.end_time <= elem.start_time for
                         elem in self._conference])
        if not validator:
            raise ValueError('Провести выступление в это время невозможно')
        self._conference.append(lecture)

    def total(self):
        return self._format_time(sum(lecture.duration for lecture in self._conference))

    def longest_lecture(self):
        return self._format_time(max(lecture.duration for lecture in self._conference))

    def longest_break(self):
        result = 0
        if len(self._conference) > 1:
            conference = sorted(self._conference, key=lambda lec: lec.start_time)
            for lecture in range(len(conference) - 1):
                temp = abs(conference[lecture].end_time - conference[lecture + 1].start_time)
                result = temp if temp > result else result
        return self._format_time(result)

    @staticmethod
    def _format_time(time: int):
        hours = time // 60
        minutes = time - (hours * 60)
        return f'{hours:02}:{minutes:02}'
