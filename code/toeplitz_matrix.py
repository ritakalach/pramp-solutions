"""
Toeplitz Matrix

A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. 
Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. 
The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn’t a Toeplitz matrix, so we should return false.
"""

# O(mn) time 
# O(1) space
def isToeplitz(matrix):
  m, n = len(matrix), len(matrix[0])
  for i in range(1, m):
    for j in range(1, n):
      if matrix[i][j] != matrix[i - 1][j - 1]:
        return False
  
  return True
