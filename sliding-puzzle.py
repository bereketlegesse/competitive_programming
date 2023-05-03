class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        queue.append(board)
        isValid = lambda row, col : 0 <= row < 2 and 0 <= col < 3
        dirr = [(-1,0),(0,1),(0,-1),(1,0)]
        ops = 0
        target = [[1,2,3],[4,5,0]]

        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                curr = queue.popleft()
                visited.add(tuple([ tuple(i) for i in curr]))
                if curr == target:
                    return ops

                if 0 in curr[0]:
                    col,row = curr[0].index(0),0
                else:
                    col,row = curr[1].index(0),1

                for dr,dc in dirr:
                    newRow = row + dr
                    newCol = col + dc
                    newBoard = [[i for i in curr[0]],[j for j in curr[1]]]
                    
                    if isValid(newRow, newCol):
                        num = newBoard[newRow][newCol]
                        newBoard[newRow][newCol] = 0
                        newBoard[row][col] = num
                        
                        if tuple([tuple(i) for i in newBoard]) not in visited:
                            queue.append(newBoard.copy())
            ops += 1
        return -1