#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#exercise 1207

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}
        for n in arr:
            if n in dict: #if it's among the keys
                dict[n] += 1
            else:
                dict[n] = 1

        freqs = []
        for key, value in dict.items():
            if value in freqs:
                return False
            else:
                freqs.append(value)

        #sometimes this way is more efficient
        #freqs = list(dict.values())
        #for value in freqs:
        #    if freqs.count(value) > 1: 
        #        return False
        
        #other way is with set(), wich is a collection with unique elements
        #dict2 = set()
        #for j in dict.values():
        #    if j in dict2:
        #        return False
        #    else:
        #        dict2.add(j)

        return True
