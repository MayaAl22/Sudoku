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
