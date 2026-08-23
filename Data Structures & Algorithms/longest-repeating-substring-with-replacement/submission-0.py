class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0 
        best = 1 
        max_best = 0
        count = {}

        if not s:
            return 0

        for R in range(len(s)):
            if s[R] in count:
                count[s[R]] += 1
            else:
                count[s[R]] = 1

            frequency = sorted(count.items(), key = lambda p:p[1], reverse = True)

            while (R - L + 1) - frequency[0][1] > k:
                frequency = sorted(count.items(), key = lambda p:p[1], reverse = True)
                count[s[L]] -= 1
                L += 1
            max_best = max(max_best, R - L + 1)

        
   
        return max_best


        