class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        top = 0
        bottom = row - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1

            else:
                break

        if top > bottom:
            return False 

        L = 0
        R = col - 1

        while L <= R:
            mid = (L + R) // 2
            if target > matrix[mid_row][mid]:
                L = mid + 1
            
            elif target < matrix[mid_row][mid]:
                R = mid - 1

            else:
                return True

        return False
