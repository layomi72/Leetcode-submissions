class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    answer.append(i)
                    answer.append(j)
                    answer = sorted(answer)
                    return answer

        