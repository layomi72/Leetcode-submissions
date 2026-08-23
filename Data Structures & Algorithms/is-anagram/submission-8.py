class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in word_count:
                    word_count[s[i]] +=1
                else:
                    word_count[s[i]] = 1
        
        for i in range(len(s)):
            if t[i] in word_count:
                word_count[t[i]] -=1
            else: 
                return False
                
        if -1 in word_count.values():
            return False
        return True
        
        