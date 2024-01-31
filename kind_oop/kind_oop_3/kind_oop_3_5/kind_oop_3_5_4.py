class Track:
    def __init__(self, start_x, start_y):
        self.track = (TrackLine(start_x, start_y, 0), )

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.track += (tr, )

    def get_tracks(self):
        return self.track[1:]

    def __len__(self):
        return int(sum(self._get_len(i) for i in range(1, len(self.track))))

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def _get_len(self, index):
        return ((self.track[index - 1].to_x - self.track[index].to_x) ** 2 + (self.track[index - 1].to_y - self.track[index].to_y) ** 2) ** .5


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
