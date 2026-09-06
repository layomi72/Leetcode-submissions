class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        
        ans = heapq.nlargest(self.k,self.nums)

        return ans[self.k-1]