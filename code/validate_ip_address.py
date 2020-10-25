"""
Validate IP Address
"""

# O(n) time
# O(n) space
def validateIP(ip):
  nums = ip.split(".")
  if len(nums) != 4:
    return False
  
  for num in nums:
    if not is_valid_num(num):
      return False
  
  return True


def is_valid_num(num):
  if not num:
    return False
  
  # Check that each character in num is a digit 0-9
  for digit in num:
    if digit < '0' or digit > '9':
      return False
  
  # Check for leading zeros
  # E.g. '4' should return True, '04' and '004' should return False.
  if len(num) > 1 and num[0] == '0':
    return False
  
  # Check that num is in the range 0-255
  if int(num) < 0 or int(num) > 255:
    return False
  
  return True
