class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        act_height = 0
        max_height = 0

        for g in gain:
            act_height+=g
            max_height=max(act_height, max_height)

        return max_height