#There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
#Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
#It's guaranteed that each city can reach city 0 after reorder.

#exercise 1466

class Solution:

    def minReorder(self, n, connections):
        #make a undirected graph (it was a hint)
        graph = []
        for i in range(n):
            graph.append([])
        for i in connections:
            graph[i[0]].append(i[1]) #is the origin and 0 the destination
            graph[i[1]].append(-i[0]) #we put a new conection in the other direction

        #mark each node as not visited
        visited = [False] * n

        #we do a normal dfs from 0 as root. If we go down to a leaf and we need a different direction we see that as a change
        return self.dfs(graph, visited, 0)

    def dfs(self, graph, visited, origin): #normal dfs going down
        changes = 0
        visited[origin] = True

        for destination in graph[origin]:
            if not visited[abs(destination)]: #for each unvisited adjacent
                changes += self.dfs(graph, visited, abs(destination))
                if (destination > 0): #If to go down we had to use an inverted path, then a change must be made
                    changes += 1

        return changes