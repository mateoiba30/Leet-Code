#You are given the root of a binary tree.
#A ZigZag path for a binary tree is defined as follow:
#Choose any node in the binary tree and a direction (right or left).
#If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
#Change the direction from right to left or from left to right.
#Repeat the second and third steps until you can't move in the tree.

#Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
#Return the longest ZigZag path contained in that tree.

#exercise 1372

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max( self.zigzagRecursive(root, -1, True), self.zigzagRecursive(root, -1, False) )

    def zigzagRecursive(self, root: Optional[TreeNode], maxZigzag: int, fromRight: bool) -> int:
        if root == None:
            return maxZigzag
        
        maxZigzag += 1
        
        if fromRight:
            maxZigzag = max( self.zigzagRecursive(root.left, maxZigzag, False), self.zigzagRecursive(root.right, 0, True) )
        else:
            maxZigzag = max( self.zigzagRecursive(root.left, 0, False), self.zigzagRecursive(root.right, maxZigzag, True) )

        return maxZigzag