class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        total = numbers[L] + numbers[R]

        while L < R and total != target:
            
            while target > total and L < R:
                L += 1
                total = numbers[L] + numbers[R]

            while target < total and L < R:
                R -= 1
                total = numbers[L] + numbers[R]

        return [L+1, R+1]


                

        
        