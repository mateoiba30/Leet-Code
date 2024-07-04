#Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#exercise 199

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        if root:
            right_view.append(root.val)
            list = []
            list.append(root)
            list.append(None) #marks the end of each level

            end = False
            while not end:
                actNode = list.pop(0)
                if actNode:
                    if actNode.left:
                        list.append(actNode.left)
                    if actNode.right:
                        list.append(actNode.right)
                else:
                    if list: 
                        right_view.append(list[-1].val)
                        list.append(None) #marks the end of each level, this means that now the first node is the rightest of his level
                    else: #if the list len is 1, it means ir only has the None node, so we have to finish the execution
                        end = True

        return right_view
    
#        1
#         \
#          3

root = TreeNode(1)
root.right = TreeNode(3)

# Crear una instancia de Solution y llamar a rightSideView
solution = Solution()
result = solution.rightSideView(root)

# Imprimir el resultado
print("Right side view of the tree:", result)
