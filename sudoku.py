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

def erase(row, column):
    sudoku_table[row][column] = None

def set(row, column, chosenNumber):
    sudoku_table_column = []
    for loop_row in sudoku_table:
        sudoku_table_column.append(loop_row[column])

    if chosenNumber in sudoku_table[row]:
        print("Number already exists in row")
    elif chosenNumber in sudoku_table_column:
        print("Number already exists in column")
    else:
        sudoku_table[row][column] = chosenNumber  

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

def game_won():
    for row in sudoku_table:
        for column in row:
            if column == None:
                return False
    return True

set_numbers_in_table()

print_grid()

while True:
    answer = choose_ee()
    row, column = choose_rc()
    if answer == "erase":
        erase(row, column)
    elif answer == "enter":
        chooseNumber = choose_number()
        set(row, column, chooseNumber)

    if game_won():
        print("Game won!")
        break
    print_grid()
    