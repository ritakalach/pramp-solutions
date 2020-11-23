"""
Validate IP Address

Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, 
while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.


ip = '192.168.0.1'
output: true

ip = '0.0.0.0'
output: true

ip = '123.24.59.99'
output: true

ip = '192.168.123.456'
output: false

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
    if digit < '0' or digit > '9': # if not digit.isdigit():
      return False
  
  # Check for leading zeros
  # E.g. '4' should return True, '04' and '004' should return False.
  if len(num) > 1 and num[0] == '0':
    return False
  
  # Check that num is in the range 0-255
  if int(num) < 0 or int(num) > 255:
    return False
  
  return True
