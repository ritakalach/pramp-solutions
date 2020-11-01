"""
Number of Paths

You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. 
The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. 
Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.

For convenience, let’s represent every square in the grid as a pair (i,j). 
The first coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis. 
The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border. 
In other words, in every step the position (i,j) needs to maintain i >= j. 
In every step, it may go one square North (up), or one square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

input:  n = 4
output: 5

"""


# Recursive
# O(n^2) time
# O(n^2) space
def num_of_paths_to_dest(n):
  memo = [[0 for _ in range(n)] for _ in range(n)]
  return dfs(0, 0, memo, n)

def dfs(i, j, memo, n):
  # Base case
  if i == n - 1 and j == n - 1:
    return 1
  if memo[i][j]:
    return memo[i][j]
  
  number_of_paths = 0
  # Going up
  if i < n - 1 and i >= j:
    number_of_paths += dfs(i + 1, j, memo, n)
  # Going right  
  if j < n - 1:
    number_of_paths += dfs(i, j + 1, memo, n)
    
  memo[i][j] = number_of_paths
  return number_of_paths
  
  
# Iterative
# O(n^2) time
# O(n^2) space
def num_of_paths_to_dest(n):
  dp = [[0 for j in range(n)] for i in range(n)]
  dp[0] = [1 for j in range(n)]
  
  for i in range(1, n):
    for j in range(1, n):
      if i <= j:
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 
  
  return dp[-1][-1]


# Iterative
# O(n^2) time
# O(n) space

  
