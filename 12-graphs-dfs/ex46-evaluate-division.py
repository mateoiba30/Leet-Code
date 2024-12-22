# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

# excercise 399
import collections
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #make a graph
        graph = collections.defaultdict(dict)

        # for i in range(len(equations)): #the same as below
        #     a = equations[i][0]
        #     b = equations[i][1]
        #     val = values[i]
        #     graph[a][b] = val
        #     graph[b][a] = 1.0 / val
        #     i+=1

        # Step 2. DFS function
        def dfs(x, y, visited):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0
            
            # x points to y
            if y in graph[x]:
                return graph[x][y]
            
            # x maybe connected to y through other nodes
            # use dfs to see if there is a path from x to y
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
            return -1
            
        # go through each of the queries and find the value
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res