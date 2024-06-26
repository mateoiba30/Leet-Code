#exercise 1768
#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.
class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        word3=""
        l1=len(word1)
        l2=len(word2)
        largo = min(l1, l2)
        for i in range(largo):
            word3 = word3 + word1[i:i+1]
            word3 = word3 + word2[i:i+1]

        if l1 > l2:
            return (word3 + word1[largo:l1])
        elif l1 < l2:
            return (word3 + word2[largo:l2])
        else:
            return (word3)