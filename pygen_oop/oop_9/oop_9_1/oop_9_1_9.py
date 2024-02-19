class TicTacToe:
    def __init__(self):
        self._field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self._turn = 1
        self._marker = 'X'

    def mark(self, row, column):
        winner = self.winner()
        if self._turn > 9 or winner is not None:
            print('Игра окончена')
        else:
            if winner is not None:
                return winner
            elif self._field[row - 1][column - 1] == ' ':
                self._field[row - 1][column - 1] = self._marker
                self._turn += 1
                self._marker = 'X' if self._turn % 2 else 'O'
            else:
                print('Недоступная клетка')

    def winner(self):
        result = None
        main_diagonal_validator = [self._field[0][0], self._field[1][1], self._field[2][2]]
        side_diagonal_validator = [self._field[0][2], self._field[1][1], self._field[0][0]]
        for i in range(3):
            rows_validator = []
            columns_validator = []
            for j in range(3):
                rows_validator.append(self._field[i][j])
                columns_validator.append(self._field[j][i])
            if all(x == 'O' for x in rows_validator) or all(x == 'O' for x in columns_validator):
                result = 'O'
            elif all(x == 'X' for x in rows_validator) or all(x == 'X' for x in columns_validator):
                result = 'X'
        if all(x == 'O' for x in main_diagonal_validator) or all(x == 'O' for x in side_diagonal_validator):
            result = 'O'
        elif all(x == 'X' for x in side_diagonal_validator) or all(x == 'X' for x in main_diagonal_validator):
            result = 'X'
        elif self._turn > 9:
            result = 'Ничья'
        return result

    def show(self):
        result = []
        for row in self._field:
            result.append('|'.join(row))
            result.append('-----')
        [print(line) for line in result[:-1]]
