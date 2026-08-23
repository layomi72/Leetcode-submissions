class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        index = 0
        localmax = 0
        while (index < len(nums)):
            if nums[index] == 1:
                localmax +=1
                maximum = max(maximum,localmax)
            else:
                localmax = 0

            index += 1

        return maximum