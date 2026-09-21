class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer, current = [], []
        self.helper(s, answer, current)
        return answer

    def helper(self, s, answer, current):
        if not s:                                  # nothing left to cut
            answer.append(current.copy())
            return

        for i in range(len(s)):
            piece = s[:i + 1]                      # first piece: 1, 2, 3... letters
            if piece == piece[::-1]:               # only keep palindromes
                current.append(piece)
                self.helper(s[i + 1:], answer, current)   # solve the REST
                current.pop()