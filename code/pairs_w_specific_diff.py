"""
Pairs with Specific Difference

Given an array arr of distinct integers and a nonnegative integer k, 
write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. 
If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.


input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

"""


# all solutions are O(n) time and O(n) space complexity 


# one pass solution
# however, doesn't return output in required order
def find_pairs_with_given_difference(arr, k):
  output = []
  complements = set()
  
  for num in arr:
    # if num is y
    x = k + num
    # if num is x
    y = num - k
    if x in complements:
      output.append([x, num])
    if y in complements:
      output.append([num, y])
    complements.add(num)

  return output


# two pass solution
# pass once through the array to create a set for constant lookups
# pass a second time through the array to see if we have a pair that satisfies x - y = k
def find_pairs_with_given_difference(arr, k):
  output = []
  arr_set = set(arr)
  
  for y in arr:
    x = k + y
    if x in arr_set:
      output.append([x, y])
      
  return output 


# solution provided by pramp
# also requires two passes
# on the first pass: create a y_to_x hashmap
# on the second pass: check if y is in the y_to_x hashmap
def find_pairs_with_given_difference(arr, k):
  output = []
  y_to_x = {}
  
  for x in arr:
    y = x - k 
    y_to_x[y] = x
    
  for y in arr:
    if y in y_to_x:
      x = y_to_x[y]
      output.append([x, y])
  
  return output
