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
    
class Grid:
    """A class to represent a the Sudoku grid"""

    def __init__(self, height, width):
        """Constructs a region with given height and width"""

        self._height = height
        self._width = width

        self._grid = [ [ Region(self._height, self._width) for _ in range(self._height) ] for _ in range(self._width) ]
        self._set_values()
    
    def _set_values(self):
        pass
    
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

    def erase_field(self, row, column):
        pass

    def set_field(self, row, column, number):
        pass
        
    def is_won(self):
        pass

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
