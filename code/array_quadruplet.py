"""
Array Quadruplet (meaning 4Sum)

Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. 
Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.


input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)             
                     
"""

# O(n^3) time
# O(1) space
def find_array_quadruplet(nums, target):
  n = len(nums)  
  if n < 4:
    return []
  
  nums.sort()
  
  for i in range(n - 3):
    if i != 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, n - 2):
      if j != 1 and nums[j] == nums[j - 1]:
        continue
      curr_sum = nums[i] + nums[j]
      target_complement = target - curr_sum
      low = j + 1
      high = n - 1
      
      while low < high:
        curr_complement = nums[low] + nums[high]
        if curr_complement > target_complement:
          high -= 1
        elif curr_complement < target_complement:
          low += 1
        else:
          return [nums[i], nums[j], nums[low], nums[high]]      
          
  return []
