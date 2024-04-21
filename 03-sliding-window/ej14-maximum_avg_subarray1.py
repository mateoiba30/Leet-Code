#exercise 643
#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
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