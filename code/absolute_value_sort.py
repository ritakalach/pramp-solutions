"""
Absolute Value Sort

Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr. 
If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
"""


# O(n^2) time
# O(1) space
def absSort(arr):
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if swap(arr[i], arr[j]):
        arr[i], arr[j] = arr[j], arr[i]       
  return arr

def swap(num1, num2):
  if abs(num1) < abs(num2):
    return False
  elif abs(num1) > abs(num2):
    return True
  else: # Case where abs values of numbers are equal, e.g. -2 and 2
    return num1 > num2
    

# O(nlogn) the time complexity of sorting
# O(n) the space typically used by compilers in their implementation of sorting operations
def absSort(arr):
	return sorted(arr, cmp = compare)

def compare(a,b):
  # Compare abs values
  if abs(a) < abs(b):
    return -1
  elif abs(a) > abs(b):
    return 1
  # Compare signs
  elif a < b:
    return -1
  elif a > b:
    return 1
  else:
    return 0
  

# Using python 
def absSort(arr):
	return sorted(arr, key = lambda x: (abs(x), x))
