"""
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. 
For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets 
at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets 
you’d need to add to the input in order to make it correctly matched.


input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
"""

# O(n)
# O(1)
def bracket_match(text):
  count_missing_closing = 0
  count_missing_opening = 0
  n = len(text)
  
  for i in range(n):
    if text[i] == "(":
      count_missing_closing += 1
    elif text[i] == ")":
      count_missing_closing -= 1
      
    if count_missing_closing < 0:
      count_missing_closing += 1
      count_missing_opening += 1
      
  return count_missing_closing + count_missing_opening
