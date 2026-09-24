class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        length = 1
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    queue.append((r,c))
                    
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [[0,1], [0, -1], [1,0], [-1,0]]:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) < 0 or nr == rows or nc == columns or (nr,nc) in visited or grid[nr][nc] == -1:
                        continue

                    grid[nr][nc] = length
                    visited.add((nr,nc))
                    queue.append((nr,nc))
                    

            length += 1

        

        
