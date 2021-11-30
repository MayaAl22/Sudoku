# Sudoku

"Sudoku is a logic-based, combinatorial number-placement puzzle." - Wikipedia

## Features

### Grid

- The grid has a square shape and is defined by the region size (height of region * width of region).

### Gameflow

- The game starts with preset numbers in the grid.
- The game provides an input to the user to enter, or erase a number in the grid.
- An entered number is checked if it is valid, for the selected row, column, and region.
- Preset numbers are not erasable.
- The game checks after each valid input if the game is won.

### Technical

- The game is terminal-based and has no graphical UI components.

## Run the game

Please clone this repository and make sure you have a working installation of the Python interpreter, minimum version is 3.10. Please refer to the Python [website](https://www.python.org/downloads/), to learn more about how to download and install Python.

The game can be executed on the terminal with the command `python sudoku.py`.
If the current working directory is not the one of the closed repository a path to the `sudoku.py` file must be added.

## Tools for development

- Python 3 - Python in version 3 is the used interpreter for running the developed code.
- Git - Git is the used version control system, and also used to push the code to Github.
- Visual Studio Code - Visual Studio Code is used to develop the code. It has the "Python" and "Git Graph" extensions installed. The "Python" extension is used for syntax highlighting and "Git Graph" for looking at the Git commits.

## Technical implementation

The game uses five classes to represent the state of the game.

The main class `Grid` represents the grid of the Sudoku.
A grid has methods to construct, print, and set or erase fields on the grid.
The grid class divides the Sudoku grid in regions, which are stored in a multi-dimensional list inside.

The regions in a Sudoku grid is represented by the `Region` class.
A region has methods to construct, get rows and columns, and set or erase fields on the region.
The region class divides the Sudoku region in fields, which are stored in a multi-dimensional list inside.

The fields in a Sudoku region are represented by the `Preset`, `Inserted`, and `Empty` classes.
The `Preset` class represents a preset number, when the game starts.
The `Inserted` class represents a number which was entered by the user.
The `Empty` class represents an empty field.
Each of the field classes have a method to construct them, and return the value stored inside.
The classes `Preset` and `Inserted` return a stored integer value.
The class `Empty` returns a `None` value.

When the game starts an instance of the grid class is created, after asking the user for the grid sizes.
In the further course of the game the print, set, and erase methods are called to make changes to the state of the grid.
Each change to the grid checks if the change is valid under the Sudoku rules.

After each successful change, the game checks if the user won.
The game is won if the grid has no empty fields left.
