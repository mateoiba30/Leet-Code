#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."

#exercise 104

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #we have to initialize without recursion
        levels = 0
        return self.maxDepthRecursion(root, levels)
    
    def maxDepthRecursion(self, root: Optional[TreeNode], levels: int):
        if root == None:
            return levels
        
        levels +=1
        levelsLeft = 0
        levelsRight = 0
        
        if root.left != None:
            levelsLeft = self.maxDepthRecursion(root.left, levelsLeft)
        if root.right != None:
            levelsRight = self.maxDepthRecursion(root.right, levelsRight)
        
        return levels + max(levelsLeft, levelsRight)