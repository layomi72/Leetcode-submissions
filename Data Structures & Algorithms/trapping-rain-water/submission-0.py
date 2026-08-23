class Solution:
    def trap(self, height: List[int]) -> int:
        max_total = 0
        max_left = []
        max_right = [0] * len(height)


        for i in range(len(height)):
            if i == 0:
                max_left.append(0)

            else:
                if height[i - 1] > max_left[i - 1]:
                    max_left.append(height[i - 1])
                else:
                    max_left.append(max_left[i - 1])

        
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])


        for i in range(len(height)):
       
                total = min(max_left[i], max_right[i]) - height[i]

                if total > 0:
                    max_total += total

    
        return max_total

        