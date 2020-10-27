""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers 
that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: 
  M ≈ N - the array lengths are approximately the same 
  M ≫ N - arr2 is much bigger than arr1.

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
output: [3, 6, 7]

""


# O(n + m) time
# O(n) space
def find_duplicates(arr1, arr2):
  duplicates = []
  
  m, n = len(arr1), len(arr2)
  i, j = 0, 0
  
  while i < m and j < n:
    if arr2[j] > arr1[i]:
      i += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else: # arr1[i] == arr2[j]
      duplicates.append(arr1[i])
      i += 1
      j += 1
      
  return duplicates


# O(mlogn) time where m = len(arr1) and n = len(arr2)
# O(n) space
def find_duplicates(arr1, arr2):
  # Make arr1 the shorter array
  if arr2 < arr1:
    arr1, arr2 = arr2, arr1
  duplicates = []
  
  # Traverse the shorter array 
  for num in arr1:
    if binary_search(arr2, num):
      duplicates.append(num)
      
  return duplicates


def binary_search(arr, num):
  left = 0
  right = len(arr) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] < num:
      left = mid + 1
    elif arr[mid] > num:
      right = mid - 1
    else: # arr[mid] == num
      return True
    
  return False
