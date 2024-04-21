#exercise 238
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

#Esto hace una división practicamente y es de O(n^2)
        # array = []
        # max = 1
        # i=0

        # for num in nums:
        #     max*=num
        
        # for i in range(len(nums)):
        #     if nums[i] !=0:
        #         array.append(int(max//nums[i]))
        #     else:
        #         j=0
        #         mult=1
        #         for j in range(len(nums)):
        #             if j!=i:
        #                  mult*=nums[j]
        #         array.append(mult)
        
    # return array



#solucion O(n) pero necestito declarar nuevos arreglos
        # longi = len(nums)
        # from_left = [1] * longi #array of 1s
        # from_right = [1]* longi #array of 1s

        # aux = 1
        # for i in range(longi): #create an array with multiplications from left to right
        #     from_left[i] = aux 
        #     aux = aux * nums[i]

        # aux = 1
        # for i in range(longi-1, -1, -1): #create an array with multiplications from right to left
        #     from_right[i] = aux 
        #     aux = aux * nums[i]

        # results = []
        # for i in range(longi):
        #     results.append(from_left[i] * from_right[i])

        # return results

#la mejor, solución O(n) y no declaro nuevo arreglo para los resultados
        longi = len(nums)
        results = [1] * longi
        aux = 1
        for i in range(longi):#create an array with multiplications from left to left
            results[i] = aux
            aux *=  nums[i] 

        aux = 1
        for i in range(longi-1, -1, -1):#to the previous array we multiply each cell with the array form right
            results[i] *= aux
            aux *=  nums[i] 

        return results