class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # x stores the corrosponding height with its index
        x = []
        max_area = 0

        for i, val in enumerate(heights):
            x.append([i,val])
        
        L = 0
        R = len(x) - 1

        while (L < R):
            # using the minimum length of the sides so container does not over spill
            length = min(x[L][1], x[R][1])
            width = x[R][0] - x[L][0]
            area = length * width
            max_area = max(max_area,area)

            if x[L][1] > x[R][1]:
                R -= 1
            else:
                L += 1

        return max_area

