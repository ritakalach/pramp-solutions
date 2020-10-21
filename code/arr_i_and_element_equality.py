"""
Array Index & Element Equality

Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. 
Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.


input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.

"""


# O(logn) time
# O(1) space
def index_equals_value_search(arr):
  low = 0
  high = len(arr) - 1 
  
  while low <= high: 
    mid = low + (high - low) // 2
    if arr[mid] == mid:
      # check if the previous index also equals its element
      while mid > 0 and arr[mid - 1] == mid - 1:
        mid -= 1
      return mid
    elif arr[mid] < mid:
      low = mid + 1
    else: 
      high = mid - 1
    
  return -1


def index_equals_value_search(arr):
  low = 0
  high = len(arr) - 1 
  
  while low <= high: 
    mid = low + (high - low) // 2
    if arr[mid] == mid and (mid == 0 or arr[mid - 1] != mid - 1):
      return mid
    elif arr[mid] < mid:
      low = mid + 1
    else: 
      # includes case where arr[mid] > mid
      # or arr[mid - 1] == mid - 1
      high = mid - 1
    
  return -1


def binary_search(arr):
  low = 0
  high = len(arr) - 1 
  
  while low <= high: 
    mid = low + (high - low) // 2
    if arr[mid] == mid:
      return mid
    elif arr[mid] < mid:
      low = mid + 1
    else: 
      high = mid - 1
      
  return -1
      
def index_equals_value_search(arr):
  low = 0
  high = len(arr) - 1 
  
  ans = binary_search(arr)      
  # check if the previous index also equals its element
  while ans > 0 and arr[ans - 1] == ans - 1:
    ans -= 1
    
  return ans
