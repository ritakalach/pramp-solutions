"""
Array of Array Products

Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). 
Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.


input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

"""

# O(n) time
# O(n) space
def array_of_array_products(arr):
  n = len(arr)
  if n < 2: # no values to multiply if n equals to 0 or 1
    return []
  
  products_arr = [None for _ in range(n)]
  
  product_before_i = 1
  for i in range(n):
    products_arr[i] = product_before_i
    product_before_i *= arr[i]

  product_after_j = 1
  for j in range(n - 1, -1, -1):
    products_arr[j] *= product_after_j
    product_after_j *= arr[j]
    
  return products_arr
