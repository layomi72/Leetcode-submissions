class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []



        for i in range(len(logs)):
            print(stack)
            x = logs[i]
            if x != "../" and x != "./":
                stack.append(x)

            if stack and x == "../":
                stack.pop()

        return len(stack)