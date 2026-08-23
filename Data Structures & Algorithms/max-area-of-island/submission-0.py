class Solution:
    def maximumarea(self, grid: List[List[int]], row: int, column: int, visited: set) -> int:
        area = 1
        visited.add((row,column))

        # check down for the area
        if row + 1 >= 0 and row + 1 < len(grid) and (row + 1, column) not in visited and column >= 0 and column < len(grid[0]):
            if grid[row + 1][column] == 1:
                area += self.maximumarea(grid, row + 1, column, visited)

        # check up for the area 
        if row - 1 >= 0 and row - 1 < len(grid) and (row - 1, column) not in visited and column >= 0 and column < len(grid[0]):
            if grid[row - 1][column] == 1:
                area += self.maximumarea(grid, row - 1, column, visited)

        # check left for the area 
        if row >= 0 and row  < len(grid) and (row, column - 1) not in visited and column - 1 >= 0 and column - 1 < len(grid[0]):
            if grid[row][column - 1] == 1:
                area += self.maximumarea(grid,row, column - 1, visited)

        # check the right for the area
        if row >= 0 and row  < len(grid) and (row, column + 1) not in visited and column + 1 >= 0 and column + 1 < len(grid[0]):
            if grid[row][column + 1] == 1:
                area += self.maximumarea(grid,row, column + 1, visited)

        return area
               

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        max_area = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1 and grid[row][column] not in visited:
                    area = self.maximumarea(grid,row,column,visited)
                    max_area = max(area, max_area)
                    



        return max_area