from board import newBoard

class tctct(newBoard):
    def __init__(self, rows: int = 3, columns: int = 3, length: tuple = (7, 1), pad = 0, marks: list = ['X', 'O']):
        super().__init__(rows, columns, length, pad)
        for mark in marks:
            assert len(mark) <= self.x_length, f'String selected to mark on the board is too long (max. {self.x_length} characters): {mark}'
        self.marks = marks

    def is_occupied(self, place: str) -> bool:
        if not place.isnumeric():
            return True
        x, y = self.place_to_index[int(place)]
        return self.board[x][y] in self.marks

    def choose(self, place: str, mark: str) -> None:
        if self.is_occupied(place):
            return None
        else:
            place = int(place)
            row, column = self.place_to_index[place]
            self.board[row][column] = mark  
            return not None

    def transpose(self, lst: list) -> list:
        return [[row[i] for row in lst] for i in range(len(lst[0]))]
    
    def check_values_equality(self, row):
        return all(element == row[0] for element in row) and row[0] != self.placeholder
    
    def check_diagonals(self):
        if len(self.board) != len(self.board[0]):
            return (False, None)
        upper_x, upper_y = (0, 0)
        lower_x, lower_y = (len(self.board)-1, 0)
        upper_ref = self.board[upper_x][upper_y]
        lower_ref = self.board[lower_x][lower_y]
        if upper_ref == self.placeholder and lower_ref == self.placeholder:
            return (False, None)
        upper_lst = []
        lower_lst = []
        for i in range(len(self.board)):
            upper_value = self.board[upper_x + i][upper_y + i]
            lower_value = self.board[lower_x - i][lower_y + i]
            if upper_ref != upper_value and lower_ref != lower_value:
                return (False, None)
            upper_lst.append(upper_value)
            lower_lst.append(lower_value)
        if self.check_values_equality(upper_lst):
            return (True, upper_ref)
        elif self.check_values_equality(lower_lst):
            return (True, lower_ref)
        return (False, None)
        
    def check_win(self) -> tuple:
        diagonal_win, mark = self.check_diagonals()
        if diagonal_win:
            return mark
        for row in self.board:
            if self.check_values_equality(row):
                return row[0]
        for column in self.transpose(self.board):
            if self.check_values_equality(column):
                return column[0]
        return False