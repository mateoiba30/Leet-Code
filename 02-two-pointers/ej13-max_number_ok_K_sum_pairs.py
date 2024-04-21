#exercise 1679
#You are given an integer array nums and an integer k.
#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#Return the maximum number of operations you can perform on the array.

from typing import List

class Solution:

    #too expensive in time
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    nums[j]=k+1
                    operations+=1
                    break

        return operations

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    k1 = 5
    print("Resultado nums1:", solution.maxOperations(nums1, k1))