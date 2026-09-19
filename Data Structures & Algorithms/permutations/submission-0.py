class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer, current = [], []
        used = [False] * len(nums)
        self.helper(0, nums, answer,current, used)
        return answer


    def helper(self, i, nums, answer, current, used):
        if len(current) == len(nums):
            answer.append(current.copy())
        
        if i >= len(nums):
            return

        for j in range(len(nums)):
            if used[j]:
                continue

            used[j] = True
            current.append(nums[j])
            self.helper(i + 1, nums,answer, current, used)

            used[j] = False
            current.pop()