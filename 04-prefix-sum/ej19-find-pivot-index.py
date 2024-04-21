#exercise 724
#Given an array of integers nums, calculate the pivot index of this array.
#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#if the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
#Return the leftmost pivot index. If no such index exists, return -1.

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
