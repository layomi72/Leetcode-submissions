class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0 
        window = {}
        require = {}
        count = 0
      
        minn = float("inf")

        if len(s) < len(t):
            return ""

        for i in range(len(t)):
            require[t[i]] = require.get(t[i],0) + 1
        

        for R in range(len(s)):
            # add to window
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in require and window[s[R]] == require[s[R]]:
                count += 1

    
            # while valid remove the last item in the window
            while count >= len(require):
                if R - L + 1 < minn:
                    ans = [L,R]
                    minn = min(minn,R - L + 1)

                if s[L] in require and window[s[L]] == require[s[L]]:
                    count -= 1
                window[s[L]] -= 1
                L += 1
       


        if minn == float("inf"):
            return ""
        else:
            return "".join(s[ans[0]:ans[1]+1])


            
            