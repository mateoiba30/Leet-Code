#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."

#exercise 104

#this is a simpler way of doing it

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        levelsLeft = 1
        levelsRight = 1

        levelsLeft += self.maxDepth(root.left)
        levelsRight += self.maxDepth(root.right)

        return max(levelsLeft, levelsRight)