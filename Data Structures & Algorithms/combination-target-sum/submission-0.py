class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer, curset = [], []
        self.helper(0,nums, answer, curset, target)
        return answer


    def helper(self,i, nums, answer, curset, target):
        if sum(curset) == target:
            answer.append(curset.copy())
            return 

        if sum(curset) > target:
            return

        for j in range(i, len(nums)):
            curset.append(nums[j])
            self.helper(j, nums, answer, curset, target)
            curset.pop()