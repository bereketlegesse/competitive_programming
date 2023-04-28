class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] != 0:
            return -1

        isValid = lambda row, col: 0 <= row < n and 0 <= col < m and grid[row][col] == 0
        queue = deque()
        queue.append((0, 0))
        distance = 0
        # directions = [(0, 1),(1,0),(1,1),(-1,0),(0, -1),(-1,-1),(0, -1),(-1,1)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            distance += 1
            curLen = len(queue)
            for _ in range(curLen):
                row, col = queue.popleft()
                if row == n -1 and col == m - 1:
                    return distance

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if isValid(newRow, newCol):
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 1

        return -1