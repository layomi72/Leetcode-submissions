class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        anyDuplicates = sorted(set(nums))
        nums[:len(nums)] = sorted(nums)

        if anyDuplicates == nums:
            return False
        else:
            return True