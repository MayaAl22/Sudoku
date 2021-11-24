class Preset:
    """A class to represent a preset number field in a region object"""

    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        return self._value

class Inserted:
    """A class to represent an inserted number field in a region object"""

    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        return self._value

class Empty:
    """A class to represent an empty field in a region object"""

    def __init__(self):
        self._value = None
    
    def get_value(self):
        return self._value

class Region:
    """A class to represent a region in a Sudoku grid"""

    def __init__(self, height, width):
        """Constructs a region with given height and width"""

        self._region = [ [ Empty() for _ in range(width) ] for _ in range(height) ]
    
    def get_column(self, index):
        """Returns the values of a column"""

        column = []

        for row in self._region:
            column.append(row[index])

        return column
    
    def get_region(self):
        """Returns the values of a region"""

        region = []

        for row in self._region:
            for element in row:
                region.append(element)

        return region
    
    def get_row(self, index):
        """Returns the values of a row"""

        return self._region[index]

    def set_field(self, row_index, column_index, value):
        """Sets a value of a field"""

        if isinstance(self._region[row_index][column_index], Empty):
            self._region[row_index][column_index] = Inserted(value)
        elif isinstance(self._region[row_index][column_index], Preset):
            raise ValueError("Field has preset number")
        elif isinstance(self._region[row_index][column_index], Inserted):
            raise ValueError("Field already has a number")
    
    def erase_field(self, row_index, column_index):
        """Sets an empty value on a field"""

        if isinstance(self._region[row_index][column_index], Inserted):
            self._region[row_index][column_index] = Empty()
        elif isinstance(self._region[row_index][column_index], Preset):
            raise ValueError("Field has preset number")
        elif isinstance(self._region[row_index][column_index], Empty):
            raise ValueError("Field is empty")
    
