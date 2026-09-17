class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:
            reverse = str(x)
            reverse = reverse[::-1]
            ans = int(reverse)
        else:
            reverse = str(x)
            reverse = reverse[::-1]
            ans = ""
            for c in reverse:
                if c.isdigit():
                    ans += c

            ans = int(ans) * -1
            
        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans