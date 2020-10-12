"""
Root of Number

Many times, we need to re-implement basic functions without using any standard library functions already implemented. 
For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number. 
The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 
(i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis 
(some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking. 
Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.


input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3
"""

def root(x, n):
  if n == 0:
    raise ValueError("Can't take 0'th root of a number.")
    
  low = 0
  high = max(1, x)

  while high - low > 0.001:
    mid = (low + high) / 2.0 
    if mid ** n < x:
      low = mid
    elif mid ** n > x:
      high = mid
    else: # mid ** n == x:
      break
  
  return mid
