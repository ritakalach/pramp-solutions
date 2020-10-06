"""
Shortest Word Edit Path

Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.


source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]

output: -1
"""

import string     
from collections import deque 

def shortestWordEditPath(source, target, words):
  alphabet = string.ascii_lowercase
  words_set = set(words)
  queue = deque([(source, 0)])
  seen = set()
  
  while queue:
    curr_word, depth = queue.popleft()
    if curr_word == target:
      return depth
    for i in range(len(curr_word)):
      for char in alphabet:
        potential_next_word = curr_word[:i] + char + curr_word[i+1:]
        if potential_next_word in words_set and potential_next_word not in seen:
          queue.append((potential_next_word, depth+1))
          seen.add(potential_next_word)
          
  return -1
