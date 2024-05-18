#We are given an array asteroids of integers representing asteroids in a row.
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

#excersice number 735

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while asteroid < 0 and stack and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff < 0: #if the negative is bigger, it means the left asteroid is stronger, so he will crush with the previous right asteroid
                    stack.pop()
                elif diff > 0:
                    asteroid = 0 #we save a false boolean to not push the left asteroid
                else: #we do both things on this case
                    asteroid = 0
                    stack.pop()
            if asteroid: 
                stack.append(asteroid)

        return stack