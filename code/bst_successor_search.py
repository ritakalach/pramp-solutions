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
