class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = x
        y = x
        if n==0:
            return 1
        if (n>=0):
            for i in range(0, n-1):
                answer *=y
        else:
            n *= -1
            for i in range(0, n-1):
                answer *=y

            answer = 1/answer
        return float(answer)
        