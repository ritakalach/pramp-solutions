"""
Word Count Engine

Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it 
and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, 
they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. 
You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.


input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).

"""

# Let N be the number of words in document and M the number of unique words in it (M ≤ N)
# O(N) time
# O(M) space
from collections import OrderedDict

def word_count_engine(document):
  word_to_count = OrderedDict()
  words = document.split()
  max_count = 0
  
  for word in words:
    tidy_word = ""
    for char in word:
      if char.isalpha():
        tidy_word += char.lower()
    
    if tidy_word:
      curr_count = word_to_count.get(tidy_word, 0) + 1
      word_to_count[tidy_word] = curr_count
      max_count = max(max_count, curr_count)
  
  # Bucket sort
  buckets = [[] for _ in range(max_count + 1)]
  for key, value in word_to_count.items():
    buckets[value].append(key)
    
  # Iterate through buckets
  output = []
  for i in range(len(buckets) - 1, 0, -1):
    for word in buckets[i]:
      output.append([word, str(i)]) # i is the count
  return output
