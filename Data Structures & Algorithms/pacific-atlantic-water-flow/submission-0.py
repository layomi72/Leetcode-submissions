class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #adjacent to the ocean means r == 0 or c == 0
        # from neighbouring cell if height[nr,nc] >= height[r,c]

        pacific = set()
        queue = deque()

        atlantic = set()
        queue1 = deque()
   
        answer = []

        rows, columns = len(heights), len(heights[0])

        for r in range(rows):
            for c in range(columns):
                if r == 0 or c == 0:
                    queue.append((r,c))
                    pacific.add((r,c))
        

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()        
                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == rows or nc == columns or heights[nr][nc] < heights[r][c] or (nr,nc)  in pacific:
                        continue

                    pacific.add((nr,nc))
                    queue.append((nr, nc))
                        
                    
        for r in range(rows):
            for c in range(columns):
                if r == rows - 1 or c == columns - 1:
                    queue1.append((r,c))
                    atlantic.add((r,c))
        

        while queue1:
            for i in range(len(queue1)):
                r, c = queue1.popleft()        
                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == rows or nc == columns or heights[nr][nc] < heights[r][c] or (nr,nc) in atlantic:
                        continue

                    atlantic.add((nr,nc))
                    queue1.append((nr, nc))


        for cell in atlantic:
            if cell in pacific:
                answer.append(list(cell))

        return answer
        