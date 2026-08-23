class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through each element in a row and return false if there are any duplicates, use a set to track duplicates 
        for r in range(9):
            seen_items = set()
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
        
                if num not in seen_items:
                    seen_items.add(num)
                else:
                    return False
            
 # loop through each element in a column and return false if there are any duplicates, use a set to track duplicates 
    
        for c in range(9):
            seen_items = set()
            for r in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                if num not in seen_items:
                    seen_items.add(num)
                else:
                    return False

# loop through each element in the 3 by 3 
        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                seen_items = set()
                for ri in range(r, r + 3):
                    for ci in range(c, c + 3):
                        num = board[ri][ci]
                        if num == ".":
                            continue
                        if num not in seen_items:
                            seen_items.add(num)
                        else:
                            return False

    
        return True