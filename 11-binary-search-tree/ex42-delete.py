# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

#exercise 450

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:

                if not root.left:
                    root = root.right #we just "jump" the node to delete
                elif not root.right:
                    root = root.left #we just "jump" the node to delete
                else: 
                    aux = self.minRightNode(root.right) 
                    root.val = aux.val #replace with one value that not affects the structure
                    root.right = self.deleteNode(root.right, aux.val) #now delete the duplicated node value, which is a leaf
            return root
        
    def minRightNode(self, actual): #we can also search for the maxLeftNode
        while not actual.left == None:
            actual = actual.left
        return actual