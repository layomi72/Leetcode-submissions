class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + j == target
        # make a hsshmap mapping values to its index. (values here represent i)
        sum1 = {}
        for i in range(len(nums)):
            sum1[nums[i]] = i
        # now loop through each index to see if we have j = target - i
        
        for i in range(len(nums)):
            j = target - nums[i]
            if j in sum1 and sum1[j] != i:
                if sum1[j] > i:
                    return [i,sum1[j]]
                else:
                    return [sum1[j],i]