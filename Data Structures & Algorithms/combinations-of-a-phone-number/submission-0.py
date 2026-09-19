class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
        "2": "abc",  "3": "def",  "4": "ghi",
        "5": "jkl",  "6": "mno",  "7": "pqrs",
        "8": "tuv",  "9": "wxyz",
        }

        answer, current = [], []

        if len(digits) == 0:
            return []
            
        self.helper(0, digits, answer, current, mapping)
        
        return answer

    def helper(self, i, digits, answer, current, mapping):
        if len(current) == len(digits):
            answer.append("".join(current.copy()))

        if i >= len(digits):
            return 

        
        for value in mapping[digits[i]]:
            current.append(value)
            self.helper(i + 1, digits, answer, current, mapping)
            current.pop()
        
