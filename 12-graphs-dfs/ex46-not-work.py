# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

# excercise 399

#THIS WAS A FIRST APPROACH, WE REALIZED THAT WE MUST MANIPULATE A SIMPLE MATRIX AS  GRAPH

class Solution(object):
    graph = []
#we return the multiplications of weights to arrive to the destination with the first way we find
    def dfs(self, origin, objetive): #normal dfs going down

    def addNode(graph, origin, destination):
        encontre = False

        pos = 0
        while (pos < len(graph) and encontre == False):
            if graph[pos][0][0] == origin[0][0]:
                encontre = True
            else:
                pos += 1

        if not encontre:
            graph.append[origin]
            pos = len(graph)-1 #same as pos+=1

        graph[pos][0].append(destination)

        def calcEquation(self, equations, values, queries):
            #make graph
            i = 0
            for row in equations:
                weight = values[i]
                i += 1
                self.addNode(graph, [[row[0], 1]], [row[1], weight])   
                self.addNode(graph, [[row[1], 1]], [row[0], 1/weight])

            #responder queries
            answers = []
            for row in queries:
                visited = [False] * len(graph)
                answers.append(self.dfs(graph, row[0], row[1], visited))

            return answers