from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        pivot = 0

        for pivot in range(len(nums)):
            if left == right:
                return pivot
            left += nums[pivot] #not neccesary the 'else' statement
            if pivot + 1 < len(nums):#we need to be carefull with the last element
                right -= nums[pivot + 1]
        
        return -1