class Grid:
    """A class to represent a the Sudoku grid"""

    def __init__(self, height, width):
        """Constructs a region with given height and width"""

        self._height = height
        self._width = width

        self._grid = [ [ Region(self._height, self._width) for _ in range(self._height) ] for _ in range(self._width) ]
        self._set_values()
    
    def _set_values(self):
        """Writes prior defined numbers (4x4 6x6 9x9 grid) to the grid"""
        
        if self._height == 2 and self._width == 2:
            self._grid[0][0]._region[0][0] = Preset(3)
            self._grid[0][0]._region[0][1] = Preset(4)
            self._grid[0][1]._region[0][0] = Preset(1)
            self._grid[0][0]._region[1][1] = Preset(2)
            self._grid[1][1]._region[0][0] = Preset(2)
            self._grid[1][0]._region[1][1] = Preset(1)
            self._grid[1][1]._region[1][0] = Preset(4)
            self._grid[1][1]._region[1][1] = Preset(3)
        elif self._height == 2 and self._width == 3:
            self._grid[0][0]._region[0][2] = Preset(6)
            self._grid[0][1]._region[0][1] = Preset(3)
            self._grid[0][0]._region[1][0] = Preset(3)
            self._grid[0][0]._region[1][1] = Preset(1)
            self._grid[0][0]._region[1][2] = Preset(4)
            self._grid[0][1]._region[1][1] = Preset(2)
            self._grid[1][0]._region[0][2] = Preset(5)
            self._grid[1][1]._region[0][0] = Preset(1)
            self._grid[1][1]._region[0][1] = Preset(4)
            self._grid[1][1]._region[0][2] = Preset(3)
            self._grid[1][0]._region[1][0] = Preset(1)
            self._grid[1][0]._region[1][1] = Preset(4)
            self._grid[1][0]._region[1][2] = Preset(3)
            self._grid[1][1]._region[1][0] = Preset(2)
            self._grid[2][0]._region[0][1] = Preset(3)
            self._grid[2][1]._region[0][0] = Preset(5)
            self._grid[2][1]._region[0][1] = Preset(6)
            self._grid[2][1]._region[0][2] = Preset(2)
            self._grid[2][0]._region[1][1] = Preset(6)
            self._grid[2][1]._region[1][0] = Preset(3)
        elif self._height == 3 and self._width == 3:
            self._grid[0][1]._region[0][0] = Preset(8)
            self._grid[0][1]._region[0][2] = Preset(7)
            self._grid[0][0]._region[1][1] = Preset(1)
            self._grid[0][1]._region[1][1] = Preset(9)
            self._grid[0][2]._region[1][1] = Preset(8)
            self._grid[0][1]._region[2][0] = Preset(3)
            self._grid[0][1]._region[2][1] = Preset(4)
            self._grid[0][1]._region[2][2] = Preset(1)
            self._grid[1][0]._region[0][1] = Preset(3)
            self._grid[1][0]._region[0][2] = Preset(8)
            self._grid[1][2]._region[0][0] = Preset(7)
            self._grid[1][2]._region[0][1] = Preset(9)
            self._grid[1][0]._region[1][0] = Preset(9)
            self._grid[1][2]._region[1][2] = Preset(1)
            self._grid[1][0]._region[2][1] = Preset(6)
            self._grid[1][0]._region[2][2] = Preset(1)
            self._grid[1][2]._region[2][0] = Preset(8)
            self._grid[1][2]._region[2][1] = Preset(4)
            self._grid[2][1]._region[0][0] = Preset(4)
            self._grid[2][1]._region[0][1] = Preset(5)
            self._grid[2][1]._region[0][2] = Preset(9)
            self._grid[2][0]._region[1][0] = Preset(7)
            self._grid[2][0]._region[1][2] = Preset(4)
            self._grid[2][1]._region[1][0] = Preset(1)
            self._grid[2][1]._region[1][2] = Preset(3)
            self._grid[2][2]._region[1][0] = Preset(6)
            self._grid[2][2]._region[1][2] = Preset(5)
            self._grid[2][0]._region[2][1] = Preset(8)
            self._grid[2][1]._region[2][0] = Preset(7)
            self._grid[2][1]._region[2][2] = Preset(2)
            self._grid[2][2]._region[2][1] = Preset(1)
    
    def _get_column(self, index):
        """Returns the values of a column"""

        values = []
        grid_column = int(index / self._width)
        region_column = index % self._width

        for row in self._grid:
            column = row[grid_column].get_column(region_column)
            for element in column:
                values.append(element)

        return values

    def _get_region(self, row_index, column_index):
        """Returns the values of a region"""

        return self._grid[row_index][column_index].get_region()

    def _get_row(self, index):
        """Returns the values of a row"""

        values = []
        grid_row = int(index / self._height)
        region_row = index % self._height

        for region in self._grid[grid_row]:
            values.extend(region.get_row(region_row))
        return values
    
    def print(self):
        """Prints the values of the grid"""

        for row in range(self._height * self._width):
            for column in range(self._height * self._width):
                # print value
                if isinstance(self._get_row(row)[column], Empty):
                    print(".", end=" ")
                else:
                    print(self._get_row(row)[column].get_value(), end=" ")

                # print vertical line
                if column > 0 and column < (self._height * self._width - 1) and (column + 1) % self._width == 0:
                    print("|", end=" ")
            print()

            # print horizontal line
            if row > 0 and row < (self._height * self._width - 1) and (row + 1) % self._height == 0:
                print("--" * (self._height * self._width + int(self._height * self._width / self._width) - 1))

    def set_field(self, row_index, column_index, value):
        """Sets a value of a field"""

        grid_row = int(row_index / self._height)
        grid_column = int(column_index / self._width)

        region_row = row_index % self._height
        region_column = column_index % self._width

        row = [ element.get_value() for element in self._get_row(row_index) ]
        column = [ element.get_value() for element in self._get_column(column_index) ]
        region = [ element.get_value() for element in self._get_region(grid_row, grid_column) ]

        if value in row:
            raise ValueError("Value already exists in row")
        elif value in column:
            raise ValueError("Value already exists in column")
        elif value in region:
            raise ValueError("Value already exists in region")
        else:
            self._grid[grid_row][grid_column].set_field(region_row, region_column, value)
    
    def erase_field(self, row_index, column_index):
        """Sets an empty value on a field"""

        grid_row = int(row_index / self._height)
        grid_column = int(column_index / self._width)

        region_row = row_index % self._height
        region_column = column_index % self._width

        self._grid[grid_row][grid_column].erase_field(region_row, region_column)
        
    def is_won(self):
        """Returns true if the game is won, otherwise false"""
        for row_index in range(self._height * self._width):
            row = [ element.get_value() for element in self._get_row(row_index) ]

            if None in row:
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
            try:
                grid.erase_field(row, column)
            except ValueError as e:
                print("Error: {}".format(e))
        elif answer == "enter":
            chooseNumber = choose_number()
            try:
                grid.set_field(row, column, chooseNumber)
            except ValueError as e:
                print("Error: {}".format(e))

        if grid.is_won():
            print("Game won!")
            break
        grid.print()

if __name__ == "__main__":
    main()
