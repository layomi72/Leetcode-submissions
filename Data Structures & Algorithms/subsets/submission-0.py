class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, curset = [], []
        self.helper(0, nums, subset, curset)
        return subset

    
    def helper(self, i, nums, subset, curset):
        if i >= len(nums):
            subset.append(curset.copy())
            return 

        curset.append(nums[i])
        self.helper(i + 1, nums, subset,curset)

        curset.pop()
        self.helper(i + 1, nums, subset, curset)
        return