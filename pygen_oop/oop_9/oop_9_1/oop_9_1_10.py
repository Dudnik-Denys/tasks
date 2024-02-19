from random import randint


class Game:
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self._mining()

    def _mining(self):
        mines = self.mines

        while mines:
            i = randint(0, self.rows - 1)
            j = randint(0, self.cols - 1)
            if self.board[i][j].mine:
                continue
            self.board[i][j].mine = True
            mines -= 1

        indexes = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.rows):
            for y in range(self.cols):
                if not self.board[x][y].mine:
                    count = sum((self.board[x + i][y + j].mine for i, j in indexes if 0 <= x + i < self.rows and
                                 0 <= y + j < self.cols))
                    self.board[x][y].neighbours = count


class Cell:
    def __init__(self, row: int, col: int, mine: bool = False):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0


# game = Game(14, 18, 40)
#
# for line in game.board:
#     for cell in line:
#         print((cell.mine, cell.neighbours), end=' | ' if cell.mine else '| ')
#     print()
