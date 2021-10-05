# Sudoku

"Sudoku is a logic-based, combinatorial number-placement puzzle." - Wikipedia

## Grid

- The grid has a square shape and is divided into 64 (9x9) boxes.
- The columns and rows of the grid are enumerated with letters on the top and numbers on the left side.

## Gameflow

- The game starts with preset numbers in the grid. Randomization of the numbers at each start of the game is an optional feature and may not be implemented.
- The game provides an input to the user to erase, or place a number in the grid.
- The input of a number must be checked if it is valid, for column and row, before saving it in the grid.
- The game must check after each valid input if the game is won.
- Numbers which are present in the grid, at the start of the game, are not erasable.

## Technical

- The game is terminal-based and has no graphical UI components.
