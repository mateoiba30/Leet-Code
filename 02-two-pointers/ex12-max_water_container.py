#exercise 11
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

 
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_areas = [0] * len(height)

        limit = len(height)-1
        i=0
        j=limit
        end = False
        max_area = 0

        while (end == False):
            left_bar = height[i]
            right_bar = height[j]
            min_bar = min(left_bar, right_bar) 
            act_area = min_bar * (j - i)

            if act_area > max_area:
                max_area = act_area

            if min_bar == left_bar and i<limit:
                i+=1
            elif j>0:
                j-=1
            else:
                end = True

        return max_area
