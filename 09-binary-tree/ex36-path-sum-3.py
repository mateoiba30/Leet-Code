#Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
#The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

#exercise 437

#curretnPathSum is the sum from root to the actual node. 
#cache is a dictionary that counts the times where a currentPathSum get some value. It's values are the counters and the keys the sums
#if there is a previous path sum that we can extract to the currentPathSum to reach the target, that means that (currPathSum-target) is in cache
#when an oldPath sum is not more available we remove ir from cache, this happens after going throw the childs, when we are "going up"

class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        self.dfs(root, target, 0, cache)
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  

        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0) #there are negative numbers, son maybe we can cut our current path on differents nodes and have the same value
        
        cache[currPathSum] = cache.get(currPathSum, 0) + 1 #we add the actual sum to the cache of old sums

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1 #remove the oldPathSum that we cannot use anymore