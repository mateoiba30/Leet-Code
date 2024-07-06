#You are given the root of a binary search tree (BST) and an integer val.
#Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null

#exercise 700

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

root = TreeNode(18)
root.left = TreeNode(2)
root.right = TreeNode(22)
root.right.right = TreeNode(63)
root.right.right.right = TreeNode(84)

sol = Solution()
val = 84
result = sol.searchBST(root, val)

if result:
    print(f"Node with value {val} found: {result.val}")
else:
    print(f"Node with value {val} not found in the tree.")