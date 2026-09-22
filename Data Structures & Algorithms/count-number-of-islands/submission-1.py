class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows, columns = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    self.dfs(visited, r, c,grid)
        
        return count

    def dfs(self, visited, r, c, grid):
        rows, columns = len(grid), len(grid[0])
        if min(r,c) < 0 or r == rows or c == columns or (r,c) in visited:
            return 
        if grid[r][c] == "0":
            return

        visited.add((r,c))
        self.dfs(visited, r+1, c,grid)
        self.dfs(visited, r-1, c,grid)
        self.dfs(visited, r, c+1,grid)
        self.dfs(visited, r, c-1,grid)
        