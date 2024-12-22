# Nearest Exit from Entrance in Maze
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists

#excersize 926

#these first solution is not fast enough

class Solution:
    def addNeighbors(self, neighbors, r, c, rows, columns):
        if (r+1<rows):
            neighbors.append((r+1, c))
        if (r-1>=0):
            neighbors.append((r-1, c))
        if (c+1<columns):
            neighbors.append((r, c+1))
        if(c-1>=0):
            neighbors.append((r, c-1))

    def nearestExit(self, maze, entrance):
        steps = 0
        pending = []
        pending.append((entrance[0], entrance[1], 0))
        visited = []
        neighbors = []
        rows = len(maze)
        columns = len(maze[0])

        while len(pending) > 0:
            r, c, steps = pending.pop(0) #we must pop out the first cell because we are using append(), which adds the new element at the end
            visited.append((r, c))
            self.addNeighbors(neighbors, r, c, rows, columns)
            for r, c in neighbors:
                if(maze[r][c]==".")and((r,c) not in visited):
                    if (r==0) or (r==rows-1) or (c==0) or (c==columns-1): #if is an exit
                        return steps+1
                    else:
                        pending.append((r, c, steps+1))
        return -1
    
entrance = [0,1]
maze =[["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
sol = Solution()
steps = sol.nearestExit(maze, entrance)
print("steps: ", steps)