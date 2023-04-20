class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxSum = float("-inf")

        for row in range(n-2):
            for col in range(m-2):
                curSum = sum(grid[row][col:col+3]) + sum(grid[row+2][col:col+3]) + grid[row + 1][col + 1]
                maxSum = max(maxSum, curSum)
                
        return maxSum