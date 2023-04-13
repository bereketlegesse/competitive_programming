class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        count = 0

        checkIndex = lambda row, col : 0 <= row < n and 0 <= col < m
        checkGrid1 = lambda row, col : grid1[row][col] == 1
        
        def dfs(row, col):
            if not checkIndex(row, col) or grid2[row][col] == 0:
                return True

            if checkIndex(row,col) and not checkGrid1(row,col):
                return False
            
            grid2[row][col] = 0
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            up = dfs(row -1 , col)
            down = dfs(row + 1, col)

            return left and right and up and down


        for row in range(n):
            for col in range(m):
                if grid2[row][col] == 1:
                    if dfs(row, col):
                        count += 1
                        
        return count