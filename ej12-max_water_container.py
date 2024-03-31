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
