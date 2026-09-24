class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        length = 0
        fresh = 0


       
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))
                
                if grid[r][c] == 1:
                    fresh += 1

        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == rows or nc == columns or (nr,nc) in visited or grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 2
                    fresh -=1
                    visited.add((nr,nc))
                    queue.append((nr,nc))

            length +=1




    
        return length if fresh == 0 else -1   
        

     
            
        