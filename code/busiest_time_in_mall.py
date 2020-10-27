"""
Busiest Time in The Mall

The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. 
You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. 
The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), 
respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. 
The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. 


input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378

"""

# O(n) time
# O(1) space
def find_busiest_period(data):
  n = len(data)
  count = 0
  max_count = 0
  timestamp = None
  
  for i in range(n):
    curr_timestamp, visitors, entered = data[i]
    if entered: # entered == 1 means visitors entered
      count += visitors
    else: # entered == 0 means visitors exited
      count -= visitors
      
    # Check if there are more data points with same timestamp
    if i < n - 1 and curr_timestamp == data[i + 1][0]:
      continue
