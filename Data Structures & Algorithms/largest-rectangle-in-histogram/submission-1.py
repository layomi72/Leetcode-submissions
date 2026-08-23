class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Area = width x height 
        # Use a stack to track the highest area
        stack = []
        max_area = 0
    
        for i,val in enumerate(heights):
            if not stack:
                stack.append([i,val])

            else:
            
                if stack and val >= stack[-1][1]:
                    stack.append([i,val])

                else:
                    height = stack[-1][1]
                    index  = stack[-1][0]
                    area   = height * (i - index)

                    max_area = max(area,max_area)
                    stack.pop()



                    while stack and val < stack[-1][1]:
                        height = stack[-1][1]
                        index  = stack[-1][0]
                        area   = height * (i - index)
                        max_area = max(area,max_area)
                        stack.pop()

                    stack.append([index,val])

           

    

        while stack:
        
            height = stack[-1][1]
            index  = stack[-1][0]
            area   = height * (len(heights) - index)

            max_area = max(area,max_area)
            stack.pop()



        return max_area


            
