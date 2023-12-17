class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    @staticmethod
    def get_char() -> str:
        return 'N'

    def can_move(self, x, y) -> bool:
        return (ord(self.horizontal) - ord(x)) ** 2 + (self.vertical - y) ** 2 == 5

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal, self.vertical = x, y

    def draw_board(self):
        for v in range(8, 0, -1):
            for h in 'abcdefgh':
                if self.horizontal == h and self.vertical == v:
                    print(self.get_char(), end='')
                elif self.can_move(h, v):
                    print('*', end='')
                else:
                    print('.', end='')
            print()
