"""
Pancake Sort

Given an array of integers arr:
   1. Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
   2. Write a function pancakeSort(arr) that sorts and returns the input array. 
      You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.


input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output

"""


def flip(arr, k):
  low = 0
  high = k
  while low < high:
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1

    
def find_max_index(arr, last_index):
  max_num_index = 0
  for i in range(1, last_index + 1):
    if arr[i] > arr[max_num_index]:
      max_num_index = i
  return max_num_index 
  

# O(n^2) time
# O(1) space
def pancake_sort(arr):
  n = len(arr)
  for i in range(n - 1, -1, -1):
    max_num_index = find_max_index(arr, i)
    flip(arr, max_num_index)
    flip(arr, i) # i is the last index of the unsorted portion of the array
  return arr
