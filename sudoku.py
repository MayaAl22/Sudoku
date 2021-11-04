class grid:
    _region_size_width = 0
    _region_size_height = 0
    _grid = []
    
    def __init__(self, size):
        # determine region size and save in attribute
        if size == 4:
            self._region_size_width = 2
            self._region_size_height = 2
        elif size == 6:
            self._region_size_width = 3
            self._region_size_height = 2
        elif size == 9:
            self._region_size_width = 3
            self._region_size_height = 3

        # create grid
        for row in range(size):
            self._grid.append([])
            for _ in range(size):
                self._grid[row].append(None)
        self._set_values()
    
    def _set_values(self):
        if len(self._grid) == 4:
            self._grid[0][0] = 3
            self._grid[0][1] = 4
            self._grid[0][2] = 1
            self._grid[1][1] = 2
            self._grid[2][2] = 2
            self._grid[3][1] = 1
            self._grid[3][2] = 4
            self._grid[3][3] = 3
        elif len(self._grid) == 6:
            self._grid[0][2] = 6
            self._grid[0][4] = 3
            self._grid[1][0] = 3
            self._grid[1][1] = 1
            self._grid[1][2] = 4
            self._grid[1][4] = 2
            self._grid[2][2] = 5
            self._grid[2][3] = 1
            self._grid[2][4] = 4
            self._grid[2][5] = 3
            self._grid[3][0] = 1
            self._grid[3][1] = 4
            self._grid[3][2] = 3
            self._grid[3][3] = 2
            self._grid[4][1] = 3
            self._grid[4][3] = 5
            self._grid[4][4] = 6
            self._grid[4][5] = 2
            self._grid[5][1] = 6
            self._grid[5][3] = 3
        elif len(self._grid) == 9:
            self._grid[0][3] = 8
            self._grid[0][5] = 7
            self._grid[1][1] = 1
            self._grid[1][4] = 9
            self._grid[1][7] = 8
            self._grid[2][3] = 3
            self._grid[2][4] = 4
            self._grid[2][5] = 1
            self._grid[3][1] = 3
            self._grid[3][2] = 8
            self._grid[3][6] = 7
            self._grid[3][7] = 9
            self._grid[4][0] = 9
            self._grid[4][8] = 1
            self._grid[5][1] = 6
            self._grid[5][2] = 1
            self._grid[5][6] = 8
            self._grid[5][7] = 4
            self._grid[6][3] = 4
            self._grid[6][4] = 5
            self._grid[6][5] = 9
            self._grid[7][0] = 7
            self._grid[7][2] = 4
            self._grid[7][3] = 1
            self._grid[7][5] = 3
            self._grid[7][6] = 6
            self._grid[7][8] = 5
            self._grid[8][1] = 8
            self._grid[8][3] = 7
            self._grid[8][5] = 2
            self._grid[8][7] = 1
    
    def print(self):
        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # print value
                if self._grid[row][column] == None:
                    print(".", end=" ")
                else:
                    print(self._grid[row][column], end=" ")
                # print vertical line
                if column > 0 and column < len(self._grid[row])-1 and (column+1) % self._region_size_width == 0:
                    print("|", end=" ")
            print()
            # print horizontal line
            if row > 0 and row < len(self._grid)-1 and (row+1) % self._region_size_height == 0:
                print("--" * (len(self._grid) + int(len(self._grid) / self._region_size_width) - 1))

    def erase(self, row, column):
        self._grid[row][column] = None

    def set(self, row, column, chosenNumber):
        sudoku_table_column = []
        for loop_row in self._grid:
            sudoku_table_column.append(loop_row[column])

        if chosenNumber in self._grid[row]:
            print("Number already exists in row")
        elif chosenNumber in sudoku_table_column:
            print("Number already exists in column")
        else:
            self._grid[row][column] = chosenNumber
        
    def is_won(self):
        for row in self._grid:
            for column in row:
                if column == None:
                    return False
        return True

def choose_grid_size():
    size = 0
    while not (size == 4 or size == 6 or size == 9):
        size = int(input("Choose Sudoku size (4 / 6 / 9): "))
    return size

def choose_ee():
    answer = ""
    while not answer in ["enter", "erase"]:
        answer = input("Would you enter or erase a number? ")
    return answer

def choose_rc():
    row = 0
    column = 0

    while not (row >= 1 and row <= 9):
        row = int(input("What row (1-9)? "))

    while not (column >= 1 and column <= 9):
        column = int(input("What column (1-9)? "))
    return row - 1, column - 1

def choose_number():
    chooseNumber = 0
    while not (chooseNumber >= 1 and chooseNumber <= 9):
        chooseNumber = int(input("Please enter a number: "))
    return chooseNumber

size = choose_grid_size()
my_grid = grid(size)
my_grid.print()

while True:
    answer = choose_ee()
    row, column = choose_rc()
    if answer == "erase":
        my_grid.erase(row, column)
    elif answer == "enter":
        chooseNumber = choose_number()
        my_grid.set(row, column, chooseNumber)

    if my_grid.is_won():
        print("Game won!")
        break
    my_grid.print()
    