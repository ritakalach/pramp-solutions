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
# O(1) space
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
