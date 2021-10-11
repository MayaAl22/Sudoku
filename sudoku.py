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

def set_numbers_in_table():
    sudoku_table[0][3] = 8
    sudoku_table[0][5] = 7
    sudoku_table[1][1] = 1
    sudoku_table[1][4] = 9
    sudoku_table[1][7] = 8
    sudoku_table[2][3] = 3
    sudoku_table[2][4] = 4
    sudoku_table[2][5] = 1
    sudoku_table[3][1] = 3
    sudoku_table[3][2] = 8
    sudoku_table[3][6] = 7
    sudoku_table[3][7] = 9
    sudoku_table[4][0] = 9
    sudoku_table[4][8] = 1
    sudoku_table[5][1] = 6
    sudoku_table[5][2] = 1
    sudoku_table[5][6] = 8
    sudoku_table[5][7] = 4
    sudoku_table[6][3] = 4
    sudoku_table[6][4] = 5
    sudoku_table[6][5] = 9
    sudoku_table[7][0] = 7
    sudoku_table[7][2] = 4
    sudoku_table[7][3] = 1
    sudoku_table[7][5] = 3
    sudoku_table[7][6] = 6
    sudoku_table[7][8] = 5
    sudoku_table[8][1] = 8
    sudoku_table[8][3] = 7
    sudoku_table[8][5] = 2
    sudoku_table[8][7] = 1

set_numbers_in_table()

print_grid()
