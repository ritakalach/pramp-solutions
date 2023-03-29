"""
Diff Between Two Strings

Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source to target 
that uses the least edits possible.

For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]

More formally, for each character C in source, we will either write the token C, which does not count as an edit; 
or write the token -C, which counts as an edit.

Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.

At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, the letters should spell out target 
(when ignoring plus-signs.)

In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), a
nd ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.

If there are multiple answers, use the answer that favors removing from the source first.

"""

# O(mn) time
# O(mn) space
# Doesn't return correct order in case of multiple answers
def diffBetweenTwoStrings(source, target):
  m, n = len(target), len(source) 
  dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
  
  # Build dp
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      else:
        if target[i - 1] == source[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
  
  # Reconstruct path
  path = []
  i, j = m, n

  while i > 0 and j > 0:
    if target[i - 1] == source[j - 1]:
      # Write char with no edits
      path.append(source[j - 1])
      i -= 1
      j -= 1
    else:
      # We must either subtract source[j - 1] or add target[i - 1]
      if dp[i][j - 1] < dp[i - 1][j]:
        path.append("-" + source[j - 1])   
        j -= 1
      else:
        path.append("+" + target[i - 1])
        i -= 1
        
  while i > 0:
    path.append("+" + target[i - 1])
    i -= 1
  
  while j > 0:
    path.append("-" + source[j - 1])   
    j -= 1
    
  path.reverse()
  return path
