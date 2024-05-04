#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

#excercise 2352

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int: #grid is a list of rows
        count=0

        for i in range(len(grid)):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            count+= grid.count(column) #if the column is equal to more than a row, we have to sum more than one

        return count
