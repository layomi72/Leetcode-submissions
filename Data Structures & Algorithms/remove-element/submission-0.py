class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        correctedNums = []
        for i in range(0, len(nums)):
            if nums[i] != val:
                correctedNums.append(nums[i])
        
        nums[:len(correctedNums)] = correctedNums
        return len(correctedNums)