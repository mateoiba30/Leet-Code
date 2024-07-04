#Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#exercise 872

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaves(root1) == self.leaves(root2)
    
    def leaves(self, root: Optional[TreeNode]):
        leaves = []
        self.leavesRecursion(root, leaves)
        return leaves
    
    def leavesRecursion(self, root: Optional[TreeNode], leaves):
        if root == None:
            return
        
        if root.right == None and root.left == None:
            leaves.append(root.val)

        self.leavesRecursion(root.left, leaves) #nhot neccesary check if root.left it's null because i check if the root of the function is none at the beggining
        self.leavesRecursion(root.right, leaves)