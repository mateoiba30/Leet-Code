# Nearest Exit from Entrance in Maze
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists

#excersize 926

class Solution:
    def nearestExit(self, maze, entrance):
        steps = 0
        pending = [(entrance[0], entrance[1], 0)]
        rows = len(maze)
        colums = len(maze[0])
        rowAddition = [-1,1,0,0]
        colAddition = [0,0,-1,1]
        visited=[[-1]*colums for i in range(rows)] #dont use a list of visiteds
        visited[entrance[0]][entrance[1]]=1

        while pending:
            r, c, steps = pending.pop(0)
            for i in range(4): #dont use a list for neighbors, instead we use the rowAddition and colAddition arrays
                r2 = r+rowAddition[i]
                c2 = c+colAddition[i]
                #now we put all in one if
                if  r2< rows and r2>=0 and c2 < colums and c2 >=0 and maze[r2][c2]=="." and visited[r2][c2]==-1 :
                    if ( r2==0 or r2==rows-1 or c2==0 or c2==colums-1): #these must be other if to not have an index error
                        return steps+1
                    else:
                        pending.append((r2, c2, steps+1))
                        visited[r2][c2]=1 #now we mark as visited only if the cell passed the big filter, we are touching this matrix the less possible
        return -1
    
entrance = [0,1]
maze =[["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
sol = Solution()
steps = sol.nearestExit(maze, entrance)
print("steps: ", steps)