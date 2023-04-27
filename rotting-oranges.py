class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        numberOfFresh = 0
        queue = deque()
        minute = 0
        

        isValid = lambda row, col: 0 <= row < n and 0 <= col < m and grid[row][col] == 1

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    numberOfFresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
        count = 0
        dirr = [[-1, 0], [1, 0] , [0, 1], [0, -1]]
        while queue:
            cur_rotten = len(queue)
            minute += 1
            
            for _ in range(cur_rotten):
                row, col = queue.popleft()
        
                for dr, dc in dirr:
                    new_row = row + dr
                    new_col = col + dc
                    if isValid(new_row, new_col):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2


            count += len(queue) 
        
        return max (0, minute - 1) if not( numberOfFresh - count) else -1