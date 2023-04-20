class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows():
            for row in range(9):
                Row = []
                for col in range(9):
                    if board[row][col] != ".":
                        Row.append(board[row][col])
                if len(Row) != len(set(Row)):
                    return False
            return True
        
        def checkCols():
            for col in range(9):
                Col = []
                for row in range(9):
                    if board[row][col] != ".":
                        Col.append(board[row][col])

                if len(Col) != len(set(Col)):
                    return False
            return True
            
        def checkSubboxes():
            for row in range(3):
                for col in range(3):
                    subBox = []
                    for i in range(3):
                        subBox.append(board[row*3][col*3 + i]) if board[row*3][col*3 + i] != "." else None
                        subBox.append(board[row*3 + 1][col*3 + i]) if board[row*3 + 1][col*3 + i] != "." else None
                        subBox.append(board[row*3 + 2][col*3 + i]) if board[row*3 + 2][col*3 + i] != "." else None
                   
                    if len(subBox) != len(set(subBox)):
                        return False
            return True
        
        return checkSubboxes() and checkRows() and checkCols()