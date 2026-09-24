class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])
        visited = set()
        for r in range(rows):
            for c in range(columns):
                if (board[r][c] == "O" )and (r == rows - 1 or r == 0 or c == columns - 1 or c == 0):
                    self.dfs(r,c,board,visited)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

    def dfs(self, r, c, board, visited):
        rows, columns = len(board), len(board[0])
        if min(r,c) < 0 or r == rows or c == columns or (r,c) in visited or board[r][c] == "X":
            return 
        

        
        visited.add((r,c))
        self.dfs(r + 1,   c, board, visited)
        self.dfs(r - 1,c, board, visited)
        self.dfs(r       ,c + 1, board, visited)
        self.dfs(r       ,c - 1, board, visited)

