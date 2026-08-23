class Solution:
    def isValid(self, s: str) -> bool:
        x = []

        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                x.append(s[i])

            elif s[i] == ")" and x and x[-1] == "(":
                x.pop()

            elif s[i] == "}" and x and x[-1] == "{":
                x.pop()

            elif s[i] == "]" and x and x[-1] == "[":
                x.pop()

            else:
                return False

        if not x:
            return True
        else:
            return False


            

        