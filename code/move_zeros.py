"""
Move Zeros To End

Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. 
You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]

"""

# O(n) time
# O(1) space
def moveZerosToEnd(arr):
  left_pointer = 0 # everything before left_pointer is not a zero
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[i], arr[left_pointer] = arr[left_pointer], arr[i]
      left_pointer += 1
  
  return arr
