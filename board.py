class newBoard:
    def __init__(self, rows: int = 3, columns : int = 2, length: tuple = (7, 1), pad = 0):
        #the ratio of x_length : y_length is 7:1
        self.placeholder = 0
        self.pad = pad
        self.rows = rows
        self.x_length, self.y_length = length
        self.columns = columns
        self.column_char = '|'
        self.dash = '-'
        self.intersect = '+'
        self.space = ' ' * self.x_length
        self.pad_symbol = ' '
        self.board = [[self.placeholder for _ in range(self.columns)]  for _ in range(self.rows)]
        values = [(i, j) for i, row in enumerate(self.board) for j, _ in enumerate(row)]
        self.place_to_index = {key+1 : value for key, value in enumerate(values)}

        def place_list(rows, columns):
            result = []
            counter = 1
            for i in range(rows):
                row = []
                for j in range(columns):
                    row.append(counter)
                    counter += 1
                result.append(row)
            return result
        
        self.place_list = place_list(self.rows, self.columns)

    def column_with_values(self, row: list) -> str:
        string = ''
        for value in row:
            diff = self.x_length - len(str(value))
            if len(str(value)) % 2 != 0 and self.x_length % 2 != 0 or len(str(value)) % 2 == 0 and self.x_length % 2 == 0: 
                pad = (diff // 2, diff // 2)
            else:
                pad = (diff // 2, (diff // 2) + 1)
            string += f'{self.column_char}{self.pad_symbol * pad[0]}{value}{self.pad_symbol * pad[1]}'
        return string + self.column_char
    
    def display_board(self) -> None:
        result = ''
        dashes = self.intersect + (self.dash * (self.x_length))
        line = (dashes * self.columns) + self.intersect
        column = ((self.column_char + self.space) * self.columns) + self.column_char
        for number_line in self.place_list:
            for value in [line, self.column_with_values(number_line)]:
                result += (self.pad_symbol  * self.pad) + value + '\n'
                if self.y_length > 0:
                    result += (self.pad_symbol * self.pad) + ((column + '\n') * (self.y_length-1)) + column + '\n'
        result += (self.pad_symbol * self.pad) + line + '\n'
        print(result, end="\r")