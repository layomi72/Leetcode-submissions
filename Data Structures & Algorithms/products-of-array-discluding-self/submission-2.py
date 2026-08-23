class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # if we need to calculate everything for an element before and after it in a list we use a prefix and suffix array

        prefix = []
        suffix = []
        output = []

        #creating the prefix array
        runningtotal = 1
        for num in nums:
            prefix.append(runningtotal)
            runningtotal *= num
        
        #creating the suffix array
        runningtotal = 1
        for num in reversed(nums):
            suffix.append(runningtotal)
            runningtotal *= num

        suffix.reverse()

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output
