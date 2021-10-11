sudoku_table = [
    [None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
    ]

def print_grid():
    for row in range(9):
        for column in range(9):
            if sudoku_table[row][column] == None:
                print(".", end=" ")
            else:
                print(sudoku_table[row][column], end=" ")
            if column == 2 or column == 5:
                print("|", end=" ")
        print("")
        if row == 2 or row == 5:
            print("------+-------+------")

print_grid()
