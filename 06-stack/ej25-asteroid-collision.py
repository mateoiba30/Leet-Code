#We are given an array asteroids of integers representing asteroids in a row.
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

#excersice number 735

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        leftStock = []
        rightStock = []

        for x in asteroids:
            if x < 0:
                leftStock.append(x)
                while len(rightStock) > 0 and abs(x) > rightStock[-1]:
                    rightStock.pop()
                if len(rightStock) > 0 and abs(x) == rightStock[-1]:
                    rightStock.pop()
                    leftStock.pop()   
                elif len(rightStock) > 0 and abs(x) < rightStock[-1]:    
                    leftStock.pop()  
            else:
                rightStock.append(x)
        
        return leftStock + rightStock
    

asteroids = [-2,2,1,-1]
solution = Solution()
result = solution.asteroidCollision(asteroids)
print("Resultado:", result)