class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if nums[i] % 2 ==  nums[i - 1]  % 2:
                    return False

            else:
                if (nums[i] % 2) ==  (nums[i + 1]  % 2):
                    return False

        return True