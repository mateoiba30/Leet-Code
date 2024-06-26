#exercise 1679
#You are given an integer array nums and an integer k.
#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#Return the maximum number of operations you can perform on the array.

from typing import List

class Solution:

    #best solution
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        nums.sort()
        left=0
        right=len(nums)-1

        while right>0 and nums[right]>k:
            right-=1

        while left<right:
            if nums[left]+nums[right]>k:
                right-=1
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                operations+=1
                left+=1
                right-=1

        return operations

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    k1 = 5
    print("Resultado nums1:", solution.maxOperations(nums1, k1))