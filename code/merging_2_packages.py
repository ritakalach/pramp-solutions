"""
Merging 2 Packages

Given a package with a weight limit limit and an array arr of item weights, 
implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. 
Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. 
If such a pair doesn’t exist, return an empty array.


input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
               
"""

# O(n), O(n)
def get_indices_of_item_wights(arr, limit):
  if len(arr) < 2:
    return []
  
  complements = {}
  
  for i, num in enumerate(arr):
    complement = limit - num
    if complement in complements:
      j = complements[complement]
      return [i, j]
    complements[num] = i
    
  return []
               
