"""
Smallest Substring of All Characters

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str 
containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

"""

# O(m + n) time
# O(m) space
def get_shortest_unique_substring(arr, string):
  start_idx = 0
  substring = ""
  expected_char_num = len(arr)
  actual_char_num = 0
  char_to_count = {key: 0 for key in arr}

  for end_idx in range(len(string)):
    add_char = string[end_idx]
    if add_char not in char_to_count:
      continue
    if char_to_count[add_char] == 0:
      actual_char_num += 1
    char_to_count[add_char] += 1

    # if substring satisfies, make window smaller by incrementing start_idx
    while actual_char_num == expected_char_num:
      curr_window_len = end_idx - start_idx + 1
      if curr_window_len == expected_char_num:
        # case: we won't find a shorter substring that satisfies
        return string[start_idx:end_idx + 1]
      if substring == "" or curr_window_len < len(substring):
        substring = string[start_idx:end_idx + 1]
      remove_char = string[start_idx]
      if remove_char in char_to_count:
        char_to_count[remove_char] -= 1
        if char_to_count[remove_char] == 0:
          actual_char_num -= 1
      start_idx += 1
      
  return substring
