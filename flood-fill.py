class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        original = image[sr][sc]
        visited = set()
        inbound = lambda row,col: 0 <= row < n  and 0 <= col < m 
        def dfs(row,col):
            if  not inbound(row, col) or image[row][col] != original or (row,col) in visited:
                return

            visited.add((row, col))
            image[row][col] = color
            
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)

        dfs(sr, sc)
        return image