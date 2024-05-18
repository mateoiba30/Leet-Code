#exercise 392
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        not_matched = s
        for char in t:
            if len(not_matched) == 0 :
                break
            elif( char == not_matched[0] ):
                not_matched = not_matched[1:]
                
        return len(not_matched) == 0