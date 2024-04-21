#exercise 283
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.

 
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes=0
        i=0
        while i <(len(nums)) - zeroes:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                zeroes +=1
            else:
                i+=1

# Función main para testear
if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    print("Original nums:", nums)
    s.moveZeroes(nums)
    print("Modified nums:", nums)
