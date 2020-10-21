"""
Time Planner

Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, 
returns the earliest time slot that works for both of them and is of duration dur. 
If there is no common time slot that satisfies the duration requirement, return an empty array.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. 
The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. 
The input variable dur is a positive integer that represents the duration of a meeting in seconds. 
The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, 
time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.


input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12

"""

# O(m + n) time
# O(1) space

def meeting_planner(slotsA, slotsB, dur):
  A_idx, B_idx = 0, 0
  m, n = len(slotsA), len(slotsB)
  
  while A_idx < m and B_idx < n:
    A_start, A_end = slotsA[A_idx]
    B_start, B_end = slotsB[B_idx]
    
    start = max(A_start, B_start)
    end = min(A_end, B_end)
    overlap = end - start
    if overlap >= dur:
      return [start, start + dur]
    
    if A_end < B_end:
      A_idx += 1
    else:
      B_idx += 1
  
  return []
