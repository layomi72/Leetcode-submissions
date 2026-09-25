class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        if word1 and not word2:
            return word1

        if word2 and not word1:
            return word2

        
        while word2 and word1:
            answer.append(word1[:1])
            answer.append(word2[:1])
            word2 = word2[1:]
            word1 = word1[1:]

        if word2:
            answer.append(word2)
            
        if word1:
            answer.append(word1)

        
        return "".join(answer)
