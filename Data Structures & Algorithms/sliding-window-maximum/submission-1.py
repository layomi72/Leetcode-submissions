class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        ans = []
        window = {}
        best = 0

        for R in range(len(nums)):
            window[nums[R]] = window.get(nums[R], 0) + 1
            while R - L + 1 > k:
                window[nums[L]] -= 1
                if window[nums[L]] == 0:
                    window.pop(nums[L])
                L += 1
                
            if R - L + 1 == k:
                ans.append(max(window))


        return ans
