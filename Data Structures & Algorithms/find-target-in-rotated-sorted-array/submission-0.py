class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            mid = ( L + R ) // 2
            if nums[mid] > nums[R]:
               L = mid + 1

            else:
                R = mid 

        pivot = L

        if target <= nums[-1]:
            L = pivot 
            R = len(nums) - 1

        else:
            L = 0
            R = pivot - 1


        while L <= R:
            mid = ( L + R ) // 2

            if target > nums[mid]:
                L = mid + 1
            
            elif target < nums[mid]:
                R = mid - 1

            else:
                return mid

        return -1