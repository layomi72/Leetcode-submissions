class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.counter(0,0,grid,set())
        

    def counter(self, r: int, c:int, grid: List[List[int]], visited:set)-> int:
        rows = len(grid)
        columns = len(grid[0])
        # if the coordinates are out of bound return 0 for that count
        if r < 0 or r == rows or c < 0 or c == columns or grid[r][c] == 1:
            return 0

        # if we have already visited this node then we should return 0
        if (r,c) in visited:
            return 0

        # if you get to the final destination return a count of 1
        if r == rows - 1 and c == columns - 1:
            return 1
        
        visited.add((r,c))

        
        count = self.counter(r+1,c,grid,visited) + self.counter(r-1,c,grid,visited) + self.counter(r,c+1,grid,visited) + self.counter(r,c-1,grid,visited)

        visited.remove((r,c))

        return count











