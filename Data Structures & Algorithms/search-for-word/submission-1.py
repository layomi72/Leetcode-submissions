class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, columns = len(board), len(board[0])
        for r in range(rows):
            for c in range(columns):
                if board[r][c]:
                    if self.dfs(board, r,c, visited, word):
                        return True

        return False

    def dfs(self, board, r, c, visited,word):
        rows, columns = len(board), len(board[0])
        if not word:
            return True
        if min(r,c) < 0 or r == rows or c == columns or (r,c) in visited:
            return 

 

        if board[r][c] == word[:1]:
            visited.add((r,c))
            if self.dfs(board, r + 1,c, visited, word[1:]):
                return True
            if self.dfs(board, r - 1,c, visited, word[1:]):
                return True
            if self.dfs(board, r,c + 1, visited, word[1:]):
                return True
            if self.dfs(board, r,c - 1, visited, word[1:]):
                return True
            visited.remove((r,c))

        return False

          
