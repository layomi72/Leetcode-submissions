class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        x = []
        for token in tokens:
            if token == "+":
                a = x.pop()
                b = x.pop()
               

                x.append(a + b)

            elif token == "*":
               a = x.pop()
               b = x.pop()

               x.append(a*b)

            elif token == "-":
                a = x.pop()
                b = x.pop()

                x.append(b - a)

            elif token == "/":
                a = x.pop()
                b = x.pop()
                x.append(int(b / a))
            
            else:
                x.append(int(token))



        return x[-1]