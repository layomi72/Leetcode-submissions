class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0

        for num in nums:
            x ^= num

        
        for i in range(len(nums) + 1):
            y ^= i

        return x ^ y