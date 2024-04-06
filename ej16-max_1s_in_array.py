from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips = k
        cont1=0
        max1=0
        start = 0

        for i in range(len(nums)):
            if nums[i]==1:
                cont1+=1
            elif nums[i]==0 and flips > 0:
                flips -=1
                cont1+=1
            elif nums[i]==0 and flips ==0: #restart counting
                max1=max(max1, cont1)
                cont1+=1
                ceroJumped = False
                while not ceroJumped: #i need to jump a 0
                    if nums[start]==0:
                        ceroJumped=True
                    start+=1
                    cont1-=1

        return max(max1, cont1) 
    
#other way:
#    def longestOnes(self, nums: List[int], k: int) -> int:
        # both left and right = 0; edge case: array size = 1
#        left = right = 0

#        for right in range(len(nums)):
#            # if next right num is 0, flip it
#            if nums[right] == 0:
#                k -= 1

            # if we're out of flips, move left side to the right
 #           if k < 0:
                # if left num was a 0, unflip (no longer needed)
#                if nums[left] == 0:
##                    k += 1
  #              left += 1

#        return right - left + 1
    

if __name__ == "__main__":
    sol = Solution()
    
    # Ejemplo de uso:
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(sol.longestOnes(nums, k))  # Salida esperada: 10