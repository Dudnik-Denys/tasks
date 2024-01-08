from random import choice


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.init(self.N, self.M)

    def show(self):
        for line in self.pole:
            temp = ''
            for cell in line:
                if cell.mine:
                    temp += '* '
                elif not cell.fl_open:
                    temp += '# '
                else:
                    temp += str(cell.around_mines) + ' '
            print(temp.strip())

    @staticmethod
    def init(size, mines):
        total_sizing = size ** 2
        result = []

        for line in range(size):
            temp = []
            for cell in range(size):
                if mines >= total_sizing and mines > 0:
                    temp.append(Cell(mine=True, fl_open=True))
                    total_sizing -= 1
                    mines -= 1
                elif mines > 0:
                    c = Cell(mine=choice([False, False, False, True, False, False, False]))
                    temp.append(c if c.mine else Cell(fl_open=choice([True, False])))
                    total_sizing -= 1
                    mines = mines - 1 if c.mine else mines
                else:
                    temp.append(Cell(fl_open=choice([True, False])))
                    total_sizing -= 1
            result.append(temp)

        look_around = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        for i in range(size):
            for j in range(size):
                if not result[i][j].mine:
                    mines_around = sum([result[i + x][j + y].mine for x, y in look_around if 0 <= i + x < size and
                                       0 <= j + y < size])
                    result[i][j].around_mines = mines_around
        return result


pole_game = GamePole(10, 12)
pole_game.show()
