class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        ans = s.lower()
        while L < R:
            while L < R and not ans[L].isalnum():
                L += 1

            while L < R and not ans[R].isalnum():
                R -= 1
                
            if ans[L] != ans[R]:
                return False
            
            else:
                L += 1
                R -= 1

        return True