#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#Return the number of good nodes in the binary tree.

#exercise 1448

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = [0] # if its integer i can´t use references
        maxVal = -10**5
        self.goodNodesRecursive(root, goodNodes, maxVal)
        return goodNodes[0]

    def goodNodesRecursive(self, root: TreeNode, goodNodes: list, maxVal: float):
        if root == None:
            return
        if root.val >= maxVal:
            maxVal = root.val
            goodNodes[0] += 1
        self.goodNodesRecursive(root.left, goodNodes, maxVal)
        self.goodNodesRecursive(root.right, goodNodes, maxVal)