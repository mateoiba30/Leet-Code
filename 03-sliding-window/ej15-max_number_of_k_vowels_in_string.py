class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows_act = 0
        vowels = 'aeiou'
        for i in range(k):
            if s[i] in vowels:
                vows_act += 1
        vows_max = vows_act

        start = 0
        end = k -1

        for i in range(len(s) - k):
            if s[start] in vowels: 
                vows_act -= 1
            start += 1
            end += 1
            if s[end] in vowels: 
                vows_act += 1
            vows_max = max (vows_max, vows_act)

        return vows_max