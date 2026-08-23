class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        best = 0
        size = set()
        if s:
            size.add(s[L])
            best = 1

        for R in range(1,len(s)):
            while s[R] in size:
                size.remove(s[L])
                L += 1
            size.add(s[R])
            
            best = max(best, R - L + 1)
        
        return best
        