from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips = k
        cont1=0
        max1=0

        for i in range(len(nums)):
            if nums[i]==1:
                cont1+=1
            elif nums[i]==0 and flips > 0:
                flips -=1
                cont1+=1
            elif flips ==0: #restart counting
                max1=max(max1, cont1)
                cont1=1
                flips=k-1

            max1=max(max1, cont1)   

        return cont1
    

if __name__ == "__main__":
    sol = Solution()
    
    # Ejemplo de uso:
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(sol.longestOnes(nums, k))  # Salida esperada: 6