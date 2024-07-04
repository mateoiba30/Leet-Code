#Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

#exercise 1161

from typing import List
from typing import Optional
from typing import deque
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        best_level = 0
        actLevel = 1
        
        if root:
            list = deque()
            list.append(root)
            list.append(None) #marks the end of each level
            level_sum = 0

            while list:   
                actNode = list.popleft()
                if actNode:
                    level_sum += actNode.val
                    if actNode.left:
                        list.append(actNode.left)
                    if actNode.right:
                        list.append(actNode.right)
                else:
                    if level_sum > max_sum:
                        max_sum = level_sum
                        best_level = actLevel
                    level_sum = 0
                    actLevel += 1
                    if list: 
                        list.append(None) #marks the end of each level, this means that now the first node is the rightest of his level

        return best_level
    