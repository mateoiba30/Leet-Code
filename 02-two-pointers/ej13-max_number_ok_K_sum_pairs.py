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