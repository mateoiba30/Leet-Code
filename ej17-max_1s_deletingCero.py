from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        eliminated = False
        neverDelete = True
        maxLarge = 0
        start = 0
        end = 0

        while end < len(nums):
            while end < len(nums) and not(nums[end]==0 and eliminated):
                if nums[end] == 0 or (end == len(nums)-1 and neverDelete):#eliminar un cero, o un 1 si llego al final y no encontré ningún creo y el arreglo no tiene otro cero para eliminar
                    eliminated = True
                    neverDelete = False
                end += 1

            if eliminated:
                maxLarge = max(maxLarge, end - start -1) #resto 1 porque el eliminado no cuenta
                eliminated = False
            else:
                maxLarge = max(maxLarge, end - start)

            while not eliminated and start<len(nums): #i need to jump a 0
                if nums[start]==0:
                    eliminated=True
                start+=1
            eliminated = False

        if (end < len(nums)):
            maxLarge = max(maxLarge, end - start)

        return maxLarge
    
if __name__ == "__main__":
    sol = Solution()
    nums1 =[0,0,1,1]
    print("Prueba 1:", sol.longestSubarray(nums1))