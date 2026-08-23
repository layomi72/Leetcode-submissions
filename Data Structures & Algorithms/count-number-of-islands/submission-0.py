class Solution:
    def addislandpoints(self, r: int, c: int, grid: List[List[str]], visited: set) -> None:
        rright = r + 1
        cup = c + 1
        rleft = r - 1
        cdown = c - 1

        if (r,c) in visited:
            return

        visited.add((r,c))
        # check for land below 
        if rright >= 0 and rright < len(grid):
            if grid[rright][c] == "1" and (rright, c) not in visited:
                self.addislandpoints(rright,c,grid,visited)

        # check for land above
        if rleft >= 0 and rleft < len(grid):
            if grid[rleft][c] == "1" and (rleft, c) not in visited:
                self.addislandpoints(rleft,c,grid,visited)

        # check for land to the right
        if cup >= 0 and cup < len(grid[0]):
            if grid[r][cup] == "1" and (r, cup) not in visited:
                self.addislandpoints(r,cup,grid,visited)


        # check for land to the left 
        if cdown >= 0 and cdown < len(grid[0]):
            if grid[r][cdown] == "1" and (r, cdown) not in visited:
                self.addislandpoints(r,cdown,grid,visited)

        return




    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    #find other island connecters
                    self.addislandpoints(r,c,grid,visited)



        return islands
