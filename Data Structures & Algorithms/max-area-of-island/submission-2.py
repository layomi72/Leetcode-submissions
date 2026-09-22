class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, columns = len(grid), len(grid[0])
        max_area = -1

        for r in range(rows):
            for c in range(columns):
                max_area = max(max_area,self.dfs(grid,r,c,visited))

        return max_area
                

    def dfs(self, grid, r, c, visited):
        rows, columns = len(grid), len(grid[0])
        if min(r,c) < 0 or r == rows or c == columns or (r,c) in visited:
            return 0

        if grid[r][c] == 0:
            return 0
        
        area = 1
        visited.add((r,c))
        area += self.dfs(grid, r + 1, c, visited)
        area += self.dfs(grid, r - 1, c, visited)
        area += self.dfs(grid, r, c - 1, visited)
        area += self.dfs(grid, r, c + 1, visited)
    

        return area
        