class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer, current = [], []
        self.helper(s, answer, current)
        return answer

    def helper(self, s, answer, current):
        if not s:
            answer.append(current.copy())
            return 

        for i in range(len(s)):
            piece = s[:i + 1]
            if piece == piece[::-1]:
                current.append(piece)
                self.helper(s[1 + i: ], answer, current)
                current.pop()