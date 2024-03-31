from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma_act = 0
        for i in range(k):
            suma_act += nums[i]
        suma_max = suma_act

        inicio = 0
        fin = k -1

        for i in range(len(nums) - k): #sumar 1?
            suma_act -= nums[inicio]
            inicio += 1
            fin += 1
            suma_act += nums[fin]
            suma_max = max (suma_max, suma_act)

        return suma_max/k