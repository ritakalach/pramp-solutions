"""
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.


input:  arr = [0, 1, 2, 3]
output: 4 

input:  arr = [0, 2, 3]
output: 1

"""

# O(n)
# O(n)
def get_different_number(arr):
  n = len(arr)
  arr_set = set(arr)
  
  for i in range(n):
    if i not in arr_set:
      return i
    
  return n
