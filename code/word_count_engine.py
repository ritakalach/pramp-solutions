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
