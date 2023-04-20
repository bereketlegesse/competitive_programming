class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        isValid = lambda click: 0 <= click[0] < n and 0 <= click[1] < m

        def checkAdj(row, col):
            if not isValid((row, col)) or board[row][col] != "M":
                return 0
            return 1

        def recursive(row, col):
            if not isValid((row, col)):
                return 

            if board[row][col] == 'M':
                board[row][col] = "X"
                return

            if board[row][col] == "E":
                adjMines = 0
                diagonals = (checkAdj(row+1,col+1)+checkAdj(row-1,col+1)+checkAdj(row-1,col-1)+checkAdj(row+1,col-1))
                neighbors = (checkAdj(row+1,col)+checkAdj(row-1,col)+checkAdj(row,col-1)+checkAdj(row,col+1))
                adjMines += (diagonals + neighbors)

                if adjMines:
                    board[row][col] = str(adjMines)
                    return
                    
                board[row][col] = "B"
                recursive(row, col + 1)
                recursive(row, col - 1)
                recursive(row + 1, col)
                recursive(row - 1, col)
                recursive(row - 1, col - 1)
                recursive(row + 1, col - 1)
                recursive(row - 1, col + 1)
                recursive(row + 1, col + 1)
                
        recursive(click[0], click[1])
        return board