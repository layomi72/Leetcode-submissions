class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if smaller position and smaller time it joins fleet with bigger positon bigger time
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]


            while stack and cars[i][0] < stack[-1][0] and time <= stack[-1][1]:
                     time = stack[-1][1]
                     stack.pop()

            stack.append([cars[i][0],time])

        return len(stack)