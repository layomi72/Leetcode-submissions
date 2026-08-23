class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1

        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        queue = deque()
        
        queue.append((0,0))
        visited.add((0,0))

        length = 1

        directions = [[0,1], [0,-1],[1,0],[-1,0],[-1,-1], [1,1], [-1,1], [1,-1]]

        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                if row == rows - 1 and column == columns - 1:
                    return length
                else:
                    for dr, dc in directions:
                        new_row = row + dr
                        new_column = column + dc

                        if new_row < 0 or new_row >= rows or new_column < 0 or new_column >= columns or grid[new_row][new_column] == 1 or ((new_row,new_column)) in visited:
                            continue 
                        else:
                            queue.append((new_row,new_column))
                            visited.add((new_row,new_column))
            length += 1

        return -1