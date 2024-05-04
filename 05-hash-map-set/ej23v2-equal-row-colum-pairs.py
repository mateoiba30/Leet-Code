#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

#excercise 2352

from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = Counter([tuple(row) for row in grid])#each row (list) we convert it to a tuple to use them as a key on a dictionary
        #d is a Counter (a dictionary with more functionality) with the number of ocurrences of each row (tuple)

        cnt = 0
        for col in zip(*grid): #zip(*grid) transposes the matrix, letting us to iterate over the columns and not over rows
            cnt += d[col] #we add the number of ocurrences of the column to the count
        
        return cnt