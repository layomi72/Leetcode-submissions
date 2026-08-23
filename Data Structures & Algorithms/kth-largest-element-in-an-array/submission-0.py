class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        answer = []

        for i in range(0,k):
            y = heapq.heappop(nums)
            answer.append(y)
            
        answer[k - 1] *= -1
        
        return answer[k - 1]