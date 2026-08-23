class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #hash map to store the count and the length of the count
        highest_increase = 1
        highest_decrease = 1

        #for loop to count highest increase
        count = 1
        for i in range(len(nums)):
            if i + 1 == len(nums):
                continue
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                highest_increase = max(highest_increase,count)
                count = 1

            highest_increase = max(highest_increase,count)

        #for loop to count highest decrease
        count = 1
        for i in range(len(nums)):
            if i + 1 == len(nums):
                continue
            if nums[i + 1] < nums[i]:
                count += 1
            else:
                highest_decrease = max(highest_decrease,count)
                count = 1

            highest_decrease = max(highest_decrease,count)

        if highest_increase > highest_decrease:
            return highest_increase
        else:
            return highest_decrease