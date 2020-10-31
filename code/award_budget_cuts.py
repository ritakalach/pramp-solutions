"""
Award Budget Cuts

The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. 
Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars 
and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying 
a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. 
Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, 
write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted 
and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).


input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
           
"""


# O(nlogn) time
# O(1) space 
def find_grants_cap(grantsArray, newBudget): 
  n = len(grantsArray)
  grantsArray.sort()
  
  # Initiate variables to track how much of the budget is left
  # and how many grants left to cover
  amount_budget_left = float(newBudget)
  count_grants_left = n
  for i in range(n):
    money_req = grantsArray[i] * count_grants_left
    if money_req >= amount_budget_left:
      # Case 1: we'd need more money than we have left
      # meaning we need to set the cap at this point
      cap = amount_budget_left / count_grants_left
      return cap
    # Case 2: we have more money left to allocate
    # so we don't set the cap yet
    amount_budget_left -= grantsArray[i]
    count_grants_left -= 1
    
  return newBudget
