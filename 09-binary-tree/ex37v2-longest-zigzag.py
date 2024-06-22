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
        self.maxi = 0
        self.dfs(root, 0, 0)
        return self.maxi

    def dfs(self, node, left, right): #left and right are the max lenghts reacheds
        self.maxi = max(self.maxi, left, right)

        if node.left:
            self.dfs(node.left, right+1, 0) #we came from left but we are going to the right, we must switch counters
        if node.right:
            self.dfs(node.right, 0, left+1)

        