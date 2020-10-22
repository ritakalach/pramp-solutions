"""
Basic Regex Parser

Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - 
and should return true if the text matches the pattern as a regular expression.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' 
is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter.


input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true

"""

def is_match(text, pattern):
  m, n = len(text), len(pattern)
  if not m and not n:
    return True
  if not pattern: # e.g. text = "a" pattern = ""
    return False
  
  dp = [[False for j in range(n + 1)] for i in range(m + 1)]
  dp[0][0] = True
  for j in range(1, n + 1):
    if pattern[j - 1] == "*":
      dp[0][j] = dp[0][j-1] or (dp[0][j - 2] if j > 1 else False)
  
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if text[i - 1] == pattern[j - 1] or pattern[j - 1] == ".":
        dp[i][j] = dp[i - 1][j - 1]
      elif pattern[j - 1] == "*":
          dp[i][j] = dp[i][j - 1] or (dp[i][j - 2] if j > 1 else False)
          if j > 1 and (text[i - 1] == pattern[j - 2] or pattern[j - 2] == "."):
            dp[i][j] = dp[i][j] or dp[i - 1][j] 

  return dp[-1][-1]
