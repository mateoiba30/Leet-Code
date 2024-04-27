#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#You can use the operations on either string as many times as necessary.

#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

#excersie 1657

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True
            
        if len(word1) != len(word2):
            return False

        dict1 = {}
        dict2 = {}

        for c in word1:
            if c in dict1: #if it's among the keys
                dict1[c] += 1
            else:
                dict1[c] = 1

        for c in word2:
            if c in dict2: #if it's among the keys
                dict2[c] += 1
            else:
                dict2[c] = 1
        
        if len(dict1) != len(dict2) or len(dict1)<2:
            return False

        #both dictionaries must have same keys or the same except one
        oneWrong = False
        for key, value in dict2.items():
            if key not in dict1 and not oneWrong:
                oneWrong = True
            elif key not in dict1 and oneWrong:
                return False


        freqs1 = sorted(list(dict1.values()))
        freqs2 = sorted(list(dict2.values()))

        if freqs1 == freqs2:
            return True
        else:
            return False
        
solution = Solution()
word1 = "a"
word2 = "b"
print(solution.closeStrings(word1, word2))