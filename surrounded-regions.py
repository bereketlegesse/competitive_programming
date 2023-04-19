class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        isValid = lambda row, col: 0 <= row < n and 0 <= col < m
        visited = set()
        def dfs(row, col):
            if not isValid(row, col):
                return 
            if (row, col) in visited:
                return True

            visited.add((row, col))
            if board[row][col] == "X":
                return True

            left = dfs(row, col-1)
            right =  dfs(row, col+1)
            up = dfs(row-1, col)
            down = dfs(row+1, col)

            return left and right and up and down

        for row in range(n):
            for col in range(m):
                if board[row][col]=="O" and dfs(row, col):
                    for r, c in visited:
                        board[r][c] = "X"
                visited = set()