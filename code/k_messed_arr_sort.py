"""
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. 
For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array 
will be located at either index 4, 5, 6, 7 or 8 in the input array.


input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

# O(nlogk) time
# O(k) space
import heapq
def sort_k_messed_array(arr, k):
  n = len(arr)
  # Build min-heap for first k elements
  heap = arr[:k + 1]
  heapq.heapify(heap)

  sorted_pointer = 0
  for i in range(k + 1, n):
    # Assign top element to correct index in array
    arr[sorted_pointer] = heapq.heappop(heap)
    sorted_pointer += 1
    # Push next element in array into the min-heap
    heapq.heappush(heap, arr[i])
    
  # Extract remaining elements from the min-heap
  while heap:
    arr[sorted_pointer] = heapq.heappop(heap)
    sorted_pointer += 1
    
  return arr
