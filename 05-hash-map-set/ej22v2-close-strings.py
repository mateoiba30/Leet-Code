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

        w1_set = set(word1)
        w2_set = set(word2)
        if w1_set != w2_set:
            return False

        word1_val = [0] * len(w1_set)
        word2_val = [0] * len(w1_set)
        i = 0
        for letter in w1_set:
            word1_val[i] = word1.count(letter)
            i += 1
        i = 0
        for letter in w2_set:
            word2_val[i] = word2.count(letter) #if i recieve the same letter in other position we will have a duplicated value in the array, but if we use dictionaries then we need to check for repeted keys
            i += 1

        return sorted(word1_val) == sorted(word2_val)
solution = Solution()
word1 = "a"
word2 = "b"
print(solution.closeStrings(word1, word2))