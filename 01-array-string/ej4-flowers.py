#exercise 605
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        places=0
        antepenultimo=1
        anterior=0

        for actual in flowerbed:
            if antepenultimo == 0 and anterior == 0 and actual == 0:
                anterior = 1
                places+=1
            antepenultimo = anterior
            anterior = actual
        
        if anterior == 0 and antepenultimo == 0:
            places+=1
        
        return n<=places
