class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:len(nums)] = sorted(set(nums))
        return len(nums)