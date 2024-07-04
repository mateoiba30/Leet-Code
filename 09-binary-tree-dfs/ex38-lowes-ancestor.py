#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

#exercise 236

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
      return root #if one of the nodes we are looking for is de root, it means he is the lowest common ancestor

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left!=None and right!=None: #if we founded p and q in different subtrees of the actual root
      return root
    
    if left != None:
       return left
    return right #maybe is None
  
#we explore the tree, if a recursive path from a node ends without finding p or q, the node it will return None to his father. On the other hand, if there was p or q on the path, the node it will return itself. This all means that when we find a node where boths children returned Not None is because they both have p and q respectively, beeing the actual node the answer