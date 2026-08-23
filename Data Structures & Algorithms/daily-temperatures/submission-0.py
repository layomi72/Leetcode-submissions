class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            if not stack:
                stack.append([i,t])
            
            if stack[-1][1] >= t:
                stack.append([i,t])
            else:
                while stack and stack[-1][1] < t:
                    x = stack.pop()
                    output[x[0]] = i - x[0]
                stack.append([i,t])

        return output


        