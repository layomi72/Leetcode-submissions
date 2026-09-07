class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        ans = []

        for num in nums:
            heapq.heappush(heap, num)

        ans = heapq.nlargest(k,heap)

        return ans[k-1]
        