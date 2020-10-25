"""
Decrypt Message

Every word is encrypted as follows:
  - Convert every letter to its ASCII value. 
  - Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. 
  - Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. 
  - Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	 r	 i	 m	 e
Step 1:	              99	114	105	109	101
Step 2:	              100	214	319	428	529
Step 3:	              100	110	111	116	113
Encrypted message:  d	 n	 o	 t	 q

Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

input:  word = "dnotq"
output: "crime"

input:  word = "flgxswdliefy"
output: "encyclopedia"

"""

# O(n) time
# O(n) space
def decrypt(word):
  decryption = ""
  prev_letter_val = 1
  
  for letter in word:
    letter_ascii_val = ord(letter)
    letter_ascii_val -= prev_letter_val
    
    while letter_ascii_val < ord('a'):
      letter_ascii_val += 26
      
    decryption += chr(letter_ascii_val)
    prev_letter_val += letter_ascii_val

  return decryption
