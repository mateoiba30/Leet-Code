class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        not_matched = s
        for char in t:
            if len(not_matched) == 0 :
                break
            elif( char == not_matched[0] ):
                not_matched = not_matched[1:]
                
        return len(not_matched) == 0