class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        x = n

        while x > 0:
            if x & 1 == 1:
                count +=1 
            
            x = x >> 1

        return count