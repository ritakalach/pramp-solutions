"""
Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. 
For instance, the deletion distance between "heat" and "hit" is 3:
By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.

Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. 


input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0

"""

# O(mn) time
# O(mn) space
def deletion_distance(str1, str2):
  deletions = 0
  if str1 == str2:
    return deletions
  
  m, n = len(str1), len(str2)
  dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

  # Update first row
  for i in range(m + 1):
    dp[i][0] = i
  
  # Update first col
  for j in range(n + 1):
    dp[0][j] = j
  
  # Update the rest of the matrix
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i - 1] != str2[j - 1]:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
      else:
        dp[i][j] = dp[i - 1][j - 1]
        
  return dp[-1][-1]
