"""
Island Count

Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next 
to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” 
(i.e. they are diagonally neighbors).


input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.
          
"""

# Recursive
# O(mn) time
# O(mn) space
def get_number_of_islands(binaryMatrix):
  m, n = len(binaryMatrix), len(binaryMatrix[0])
  islands = 0
  for i in range(m):
    for j in range(n):
      if binaryMatrix[i][j] == 1:
        dfs(binaryMatrix, i, j, m, n)
        islands += 1
  return islands

def dfs(matrix, i, j, m, n):
  if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] != 1:
    return
  matrix[i][j] = "#"
  dfs(matrix, i - 1, j, m, n)
  dfs(matrix, i + 1, j, m, n)
  dfs(matrix, i, j - 1, m, n)
  dfs(matrix, i, j + 1, m, n)
  
  
# Iterative 
# O(mn) time
# O(mn) space
def get_number_of_islands(binaryMatrix):
  m, n = len(binaryMatrix), len(binaryMatrix[0])
  islands = 0
  for i in range(m):
    for j in range(n):
      if binaryMatrix[i][j] == 1:
        dfs(binaryMatrix, i, j, m, n)
        islands += 1
  return islands

def dfs(matrix, x, y, m, n):
  stack = [[x, y]]
  while stack:
    i, j = stack.pop()
    if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] != 1:
      continue
    else:
      matrix[i][j] = "#"
      stack.append([i - 1, j])
      stack.append([i + 1, j])
      stack.append([i, j - 1])
      stack.append([i, j + 1])
