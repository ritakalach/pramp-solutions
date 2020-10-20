"""
Matrix Spiral Copy

Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise. 
Your function then should return that array. Analyze the time and space complexities of your solution.


input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

"""


# Simulation
# O(mn) time
# O(mn) space
def spiral_copy(matrix):
  m, n = len(matrix), len(matrix[0])
  top, bottom = 0, m - 1 
  left, right = 0, n - 1
  path = []
  
  while top <= bottom and left <= right:
    # Top row, going left to right.
    for j in range(left, right + 1):
      path.append(matrix[top][j])
    top += 1
    
    # Right column, going top to bottom.
    for i in range(top, bottom + 1):
      path.append(matrix[i][right])
    right -= 1
    
    # Bottom row, going right to left.
    if top <= bottom:
      for j in range(right, left - 1, -1):
        path.append(matrix[bottom][j])    
      bottom -= 1
    
    # Left column, going bottom to top.
    if left <= right:
      for i in range(bottom, top - 1, -1):
        path.append(matrix[i][left])
      left += 1  
    
  return path


# Layer-by-layer
# O(mn) time
# O(mn) space
def copy_layer(matrix, top, bottom, left, right, path):
  # Copy top row, going left to right.
  for j in range(left, right + 1):
    path.append(matrix[top][j])
    
  if top == bottom: # case where we don't have a right column to copy (like a matrix with only one row)
    return
  # Copy right column, going top to bottom.
  for i in range(top + 1, bottom + 1):
    path.append(matrix[i][right])
    
  if right == left: # case where we don't have a bottom row to copy (like a matrix with only one column)
    return 
  # Copy bottom row, going right to left.
  for j in range(right - 1, left - 1, -1):
    path.append(matrix[bottom][j])
  
  # Copy left column, going bottom to top.
  for i in range(bottom - 1, top, -1):
    path.append(matrix[i][left])
  
def spiral_copy(matrix):
  m, n = len(matrix), len(matrix[0])
  top, bottom = 0, m - 1 
  left, right = 0, n - 1
  path = []
  
  while top <= bottom and left <= right:
    copy_layer(matrix, top, bottom, left, right, path)
    # Move edges to next layer
    top += 1
    bottom -= 1
    left += 1
    right -= 1
    
  return path
