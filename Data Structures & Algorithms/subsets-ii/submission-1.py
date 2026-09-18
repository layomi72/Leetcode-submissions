class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset, curset = [], []
        nums.sort()
        self.helper(0, nums, subset, curset)
        return subset

    
    def helper(self,i, nums, subset, curset):

        if i >= len(nums):
            subset.append(curset.copy())
            return 

        curset.append(nums[i])
        self.helper(i + 1, nums, subset, curset)

        curset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i = i + 1

        self.helper(i + 1, nums, subset, curset)

        return