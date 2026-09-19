class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer , current= [], []
        candidates.sort()
        self.helper(0,candidates, answer, current, target)
        return answer

    
    def helper(self, i, candidates, answer, current, target):
        if sum(current) == target:
            answer.append(current.copy())
            return 

        if sum(current) > target:
            return 

        seen = set()
        for j in range(i, len(candidates)):
            if candidates[j] not in seen:
                current.append(candidates[j])
                seen.add(candidates[j])
                self.helper(j + 1, candidates, answer, current, target)
                current.pop()
