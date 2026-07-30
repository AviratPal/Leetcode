class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        perimeter=0
        for i in range(row):
            for j in range(column):
                if grid[i][j]==1:
                    perimeter+=4
                    if i+1<row and grid[i+1][j]==1:
                        perimeter-=2
                    if j+1<column and grid[i][j+1]==1:
                        perimeter-=2
        return perimeter                    

        