class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_bracket = 0
        close_bracket = 0
        answer = []
        current = []

        self.helper(open_bracket, close_bracket, answer, current, n)

        return answer

    def helper(self, open_bracket, close_bracket, answer, current, n):
        if close_bracket > open_bracket:
            return
        
        if open_bracket > n:
            return
        
        if close_bracket > n:
            return
        
        if close_bracket == n and open_bracket == n:
            answer.append("".join(current.copy()))

        current.append("(")
        open_bracket += 1
        self.helper(open_bracket, close_bracket, answer, current, n)

        current.pop()
        open_bracket -= 1

        current.append(")")
        close_bracket += 1

        self.helper(open_bracket, close_bracket, answer, current, n)
        current.pop()
        close_bracket -= 1