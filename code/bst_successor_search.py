"""
BST Successor Search

In a Binary Search Tree (BST), an Inorder Successor of a node is defined as the node with the smallest key greater than the key of the input node 
(see examples below). Given a node inputNode in a BST, you’re asked to write a function findInOrderSuccessor that returns the Inorder Successor of inputNode. 
If inputNode has no Inorder Successor, return null.

            20
           /  \
          9    25
         / \ 
        5   12
           /  \ 
         11    14

input = node 11
output = node 12

input = node 9
output = node 11

input = node 14
output = node 20

"""


# Starting at the root
def find_in_order_successor(self, inputNode):
    successor = None
    node = self.root
    
    while node: 
      if node.key > inputNode.key:
        successor = node
        node = node.left
      else:
        node = node.right 
        
    return successor


# Starting at the node
  def find_in_order_successor(self, inputNode):
    curr_node = inputNode
    
    if curr_node.right:
      # Return left-most node in the right subtree
      curr_node = curr_node.right
      while curr_node.left:
        curr_node = curr_node.left
      return curr_node
    
    else:
      # Return first ancestor whose key is larger than inputNode's key
      while curr_node.parent:
        if curr_node.parent.key < curr_node.key:
          curr_node = curr_node.parent
        else:
          return curr_node.parent
        
    # Succesor doesn't exist
    return None


# Starting at the node, modular
  def find_in_order_successor(self, inputNode):
    if inputNode.right:
      return self.find_min_key(inputNode.right)
    
    ancestor = inputNode.parent
    child = inputNode   
    while ancestor and child == ancestor.right:
      child = ancestor
      ancestor = child.parent     
    return ancestor
  
  def find_min_key(self, inputNode):
    while inputNode.left:
      inputNode = inputNode.left
    return inputNode
