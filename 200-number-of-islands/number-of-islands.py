from collections import deque
class Solution(object):
    def numIslands(self,grid):
        rows=len(grid)
        columns=len(grid[0])
        island=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=columns:
                return
            if grid[r][c]=="0":
                return
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j) 
        return island

                  

        
       
        