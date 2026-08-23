class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if the grid is empty then the state is impossible hence return -1
        if grid == []:
            return -1

        rows,columns = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        minute = 0

        # loop through matrix and store all the rotten fruit in the queue if it is not in the queue already

        for row in range(rows):
            for column in range(columns):
                if ((row,column)) not in queue and grid[row][column] == 2:
                    queue.append((row,column))


        # Now explore all the rotten fruits in the queue level by level
        while queue:
            for _ in range(len(queue)):
                row,column = queue.popleft()
                for dr,dc in directions:
                    new_row = row + dr
                    new_column = column + dc
                    # check neighbours 
                    if new_row < 0 or new_column < 0 or new_row >= rows or new_column >= columns or grid[new_row][new_column] == 0 or grid[new_row][new_column] == 2 or ((new_row,new_column)) in visited:
                        continue

                    else:
                        grid[new_row][new_column] = 2
                        queue.append((new_row,new_column))
                        visited.add((new_row,new_column))
            
            if queue:
                minute +=1

        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    return -1
        

        return minute 

