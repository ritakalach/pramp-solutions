"""
Basic Regex Parser

Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - 
and should return true if the text matches the pattern as a regular expression.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' 
is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter.


input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true

"""
