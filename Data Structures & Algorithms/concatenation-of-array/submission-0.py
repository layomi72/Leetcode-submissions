class Solution:
    
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        ans[:len(nums)] = nums
        for i in range(0,len(nums)):
            ans[i + len(nums)] = nums[i]
        
        return ans
