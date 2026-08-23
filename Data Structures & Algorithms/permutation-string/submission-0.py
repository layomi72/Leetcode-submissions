class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        L = 0
        window = []

        for R in range(len(s2)):
            window.append(s2[R])
            if R - L + 1 > len(s1):
                window.remove(s2[L])
                L += 1

            answer = sorted(window)
            if sorted(s1) == answer:
                return True


        return False