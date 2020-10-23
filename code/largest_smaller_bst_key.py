"""
Largest Smaller BST Key

Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree 
that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.


For num = 17 and the binary search tree below:

            20
           /  \
          9    25
         / \ 
        5   12
           /  \ 
         11    14

Your function would return: 14 since it’s the largest key in the tree that is still smaller than 17.

"""

  # O(logn) time complexity if the tree is balanced, O(N) otherwise
  # O(1) space
  def find_largest_smaller_key(self, num):
    predecessor = -1
    node = self.root
    
    while node:
      if node.key >= num:
        node = node.left
      else:
        predecessor = node.key
        node = node.right

    return predecessor
