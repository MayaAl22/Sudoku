class Preset:
    def __init__(self, number):
        self._value = number
    
    def get_value(self):
        return self._value

class Inserted:
    def __init__(self, number):
        self._value = number
    
    def get_value(self):
        return self._value

class Empty:
    def __init__(self):
        self._value = None
    
    def get_value(self):
        return self._value

class Grid:
    def __init__(self, region_height, region_width):
        self._region_height = region_height
        self._region_width = region_width

        # create grid
        self._grid = []
        for row in range(self._region_height * self._region_width):
            self._grid.append([])
            for _ in range(self._region_height * self._region_width):
                self._grid[row].append(Empty())
        self._set_values()
    
    def _set_values(self):
        if len(self._grid) == 4:
            self._grid[0][0] = Preset(3)
            self._grid[0][1] = Preset(4)
            self._grid[0][2] = Preset(1)
            self._grid[1][1] = Preset(2)
            self._grid[2][2] = Preset(2)
            self._grid[3][1] = Preset(1)
            self._grid[3][2] = Preset(4)
            self._grid[3][3] = Preset(3)
        elif len(self._grid) == 6:
            self._grid[0][2] = Preset(6)
            self._grid[0][4] = Preset(3)
            self._grid[1][0] = Preset(3)
            self._grid[1][1] = Preset(1)
            self._grid[1][2] = Preset(4)
            self._grid[1][4] = Preset(2)
            self._grid[2][2] = Preset(5)
            self._grid[2][3] = Preset(1)
            self._grid[2][4] = Preset(4)
            self._grid[2][5] = Preset(3)
            self._grid[3][0] = Preset(1)
            self._grid[3][1] = Preset(4)
            self._grid[3][2] = Preset(3)
            self._grid[3][3] = Preset(2)
            self._grid[4][1] = Preset(3)
            self._grid[4][3] = Preset(5)
            self._grid[4][4] = Preset(6)
            self._grid[4][5] = Preset(2)
            self._grid[5][1] = Preset(6)
            self._grid[5][3] = Preset(3)
        elif len(self._grid) == 9:
            self._grid[0][3] = Preset(8)
            self._grid[0][5] = Preset(7)
            self._grid[1][1] = Preset(1)
            self._grid[1][4] = Preset(9)
            self._grid[1][7] = Preset(8)
            self._grid[2][3] = Preset(3)
            self._grid[2][4] = Preset(4)
            self._grid[2][5] = Preset(1)
            self._grid[3][1] = Preset(3)
            self._grid[3][2] = Preset(8)
            self._grid[3][6] = Preset(7)
            self._grid[3][7] = Preset(9)
            self._grid[4][0] = Preset(9)
            self._grid[4][8] = Preset(1)
            self._grid[5][1] = Preset(6)
            self._grid[5][2] = Preset(1)
            self._grid[5][6] = Preset(8)
            self._grid[5][7] = Preset(4)
            self._grid[6][3] = Preset(4)
            self._grid[6][4] = Preset(5)
            self._grid[6][5] = Preset(9)
            self._grid[7][0] = Preset(7)
            self._grid[7][2] = Preset(4)
            self._grid[7][3] = Preset(1)
            self._grid[7][5] = Preset(3)
            self._grid[7][6] = Preset(6)
            self._grid[7][8] = Preset(5)
            self._grid[8][1] = Preset(8)
            self._grid[8][3] = Preset(7)
            self._grid[8][5] = Preset(2)
            self._grid[8][7] = Preset(1)
    
    def _number_in_row_column(self, row, column, number):
        # check row
        if number in [ field.get_value() for field in self._grid[row] ]:
            return True
        # check column
        elif number in [ row[column].get_value() for row in self._grid ]:
            return True
        else:
            return False
    
    def print(self):
        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # print value
                if isinstance(self._grid[row][column], Empty):
                    print(".", end=" ")
                else:
                    print(self._grid[row][column].get_value(), end=" ")
                # print vertical line
                if column > 0 and column < len(self._grid[row])-1 and (column+1) % self._region_width == 0:
                    print("|", end=" ")
            print()
            # print horizontal line
            if row > 0 and row < len(self._grid)-1 and (row+1) % self._region_height == 0:
                print("--" * (len(self._grid) + int(len(self._grid) / self._region_width) - 1))

    def erase_field(self, row, column):
        if isinstance(self._grid[row][column], Preset):
            print("Field has preset number")
        elif isinstance(self._grid[row][column], Empty):
            print("Field is empty")
        else:
            self._grid[row][column] = Empty()

    def set_field(self, row, column, number):
        if self._number_in_row_column(row, column, number):
            print("Number already exists in row or column")
        else:
            self._grid[row][column] = Inserted(number)
        
    def is_won(self):
        for row in self._grid:
            for field in row:
                if isinstance(field, Empty):
                    return False
        return True

def choose_grid_size():
    size = 0
    while not size in [4, 6, 9]:
        size = int(input("Choose Sudoku size (4 / 6 / 9): "))
    
    region_height = 0
    region_width = 0
    if size == 4:
        region_height = 2
        region_width = 2
    elif size == 6:
        region_height = 2
        region_width = 3
    elif size == 9:
        region_height = 3
        region_width = 3

    return (region_height, region_width)

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

def main():
    (region_height, region_width) = choose_grid_size()
    grid = Grid(region_height, region_width)
    grid.print()

    while True:
        answer = choose_ee()
        row, column = choose_rc()
        if answer == "erase":
            grid.erase_field(row, column)
        elif answer == "enter":
            chooseNumber = choose_number()
            grid.set_field(row, column, chooseNumber)

        if grid.is_won():
            print("Game won!")
            break
        grid.print()

if __name__ == "__main__":
    main()
