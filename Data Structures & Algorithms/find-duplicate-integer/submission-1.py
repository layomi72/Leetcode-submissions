class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       for i in range (0,len(nums)):
            for j in range (0,len(nums)):
                if nums[i] == nums[j] and i != j:
                    return nums[i]