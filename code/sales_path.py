"""
Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). 
The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node 
and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. 
In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:
                0
           /    |    \
        5       3       6
       /       / \     / \
      4       2   0   1   5
             /   /
            1   10
             \
              1
              
              
"""

# O(n) time
# O(n) space
def get_cheapest_cost(rootNode):
  stack = [(rootNode, rootNode.cost)] 
  min_cost = float('inf')
  
  while stack:
    curr_node, curr_cost = stack.pop()
    if not curr_node.children:
      min_cost = min(min_cost, curr_cost)
    else:
      for child_node in curr_node.children: 
        stack.append((child_node, curr_cost + child_node.cost))
  
  return min_cost
