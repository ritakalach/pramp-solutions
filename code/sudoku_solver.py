"""
Sudoku Solver

Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. 
Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards 
that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, 
which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. 
No need to return the actual numbers that make up a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space. 
The function should fill the blank spaces with characters such that the following rules apply:
  1) In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
  2) In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
  3) In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.

A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. 
If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).

"""

# O(9^(n*n)) time
# O(1) space
def sudoku_solve(board):
  # Find an empty cell
  i, j = find_empty_cell(board)
  if i is None:
    return True # no empty cells means we solved the sudoku
  
  # Fill empty cell with a number between 1-9
  for guess in range(1, 10):
    # Check that our guess is a valid number that won't break game rules
    if is_valid(board, guess, i, j):
      # Fill empty cell with the number we guessed
      board[i][j] = guess
      # Fill the next empty cell
      if sudoku_solve(board): # return True if there are no more empty cells
        return True
      board[i][j] = "." # backtrack
  
  # Return False if we can't fill empty cell with a valid number
  return False


def find_empty_cell(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == ".":
        return i, j
  return None, None


def is_valid(board, guess, i, j):
  # Check that the number guessed doesn't already appear in current row i
  for num in board[i]:
    if num != "." and guess == int(num):
      return False
  
  # Check that it doesn't appear in current column j
  for row in range(9):
    num = board[row][j]
    if num != "." and guess == int(num):
      return False
    
  # Check each 3x3 sub-board
  row_start = i // 3 * 3
  col_start = j // 3 * 3
  for row in range(row_start, row_start + 3):
    for col in range(col_start, col_start + 3):
      num = board[row][col]
      if num != "." and guess == int(num):
        return False
  
  # This is a valid guess
  return True
