"""
Shifted Array Search

A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. 
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.


input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
"""

# one pass solution
# O(logn) time
# O(1) space
def shifted_arr_search(arr, num):
  low, high = 0, len(arr) - 1
  
  while low <= high:
    mid = (low + high) // 2
    # Case 0: we found the target num at index mid
    if arr[mid] == num:
      return mid
    # Case 1: no pivot in low-mid range, nums are ordered
    elif arr[low] <= [mid]:
      if arr[low] <= num < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
    # Case 2: pivot in low-mid range, nums are unordered
    else:
      if arr[mid] < num <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1

  return -1


# two pass solution
def shifted_arr_search(arr, num):
  n = len(arr)
  pivot = find_pivot(arr, 0, n - 1)
  
  if pivot == 0 or arr[0] > num:
    return binary_search(arr, pivot, n - 1, num)
  
  return binary_search(arr, 0, pivot - 1, num)

def find_pivot(arr, low, high):
  while low <= high:
    mid = low + (high - low) // 2
    if mid == 0 or arr[mid - 1] > arr[mid]:
      return mid
    elif arr[mid] > arr[0]:
      low = mid + 1
    else:
      high = mid - 1
      
  return 0

def binary_search(arr, low, high, num):
  while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == num:
      return mid
    elif arr[mid] < num:
      low = mid + 1
    else:
      high = mid - 1
      
  return -1
