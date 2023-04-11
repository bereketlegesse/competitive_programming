class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(row,col):
            if row >= rows or col >= cols or col < 0 or row < 0 or grid[row][col] == 0 :
                return 0
            grid[row][col] = 0
            left = dfs(row, col-1)
            right =  dfs(row, col+1)
            down = dfs(row+1, col)
            up = dfs(row-1, col)
            area = left + right + down + up + 1
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
                
        return maxArea