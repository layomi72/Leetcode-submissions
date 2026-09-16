class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            output.append(self.countbit(i))

        return output 

    def countbit(self,n):
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count